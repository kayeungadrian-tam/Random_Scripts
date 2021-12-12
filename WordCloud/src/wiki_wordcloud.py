from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import wikipediaapi
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def list_section(sections, level=1):
    for section in sections:
        print(f"{'*'*level}\t{section.title}")
        list_section(section.sections, level=2)

def vis_wordcloud(wc):
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()

def create_wordcloud(text):    
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 10)
    wc = wordcloud.generate(text)
    return wc

def output(title, summary, section):
    print(f'{"-"*20} Title {"-"*20}')
    print(title)
    print(f'{"-"*20} Summary {"-"*20}')
    print(summary)
    print(f'{"-"*20} Sections {"-"*20}')
    list_section(section)
    print(f'{"-"*20} EOF {"-"*20}')

def check_ambiguation(summary, selected_page):
    if " may refer to" in summary:
        print(f"{bcolors.WARNING}WARNING: Ambiguation, see suggestions below.{bcolors.ENDC}")
        print(list(selected_page.links.keys()), flush=True)
        sys.exit()

def main():
    serach_word = input("Enter keyword: ")
    print("Searching WIKIPEDIA ... ", end=" ", flush=True)

    wiki_wiki = wikipediaapi.Wikipedia()
    page_py = wiki_wiki.page(serach_word)

    if page_py.exists():
        print(f"{bcolors.OKGREEN}SUCCESSFUL.{bcolors.ENDC}")
        languages = page_py.langlinks
        
        print(">>> Type 'Y' to choose other languages or 'Enter' to conintue in English.")
        select_en = input(">>> Choose other languages? ")
        
        if select_en in ["Y", "y"]:
            for idx, (k, v) in enumerate(languages.items()):
                print(f"[{idx}]\t{k}: {v}")
            select = int(input(">>> Select number: "))
            selected_page = page_py.langlinks[list(languages)[select]]
        else:
            selected_page = page_py 
        
        title = selected_page.title
        summary = selected_page.summary

        check_ambiguation(summary, selected_page)
        output(title, summary, selected_page.sections)
        
        wc = create_wordcloud(summary)

        vis_wordcloud(wc)
    else:
        print(f"{bcolors.FAIL}ERROR 404: Page not found. {bcolors.ENDC}")

if __name__ == "__main__":
    main()