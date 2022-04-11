from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
import time


options = ChromeOptions()
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。

driver = Chrome(
    executable_path=r'.\chromedriver.exe',
    options=options
    )
driver.maximize_window()
time.sleep(2)
# driver = Chrome(options=options)

# Googleのトップ画面を開く。
driver.get('https://bible.prsi.org/ja/Account/Login')

driver.find_element_by_id("Email").send_keys("mine.mail.444@gmail.com")
driver.find_element_by_id("Password").send_keys("Atam1526")
driver.find_element_by_xpath("//input[@type='submit' and @value='ログイン']").click()
time.sleep(2)



driver.find_element_by_id("location_book").click()
time.sleep(2)


driver.save_screenshot('chrome_search_results.png')


exit()

# タイトルに'Google'が含まれていることを確認する。
assert 'Google' in driver.title

# 検索語を入力して送信する。
input_element = driver.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# タイトルに'Python'が含まれていることを確認する。
assert 'Python' in driver.title

# スクリーンショットを撮る。
driver.save_screenshot('chrome_search_results.png')

# 検索結果を表示する。
for a in driver.find_elements_by_css_selector('h3 > a'):
    print(a.text)
    print(a.get_attribute('href'))

driver.quit()  # ブラウザーを終了する。