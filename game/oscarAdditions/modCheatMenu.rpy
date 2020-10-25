define cheatMenuDict = {
    "Miracle": [
    ["Miracle Points", "miraclepts", 50],
    ["Miracle+Sabrina Points", "MBpts", 50],
    ],
    "Paris": [
    ["Paris Points", "parispts", 50],
    ["Paris+Sasha Points", "IApts", 50],
    ],
    "Sasha": [
    ["Sasha Points", "sashapts", 50],
    ["Paris+Sasha Points", "IApts", 50],
    ],
    "Sabrina": [
    ["Sabrina Points", "sabrinapts", 50],
    ["Miracle+Sabrina Points", "MBpts", 50],
    ],
    }

screen cheatMenu():
    modal True
    zorder 200
    add "#23272a"

    python:
        cheatMenuList = ["Miracle", "Paris", "Sasha", "Sabrina"]

    default shownCheatMenu = None

    add "/oscarAdditions/images/cheatMenuBackground.png"
    fixed:
        xysize (1877, 99)
        pos (18, 13)

        hbox:
            xcenter 0.5
            ycenter 0.5
            spacing 100
            for i in cheatMenuList:
                textbutton i:
                    action [Function(renpy.retain_after_load), SetScreenVariable("shownCheatMenu", value=i)]
                    text_style "modTextButtonHeader"

    for i in cheatMenuList:
        if shownCheatMenu == i:
            use cheatMenuValues(cheatMenuChar=i)

    imagebutton:
        action Hide("cheatMenu"), Hide("cheatMenuValues"), SetVariable("quick_menu", True)
        idle "/oscarAdditions/images/cheatMenuBackButton.png"
        hover im.MatrixColor("/oscarAdditions/images/cheatMenuBackButton.png", im.matrix.brightness(0.2))
        pos (1666, 50)

screen cheatMenuValues(cheatMenuChar):
    tag cheatmenu

    vbox:
        pos (100, 200)
        spacing 50

        vpgrid:
            cols 4
            xsize 1000
            spacing 50
            for x in cheatMenuDict[cheatMenuChar]:

                vbox:
                    spacing 20
                    text "[x[0]]:" style "modTextBody2"
                    fixed:
                        xysize (352, 42)

                        bar value VariableValue(x[1], x[2]):
                            left_bar Frame("gui/bar/left.png", 10, 0)
                            right_bar Frame("gui/bar/right.png", 10, 0)
                        text "{:}".format(getattr(store, x[1])) xcenter 0.5 ycenter 0.5

        hbox:
            spacing 100
            style_prefix "check"

            if cheatMenuChar == "Miracle":
                textbutton "MiracleKiss" action ToggleVariable("miraclekiss")
                textbutton "MiracleRoute" action ToggleVariable("Mroute")
                textbutton "Miracle+SabrinaLessons" action ToggleVariable("MBlessons")
            if cheatMenuChar == "Paris":
                textbutton "ParisRoute" action ToggleVariable("Iroute")
                textbutton "ParisPreg" action ToggleVariable("Ipreg")
            if cheatMenuChar == "Sasha":
                textbutton "SashaRoleplay" action ToggleVariable("sasharp")
                textbutton "SashaRoute" action ToggleVariable("Aroute")
                textbutton "SashaSex" action ToggleVariable("Asex")
            if cheatMenuChar == "Sabrina":
                textbutton "SabrinaConfide" action ToggleVariable("sabrinaconfide")
                textbutton "Miracle+SabrinaLessons" action ToggleVariable("MBlessons")
                textbutton "SabrinaRoute" action ToggleVariable("Broute")
