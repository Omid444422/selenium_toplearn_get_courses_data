from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from time import sleep
import json

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://toplearn.com/TodayDiscounts')

courses_list = list()

courses = driver.find_elements(By.XPATH,'//*[@id="filter-search"]/div[3]/div/div/div/div')

for single_course in courses:
    driver.execute_script("arguments[0].scrollIntoView();", single_course)
    sleep(1)

    single_course_title = single_course.find_element(By.XPATH,'.//h2').text
    single_course_discount = single_course.find_element(By.XPATH,'.//a[@class="discount"]').text
    single_course_price_without_discount = single_course.find_element(By.XPATH,'.//span[@class="price"]/i').text
    single_course_price_with_discount = single_course.find_element(By.XPATH,'.//del').text

    single_course_data = {'title':single_course_title,'discount':single_course_discount,'price_without_discount':single_course_price_without_discount,'price_with_discount':single_course_price_with_discount}

    print(single_course_data)

    courses_list.append(single_course_data)


courses_list_json = json.dumps(courses_list,ensure_ascii=False)

with open('./toplearn_courses_with_free.json','w',encoding='utf-8') as toplearn_courses_with_free:
    toplearn_courses_with_free.write(courses_list_json)

print('successfully ended')




    


