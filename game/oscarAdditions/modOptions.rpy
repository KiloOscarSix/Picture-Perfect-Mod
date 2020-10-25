define gr = "{color=#0f0}"
define MiraclePath = "{color=#0f0}[Miracle Path]"
define ParisPath = "{color=#0f0}[Paris Path]"
define SashaPath = "{color=#0f0}[Sasha Path]"
define SabrinaPath = "{color=#0f0}[Sabrina Path]"
define MiracleSabrinaPath = "{color=#0f0}[Miracle+Sabrina Path]"
define ParisSashaPath = "{color=#0f0}[Paris+Sasha Path]"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

label changeGalleryNames:
    python:
        persistent.player_name = renpy.input("What is your name?", default="Brandon")
        persistent.player_nik = renpy.input("What is the your nickname?", default="Big Guy")
        persistent.rel_f = renpy.input("What is your relationship to the girls?", default="landlord")
        persistent.rel_d = renpy.input("What is the girls' relationship to you?", default="tennant")
    mod "Gallery names successful changed"
    return

label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    python:
        player_name = renpy.input("What is your name?", default="Brandon")
        player_nik = renpy.input("What is the your nickname?", default="Big Guy")
        rel_f = renpy.input("What is your relationship to the girls?", default="landlord")
        rel_d = renpy.input("What is the girls' relationship to you?", default="tennant")
    mod "Names successful changed"
    return
