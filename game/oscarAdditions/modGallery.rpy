init python:
    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

default galleryPageNumber = 1

define sceneGalleryMenuDict = {
    "galleryMenu": [
    ["Miracle", "/images/a1.webp"],
    ["Paris", "images/a32.webp"],
    ["Sasha", "images/a41.webp"],
    ["Sabrina", "images/b300.webp"],
    ],
    "Miracle": {
    1: [
    ["galleryScene1", {}, "/images/a136.webp"],
    ["galleryScene2", {}, "/images/c671-2.webp"],
    ["galleryScene3", {}, "/images/d860.webp"],
    # ["galleryScene4", {"Mroute":True}, "/images/b1221-2.webp"],
    ],
    },
    "Paris": {
    1: [
    ["galleryScene5", {}, "/images/a108.webp"],
    ["u3open", {}, "/images/c601.webp"],
    ["galleryScene7", {"Iroute":True}, "/images/d708.webp"],
    ["galleryScene8", {}, "/images/d730.webp"],
    ["U5", {}, "/images/e887.webp"],
    ["galleryScene10", {}, "/images/e941.webp"],
    ],
    },
    "Sasha": {
    1: [
    ["galleryScene7", {}, "/images/d708.webp"],
    ["galleryScene11", {}, "/images/e1051.webp"],
    # ["CH7PLAY", {}, "/images/b1253.webp"],
    # ["galleryScene12", {}, "/images/a95.webp"],
    # ["galleryScene13", {"Iroute":True}, "/images/a128.webp"],
    ],
    },
    "Sabrina": {
    1: [
    ["galleryScene2", {}, "/images/c671-2.webp"],
    ["galleryScene3", {}, "/images/d860.webp"],
    # ["CH6ask", {}, "/images/1186.webp"],
    ],
    },
    }

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
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="Miracle"):
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
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"player_name":persistent.player_name, "player_nik":persistent.player_nik, "rel_d":persistent.rel_d, "rel_f":persistent.rel_f}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
