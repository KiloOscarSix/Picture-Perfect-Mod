init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = len(filter(lambda s: s.char == char, galleryItems)) // 8 + 1
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
    ["Harem", "images/m331.webp"]
]

define Miracle = GalleryItem("Miracle", "galleryScene1", "a136.webp")
define MiracleSabrina = GalleryItem("Miracle", "galleryScene2", "c671-2.webp")
define MiracleSabrina = GalleryItem("Miracle", "galleryScene3", "d860.webp")
define Miracle = GalleryItem("Miracle", "galleryScene4", "g1221-2.webp", {"Mroute":True})
define Miracle = GalleryItem("Miracle", "galleryScene14", "i67.webp", {"Mroute":True})
define MiracleSabrina = GalleryItem("Miracle", "galleryScene18", "k44.webp")
define MiracleSabrina = GalleryItem("Miracle", "galleryScene19", "k64.webp")
define MiracleSabrina = GalleryItem("Miracle", "galleryScene20", "k166.webp")

define Paris = GalleryItem("Paris", "galleryScene5", "a108.webp")
define Paris = GalleryItem("Paris", "u3open", "c601.webp")
define Paris = GalleryItem("Paris", "galleryScene7", "d708.webp", {"Iroute":True})
define Paris = GalleryItem("Paris", "galleryScene8", "d730.webp")
define Paris = GalleryItem("Paris", "U5", "e887.webp")
define Paris = GalleryItem("Paris", "galleryScene10", "e941.webp")
define Paris = GalleryItem("Paris", "galleryScene16", "j48.webp")
define Paris = GalleryItem("Paris", "galleryScene17", "j143.webp")

define Sasha = GalleryItem("Sasha", "galleryScene7", "d708.webp")
define Sasha = GalleryItem("Sasha", "galleryScene11", "e1051.webp")
define Sasha = GalleryItem("Sasha", "CH7PLAY", "g1253.webp", {"sashapts": 4})
define Sasha = GalleryItem("Sasha", "galleryScene12", "h95.webp")
define Sasha = GalleryItem("Sasha", "galleryScene13", "h128.webp", {"Iroute":True})
define Sasha = GalleryItem("Sasha", "galleryScene15", "f47.webp")

define MiracleSabrina = GalleryItem("Sabrina", "galleryScene2", "c671-2.webp")
define MiracleSabrina = GalleryItem("Sabrina", "galleryScene3", "d860.webp")
define Sabrina = GalleryItem("Sabrina", "CH6ask", "f1186.webp", {"sabrinapts": 2})
define MiracleSabrina = GalleryItem("Sabrina", "galleryScene18", "k44.webp")
define MiracleSabrina = GalleryItem("Sabrina", "galleryScene19", "k64.webp")
define MiracleSabrina = GalleryItem("Sabrina", "galleryScene20", "k166.webp")

define Harem = GalleryItem("Harem", "galleryScene20", "m81.webp")
define Harem = GalleryItem("Harem", "galleryScene21", "m258.webp")
define Harem = GalleryItem("Harem", "U14yes", "m331.webp")

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
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for i in galleryMenu:
                vbox:
                    imagebutton:
                        action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                        idle Transform(i[1], zoom=0.2)
                        hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                    text i[0]:
                        style "modTextBody"
                        xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="None"):
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
            else:
                action SetVariable(galleryPageNumber, galleryPageNumber - 1)
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action SetVariable(galleryPageNumber, galleryPageNumber + 1)
                idle "/modAdditions/images/nextButton.png"
                hover im.MatrixColor("/modAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)