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
                idle "/oscarAdditions/images/SceneGallery.png"
                hover "/oscarAdditions/images/SceneGallery1.png"
                pos(-20, 36)

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

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

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            if title == "Save":
                text "{color=#fff}Save Name:{/color}":
                    xalign 0
                    yalign -0.005
                input:
                    xalign 0
                    yalign 0.05
                    value VariableInputValue("save_name")

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()
