# Completion time 2 mins lol
class LinearSearch:
    def __init__(self,array,sel):
        self.array = array
        self.sel = sel
        self.res = None
        self.sort()

    def __str__(self):
        return str(self.res)

    def sort(self):
        for i in range(len(self.array)):
            if self.array[i] == self.sel:
                self.res = i
                return

if __name__ == '__main__':
    arr = [2, 1, 4, 5, 6, 7, 1, 0, 4, 9, 3, 8, 11, 2, 10, 34, 6, 22, 34, 67, 86, 42]
    a = LinearSearch(arr,7)
    print(a)