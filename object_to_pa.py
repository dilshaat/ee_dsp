import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

## Initiating Chrome WebDrive
driver = webdriver.Chrome(r'C:\WebDrivers\chromedriver.exe')
# Give the URL or IP address of your website below
driver.get('http://10.1.1.225/dsp/Virtual.aspx')
# WebDrive will wait max 30 seconds and periodically polls the DOM to find the elements requested
driver.implicitly_wait(10)

## Login to DSP section
# first locate username and password field on the page
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('passwd')
login_button = driver.find_element_by_id('login-button')

# passing login credentials
username.send_keys('administrator')
password.send_keys('Br3wst3r')
login_button.click()

## Registering Objects
# making sure Sliding Icon is selected, treeNode view may fail
slidingIcon = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '//*[@id="sidebarSlidingIcon"]')))
slidingIcon.click()
# selecting 'dspMigrate' App
dspMigrate = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,
                                                                       '//*[@id="navigationview"]/span[4]/span')))
dspMigrate.click()

# Adding Objects to Specified Process Area
select_pa = driver.find_element_by_xpath("//*[starts-with(text(), 'PTP')]/parent::td/following-sibling::td[@positionindex='5']")
select_pa.click()
time.sleep(1)

def associate_object_pa(name, priority, comment):
    add_object_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[1]/div/span')))
    add_object_button.click()

    choose_input = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class, "select2-choice select2-default")]')))
    choose_input.click()
    choose_input.send_keys(name)
    time.sleep(1)
    choose_input.send_keys(Keys.ENTER)
    priority_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/input')
    priority_input.send_keys(priority)
    comment_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/input')
    comment_input.send_keys(comment)
    time.sleep(1)
    save_obj_button = driver.find_element_by_xpath('//*[@id="Save"]/div/span')
    save_obj_button.click()
    data_source_id = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/div/a/span')))
    report_data_source_id_text = data_source_id.text
    print(report_data_source_id_text)
    report_id_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/table/tbody/tr[4]/td[2]/div/input')
    report_id_input.send_keys(report_data_source_id_text)
    driver.find_element_by_xpath('/html/body/div[9]/div[1]/input').send_keys(Keys.ENTER)
    save_vertical = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[1]/div/span')
    save_vertical.click()
    time.sleep(1)

with open('test_object.csv', 'r') as f:
    lines = csv.reader(f, delimiter='\t')
    for line in lines:
        associate_object_pa(line[1], line[0], line[3])

#driver.close()

