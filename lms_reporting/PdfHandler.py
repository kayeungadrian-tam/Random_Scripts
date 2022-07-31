# from fpdf import FPDF
# from matplotlib import pyplot as plt


# pdf = FPDF()
# pdf.add_page()
# pdf.set_font('Arial', 'B', 16)
# pdf.cell(40, 10, 'Hello World!')
# pdf.output('tuto1.pdf', 'F')


# class PDF(FPDF):
#     def header(self):
#         # Logo
#         self.image('demo.png', 10, 8, 33)
#         # Arial bold 15
#         self.set_font('Arial', 'B', 15)
#         # Move to the right
#         self.cell(80)
#         # Title
#         self.cell(30, 10, '今後はどうしマスクを作成、', 1, 0, 'C')
#         # Line break
#         self.ln(20)

#     # Page footer
#     def footer(self):
#         # Position at 1.5 cm from bottom
#         self.set_y(-15)
#         # Arial italic 8
#         self.set_font('Arial', 'I', 8)
#         # Page number
#         self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# # Instantiation of inherited class
# pdf = PDF()
# pdf.alias_nb_pages()
# pdf.add_page()
# pdf.set_font('Times', '', 12)
# for i in range(1, 41):
#     pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
# pdf.output('tuto2.pdf', 'F')

# title = '20000 Leagues Under the Seas'

# class PDF2(FPDF):
#     def header(self):
#         # Arial bold 15
#         self.set_font('Arial', 'B', 15)
#         # Calculate width of title and position
#         w = self.get_string_width(title) + 6
#         self.set_x((210 - w) / 2)
#         # Colors of frame, background and text
#         self.set_draw_color(0, 80, 180)
#         self.set_fill_color(230, 230, 0)
#         self.set_text_color(220, 50, 50)
#         # Thickness of frame (1 mm)
#         self.set_line_width(1)
#         # Title
#         self.cell(w, 9, title, 1, 1, 'C', 1)
#         # Line break
#         self.ln(10)

#     def footer(self):
#         # Position at 1.5 cm from bottom
#         self.set_y(-15)
#         # Arial italic 8
#         self.set_font('Arial', 'I', 8)
#         # Text color in gray
#         self.set_text_color(128)
#         # Page number
#         self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

#     def chapter_title(self, num, label):
#         # Arial 12
#         self.set_font('Arial', '', 12)
#         # Background color
#         self.set_fill_color(200, 220, 255)
#         # Title
#         self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
#         # Line break
#         self.ln(4)

#     def chapter_body(self, name):
#         # Read text file
#         with open(name, 'rb') as fh:
#             txt = fh.read().decode('latin-1')
#         # Times 12
#         self.set_font('Times', '', 12)
#         # Output justified text
#         self.multi_cell(0, 5, txt)
#         # Line break
#         self.ln()
#         # Mention in italics
#         self.set_font('', 'I')
#         self.cell(0, 5, '(end of excerpt)')

#     def print_chapter(self, num, title, name):
#         self.add_page()
#         self.chapter_title(num, title)
#         self.chapter_body(name)

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import webbrowser

# 源真ゴシック（ http://jikasei.me/font/genshin/）
GEN_SHIN_GOTHIC_MEDIUM_TTF = "./genshingothic-20150607/GenShinGothic-Bold.ttf"

# 白紙をつくる（A4縦）
FILENAME = 'HelloWorld.pdf'
c = canvas.Canvas(FILENAME, pagesize=portrait(A4))

# フォント登録
pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC_MEDIUM_TTF))
font_size = 20
c.setFont('GenShinGothic', font_size)

# 真ん中に文字列描画
width, height = A4  # A4用紙のサイズ
c.drawCentredString(width / 2, height / 2 - font_size * 0.4, 'こんにちは、世界！')

# Canvasに書き込み
c.showPage()
# ファイル保存
c.save()

# ブラウザーで表示
webbrowser.open(FILENAME)