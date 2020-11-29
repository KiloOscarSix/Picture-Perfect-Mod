screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton(""):
                area(-20, 30, 390, 56)
                background "gui/button/start.png"
                hover_background "gui/button/start1.png"

                action Start()

        else:

            textbutton _("{size=50}Mod Options") action Show("modOptions")

            textbutton(""):
                area(-20, 30, 390, 56)
                background "gui/button/history.png"
                hover_background "gui/button/history1.png"

                action ShowMenu("history")

            textbutton(""):
                area(-20, 30, 390, 56)
                background "gui/button/save.png"
                hover_background "gui/button/save1.png"

                action ShowMenu("save")

        textbutton(""):
            area(-20, 30, 390, 56)
            background "gui/button/load.png"
            hover_background "gui/button/load1.png"

            action ShowMenu("load")

        textbutton(""):
            area(-20, 30, 390, 56)
            background "gui/button/preferences.png"
            hover_background "gui/button/preferences1.png"

            action ShowMenu("preferences")

        if main_menu:
            imagebutton:
                action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")]
                idle "/modAdditions/images/SceneGallery.png"
                hover "/modAdditions/images/SceneGallery1.png"
                pos(-20, 36)

        if _in_replay:
            imagebutton:
                action EndReplay(confirm=True)
                idle "/modAdditions/images/EndReplay.png"
                hover "/modAdditions/images/EndReplay1.png"
                pos(-20, 33)

        elif not main_menu:

            textbutton(""):
                area(-20, 30, 390, 56)
                background "gui/button/MainMenu.png"
                hover_background "gui/button/MainMenu1.png"

                action MainMenu()

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton(""):
                area(-20, 30, 390, 56)
                background "gui/button/help.png"
                hover_background "gui/button/help1.png"

                action  ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton(""):
                area(-20, 30, 390, 56)
                background "gui/button/quit.png"
                hover_background "gui/button/quit1.png"

                action Quit(confirm=not main_menu)
        textbutton(""):
            area(-20, 30, 390, 56)
            background "gui/button/discord.png"
            hover_background "gui/button/discord1.png"

            action OpenURL("https://discord.gg/J227WNy")
        textbutton(""):
            area(-20, 30, 390, 56)
            background "gui/button/patreon.png"
            hover_background "gui/button/patreon1.png"

            action OpenURL("https://www.patreon.com/SuperWriter")


screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("Cheats") action Show("cheatMenu") xoffset 550


screen save():

    tag menu

    use file_slots(_("Save"))

    vbox:
        align(0.28, 0.185)
        text "{color=#fff}Save Name:{/color}"
        input:
            yalign 0.05
            value VariableInputValue("save_name")
