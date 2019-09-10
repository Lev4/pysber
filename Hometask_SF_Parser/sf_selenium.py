import time 
from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd 
from tqdm import tqdm
driver = webdriver.Chrome('/Users/Lev4/Projects/sf/chromedriver')
driver.get('https://career18.sapsf.com/career?company=paosberbanP2&career%5fns=job%5flisting%5fsummary&navBarLevel=JOB%5fSEARCH&_s.crb=eNF2RDteQlax9i2Gd%2bBFITz3RuU%3d')
time.sleep(3)

vac_ids = []
vac_nums = driver.find_element_by_class_name("jobCount")
vac_nums = vac_nums.text

s1= Select(driver.find_element_by_id('41:'))
s1.select_by_index(4)
time.sleep(5)

# "40:_pageIndex"
last_page_index = driver.find_elements_by_id("40:_pageIndex")
last_page_index = last_page_index[0].text
last_page_index = last_page_index.split(' ')[-1]
last_page_index = int(last_page_index)


for i in tqdm(range(last_page_index - 1)):
    desc = driver.find_elements_by_class_name("jobContentEM")

    for el in desc:
        if len(el.text) == 6:
            flag_is_not_digit = 0
            for symbol in el.text:
                if not symbol.isdigit():
                    flag_is_not_digit = 1
            if flag_is_not_digit == 0:
                vac_ids.append(el.text)

    btn_next = driver.find_element_by_id("40:_next")
    btn_next.click()

    if i < 10:
        sleep_seconds = 5
    elif i < 20:
        sleep_seconds = 7
    else:
        sleep_seconds = 10

    time.sleep(sleep_seconds)

pd.DataFrame({'ids':vac_ids}).to_excel('vac_id.xlsx', index=False)

driver.quit()

