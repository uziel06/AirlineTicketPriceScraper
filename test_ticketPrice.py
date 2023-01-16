from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import smtplib
import time


#Driver Setup
service_obj = Service("C:\\browserDrivers\\chromedriver.exe")#locate webdriver folder
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(30)
driver.get("https://www.google.com/travel/explore?tfs=CBwQAxoxag0IAxIJL20vMDE5NXBkEgoyMDIzLTAyLTAxcgwIBBIIL20vMDV2OGMyAjVKMgJERxoxagwIBBIIL20vMDV2OGMSCjIwMjMtMDItMDVyDQgDEgkvbS8wMTk1cGQyAjVKMgJER3ABggELCP___________wFAAUgBmAEBsgEEGAEgAQ&tfu=GioaKAoSCda1pfkBJTNAEbGAYPJP12FAEhIJwdqW_WHSGEARYgHB5L8OXEA&hl=en&gl=ae&curr=PHP")


#Cleaning ticket price
ticketPrice = []
prices = driver.find_elements(By.XPATH, "//div[@class='MJg7fb']/span/span")

for price in prices:
    ticketPrice.append(int(price.text.replace(',', '').replace('₱', '')))

#Cleaning location list
locationList = []
locations = driver.find_elements(By.XPATH, "//div[@class='tsAU4e ']/div/h3")

for location in locations:
    locationList.append(location.text)
    for loc in locationList:
        if loc == '':
            locationList.remove(loc)

#Combining location and ticket price
locationPriceDict = dict(zip(locationList, ticketPrice))

#Filtering Dictionary
for key, value in dict(locationPriceDict).items():
    if value > 5000:
        del locationPriceDict[key]
print(locationPriceDict)

time.sleep(5)
driver.close()

server = smtplib.SMTP("smtp.gmail.com", port = 587)

emailUser = ""#yourEmail
emailPassword = ""#yourEmailPassword

server.starttls()
server.login(user = emailUser, password = emailPassword)

msg = f'From: {emailUser}\r\nTo: {emailUser}\r\n\r\n{locationPriceDict}'
server.sendmail(emailUser, emailUser, msg)
server.quit()

print("Email sent!")






