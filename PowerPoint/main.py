from pptx import Presentation
from pptx.util import Inches, Cm
from pptx.dml.color import ColorFormat, RGBColor



title_img = "./assets/2022 John.png"
background_img = "./assets/2022 John text.png"


PPT = Presentation()
# set width and height to 16 and 9 inches.
PPT.slide_width = Cm(29.7)
PPT.slide_height = Cm(21.0)

blank_slide_layout = PPT.slide_layouts[6]
slide = PPT.slides.add_slide(blank_slide_layout)
left = top = Inches(0)

width = Cm(29.7)
height = Cm(21.0)

pic = slide.shapes.add_picture(title_img, left, top, width=width, height=height)



text_layout = PPT.slide_layouts[6]
text_slide = PPT.slides.add_slide(text_layout)
pic2 = text_slide.shapes.add_picture(background_img, left, top, width=width, height=height)


english_text = '''
[38] And Peter said to them, “Repent and be baptized every one of you in the name of Jesus Christ for the forgiveness of your sins, and you will receive the gift of the Holy Spirit.”
'''
japanese_text = '''
そこで、ペテロは彼らに言った。「それぞれ罪を赦していただくために、悔い改めて、イエス・キリストの名によってバプテスマを受けなさい。そうすれば、賜物として聖霊を受けます。」
'''
left = top = width = height = Inches(1)
txBox = text_slide.shapes.add_textbox(left, top, Cm(20), Cm(20))
tf = txBox.text_frame
tf.word_wrap = True
p = tf.add_paragraph()
p.font.color.rgb = RGBColor(255, 255, 255)
p.text = english_text

txBox = text_slide.shapes.add_textbox(left, top, width, height)
p = tf.add_paragraph()
tf.word_wrap = True
p.font.color.rgb = RGBColor(255, 255, 255)
p.text = japanese_text


# first_slide.shapes.title.text = "Creating a powerpoint using Python"
# first_slide.placeholders[1].text = "Created by Tutorialpoints"


# Second_Layout = X.slide_layouts[5]
# second_slide = X.slides.add_slide(Second_Layout)


# second_slide.shapes.title.text = "Second slide"
# textbox = second_slide.shapes.add_textbox(Inches(3), Inches(1.5),Inches(3), Inches(1))
# textframe = textbox.text_frame
# paragraph = textframe.add_paragraph()
# paragraph.text = "This is a paragraph in the second slide!"


PPT.save("test.pptx")