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
    # options.add_argument('--headless')

    # e.g. Chrome path in Mac =/Users/x/Library/xx/Chrome/Default/
    # options.add_argument( "--user-data-dir=<Your chrome profile>")
    # options.add_argument("--user-data-dir=D:/Adrian/User_Data")
    options.add_argument(r"--user-data-dir=D:\Python\git\Random_Scripts\teamSpirit\User_Data")
    options.add_argument('--profile-directory=Profile 1')

    driver = uc.Chrome(options=options)

    time.sleep(4)
    url='https://stco-group.my.salesforce.com/home/home.jsp'
    # url = "https://google.com"
    driver.get(url)
    
    
    # driver.get("https://stco-group.my.salesforce.com/home/home.jsp")


    # menu1 = driver.find_element_by_xpath("//svg[@class='gb_Ve']")
    # menu1.click()
    time.sleep(2)

    # driver.find_element_by_link_text("TeamSpirit").click()
    # time.sleep(200)
        
    # menu1 = driver.find_element_by_xpath("//*[@id='gbwa']/div[1]/a")
    # menu1.click() 
    # menu2 = driver.find_element_by_xpath("//*[@id='gb23']/span[1]")
    # menu2.click() 
    time.sleep(2)

    # driver.find_element_by_xpath("//button[@class='button mb24 secondary wide']").click()
    # driver.find_element_by_xpath('//button[contains(text(), "Google Workspace")]').click()


    ts = driver.find_element(By.XPATH, "//*[contains(@class, 'button mb24 secondary wide') and contains(., 'Google Workspace')]")
    ts.send_keys("\n")

    time.sleep(5)
    # driver.save_screenshot("test2.png")
    # time.sleep(200)
    ks = driver.find_element_by_xpath("//a[@title='勤怠打刻']")
    ks.send_keys("\n")
    time.sleep(5)
    # ids = driver.find_elements_by_xpath('//button[@id]')
    ids = driver.find_element_by_xpath("//*[@id='remarks']")
    # ids.click()

    # for id in ids:
    #     print(id)
    #     print(id.get_attribute('class'))

    # driver.find_element_by_xpath("//input[@title='出社打刻']")
    # driver.find_element_by_xpath("//input[@type='button' and @value='出勤']")
    # driver.find_element_by_id("pushStart").click()

    
    time.sleep(2)
    driver.close()