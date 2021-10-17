# from openpyxl import Workbook, load_workbook
# from openpyxl.styles import Color, PatternFill, Font
# import datetime as dt
# from bs4 import BeautifulSoup
# from urllib.request import urlopen, Request

# Import All ^^^

# Calculates runtime
def timer(func):
    def inner(*args):
        then = dt.datetime.now()
        return_val = func(*args)
        print('Runtime:', dt.datetime.now() - then)
        return return_val

    return inner


class MediaList:
    green = PatternFill('solid', Color(rgb='35db61'))
    red = PatternFill('solid', Color(rgb='ff2929'))
    yellow = PatternFill('solid', Color(rgb='eaf24e'))
    black = PatternFill('solid', Color(rgb='000000'))
    white = PatternFill('solid', Color(rgb='FFFFFF'))
    white_text = Font(color='FFFFFF')

    def __init__(self, file='C:/Users/madhi/OneDrive/Documents/MediaList.xlsx',
                 lst=('Anime List', 'Games List', 'Movies List', 'TV Shows List'), special_slots=1):
        self.file = file
        self.lst = lst
        self.special_slots = special_slots

    def date_conv(self, start_date, eps, end_date=None):
        # Takes date in mm/dd/yyyy
        """Returns end date and remaining days respectively"""

        # Specifically for update() to update the remaining days
        if end_date:
            try:
                end_date = dt.datetime.strptime(end_date, '%b %d %Y')
            except ValueError:
                return '-1'
            rem = end_date - dt.datetime.now()
            days_left = str(rem).split()[0]
            return days_left

        # For anime that don't have a specified number of episodes
        try:
            eps = int(eps)
        except ValueError:
            return 'Unknown', '-1'
        start = dt.datetime.strptime(start_date, '%b %d %Y')
        end_date = start + dt.timedelta(weeks=eps)
        begin = end_date - dt.datetime.now()
        end_date = dt.datetime.strftime(end_date, '%b %d %Y')
        days_left = str(begin).split()[0]
        return end_date, days_left

    def web_scraper(self, anime_num):

        """Returns name, days left , start date, end date, broadcast day, eps respectively"""

        # To select the previous day to send as the broadcast day
        days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        req = Request(f'https://myanimelist.net/anime/{anime_num}')
        html = urlopen(req)
        soup = BeautifulSoup(html, 'lxml')
        lst = soup.find_all('div', {'class': 'spaceit_pad'})
        name = soup.find('h1', {'class': 'title-name h1_bold_none'}).get_text()

        # Gets Broadcast, Episodes and Aired from the html
        full_list = [i.get_text() for i in lst if
                     'Broadcast' in i.get_text() or 'Episodes' in i.get_text() or 'Aired' in i.get_text()]

        # Removes spaces and new lines from the data
        temp0 = []
        for i in full_list:
            temp = ''
            for j in i:
                if j != '\n':
                    temp += j
            temp0.append(temp)
        full_list = temp0

        eps = full_list[0].split()[1]

        smonth = full_list[1].split()[1]
        sday = full_list[1].split()[2][0]
        syear = full_list[1].split()[3]

        start_date = f'{smonth} {sday} {syear}'

        broadcast = full_list[2].split()[1][:-1]
        broadcast = days.index(broadcast) - 1
        broadcast = days[broadcast]

        end_date, rem = self.date_conv(start_date, eps)

        return name, rem, start_date, end_date, broadcast, eps, anime_num

    def create_wb(self):
        wb = Workbook()
        first = wb.active
        first.title = self.lst[0]
        sheets = [first]

        # Create sheets
        for i, val in enumerate(self.lst[1:], start=1):
            sheets.append(wb.create_sheet(val, i))

        ani_info = ['Name', 'Days Left', 'Start Date', 'End Date', 'Broadcast Day', 'Eps', 'Ani Num']
        etc = ['Name', 'Score']

        # Adjusting the col sizes
        for sheet in wb.worksheets:
            sheet.column_dimensions['A'].width = 40
            sheet.column_dimensions['B'].width = 10
            sheet.column_dimensions['C'].width = 14
            sheet.column_dimensions['D'].width = 14
            sheet.column_dimensions['E'].width = 14

        # Inserting values
        for i in range(self.special_slots):
            for col, val in enumerate(ani_info, start=1):
                sheets[i].cell(row=1, column=col, value=val)

        for sheet in sheets[self.special_slots:]:
            for col, val in enumerate(etc, start=1):
                sheet.cell(row=1, column=col, value=val)

        wb.save(self.file)
        return wb

    def find_empty_row(self, ws):
        # Finds and returns the next empty row num
        start_row = 2
        while True:
            if not ws.cell(row=start_row, column=1).value:
                break
            start_row += 1
        return start_row

    def multi_score(self, sel):
        # Asks for input and uses the input to sequentially score them
        lst = []
        while True:
            inp = input('Enter name and score separated by a comma: ')
            if inp == 'end':
                break
            lst.append(inp.split(','))
        for i in lst:
            self.score(i, sel)

    @timer
    def score(self, scores, sel):
        """An,Ga,Mo,Tv"""
        # Appends the scores to the empty row and updates the sheet
        scores = scores.split(',')
        try:
            wb = load_workbook(self.file)
        except PermissionError:
            print('Excel sheet open')
            return
        ws = wb.worksheets[sel]
        start_row = self.find_empty_row(ws)
        if scores[0] in [i.value for i in ws['A']]:
            print(f'{scores[0]} already in list')
            return
        for col, val in enumerate(scores, start=1):
            ws.cell(row=start_row, column=col, value=val)
        wb.save(self.file)
        self.update(sno=range(sel, sel + 1))

    def update(self, sno=range(4)):
        try:
            wb = load_workbook(self.file)
        except PermissionError:
            print('Excel sheet open')
            return
        for i in sno:
            ws = wb.worksheets[i]

            # Updates the anime sheet's days with the current date and appropriate colors
            if i == 0:
                d = [self.date_conv(0, 0, end_date=row.value) for row in ws['D'][1:]]
                for row, val in enumerate(d, start=2):
                    ws.cell(row=row, column=2, value=val)
                wb.save(self.file)
                b = [row.value for row in ws['B']][1:]
                for row, val in enumerate(b, start=2):
                    val = int(val)
                    curr = ws.cell(row=row, column=2)
                    if val < 0:
                        curr.fill = MediaList.black
                        curr.font = MediaList.white_text
                    elif 0 <= val <= 15:
                        curr.fill = MediaList.green
                    elif 15 <= val <= 50:
                        curr.fill = MediaList.yellow
                    else:
                        curr.fill = MediaList.red
                    wb.save(self.file)
            else:
                # Updates the other sheets with the appropriate colors
                b = [row.value for row in ws['B']][1:]
                for row, val in enumerate(b, start=2):
                    curr = ws.cell(row=row, column=2)
                    val = float(val)
                    if 7 < val:
                        curr.fill = MediaList.green
                    elif 5 <= val <= 7:
                        curr.fill = MediaList.yellow
                    elif 2 <= val <= 4:
                        curr.fill = MediaList.red
                    else:
                        curr.fill = MediaList.black
                        curr.font = MediaList.white_text
                    wb.save(self.file)
        wb.save(self.file)

    @timer
    def push(self, ani_num):
        # Checks if the file exists and creates a workbook if it doesn't exit
        try:
            wb = load_workbook(self.file)
        except FileNotFoundError:
            wb = self.create_wb()
        ws = wb.worksheets[0]

        # Checks if the anime is already in the list
        if ani_num in [i.value for i in ws['G']]:
            print('Anime already in list')
            return

        # Gets the necessary details
        data = self.web_scraper(ani_num)

        # Finds the empty row
        start_row = self.find_empty_row(ws)

        # Inserts the information and calls update
        for col, val in enumerate(data, start=1):
            ws.cell(row=start_row, column=col, value=val)
        wb.save(self.file)
        self.update(range(0, 1))


if __name__ == '__main__':
    person1 = MediaList()
    person1.score('Witcher 3,10',1)