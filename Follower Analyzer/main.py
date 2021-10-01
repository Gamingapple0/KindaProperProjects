# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from datetime import datetime
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Import These ^^^


def time_counter(func):
    def inner(*args):
        print(str(datetime.now())[11:19])
        func(args)
        print(str(datetime.now())[11:19])
    return  inner

def store(yes=True):
    new_followers_lst = []
    path = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://www.instagram.com/anshumadhikarmi/')

    # Logging In

    WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.LINK_TEXT,'Log In'))).click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys('madhikarmianshu@gmail.com')
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys('*****')
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]'))).click()
    time.sleep(4)
    driver.find_elements_by_tag_name('button')[1].click()

    # Follower List

    followers = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'followers')))
    follower_count = followers.text
    time.sleep(2)
    followers.click()
    time.sleep(5)
    x = 0
    driver.execute_script("a = document.getElementsByTagName('li')")
    while x < 350:
        try:
            driver.execute_script(f"a[{x}].scrollIntoView();")
            x += 5
            time.sleep(2)
        except:
            break
    time.sleep(2)
    follower_list = driver.find_elements_by_tag_name('li')

    # Computation

    if yes:
        f_list = list(map(lambda x : x.text.split()[0] + '\n',follower_list))
        with open('followers.txt', 'w') as lst:
            lst.writelines(f_list)
    else:
        for i in follower_list:
            new_followers_lst.append(i.text.split()[0])
        return new_followers_lst

@time_counter
def check(update=False):
    unfollowers = ''
    new_followers = ''
    with open('followers.txt','r') as followers:
        previous_followers_list = map(lambda x: x.replace('\n',''),followers.readlines())
        previous_followers_list1 = list(previous_followers_list)
    new_followers_list = store(False)
    for follower in previous_followers_list:
        if follower not in new_followers_list:
            unfollowers += follower + '\n'
    for follower1 in new_followers_list:
        if follower1 not in previous_followers_list1:
            new_followers += follower1 + '\n'
    print(f"""Unfollowers: \n\n{unfollowers}""")
    print(f"""New followers: \n\n{new_followers}""")
    if update:
        for i in new_followers_list:
            with open('followers.txt', 'a') as lst:
                lst.writelines(i.split()[0] + '\n')

# Use check() to check without updating the text file
# Use check(True) to check and update the text file

check()