import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import datetime

import random
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# SENDGRID_KEY = 'YORU-API-KEY-HERE'
import io


def send_mail():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox11f72a48f8bb44ec81834fc71cbabf61.mailgun.org/messages",
        auth=("api", "110b22b11f4bb2e40e60f90ced220f1f-0677517f-15ef2a9e"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox11f72a48f8bb44ec81834fc71cbabf61.mailgun.org>",
              "to": "Nagarjuna <ninjaforyou69@gmail.com>"
              "subject": "ALERT BRO !!!!!!",
              "text": "RRR Bookings are open ! Just go grab some!!!"})


def book_tickets():
    t1 = datetime.datetime.now()
    t = t1.strftime("%d")
    t = 28
    x = "Tirupati"
    y = "RRR"
    # z = "2"
    # z = int(z)
    n = "3"
    n = int(n)
    # m = "BVK"
    upi = "7995730200@ybl"

    email = "ninjaforyou69@gmail.com"
    pno = "9502243031"
    # //*[@id = "super-container"]/div[2]/div/div[2]/div/div/ul/li[2]/section[2]/div[1]

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument(
        r"user-data-dir=C:\\Users\\ninja\\AppData\\Local\\Google\\Chrome\\User Data")
    chrome_options.add_argument(r'--profile-directory=Profile 7')
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--allow-http-screen-capture")
    # chrome_options.add_argument("--disable-impl-side-painting")
    # chrome_options.add_argument("--disable-setuid-sandbox")
    # chrome_options.add_argument("--disable-seccomp-filter-sandbox")

    driver = webdriver.Chrome(options=chrome_options,
                              executable_path="chromedriver")
    wait = WebDriverWait(driver, 60)
    driver.maximize_window()

    # for opening the desired city
    driver.get("https://in.bookmyshow.com/"+x)
    # print("here")
    print(driver.title)

    # driver.implicitly_wait(5)
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//*[@id='wzrk-cancel']")))
    # # for eliminating the popup
    # print("1")
    # try:
    #     driver.find_element(
    #         by=By.XPATH, value="//*[@id='wzrk-cancel']").click()
    # except:
    #     print("No Pop-Up detected")

    driver.find_element(
        by=By.XPATH, value="//*[@id='super-container']/div[2]/header/div[1]/div/div/div/div[2]/div[2]/div[1]").click()

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='modal-root']/div/div/div/div")))
    sleep(2)
    # wait.until(EC.visibility_of_element_located(
    #     (By.XPATH, "//*[@id='modal-root']/div/div/div/div/div[2]/div/div[1]/div/div[1]")))
    # wait.until(EC.element_to_be_clickable(
    #     (By.XPATH, "//*[@id='modal-root']/div/div/div/div/div[2]/div/div[1]/div/div[1]")))
    driver.find_element(
        By.XPATH, "//*[@id='modal-root']/div/div/div/div/div[2]/div/div[1]/div/div[1]").click()
    sleep(4)
    print("here")

    # # Wait for the new window or tab
    # wait.until(EC.number_of_windows_to_be(2))

    # # new window handle
    # original_window = driver.current_window_handle
    # for window_handle in driver.window_handles:
    #     if window_handle != original_window:
    #         driver.switch_to.window(window_handle)
    #         break

    # show = driver.find_element_by_xpath(
    #     "//*[@id='identifierId']")
    # show.send_keys(email)
    # driver.implicitly_wait(1)
    # show.send_keys(Keys.RETURN)

    # driver.find_element(
    #     by=By.XPATH, value="//*[@id='identifierNext']/div/button/span").click()
    # sleep(2)
    # show = driver.find_element_by_xpath(
    #     "//*[@id='password']/div[1]/div/div[1]/input")
    # show.send_keys("Arjun@3031")
    # driver.implicitly_wait(1)
    # show.send_keys(Keys.RETURN)

    # driver.find_element(
    #     by=By.XPATH, value="//*[@id='passwordNext']/div/button/div[3]").click()

    # driver.close()
    # driver.switch_to.window(original_window)

    #
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
    # driver.find_element(
    #     by=By.XPATH, value="//*[@id='quickbook-wrapper']/div[1]/div[1]/span[1]/div/div/div[2]/span[2]").click()
    # for 3d imax pop-up
    try:
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[3]/section[2]/div[2]")))
        driver.find_element(
            by=By.XPATH, value="//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[3]/section[2]/div[2]").click()
    except:
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[3]/section[2]/div[1]")))
            driver.find_element(
                by=By.XPATH, value="//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[3]/section[2]/div[1]").click()
        except:

            try:
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[2]/section[2]/div[2]")))
                driver.find_element(
                    by=By.XPATH, value="//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[2]/section[2]/div[2]").click()
            except:
                try:
                    wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[2]/section[2]/div[1]")))
                    driver.find_element(
                        by=By.XPATH, value="//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[2]/section[2]/div[1]").click()
                except:
                    try:
                        wait.until(EC.element_to_be_clickable(
                            (By.XPATH, "//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[1]/section[2]/div[2]")))
                        driver.find_element(
                            by=By.XPATH, value="//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[1]/section[2]/div[2]").click()
                    except:
                        try:
                            wait.until(EC.element_to_be_clickable(
                                (By.XPATH, "//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[1]/section[2]/div[1]")))
                            driver.find_element(
                                by=By.XPATH, value="//*[@id='super-container']/div[2]/div/div[2]/div/div/ul/li[1]/section[2]/div[1]").click()
                        except:
                            pass

        # tr

    #     wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//*[@id='showDates']/div/div/li[4]")))
    #     driver.find_element(
    #         by=By.XPATH, value="//*[@id='showDates']/div/div/li[4]").click()
    # except:
    #     pass
    # try:
    #     # wait.until(EC.element_to_be_clickable(
    #     #     (By.XPATH, "//*[@id='showDates']/li[1]")))
    #     driver.find_element_by_xpath("//*[@id='showDates']/li[1]").click()
    # except:
    #     print("The show is not available on th current date :(")

    # wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fltrsearch']")))
    # select = driver.find_element_by_xpath("//*[@id='fltrsearch']")

    # if m != "none":
    #     select.send_keys(m)
    #     select.send_keys(Keys.RETURN)
    # check for date

    driver.find_element_by_xpath(
        "//*[@id='showDates']/div/div/li[4]/a").click()
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
    # driver.find_element_by_xpath("//*[@id='txtEmail']").send_keys(email)
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
    sleep(300)


while(True):
    res = requests.get(
        'https://in.bookmyshow.com/buytickets/rrr-tirupati/movie-tiru-ET00094579-MT/20220325')
    # print(type(res.text))
    # print('he')
    if(res.text.find('4k') != -1):
        print("BOOKINGS ARE NOW OPEN!")
        send_mail()
        book_tickets()
        break
    else:
        print("Bookings not open yet")
    sleep(60)
