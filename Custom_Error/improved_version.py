from __future__ import division
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys



def simle_error(screen):
    scenes = []

    effects = [
        BannerText(screen, ImageFile("img/simle.png", screen.height - 2, colours=screen.colours),
              0, 0),
        Print(screen,
              FigletText(
                "www ERROR www",
                font='banner3' if screen.width > 80 else 'banner'
                ),
              screen.height//2-3,
              colour=Screen.COLOUR_RED, bg=7 if screen.unicode_aware else 0)
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)

def error_404(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(
                screen, 
                "img/404.png", 
                screen.height-2,
                uni=screen.unicode_aware,
                dither=screen.unicode_aware
                ),
            0,
            stop_frame=200)
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)

def CustomError(demo):
    while True:
            try:
                Screen.wrapper(demo)
                sys.exit(0)
            except ResizeScreenError:
                pass    

if __name__ == "__main__":
    try:
        1 + "str"
    except:
        CustomError(simle_error)
    