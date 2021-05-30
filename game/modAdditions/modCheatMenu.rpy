init python:
    cheatItems = []
    cheatCatagorys = []

    class CheatItem:
        def __init__(self, catagory, name, variable, kind="Slider", minValue=0, maxValue=0, trueValue=True, falseValue=False):
            self.catagory = catagory
            self.name = name
            self.variable = variable
            if kind == "Slider":
                self.minValue = minValue
                self.maxValue = maxValue
            elif kind == "Button":
                self.trueValue = trueValue
                self.falseValue = falseValue
            else:
                raise Exception("Unsupported Cheat Type")
            self.kind = kind
            # if self not in cheatItems:
            cheatItems.append(self)

    var1 = CheatItem("Miracle", "Miracle Points", "miraclepts", maxValue=10)
    var2 = CheatItem("Miracle", "Miracle+Sabrina Points", "MBpts", maxValue=10)
    var2 = CheatItem("Miracle", "Miracle Route", "Mroute", kind="Button")

    var2 = CheatItem("Paris", "Paris Points", "parispts", maxValue=20)
    var2 = CheatItem("Paris", "Paris+Sasha Points", "IApts", maxValue=10)
    var2 = CheatItem("Paris", "Paris Route", "Iroute", kind="Button")

    var2 = CheatItem("Sasha", "Sasha Points", "sashapts", maxValue=10)
    var2 = CheatItem("Sasha", "Paris+Sasha Points", "IApts", maxValue=10)
    var2 = CheatItem("Sasha", "Sasha Route", "Aroute", kind="Button")

    var2 = CheatItem("Sabrina", "Sabrina Points", "sabrinapts", maxValue=10)
    var2 = CheatItem("Sabrina", "Miracle+Sabrina Points", "MBpts", maxValue=10)
    var2 = CheatItem("Sabrina", "Sabrina Route", "Broute", kind="Button")

    var2 = CheatItem("Harem", "Harem Route", "Hroute", kind="Button")
    var2 = CheatItem("Harem", "Harem Points", "hpts", maxValue=20)

    for cheatItem in cheatItems:
        if cheatItem.catagory not in cheatCatagorys:
            cheatCatagorys.append(cheatItem.catagory)

screen cheatMenu():
    modal True
    zorder 200

    default shownCheatMenu = cheatItems[0] or None

    add "/modAdditions/images/cheatMenuBackground.png"

    fixed:
        xysize (1536, 99)
        pos (85, 13)

        hbox:
            xcenter 0.5
            ycenter 0.5
            spacing 100
            for cheatCatagory in cheatCatagorys:
                textbutton cheatCatagory:
                    action [Function(renpy.retain_after_load), SetScreenVariable("shownCheatMenu", cheatCatagory)]
                    text_style "modTextButtonHeader"

    for cheatCatagory in cheatCatagorys:
        if shownCheatMenu == cheatCatagory:
            use cheatMenuValues(cheatMenuChar=cheatCatagory)

    imagebutton:
        action Hide("cheatMenu"), Hide("cheatMenuValues"), SetVariable("quick_menu", True)
        idle "/modAdditions/images/cheatMenuBackButton.png"
        hover im.MatrixColor("/modAdditions/images/cheatMenuBackButton.png", im.matrix.brightness(0.2))
        pos (1666, 50)

screen cheatMenuValues(cheatMenuChar="General"):
    tag cheatmenu

    vbox:
        pos (103, 258)
        spacing 100
        vpgrid:
            cols 4
            spacing 100
            for cheatItem in cheatItems:
                if cheatItem.catagory == cheatMenuChar and cheatItem.kind == "Slider":
                        vbox:
                            spacing 20
                            text "[cheatItem.name]" style "modTextBody2"
                            fixed:
                                xysize (352, 42)

                                bar value VariableValue(cheatItem.variable, cheatItem.maxValue-cheatItem.minValue, offset=cheatItem.minValue):
                                    left_bar Frame("gui/bar/left.png", 10, 0)
                                    right_bar Frame("gui/bar/right.png", 10, 0)
                                text "{:}".format(getattr(store, cheatItem.variable)) align(0.5, 0.5)
        vpgrid:
            cols 4
            spacing 100
            for cheatItem in cheatItems:
                if cheatItem.catagory == cheatMenuChar and cheatItem.kind == "Button":
                    vbox:
                        style_prefix "check"
                        textbutton "[cheatItem.name]":
                            action ToggleVariable(cheatItem.variable, true_value=cheatItem.trueValue, false_value=cheatItem.falseValue)
