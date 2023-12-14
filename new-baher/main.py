from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import time

user="mezzat@gharably.com"
password="M-ezzat5656"
website='https://id.eta.gov.eg/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3D9A029E3B-7403-4B25-8850-AB67E1FD92AB%26redirect_uri%3Dhttps%253A%252F%252Finvoicing.eta.gov.eg%252Flogin%26response_type%3Did_token%2520token%26scope%3Dopenid%2520profile%2520publicportals.bff.api%26state%3Dab6adef33db84d8fadb38a4fcdd59838%26nonce%3D2cc8ca01c70a4763910f38d563e78604'
service=Service()
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service,options=options)
driver.get(website)
actions = ActionChains(driver)
######## Login page✅
user_name=driver.find_element(by="xpath",value='//*[@id="email"]')
user_name.send_keys(user)
password_input=driver.find_element(by="xpath",value='//*[@id="Password"]')
password_input.send_keys(password)
login=driver.find_element(by="xpath",value='//*[@id="submit"]')
login.click()
time.sleep(3)
invoices=driver.find_element(by="xpath",value='//*[@id="invoices"]')
invoices.click()
time.sleep(3)
doc=driver.find_element(by="xpath",value='//*[@id="recentDocuments"]')
doc.click()
time.sleep(5)

##################
######### el 100 ❌
dropdown=(driver.find_element(By.CLASS_NAME,value='ms-Dropdown-container'))
dropdown.click()
actions.send_keys(Keys.PAGE_DOWN).perform()
actions.send_keys(Keys.PAGE_DOWN).perform()
actions.send_keys(Keys.PAGE_DOWN).perform()
actions.send_keys(Keys.ENTER).perform()
# time.sleep(3)
# drop_container=driver.find_element(By.ID,value="Dropdown158-list")
# but=drop_container.find_element(By.XPATH,value="/html/body/div[4]/div/div/div/div/div/div/button[4]")
# but.click()
time.sleep(5)
############

####### scroll to bottom

SCROLL_PAUSE_TIME = 20

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


#############

######### Extracting el data ✅

table=driver.find_element(By.CLASS_NAME,value='ms-List-page')
documents=table.find_elements(By.CLASS_NAME,value='griCellSubTitle')
titles=table.find_elements(By.CLASS_NAME,value='griCellTitleGray')
ids=table.find_elements(By.CLASS_NAME,value='griCellTitle')
x=[]
y=[]
z=[]
for id in ids:
    z.append(id.text)

for document in documents:
    y.append(document.text)
for title in titles:
    x.append(title.text)

print(x)
print(y)
#################
######### Exporting to csv ✅
id=(y[::5])
date=(x[::5])
time=(y[1::5])

type=(x[1::5])
total_value=(x[2::5])
issuer=(x[3::5])
reciver=(x[4::5])

issuer_code=(y[3::5])
reciver_code=(y[4::5])

df=pd.DataFrame({'ID':z,
                 'Internal_id':id,
                 'Date':date,
                 'Time':time,
                 'Type':type,
                 'Total_value':total_value,
                 'Issuer':issuer,
                 'Reciver':reciver,
                 'Issuer_code':issuer_code,
                 'Reciver_code':reciver_code})

df.to_csv('baher.csv',encoding='utf-8',index=False)

###########################