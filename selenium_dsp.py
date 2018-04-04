import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

# selecting 'Elements' in Console App
elements = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                            '//*[@id="navigationview"]/span[2]/span[2]')))
elements.click()

# seleing 'Objects' in Element section

objects = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                           '//*[@id="navigationview"]/span[2]/span[2]')))
objects.click()

# Clicking 'Add' object button
try:
    time.sleep(2)
    add_object_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/div/span')
    add_object_button.click()
    object_name = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="detailWID_1151685457_ObjectsDetail"]/div[2]/table/tbody/tr[2]/td[2]/input')))
    object_descriptioin = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="detailWID_1151685457_ObjectsDetail"]/div[2]/table/tbody/tr[3]/td[2]/input')))
    object_comment = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="detailWID_1151685457_ObjectsDetail"]/div[2]/table/tbody/tr[5]/td[2]/input')))
    object_name.send_keys('EAM-AAAA')
    object_descriptioin.send_keys('EAM AAAA Test')
    object_comment.send_keys('EAM AAAA Comment')
    driver.find_element_by_xpath('//*[@id="Save"]/div/span').click()
    edit = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'Edit')))
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div/div[1]/div[1]/span[1]').click()
except Exception:
    print("Add button not found")
