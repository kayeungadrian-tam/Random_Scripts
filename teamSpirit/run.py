from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
# options = Options()
# options.add_argument('--headless')
# options.add_argument("--user-data-dir=D:/Adrian/User Data")
# options.add_argument(r'--profile-directory=Profile 3')
# driver = uc.Chrome(
#     executable_path='../PowerPoint/chromedriver.exe',
#     options=options
#     )
# # driver.execute_script("window.open('https://calendar.google.com/calendar/u/0/r?tab=rc');")


# # driver.get("https://stco-group.my.salesforce.com/home/home.jsp")
# driver.get("https://google.com")

# time.sleep(2)



# driver.save_screenshot("./test.png")


# driver.close()

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument('--headless')

    # e.g. Chrome path in Mac =/Users/x/Library/xx/Chrome/Default/
    # options.add_argument( "--user-data-dir=<Your chrome profile>")
    # options.add_argument("--user-data-dir=D:/Adrian/User_Data")
    # options.add_argument(r"--user-data-dir=D:\Python\git\Random_Scripts\teamSpirit\User_Data")
    # options.add_argument('--profile-directory=Profile 1')

    driver = uc.Chrome(options=options)
    driver.maximize_window()
    time.sleep(4)
    url='https://login.salesforce.com/'
    # url = "https://google.com"
    driver.get(url)
    
    
    # driver.get("https://stco-group.my.salesforce.com/home/home.jsp")


    # menu1 = driver.find_element_by_xpath("//svg[@class='gb_Ve']")
    # menu1.click()
    time.sleep(2)

    # driver.find_element_by_link_text("TeamSpirit").click()
    # time.sleep(200)
        
    user_name = driver.find_element_by_xpath("//*[@id='username']")
    password = driver.find_element_by_xpath("//*[@id='password']")
    
    user_name.send_keys("kayeungadrian.tam.mr@ambl.group") 
    password.send_keys("Maths@152631") 
    
    
    menu2 = driver.find_element_by_xpath("//*[@id='Login']")
    menu2.click() 


    time.sleep(2)


    ks = driver.find_element_by_xpath("//a[@title='勤怠打刻']")
    ks.send_keys("\n")



    time.sleep(1)

    iframe = driver.find_element_by_xpath("//*[@id='06610000000rDxW']")
    driver.switch_to.frame(iframe)


    time.sleep(1)

    tmp = driver.find_element_by_xpath("//*[@id='btnStInput']")
    # tmp.click() 

    time.sleep(1)

    driver.switch_to.default_content()

    

    ts = driver.find_element(By.XPATH, "//*[contains(@id, '01r10000000bu9k_Tab')]")
    ts.click()


    time.sleep(1)

    date = "dateRow2022-05-09"

    ts = driver.find_element(By.XPATH, "//*[contains(@id, '" + date + "')]")

    ttt = (ts.text).replace("\n", " ").split(" ")

    print(ttt)

    driver.save_screenshot("test2.png")
