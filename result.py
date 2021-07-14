# JAI BAJARANG BALI

# 

from selenium import webdriver
import time
url='http://rajasthan-10th-result.indiaresults.com/rj/bser/class-10-result-2020/query.htm'
file=open('results.csv','w')

file.write("NAME,fathes's name,HINDI,ENGLISH,SCIENCE,SOCIAL SCIENCE,MATHEMATICS,SANSKRIT,TOTAL_MARKS,PERCENTAGE\n")

starting_roll_no=int(input())
ending_roll_no=int(input())

for i in range(starting_roll_no,ending_roll_no+1):
    web= webdriver.Chrome('chromedriver.exe')
    web.get(url)
    # time.sleep(3)
    time.sleep(2)
    Roll_no=str(i)

    roll=web.find_element_by_xpath('//*[@id="rollquery"]/table/tbody/tr[1]/td[2]/input')
    roll.send_keys(Roll_no)
    
    submit=web.find_element_by_xpath('//*[@id="rollquery"]/table/tbody/tr[1]/td[3]/button')

    submit.click()
    student_name=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[3]/td[2]/font/font')
    father_name=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[4]/td[2]/font')
    hindi=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[11]/td[4]/font')
    english=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[12]/td[4]/font')
    maths=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[15]/td[4]/font')
    science=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[13]/td[4]/font')
    social_science=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[14]/td[4]/font')
    sanskrit=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[16]/td[4]/font')
    total_marks=web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[19]/td[2]/font/font')
    total_percentage = web.find_element_by_xpath('//*[@id="table97"]/tbody/tr[20]/td[2]/font')


    
    file.write(student_name.text)
    file.write(",")
    file.write(father_name.text)
    file.write(",")
    file.write(hindi.text)
    file.write(",")
    file.write(english.text)
    file.write(",")
    file.write(science.text)
    file.write(",")
    file.write(social_science.text)
    file.write(",")
    file.write(maths.text)
    file.write(",")
    file.write(sanskrit.text)
    file.write(",")
    file.write(total_marks.text)
    file.write(",")
    file.write(total_percentage.text)
    file.write("%\n")

    web.close()
    

file.close()