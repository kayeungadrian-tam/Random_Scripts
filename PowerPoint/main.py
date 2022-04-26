from modules.bible_verse import OnlineBibleVerse
from modules.power_point import PowerPoint
# from modules.word_handler import WordHandler
from modules.word_handler import NewHandler

import json

from pptx.util import Inches, Cm
from pptx.dml.color import ColorFormat, RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Pt
from datetime import datetime

title_img = "./assets/2022 John.png"
background_img = "./assets/2022 John text.png"

doc_path = "./demo2.docx"

params = {
    "title_img": title_img,
    "background_img": background_img,
    "slide_width": Cm(25.5),
    "slide_height": Cm(14.3),
    "font_size": Pt(20),
    "verse_size": Pt(18),
    "font_color": RGBColor(255, 255, 255),
    "font_name": "Arial",
    "pic_left": Cm(0),
    "pic_top": Cm(0),
    "text_margin": Cm(2),
    "text_center": PP_ALIGN.CENTER,
    "text_left": PP_ALIGN.LEFT,
    "text_right": PP_ALIGN.RIGHT
    
}
def book_handle(book):    
    with open("./assets/books_dict.json", 'r', encoding='utf-8') as f:
        books_dict = json.load(f)
    data = books_dict[book]
    return data



def main():

    # word_handler = WordHandler(doc_path)
    word_handler = NewHandler(doc_path)
    ppt = PowerPoint(**params)
    bible = OnlineBibleVerse("./assets/credentials.json", "https://bible.prsi.org/ja/Account/Login")

    tags = word_handler.get_tag()



    for idx, key in enumerate(tags):
        splitted = key.split(":")
        
        if len(splitted) == 2:
            if splitted[0] == "PIC":
                # print("PIC")
                ppt.add_img_slide(f"PIC: {idx}")
            elif splitted[0] == "PNT":
                if splitted[1]:
                    # print(splitted[1])
                    ppt.add_point_slide("＊＊＊", splitted[1])
        if len(splitted) == 3:
            book = splitted[1].split(" ")[1]
            chapter = int(splitted[1].split(" ")[2])
            verses = splitted[2].split("-")

            if len(verses) == 2:

                verse_start = int(verses[0])
                verse_end = int(verses[1])
                ja_verse_str, en_verse_str = bible.verse_str(book, chapter, f"{verse_start}-{verse_end}")
                english = ""
                japanese = ""
                for verse in range(verse_start, verse_end+1):
                    jp_text = bible.get_verse_ja(book, chapter, verse)
                    japanese += jp_text
                    en_text = bible.get_verse_en(book, chapter, verse)
                    english += en_text

                ppt.add_verse_slides(japanese, english, ja_verse_str, en_verse_str)

            else:
                ja_verse_str, en_verse_str = bible.verse_str(book, chapter, verses[0])

                jp_text = bible.get_verse_ja(book, chapter, int(verses[0]))
                en_text = bible.get_verse_en(book, chapter, int(verses[0]))

                ppt.add_verse_slides(jp_text, en_text, ja_verse_str, en_verse_str)
                

    ppt.save()
    bible.close()

if __name__ == "__main__":
    main()