import json
from tqdm import tqdm
from regex import P
from modules.bible_verse import OnlineBibleVerse
import re

def book_handle(book):    
    with open("./assets/books_dict.json", 'r', encoding='utf-8') as f:
        books_dict = json.load(f)
    data = books_dict[book]
    return data



def check_int(str):
        return any(chr.isdigit() for chr in str)



def main():
    book = input("Enter a book: ")

    chapter = int(input("Enter a chapter: "))
    verse = int(input("Enter a verse: "))
    # verse2 = int(input("Enter a verse: "))

    data = book_handle(book)

    book_id = int(data["idx"])

    log = open("test.log", "w")
    english = ""
    japanese = ""
    BibleVerse = OnlineBibleVerse()
    # for verse in range(verse1, verse2+1):
    print("Logging in...")
    BibleVerse.ja_login("./assets/credentials.json", "https://bible.prsi.org/ja/Account/Login")
    print("Logged in.")


    ja_text = BibleVerse.get_verse_ja(book_id, chapter, verse)
    # japanese += ja_text + " "

    print(ja_text)

    en_text = BibleVerse.get_verse_en(book, data["code"], chapter, verse)
    # english += en_text + " "
    print(en_text)

    # log.write(f"{book} {chapter}:{verse1}-{verse2}\n")
    # error_log = open("./error.log", "w")
    # for book in tqdm(books):
    #     try:
    #         en_text = BibleVerse.get_verse_en(book, data[book]["code"], chapter, verse)
    #         # print(en_text)
    #         # print("Done: ", book)
    #         error_log.write(f"Done:  {book}\n")
    #     except:
    #         error_log.write(f"Error: {book}\n")
    #         # print("Error: ", book)
    # error_log.close()
if __name__ == "__main__":
    main()