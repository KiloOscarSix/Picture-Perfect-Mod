init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, pageNum, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = "/images/{}".format(thumbnail)
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

define galleryMenu = [
    ["Miracle", "/images/a1.webp"],
    ["Paris", "images/a32.webp"],
    ["Sasha", "images/a41.webp"],
    ["Sabrina", "images/b300.webp"],
]

define unknown = GalleryItem("Miracle", 1, "galleryScene1", "a136.webp")
define unknown = GalleryItem("Miracle", 1, "galleryScene2", "c671-2.webp")
define unknown = GalleryItem("Miracle", 1, "galleryScene3", "d860.webp")
define unknown = GalleryItem("Miracle", 1, "galleryScene4", "g1221-2.webp", {"Mroute":True})
define unknown = GalleryItem("Miracle", 1, "galleryScene14", "i67.webp", {"Mroute":True})

define unknown = GalleryItem("Paris", 1, "galleryScene5", "a108.webp")
define unknown = GalleryItem("Paris", 1, "u3open", "c601.webp")
define unknown = GalleryItem("Paris", 1, "galleryScene7", "d708.webp", {"Iroute":True})
define unknown = GalleryItem("Paris", 1, "galleryScene8", "d730.webp")
define unknown = GalleryItem("Paris", 1, "U5", "e887.webp")
define unknown = GalleryItem("Paris", 1, "galleryScene10", "e941.webp")

define unknown = GalleryItem("Sasha", 1, "galleryScene7", "d708.webp")
define unknown = GalleryItem("Sasha", 1, "galleryScene11", "e1051.webp")
define unknown = GalleryItem("Sasha", 1, "CH7PLAY", "g1253.webp")
define unknown = GalleryItem("Sasha", 1, "galleryScene12", "h95.webp")
define unknown = GalleryItem("Sasha", 1, "galleryScene13", "h128.webp", {"Iroute":True})

define unknown = GalleryItem("Sabrina", 1, "galleryScene2", "c671-2.webp")
define unknown = GalleryItem("Sabrina", 1, "galleryScene3", "d860.webp")
define unknown = GalleryItem("Sabrina", 1, "CH6ask", "f1186.webp")

default galleryPageNumber = 1
default scopeDict = {}

label galleryNameChange:
    default persistent.player_name = ""
    default persistent.player_nik = ""
    default persistent.rel_f = ""
    default persistent.rel_d = ""
    if persistent.player_name == "":
        $ persistent.player_name = renpy.input("What is your name?", default="Brandon")
    if persistent.player_nik == "":
        $ persistent.player_nik = renpy.input("What is the your nickname?", default="Big Guy")
    if persistent.rel_f == "":
        $ persistent.rel_f = renpy.input("What is your relationship to the girls?", default="landlord")
    if persistent.rel_d == "":
        $ persistent.rel_d = renpy.input("What is the girls' relationship to you?", default="tennant")

    $ scopeDict = {"player_name":persistent.player_name, "player_nik":persistent.player_nik, "rel_d":persistent.rel_d, "rel_f":persistent.rel_f}
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/modAdditions/images/button.png"
                hover Transform(im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/modAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/modAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in galleryMenu:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="Unknown"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/modAdditions/images/button.png"
                hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/modAdditions/images/button.png"
                    hover im.MatrixColor("/modAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for galleryItem in galleryItems:
            if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                imagebutton:
                    action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                    idle Transform(galleryItem.thumbnail, zoom=0.2)
                    hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
