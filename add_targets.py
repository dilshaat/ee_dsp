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
#driver = webdriver.Firefox()
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

design = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]')))
design.click()
target = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div/div/span')))
target.click()


def add_targets_bulk(object_name, prioriy, target_name, desc):
    add_button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/span')))
    add_button.click()
    time.sleep(1)
    object_id = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/div/a/span[2]/b')))
    object_id.click()
    object_list = driver.find_elements_by_xpath('//div[@class="select2-result-label"]')
    for obj in object_list:
        try:
            print(obj.text)
            if obj.text == object_name:
                obj.click()
        except:
            print("ignore this")

    priority_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/input')
    name_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[6]/input')
    desc_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[7]/input')
    priority_input.send_keys(prioriy)
    name_input.send_keys(target_name)
    desc_input.send_keys(desc)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/span').click()

with open('test_object.csv', 'r') as f:
    lines = csv.reader(f, delimiter='\t')
    for line in lines:
        add_targets_bulk(line[1], line[3], line[4], line[2])

time.sleep(3)
driver.close()