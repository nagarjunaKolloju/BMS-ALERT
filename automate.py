from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import datetime
import random

t1 = datetime.datetime.now()
t = t1.strftime("%d")
t = int(t)
x = "Tirupati"
y = "Radhe Shyam"
z = "23"
z = int(z)
n = "1"
n = int(n)
# m = "BVK"
upi = "9502243031@ybl"

email = "ninjaforyou69@gmail.com"
pno = "9502243031"
# //*[@id = "super-container"]/div[2]/div/div[2]/div/div/ul/li[2]/section[2]/div[1]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path="chromedriver")
wait = WebDriverWait(driver, 60)
driver.maximize_window()

# for opening the desired city
driver.get("https://in.bookmyshow.com/"+x)
# print("here")
print(driver.title)

# driver.implicitly_wait(5)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='wzrk-cancel']")))
# for eliminating the popup
print("1")
try:
    driver.find_element(by=By.XPATH, value="//*[@id='wzrk-cancel']").click()
except:
    print("No Pop-Up detected")

driver.find_element(by=By.XPATH, value="//*[@id='2']").click()
# wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//*[@id='super-container']/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/input")))
# for putting in the movie name
show = driver.find_element_by_xpath(
    "//*[@id='super-container']/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/input")
show.send_keys(y)
driver.implicitly_wait(1)
show.send_keys(Keys.RETURN)
print("3")
driver.find_element(
    by=By.XPATH, value="//*[@id='super-container']/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/ul/li/div").click()
driver.find_element(
    by=By.XPATH, value="//*[@id='page-cta-container']/button").click()
# for 3d imax pop-up
# try:
#     wait.until(EC.element_to_be_clickable(
#         (By.XPATH, "//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[2]/section[2]/div[1]")))
#     driver.find_element(
#         by=By.XPATH, value="//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[2]/section[2]/div[1]").click()
# except:
#     pass
try:
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='showDates']/div/div/li[4]")))
    driver.find_element(
        by=By.XPATH, value="//*[@id='showDates']/div/div/li[4]").click()
except:
    pass
try:
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//*[@id='showDates']/li[1]")))
    driver.find_element_by_xpath("//*[@id='showDates']/li[1]").click()
except:
    print("The show is not available on th current date :(")


# wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fltrsearch']")))
# select = driver.find_element_by_xpath("//*[@id='fltrsearch']")

# if m != "none":
#     select.send_keys(m)
#     select.send_keys(Keys.RETURN)

try:
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='venuelist']/li[1]/div[2]/div[2]/div[1]")))
    driver.find_element_by_xpath(
        "//*[@id='venuelist']/li[1]/div[2]/div[2]/div[1]").click()

except:

    try:
        wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "//*[@id='venuelist']/li[1]/div[2]/div[2]/div[2]")))

        driver.find_element_by_xpath(
            "//*[@id='venuelist']/li[1]/div[2]/div[2]/div[2]").click()

    except:
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='venuelist']/li[1]/div[2]/div[2]/div[3]")))
            driver.find_element_by_xpath(
                "//*[@id='venuelist']/li[1]/div[2]/div[2]/div[3]").click()
        except:
            try:
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='venuelist']/li[1]/div[2]/div[2]/div[4]")))
                driver.find_element_by_xpath(
                    "//*[@id='venuelist']/li[1]/div[2]/div[2]/div[4]").click()
            except:
                pass
# #venuelist > li:nth-child(4) > div.body > div:nth-child(1) > a
# #venuelist > li:nth-child(1) > div.body > div > a


try:
    driver.find_element_by_xpath("//*[@id='btnPopupAccept']").click()
except:
    print("No Acceptance")


# for no. of seats
if n == 1:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_1']")))
    driver.find_element_by_xpath("//*[@id='pop_1']").click()
elif n == 2:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_2']")))
    driver.find_element_by_xpath("//*[@id='pop_2']").click()
elif n == 3:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_3']")))
    driver.find_element_by_xpath("//*[@id='pop_3']").click()
elif n == 4:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_4']")))
    driver.find_element_by_xpath("//*[@id='pop_4']").click()
elif n == 5:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_5']")))
    driver.find_element_by_xpath("//*[@id='pop_5']").click()
elif n == 6:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_6']")))
    driver.find_element_by_xpath("//*[@id='pop_6']").click()
elif n == 7:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_7']")))
    driver.find_element_by_xpath("//*[@id='pop_7']").click()
elif n == 8:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_8']")))
    driver.find_element_by_xpath("//*[@id='pop_8']").click()
elif n == 9:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_9']")))
    driver.find_element_by_xpath("//*[@id='pop_9']").click()
elif n == 10:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pop_10']")))
    driver.find_element_by_xpath("//*[@id='pop_10']").click()


wait.until(EC.element_to_be_clickable((By.ID, "proceed-Qty")))
# for confirming seats
driver.find_element_by_id("proceed-Qty").click()


# #venuelist > li:nth-child(4) > div.body > div:nth-child(1) > a

seat = driver.find_elements_by_css_selector("a._available")
print(seat)
length = len(seat)

r = 0
while 1:
    try:
        seat[r].click()
    except:
        pass
    r = r + 1
    x = driver.find_element_by_id("btmcntbook")
    if x.is_displayed():
        x.click()
        break
driver.implicitly_wait(3)


# wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='prePay']")))
driver.find_element_by_xpath("//*[@id='prePay']").click()
print("correct")
# for email and phone no.
# wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='txtEmail']")))
driver.find_element_by_xpath("//*[@id='txtEmail']").send_keys(email)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='txtMobile']")))
driver.find_element_by_xpath("//*[@id='txtMobile']").send_keys(pno)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='dContinueContactSec']/a")))
driver.find_element_by_xpath("//*[@id='dContinueContactSec']/a").click()

driver.find_element_by_xpath("//*[@id='dTOtherWallets']").click()

driver.find_element_by_xpath(
    "//*[@id='dOtherWalletsListing']/aside[4]").click()
driver.find_element_by_xpath(
    "//*[@id='dDOtherWallets']/button").click()

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='vpa-content']/div/div[2]/div[2]")))
driver.find_element_by_xpath(
    "//*[@id='vpa-content']/div/div[2]/div[2]").click()
show = driver.find_element_by_xpath(
    "//*[@id='vpaInput']")
show.send_keys(upi)
driver.implicitly_wait(1)
show.send_keys(Keys.RETURN)


wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='vpa-content']/div/div[2]/div[3]/button")))
driver.implicitly_wait(20)
driver.find_element_by_xpath(
    "//*[@id='vpa-content']/div/div[2]/div[3]/button").click()
