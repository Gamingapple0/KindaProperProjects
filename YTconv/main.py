# import os
# import time
# import tkinter as tk
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Import these ^^^

path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(path)


class YTPconv:
    def __init__(self, playlist_url, mp, dir_name):
        links = getLinks(playlist_url)
        names = converter(mp, links)
        time.sleep(20)  # To let the links download
        dirMker(dir_name, names, mp)


def getLinks(url):  # Returns a list of the links in the playlist
    driver.get(url)
    # Done because there are 2 ways to enter a playlist, one with the video playing and one without
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, 'ytd-playlist-panel-video-renderer')))
        vid_objects = driver.find_elements_by_css_selector('ytd-playlist-panel-video-renderer>a')
        vid_list = [vid.get_attribute('href') for vid in vid_objects]
    except:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'ytd-playlist-video-renderer')))
        vid_objects = driver.find_elements_by_css_selector(
            'ytd-playlist-video-renderer>#content>#container>#meta>h3>a')
        vid_list = [vid.get_attribute('href') for vid in vid_objects]
    return vid_list


def dirMker(d_name, vid_name_lst, mp):  # Saves the downloaded content in a named directory
    path = 'C:/Users/madhi/Downloads/'
    new_dir = path + d_name
    os.mkdir(new_dir)
    for name in vid_name_lst:
        name += f'.mp{mp}'
        try:
            os.rename(path + name, new_dir + f'/{name}')
        except:
            print('error')


def converter(mp, link_list):  # Takes the list of links and uses a third party website to convert
    vid_name_lst = []  # all of them and download them
    driver.get('https://ytmp3.cc/youtubetomp3/')
    if mp == 3:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'mp3'))).click()
    else:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'mp4'))).click()
    for link in link_list:
        # Sends an error message for the first iteration
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Convert next'))).click()
        except:
            pass
        driver.find_element_by_id('input').send_keys(link)
        driver.find_element_by_id('submit').click()
        time.sleep(0.8)  # To wait for the video name to load
        vid_name = driver.find_element_by_id('title').text
        vid_name_lst.append(vid_name)
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.ID, 'download'))).click()
        windows = len(driver.window_handles)
        # To switch between away from ads
        if windows > 1:
            driver.switch_to.window(driver.window_handles[0])
    return vid_name_lst


def gui():
    global root
    root = tk.Tk()
    root.geometry('550x300')

    url = tk.Label(root, text='Playlist URL:', font=('Arial', 14)).place(x=20, y=40)
    url_inp = tk.Entry(root, width=60)
    url_inp.place(x=140, y=45)  # Split so that focus set could be used
    url_inp.focus_set()

    dir = tk.Label(root, text='Directory Name:', font=('Arial', 14)).place(x=20, y=100)
    dir_inp = tk.Entry(root, width=30)

    button = tk.Button(root, text='Start', pady=10, padx=40, background='#9796a3',
                       command=lambda: initialize(url_inp.get(), dir_inp.get(), mp.get()))
    mp = tk.IntVar()
    tk.Radiobutton(root, text='MP3', variable=mp, value=3).place(x=20, y=150)
    tk.Radiobutton(root, text='MP4', variable=mp, value=4).place(x=75, y=150)

    dir_inp.place(x=170, y=105)
    button.place(x=20, y=205)

    root.mainloop()


def initialize(url, mp, dir):
    root.destroy()
    YTPconv(url, mp, dir)
