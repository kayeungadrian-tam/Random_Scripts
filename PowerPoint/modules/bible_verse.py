import json
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time
from loguru import logger
import re

def book_handle(book):    
    with open("./assets/books_dict.json", 'r', encoding='utf-8') as f:
        books_dict = json.load(f)
    data = books_dict[book]
    return data

def check_int(str):
        return any(chr.isdigit() for chr in str)

def clean_eng_text(text):
    idx = re.search(r"\d", text)
    if idx:
        text = text[idx.start():]
    else:
        text = text
    ref_pattern = r"\[(.*?)\]"
    refs = re.findall(ref_pattern, text)
    if refs:
        for ref in refs:
            text = text.replace(f"[{ref}]", "")
    return text
    

class OnlineBibleVerse():
    def __init__(self, credentials_path, ja_url):
        options = ChromeOptions()
        options.add_argument('--headless')
        self.driver = Chrome(options=options)
        self.eng_driver = Chrome(options=options)
        self.ja_login(credentials_path, ja_url)

    def ja_login(self, credentials_path, ja_url):
        with open(credentials_path, 'r', encoding='utf-8') as f:
            credentials = json.load(f)
        email = credentials["Email"]
        password = credentials["Password"]
        self.driver.get(ja_url)
        self.driver.find_element_by_id("Email").send_keys(email)
        self.driver.find_element_by_id("Password").send_keys(password)
        self.driver.find_element_by_xpath("//input[@type='submit' and @value='ログイン']").click()
        time.sleep(2)

    def get_verse_ja(self, book, chapter, verse):
        
        data = book_handle(book)
        book_id = int(data["idx"])
        
        book, chapter, verse = int(book_id)-1, int(chapter)-1, int(verse)-1
        self.driver.find_element_by_id("location_book").click()
        time.sleep(2)
        book_button = self.driver.find_element(By.XPATH, f"//div[@book='{book}']")
        book_button.click()
        time.sleep(2)
        chapter_button = self.driver.find_element(By.XPATH, f"//div[@chapter='{chapter}']")
        chapter_button.click()
        time.sleep(2)
        verse_button = self.driver.find_element(By.XPATH, f"//div[@verse='{verse}']")
        verse_button.click()
        time.sleep(2)
        id = f"v{str(book+1).zfill(2)}{str(chapter+1).zfill(3)}{str(verse+1).zfill(3)}"
        verse_id = id
        verse_text = self.driver.find_elements(By.XPATH, f"//verse[@id='{verse_id}']")
        keep = False
        text = ""
        for id, t in enumerate(verse_text):
            for k, v  in enumerate(t.text):
                if v == "\n":
                    keep = ~keep        
                if keep:
                    text += v
        return text.replace("\n", "")

    def get_verse_en(self, book, chapter, verse):
        en_text = ""
        data = book_handle(book)
        code = data["code"]
        if check_int(book):
            parts = book.split("-")
            url = f'https://www.biblegateway.com/passage/?search={parts[0]}%20{parts[1]}+{chapter}&version=ESV'
        else:
            url = f'https://www.biblegateway.com/passage/?search={book}+{chapter}&version=ESV'
        self.eng_driver.get(url)
        time.sleep(2)
        eng_id = f"text {code}-{chapter}-{verse}"
        
        eng = self.eng_driver.find_elements(By.XPATH, f"//span[@class='{eng_id}']")
        for i in range(len(eng)):
            en_text += eng[i].text
        en_text = clean_eng_text(en_text.replace("\n", ""))
        return en_text

    def verse_str(self, book, chapter, verse):
        data = book_handle(book)
        en_verse_str = f"{book} {chapter}:{verse}"     
        ja_verse_str = f"{data['ja']} {chapter}:{verse}" 
        return ja_verse_str, en_verse_str

    def close(self):
        self.driver.close()
        self.eng_driver.close()

def case1():
    book = "John"
    chapter = 1
    verse = 4
    logger.debug(f"Debugging single verse: {book} {chapter}:{verse}")

    data = book_handle(book)
    book_id = int(data["idx"])

    bv = OnlineBibleVerse("./assets/credentials.json", "https://bible.prsi.org/ja/Account/Login")
    logger.info("Logging in...")
    # bv.ja_login("./assets/credentials.json", "https://bible.prsi.org/ja/Account/Login")
    logger.info("Logged in.")

    for i in range(2):
        logger.info(f"Japanese verse: {book} {chapter}:{verse + i}")
        ja_verse = bv.get_verse_ja(book_id, chapter, verse + i)
        logger.info(ja_verse)

        logger.info(f"English verse: {book} {chapter}:{verse + i}")
        en_verse = bv.get_verse_en(book, data["code"], chapter, verse + i)
        logger.info(en_verse)

def case2():
    book = "John"
    chapter = 1
    verse = "2-5"
    logger.debug(f"Debugging multi verse: {book} {chapter}:{verse}")

    data = book_handle(book)
    book_id = int(data["idx"])

    verses = verse.split("-")

    bv = OnlineBibleVerse()
    logger.info("Logging in...")
    bv.ja_login("./assets/credentials.json", "https://bible.prsi.org/ja/Account/Login")
    logger.info("Logged in.")

    for v in range(int(verses[0]), int(verses[1])+1):
        logger.info(f"Japanese verse: {book} {chapter}:{v}")
        ja_verse = bv.get_verse_ja(book_id, chapter, v)
        logger.info(ja_verse)

        logger.info(f"English verse: {book} {chapter}:{v}")
        en_verse = bv.get_verse_en(book, data["code"], chapter, v)
        logger.info(en_verse)


def test():
    logger.add("logs/bible_verse.log", rotation="1 day")
    case1()
    case2()

if __name__ == "__main__":
    test()