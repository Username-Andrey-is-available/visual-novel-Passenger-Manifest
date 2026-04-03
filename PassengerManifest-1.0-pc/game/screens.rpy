################################################################################
## Инициализация
################################################################################

init offset = -1


################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Внутриигровые экраны
################################################################################


## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    use character_layer(who)

    zorder 200
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_4" action NullAction()
    key "mouseup_5" action NullAction()

    $ speaker_portrait = SPEAKER_PORTRAITS.get(who, None)
    $ previous_choice_identifier = pm_previous_choice_identifier()

# затемнение снизу
    frame:
        xpos 0.5
        ypos 1.0
        xanchor 0.5
        yanchor 1.0
        xsize 1920
        ysize 320
        background Solid("#000000cc")

# -------------------------------
# ЗОНА ИМЕНИ (фиксированная)
# -------------------------------
    frame:
        xpos 320
        ypos 700
        xsize 1240
        ysize 60
        background None

        if who:
            text who:
                xpos 0
                ypos 0
                size 36
                color "#cfcfcf"
                outlines [(2, "#000", 0, 0)]
                xanchor 0.0
                yanchor 0.0

# -------------------------------
# ЗОНА ТЕКСТА (полностью независимая)
# -------------------------------
    frame:
        xpos 320
        ypos 760
        xsize 1240
        ysize 260
        background None

        text what:
            id "what"
            xpos 0
            ypos 0
            xsize 1240
            size 30
            color "#ffffff"
            outlines [(2, "#000", 0, 0)]
            xanchor 0.0
            yanchor 0.0
            text_align 0.0
            layout "subtitle"


# кнопки управления
    fixed:
        xpos 1770
        ypos 720
        xsize 110
        ysize 330

        frame:
            xfill True
            yfill True
            background Solid("#08131cb8")
            padding (18, 16)

        button:
            xfill True
            yfill True
            background None
            action NullAction()

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10

            textbutton "⏮":
                xsize 50
                ysize 50
                background Solid("#00000088")
                sensitive previous_choice_identifier is not None
                action (RollbackToIdentifier(previous_choice_identifier) if previous_choice_identifier else NullAction())

            textbutton "⏸":
                xsize 50
                ysize 50
                background Solid("#00000088")
                action Preference("auto-forward", "toggle")

            textbutton "⏭":
                xsize 50
                ysize 50
                background Solid("#00000088")
                action Skip(fast=True)

            textbutton "⚙":
                xsize 50
                ysize 50
                background Solid("#00000088")
                action ShowMenu("preferences")

            textbutton "💾":
                xsize 50
                ysize 50
                background Solid("#00000088")
                action ShowMenu("save")



## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    background None

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Экран ввода #################################################################
##
## Этот экран используется, чтобы показывать renpy.input. Это параметр запроса,
## используемый для того, чтобы дать игроку ввести в него текст.
##
## Этот экран должен создать наложение ввода с id "input", чтобы принять
## различные вводимые параметры.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    on "show" action Function(pm_record_choice_rollback_point)

    $ has_logic_hint = bool(manifest_state.current_logic_text)
    $ choice_ypos = 268 if has_logic_hint else 214
    if len(items) >= 5:
        $ choice_ypos -= 30
    elif len(items) >= 4:
        $ choice_ypos -= 12

    if has_logic_hint:
        frame:
            xalign 0.5
            ypos 122
            xsize 1180
            background Solid("#10263a96")
            padding (24, 18)

            text manifest_state.current_logic_text:
                size 28
                color "#7fd3ff"
                outlines [(2, "#000000aa", 0, 0)]
                text_align 0.5
                xalign 0.5

    vbox:
        style "choice_vbox"
        xalign 0.5
        ypos choice_ypos

        for i in items:
            $ item_stats = CHOICE_STAT_REQUIREMENTS.get(i.caption, ())
            $ idle_background = choice_plate_color(item_stats, 0.38, "d8") or "#10212bcc"
            $ hover_background = choice_plate_color(item_stats, 0.55, "e6") or "#15384acc"
            $ selected_background = choice_plate_color(item_stats, 0.68, "f0") or "#1a4760cc"
            textbutton i.caption:
                style "choice_button"
                xsize 900
                yminimum 78
                background Solid(idle_background)
                hover_background Solid(hover_background)
                selected_background Solid(selected_background)
                action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    spacing 12

style choice_button is default:
    xpadding 18
    ypadding 12
    background Solid("#10212bcc")
    hover_background Solid("#15384acc")
    selected_background Solid("#1a4760cc")

style choice_button_text is default:
    font gui.interface_text_font
    size 24
    color "#d9e3e7"
    hover_color "#f5fbff"
    selected_color "#f5fbff"
    outlines [(2, "#000000aa", 0, 0)]
    text_align 0.0
    xalign 0.0
    yalign 0.5
    xmaximum 840
    layout "subtitle"


screen character_display():

    if not main_menu:
        add "character_current" xpos 1400 ypos 200

## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

screen quick_menu():

    ## Гарантирует, что оно появляется поверх других экранов.
    zorder 100

    if quick_menu:
        $ previous_choice_identifier = pm_previous_choice_identifier()

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Назад") action Rollback()
            textbutton _("Пред. выбор"):
                action (RollbackToIdentifier(previous_choice_identifier) if previous_choice_identifier else NullAction())
                sensitive previous_choice_identifier is not None
            textbutton _("История") action ShowMenu('history')
            textbutton _("След. выбор") action Skip(fast=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Б.Сохр") action QuickSave()
            textbutton _("Б.Загр") action QuickLoad()
            textbutton _("Опции") action ShowMenu('preferences')


## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    if "hud_stats" not in config.overlay_screens:
            config.overlay_screens.append("hud_stats")

    if "top_info" not in config.overlay_screens:
            config.overlay_screens.append("top_info")


default quick_menu = False

transform premium_panel_reveal:
    alpha 0.0
    yoffset 18
    ease 0.28 alpha 1.0 yoffset 0

transform premium_soft_float:
    subpixel True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Начать"):
                default_focus True
                action [Function(pm_story_sfx, "ui_confirm"), Start()]

        else:

            textbutton _("История"):
                default_focus True
                action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("history")]

            textbutton _("Сохранить") action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("save")]

        textbutton _("Загрузить") action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("load")]

        textbutton _("Настройки") action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("preferences")]

        textbutton _("Достижения") action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("flowchart")]

        if _in_replay:

            textbutton _("Завершить повтор") action [Function(pm_story_sfx, "ui_back"), EndReplay(confirm=True)]

        elif not main_menu:

            textbutton _("Главное меню") action [Function(pm_story_sfx, "ui_back"), MainMenu()]

        textbutton _("Об игре") action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("about")]

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Помощь не необходима и не относится к мобильным устройствам.
            textbutton _("Помощь") action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("help")]

        if renpy.variant("pc"):

            ## Кнопка выхода блокирована в iOS и не нужна на Android и в веб-
            ## версии.
            textbutton _("Выход") action [Function(pm_story_sfx, "ui_back"), Quit(confirm=not main_menu)]


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    xpadding 0
    ypadding 4
    background None
    hover_background Solid("#1430396f")
    selected_background Solid("#1c45556f")

style navigation_button_text:
    font gui.interface_text_font
    size 29
    color "#aeb8bc"
    hover_color "#ffffff"
    selected_color "#ffffff"
    insensitive_color "#607279"
    text_align 0.0
    outlines [(2, "#020608aa", 0, 0)]


## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    tag menu

    default menu_caption = _("Запустите новый цикл и попробуйте вырвать Aurora из повторяющейся траектории.")

    add gui.main_menu_background
    add Solid("#051015c8")

    frame:
        style "cinematic_main_menu_shadow"

    fixed:
        xfill True
        yfill True

        add Solid("#1aa7e618") xpos 58 ypos 86 xsize 2 ysize 822
        add Solid("#f3f7f814") xpos 58 ypos 86 xsize 520 ysize 1
        add Solid("#f3f7f80a") xpos 58 ypos 908 xsize 520 ysize 1

        frame:
            style "cinematic_main_menu_panel"
            at premium_panel_reveal

            vbox:
                style "cinematic_main_menu_vbox"
                spacing 10

                text _("TEMPORAL INCIDENT // AURORA"):
                    style "cinematic_main_menu_eyebrow"

                text "[config.name!t]":
                    style "cinematic_main_menu_title"

                text _("Хроника временной петли"):
                    style "cinematic_main_menu_subtitle"

                null height 48

                textbutton _("Начать"):
                    style "cinematic_main_menu_button"
                    text_style "cinematic_main_menu_button_text"
                    default_focus True
                    action [Function(pm_story_sfx, "ui_confirm"), Start()]
                    hovered SetScreenVariable("menu_caption", _("Войти в первый цикл и заново собрать манифест до того, как корабль сорвётся к сингулярности."))
                    unhovered SetScreenVariable("menu_caption", _("Запустите новый цикл и попробуйте вырвать Aurora из повторяющейся траектории."))

                textbutton _("Загрузить"):
                    style "cinematic_main_menu_button"
                    text_style "cinematic_main_menu_button_text"
                    action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("load")]
                    hovered SetScreenVariable("menu_caption", _("Продолжить с сохранённого витка и не терять уже собранные улики."))
                    unhovered SetScreenVariable("menu_caption", _("Запустите новый цикл и попробуйте вырвать Aurora из повторяющейся траектории."))

                textbutton _("Настройки"):
                    style "cinematic_main_menu_button"
                    text_style "cinematic_main_menu_button_text"
                    action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("preferences")]
                    hovered SetScreenVariable("menu_caption", _("Настроить звук, темп текста и интерфейс перед следующим заходом в петлю."))
                    unhovered SetScreenVariable("menu_caption", _("Запустите новый цикл и попробуйте вырвать Aurora из повторяющейся траектории."))

                textbutton _("Достижения"):
                    style "cinematic_main_menu_button"
                    text_style "cinematic_main_menu_button_text"
                    action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("flowchart")]
                    hovered SetScreenVariable("menu_caption", _("Открыть экран достижений, улик, развилок и концовок по всем неделям цикла."))
                    unhovered SetScreenVariable("menu_caption", _("Запустите новый цикл и попробуйте вырвать Aurora из повторяющейся траектории."))

                textbutton _("Об игре"):
                    style "cinematic_main_menu_button"
                    text_style "cinematic_main_menu_button_text"
                    action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("about")]
                    hovered SetScreenVariable("menu_caption", _("Краткая информация о проекте и текущей версии сборки."))
                    unhovered SetScreenVariable("menu_caption", _("Запустите новый цикл и попробуйте вырвать Aurora из повторяющейся траектории."))

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                    textbutton _("Помощь"):
                        style "cinematic_main_menu_button"
                        text_style "cinematic_main_menu_button_text"
                        action [Function(pm_story_sfx, "ui_confirm"), ShowMenu("help")]
                        hovered SetScreenVariable("menu_caption", _("Подсказки по управлению для клавиатуры, мыши и других устройств."))
                        unhovered SetScreenVariable("menu_caption", _("Запустите новый цикл и попробуйте вырвать Aurora из повторяющейся траектории."))

                if renpy.variant("pc"):

                    textbutton _("Выход"):
                        style "cinematic_main_menu_button"
                        text_style "cinematic_main_menu_button_text"
                        action [Function(pm_story_sfx, "ui_back"), Quit(confirm=False)]
                        hovered SetScreenVariable("menu_caption", _("Закрыть игру и оставить манифест ждать следующего запуска."))
                        unhovered SetScreenVariable("menu_caption", _("Запустите новый цикл и попробуйте вырвать Aurora из повторяющейся траектории."))

        vbox:
            style "cinematic_main_menu_footer"
            at premium_panel_reveal

            text menu_caption:
                style "cinematic_main_menu_caption"

        if renpy.variant("pc"):

            text _("Enter  Подтвердить"):
                style "cinematic_main_menu_hint"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style cinematic_main_menu_button is button
style cinematic_main_menu_button_text is button_text
style cinematic_main_menu_title is text
style cinematic_main_menu_subtitle is text
style cinematic_main_menu_caption is text
style cinematic_main_menu_hint is text
style cinematic_main_menu_eyebrow is text
style cinematic_main_menu_panel is frame
style cinematic_main_menu_shadow is frame
style cinematic_main_menu_footer is vbox
style cinematic_main_menu_vbox is vbox

style cinematic_main_menu_panel:
    xpos 72
    ypos 92
    xsize 500
    ysize 770
    padding (40, 42, 38, 34)
    background Solid("#061218c7")

style cinematic_main_menu_shadow:
    xfill True
    yfill True
    background Solid("#02060866")

style cinematic_main_menu_vbox:
    xfill True
    yfill True

style cinematic_main_menu_button:
    xpadding 0
    ypadding 4
    background None
    hover_background Solid("#16354180")
    selected_background Solid("#1b465580")

style cinematic_main_menu_button_text:
    font gui.interface_text_font
    size 32
    color "#aeb8bc"
    hover_color "#ffffff"
    selected_color "#ffffff"
    insensitive_color "#607279"
    text_align 0.0
    outlines [(2, "#020608aa", 0, 0)]

style cinematic_main_menu_eyebrow:
    font gui.interface_text_font
    size 16
    color "#72bcd6"
    outlines [(1, "#02060888", 0, 0)]

style cinematic_main_menu_title:
    font gui.interface_text_font
    size 62
    color "#f3f7f8"
    outlines [(2, "#020608aa", 0, 0)]

style cinematic_main_menu_subtitle:
    font gui.interface_text_font
    size 18
    color "#93a8ad"
    outlines [(1, "#02060888", 0, 0)]

style cinematic_main_menu_footer:
    xalign 0.5
    yalign 1.0
    yoffset -54
    xmaximum 720

style cinematic_main_menu_caption:
    font gui.interface_text_font
    size 24
    color "#d7dddf"
    text_align 0.5
    xalign 0.5
    outlines [(2, "#020608aa", 0, 0)]

style cinematic_main_menu_hint:
    xalign 1.0
    yalign 1.0
    xoffset -40
    yoffset -28
    font gui.interface_text_font
    size 20
    color "#a7b7bc"
    outlines [(2, "#020608aa", 0, 0)]


## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None или один из "viewport" или "vpgrid". Этот
## экран предназначен для использования с одним или несколькими дочерними
## элементами, которые трансклюдируются (помещаются) внутрь него.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    add Solid("#041015d9")
    add Solid("#1aa7e610") xpos 46 ypos 116 xsize 2 ysize 872
    add Solid("#e8f4f712") xpos 46 ypos 116 xsize 1826 ysize 1
    add Solid("#0f202733") xpos 0 ypos 0 xsize 1920 ysize 1080

    frame:
        style "game_menu_outer_frame"
        at premium_panel_reveal

        hbox:

            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Вернуться"):
        style "return_button"

        action [Function(pm_story_sfx, "ui_back"), Return()]

    label title

    if main_menu:
        text _("AURORA // INTERFACE"):
            style "game_menu_meta_text"
    else:
        text _("AURORA // SHIP SYSTEMS"):
            style "game_menu_meta_text"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style game_menu_meta_text is text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 54
    top_padding 120
    left_padding 52
    right_padding 52
    background Solid("#00000000")

style game_menu_navigation_frame:
    xsize 420
    yfill True
    left_padding 34
    top_padding 40
    right_padding 30
    bottom_padding 90
    background Solid("#061218cf")

style game_menu_content_frame:
    left_margin 42
    right_margin 0
    top_margin 0
    left_padding 48
    right_padding 48
    top_padding 40
    bottom_padding 40
    xfill True
    yfill True
    background Solid("#0b171ee8")

style game_menu_viewport:
    xsize 1330

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 20

style game_menu_label:
    xpos 540
    ypos 44
    ysize 80

style game_menu_label_text:
    font gui.interface_text_font
    size 44
    color "#f3f7f8"
    yalign 0.5
    outlines [(2, "#020608aa", 0, 0)]

style game_menu_meta_text:
    xpos 1438
    ypos 56
    font gui.interface_text_font
    size 16
    color "#79bad0"
    outlines [(1, "#02060888", 0, 0)]

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

screen about():

    tag menu

    ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    ## включён в порт просмотра внутри экрана игрового меню.
    use game_menu(_("Об игре"), scroll="viewport"):

        style_prefix "about"

        frame:
            style "premium_info_card"

            vbox:
                spacing 18

                text _("ПРОЕКТ"):
                    style "premium_card_kicker"

                label "[config.name!t]"
                text _("Версия [config.version!t]")
                text _("Психологическая sci-fi визуальная новелла о временной петле, меняющихся ролях экипажа и попытке вытащить ISV Aurora с заранее заданного курса.")

                ## gui.about обычно установлено в options.rpy.
                if gui.about:
                    text "[gui.about!t]"

                null height 6

                text _("GitHub автора: {a=https://github.com/Username-Andrey-is-available}https://github.com/Username-Andrey-is-available{/a}")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style premium_info_card is frame
style premium_card_kicker is text

style about_label_text:
    size gui.label_text_size

style about_text:
    color "#d7dddf"
    outlines [(1, "#020608aa", 0, 0)]

style premium_info_card:
    xfill True
    padding (30, 26)
    background Solid("#0d1c23e4")

style premium_card_kicker:
    font gui.interface_text_font
    size 16
    color "#79bad0"
    outlines [(1, "#02060888", 0, 0)]


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen save():

    tag menu

    use file_slots(_("Сохранить"))


screen load():

    tag menu

    use file_slots(_("Загрузить"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):

        vbox:
            spacing 24
            xfill True
            yfill True

            frame:
                style "premium_info_card"

                vbox:
                    spacing 8

                    text _("АРХИВ ЦИКЛОВ"):
                        style "premium_card_kicker"

                    text _("Сохраняйте удачные попытки, чтобы возвращаться к ключевым развилкам без потери найденных улик."):
                        style "about_text"

            fixed:

                ## Это гарантирует, что ввод будет принимать enter перед остальными
                ## кнопками.
                order_reverse True

                frame:
                    style "slot_grid_frame"

                    vbox:
                        spacing 24
                        xfill True
                        yfill True

                        ## Номер страницы, который может быть изменён посредством клика на
                        ## кнопку.
                        button:
                            style "page_label"

                            key_events True
                            xalign 0.5
                            action [Function(pm_story_sfx, "ui_confirm"), page_name_value.Toggle()]

                            input:
                                style "page_label_text"
                                value page_name_value

                        ## Таблица слотов.
                        grid gui.file_slot_cols gui.file_slot_rows:
                            style_prefix "slot"

                            xalign 0.5
                            yalign 0.5

                            spacing gui.slot_spacing

                            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                                $ slot = i + 1

                                button:
                                    action [Function(pm_story_sfx, "ui_confirm"), FileAction(slot)]

                                    has vbox

                                    add FileScreenshot(slot) xalign 0.5

                                    text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пустой слот")):
                                        style "slot_time_text"

                                    text FileSaveName(slot):
                                        style "slot_name_text"

                                    key "save_delete" action FileDelete(slot)

            frame:
                style "page_footer_frame"

                hbox:
                    style_prefix "page"
                    xfill True
                    spacing 28
                    yalign 0.5

                    hbox:
                        xalign 0.5
                        spacing gui.page_spacing

                        textbutton _("<") action [Function(pm_story_sfx, "ui_confirm"), FilePagePrevious()]
                        key "save_page_prev" action FilePagePrevious()

                        if config.has_autosave:
                            textbutton _("{#auto_page}А") action [Function(pm_story_sfx, "ui_confirm"), FilePage("auto")]

                        if config.has_quicksave:
                            textbutton _("{#quick_page}Б") action [Function(pm_story_sfx, "ui_confirm"), FilePage("quick")]

                        for page in range(1, 10):
                            textbutton "[page]" action [Function(pm_story_sfx, "ui_confirm"), FilePage(page)]

                        textbutton _(">") action [Function(pm_story_sfx, "ui_confirm"), FilePageNext()]
                        key "save_page_next" action FilePageNext()

                    textbutton _("Удалить все сохранения"):
                        xalign 1.0
                        action [
                            Function(pm_story_sfx, "ui_confirm"),
                            Show(
                                "confirm",
                                message=_("Удалить все сохранения? Это действие нельзя отменить."),
                                yes_action=[
                                    Hide("confirm"),
                                    Function(pm_story_sfx, "ui_confirm"),
                                    Function(pm_delete_all_saves),
                                ],
                                no_action=[
                                    Hide("confirm"),
                                    Function(pm_story_sfx, "ui_back"),
                                ],
                            ),
                        ]

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
style slot_grid_frame is frame
style page_footer_frame is frame

style page_label:
    xpadding 28
    ypadding 10
    xalign 0.5
    background Solid("#10232b")

style page_label_text:
    size 23
    color "#d7dddf"
    textalign 0.5
    layout "subtitle"
    hover_color "#ffffff"

style page_button:
    xpadding 18
    ypadding 8
    background Solid("#0e1d24")
    hover_background Solid("#1a3540")
    selected_background Solid("#245566")

style page_button_text:
    size 23
    color "#aeb8bc"
    hover_color "#ffffff"
    selected_color "#ffffff"
    outlines [(1, "#020608aa", 0, 0)]

style slot_button:
    padding (16, 16)
    background Solid("#0f1c23")
    hover_background Solid("#17303a")
    selected_background Solid("#224653")

style slot_button_text:
    color "#d7dddf"
    hover_color "#ffffff"
    selected_color "#ffffff"
    outlines [(1, "#020608aa", 0, 0)]

style slot_time_text:
    size 18
    color "#9cafb5"

style slot_name_text:
    size 24

style slot_grid_frame:
    xfill True
    yfill True
    padding (26, 24)
    background Solid("#0d1b22df")

style page_footer_frame:
    xfill True
    padding (24, 20)
    background Solid("#0d1b22df")

## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    default settings_section = "display"

    use game_menu(_("Настройки")):

        vbox:
            spacing 24

            frame:
                style "premium_info_card"

                vbox:
                    spacing 8

                    text _("КОНТРОЛЬ СИСТЕМ"):
                        style "premium_card_kicker"

                    text _("Подстройте интерфейс, звук и темп чтения до входа в следующий виток."):
                        style "about_text"

            frame:
                style "help_tabs_frame"

                hbox:
                    spacing 14

                    if renpy.variant("pc") or renpy.variant("web"):
                        textbutton _("Дисплей") action SetScreenVariable("settings_section", "display")

                    textbutton _("Поток чтения") action SetScreenVariable("settings_section", "reading")
                    textbutton _("Интерфейс") action SetScreenVariable("settings_section", "interface")
                    textbutton _("Аудио") action SetScreenVariable("settings_section", "audio")

            frame:
                style "help_panel_frame"

                if settings_section == "display":
                    use preferences_display_panel
                elif settings_section == "reading":
                    use preferences_reading_panel
                elif settings_section == "interface":
                    use preferences_interface_panel
                elif settings_section == "audio":
                    use preferences_audio_panel


screen preferences_display_panel():

    vbox:
        spacing 12

        if renpy.variant("pc") or renpy.variant("web"):

            use settings_option_panel(_("ДИСПЛЕЙ"), _("Режим экрана"), _("Переключает игру между оконным и полноэкранным режимом.")):

                vbox:
                    style_prefix "radio"
                    spacing gui.pref_button_spacing
                    textbutton _("Оконный") action Preference("display", "window")
                    textbutton _("Полный") action Preference("display", "fullscreen")

        else:

            use settings_option_panel(_("ДИСПЛЕЙ"), _("Режим экрана"), _("На текущем устройстве этот параметр недоступен.")):
                null


screen preferences_reading_panel():

    vbox:
        spacing 12

        use settings_option_panel(_("ПОТОК ЧТЕНИЯ"), _("Пропуск"), _("Управляет тем, как игра ведёт себя при пропуске текста и переходов.")):

            vbox:
                style_prefix "check"
                spacing gui.pref_button_spacing
                textbutton _("Всего текста") action Preference("skip", "toggle")
                textbutton _("После выборов") action Preference("after choices", "toggle")
                textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))


screen preferences_interface_panel():

    vbox:
        spacing 12

        use settings_option_panel(_("ИНТЕРФЕЙС"), _("Скорость текста"), _("Определяет, насколько быстро выводятся реплики во время чтения.")):

            vbox:
                style_prefix "slider"
                spacing 10
                bar value Preference("text speed")


screen preferences_audio_panel():

    vbox:
        spacing 12

        if config.has_music:
            use settings_option_panel(_("АУДИО"), _("Громкость музыки"), _("Регулирует музыкальный фон в меню и во время сцен.")):

                vbox:
                    style_prefix "slider"
                    spacing 10
                    bar value Preference("music volume")

        if config.has_sound:
            use settings_option_panel(_("АУДИО"), _("Громкость звуков"), _("Регулирует эффекты интерфейса, тревог и событий корабля.")):

                hbox:
                    style_prefix "slider"
                    spacing 12
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton _("Тест") action Play("sound", config.sample_sound)


screen settings_option_panel(kicker, title, description):

    frame:
        style "settings_option_frame"

        vbox:
            spacing 12
            xfill True

            text kicker:
                style "settings_card_kicker"

            text title:
                style "settings_option_title"

            text description:
                style "settings_hint_text"

            transclude


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style settings_option_frame is frame
style settings_card_kicker is text
style settings_option_title is text
style settings_hint_text is text

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 780

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675

style settings_option_frame:
    xfill True
    padding (24, 20)
    background Solid("#0b1920eb")

style settings_card_kicker:
    font gui.interface_text_font
    size 15
    color "#5da6bf"
    outlines [(1, "#020608aa", 0, 0)]

style settings_option_title:
    font gui.interface_text_font
    size 30
    color "#f5f8f9"
    outlines [(2, "#020608aa", 0, 0)]

style settings_hint_text:
    font gui.interface_text_font
    size 18
    color "#9db0b7"
    outlines [(1, "#020608aa", 0, 0)]


## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Избегайте предсказывания этого экрана, так как он может быть очень
    ## массивным.
    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        frame:
            style "premium_info_card"

            vbox:
                spacing 8

                text _("ЖУРНАЛ СВИДЕТЕЛЯ"):
                    style "premium_card_kicker"

                text _("Здесь сохраняются последние реплики витка. Экран полезен, когда нужно заново связать улики, оговорки и детали разговоров."):
                    style "about_text"

        for h in _history_list:

            frame:
                style "history_entry_frame"

                vbox:
                    spacing 10

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False

                            ## Берёт цвет из who параметра персонажа, если он
                            ## установлен.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

        if not _history_list:
            frame:
                style "history_empty_frame"

                label _("История диалогов пуста.")


## Это определяет, какие теги могут отображаться на экране истории.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text
style history_entry_frame is frame
style history_empty_frame is frame

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xfill True

style history_name_text:
    size 24
    color "#78bdd1"
    outlines [(1, "#020608aa", 0, 0)]

style history_text:
    xfill True
    layout ("subtitle" if gui.history_text_xalign else "tex")
    size 23
    color "#e5edf0"
    outlines [(1, "#020608aa", 0, 0)]

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    size 25
    color "#d7e3e8"
    outlines [(1, "#020608aa", 0, 0)]

style history_entry_frame:
    xfill True
    padding (22, 18)
    background Solid("#0b1920e8")

style history_empty_frame:
    xfill True
    padding (24, 22)
    background Solid("#0b1920d8")


## Экран достижений ###########################################################
##
## Экран показывает прогресс по уликам, важным развилкам и концовкам.

screen flowchart():

    tag menu
    default ending_forecast_open = False

    $ flow_flags = pm_collect_flow_flags()
    $ unlocked_count, total_count = pm_flow_progress()
    $ ending_forecasts = [
        {"title": "Выход из петли", "share": "20%", "note": "Хорошая концовка"},
        {"title": "Истина", "share": "5%", "note": "Скрытая концовка"},
        {"title": "Цена спасения", "share": "10%", "note": "Самопожертвование"},
        {"title": "Петля замкнулась", "share": "24%", "note": "Финал по умолчанию"},
        {"title": "Инопланетная победа", "share": "14%", "note": "Мира не раскрыта"},
        {"title": "Паранойя", "share": "12%", "note": "Ложное обвинение"},
        {"title": "Обвал памяти", "share": "5%", "note": "Низкая память и стойкость"},
        {"title": "Когнитивный срыв", "share": "4%", "note": "Низкий анализ и авторитет"},
        {"title": "Раскол экипажа", "share": "3%", "note": "Низкая эмпатия и авторитет"},
        {"title": "Астероидное поле", "share": "2%", "note": "Ошибка ручного перехвата"},
        {"title": "Комната-тюрьма", "share": "1%", "note": "Капитан подавляет вас"},
    ]

    use game_menu(_("Достижения")):

        fixed:
            xfill True
            yfill True

            vbox:
                spacing 24

                frame:
                    style "flowchart_intro_frame"

                    vbox:
                        spacing 7

                        text _("Достижения цикла"):
                            style "flowchart_intro_title"

                        text _("Здесь собраны улики, ключевые развилки и концовки, которые вы уже открыли в предыдущих циклах."):
                            style "flowchart_intro_text"

                        text _("Открыто [unlocked_count] из [total_count] карточек. Тяните карту мышью влево и вправо или используйте нижнюю полосу прокрутки."):
                            style "flowchart_intro_meta"

                viewport:
                    style_prefix "flowchart"
                    draggable True
                    mousewheel False
                    pagekeys True
                    scrollbars "horizontal"
                    side_xfill True

                    hbox:
                        spacing 26

                        for week_index, week in enumerate(FLOWCHART_WEEKS):

                            frame:
                                style "flowchart_week_frame"

                                vbox:
                                    style "flowchart_week_vbox"

                                    text week["title"]:
                                        style "flowchart_week_title"

                                    text week["subtitle"]:
                                        style "flowchart_week_subtitle"

                                    null height 10

                                    for node in week["nodes"]:
                                        $ unlocked = node["key"] in flow_flags

                                        frame:
                                            style "flowchart_node_frame"
                                            background Solid((pm_flow_color(node["kind"], unlocked) + "cc") if unlocked else "#5e666daa")

                                            if unlocked:

                                                vbox:
                                                    spacing 5

                                                    text _("Открыто"):
                                                        style "flowchart_node_state"

                                                    text node["label"]:
                                                        style "flowchart_node_title"

                                                    text node["description"]:
                                                        style "flowchart_node_text"

                                            else:

                                                vbox:
                                                    spacing 10

                                                    text _("Скрыто"):
                                                        style "flowchart_node_state"

                                                    text _("?"):
                                                        style "flowchart_node_locked_mark"

                            if week_index + 1 < len(FLOWCHART_WEEKS):

                                frame:
                                    style "flowchart_connector"

            if ending_forecast_open:

                frame:
                    style "flowchart_forecast_frame"
                    xalign 0.0
                    yalign 1.0

                    vbox:
                        spacing 12

                        hbox:
                            xfill True

                            text _("Ожидаемые проценты"):
                                style "flowchart_forecast_title"

                            null xfill True

                            textbutton _("?"):
                                style "flowchart_forecast_toggle_button"
                                action ToggleScreenVariable("ending_forecast_open")

                        vbox:
                            spacing 6

                            for entry in ending_forecasts:

                                text "[entry['title']] — [entry['share']]. [entry['note']]":
                                    style "flowchart_forecast_body"

            else:

                textbutton _("?"):
                    style "flowchart_forecast_toggle_button"
                    action ToggleScreenVariable("ending_forecast_open")
                    xalign 0.0
                    yalign 1.0


style flowchart_viewport is gui_viewport
style flowchart_side is gui_side
style flowchart_hscrollbar is gui_hscrollbar
style flowchart_intro_frame is frame
style flowchart_intro_title is text
style flowchart_intro_text is text
style flowchart_intro_meta is text
style flowchart_week_frame is frame
style flowchart_week_vbox is vbox
style flowchart_week_title is text
style flowchart_week_subtitle is text
style flowchart_node_frame is frame
style flowchart_node_state is text
style flowchart_node_title is text
style flowchart_node_text is text
style flowchart_node_locked_mark is text
style flowchart_connector is frame
style flowchart_forecast_frame is frame
style flowchart_forecast_title is text
style flowchart_forecast_body is text
style flowchart_forecast_toggle_button is button
style flowchart_forecast_toggle_button_text is button_text

style flowchart_viewport:
    ymaximum 640
    xfill True

style flowchart_side:
    spacing 18

style flowchart_hscrollbar:
    unscrollable gui.unscrollable

style flowchart_intro_frame:
    xfill True
    padding (24, 20)
    background Solid("#0d1d24e6")

style flowchart_intro_title:
    font gui.interface_text_font
    size 30
    color "#f3f7f8"
    outlines [(2, "#020608aa", 0, 0)]

style flowchart_intro_text:
    font gui.interface_text_font
    size 22
    color "#c8d2d6"
    outlines [(1, "#020608aa", 0, 0)]

style flowchart_intro_meta:
    font gui.interface_text_font
    size 20
    color "#8dbfd0"
    outlines [(1, "#020608aa", 0, 0)]

style flowchart_week_frame:
    xsize 290
    yfill True
    padding (18, 18)
    background Solid("#071116dd")

style flowchart_week_vbox:
    spacing 14

style flowchart_week_title:
    font gui.interface_text_font
    size 31
    color "#f3f7f8"
    outlines [(2, "#020608aa", 0, 0)]

style flowchart_week_subtitle:
    font gui.interface_text_font
    size 18
    color "#87a0a8"
    outlines [(1, "#020608aa", 0, 0)]

style flowchart_node_frame:
    xfill True
    padding (15, 13)
    yminimum 118

style flowchart_node_state:
    font gui.interface_text_font
    size 16
    color "#f5f7f8"
    outlines [(1, "#020608aa", 0, 0)]

style flowchart_node_title:
    font gui.interface_text_font
    size 21
    xmaximum 220
    layout "subtitle"
    color "#ffffff"
    outlines [(2, "#020608aa", 0, 0)]

style flowchart_node_text:
    font gui.interface_text_font
    size 18
    xmaximum 220
    layout "subtitle"
    color "#e2edf0"
    outlines [(1, "#020608aa", 0, 0)]

style flowchart_node_locked_mark:
    font gui.interface_text_font
    size 54
    xalign 0.5
    color "#f3f7f8"
    outlines [(2, "#020608aa", 0, 0)]

style flowchart_connector:
    xsize 54
    ysize 4
    yalign 0.45
    background Solid("#2e6f87")

style flowchart_forecast_frame:
    xsize 560
    xpadding 18
    ypadding 18
    background Solid("#071116ee")

style flowchart_forecast_title:
    font gui.interface_text_font
    size 24
    color "#f3f7f8"
    outlines [(2, "#020608aa", 0, 0)]

style flowchart_forecast_body:
    font gui.interface_text_font
    size 17
    color "#dce7ea"
    outlines [(1, "#020608aa", 0, 0)]

style flowchart_forecast_toggle_button:
    xminimum 52
    yminimum 52
    xpadding 0
    ypadding 0
    background Solid("#55616aee")
    hover_background Solid("#73818bee")

style flowchart_forecast_toggle_button_text:
    font gui.interface_text_font
    size 28
    color "#f7fbfc"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Помощь")):

        style_prefix "help"

        vbox:
            spacing 24

            frame:
                style "premium_info_card"

                vbox:
                    spacing 8

                    text _("НАВИГАЦИЯ"):
                        style "premium_card_kicker"

                    text _("Короткая памятка по управлению без лишних системных подробностей. Всё, что нужно для чтения, выбора и проверки веток."):
                        style "about_text"

            frame:
                style "help_tabs_frame"

                hbox:
                    spacing 14

                    textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                    textbutton _("Мышь") action SetScreenVariable("device", "mouse")
                    textbutton _("Игровые механики") action SetScreenVariable("device", "mechanics")

                    if GamepadExists():
                        textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            frame:
                style "help_panel_frame"
                ymaximum 560

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    xfill True
                    yfill True

                    if device == "keyboard":
                        use keyboard_help
                    elif device == "mouse":
                        use mouse_help
                    elif device == "mechanics":
                        use mechanics_help
                    elif device == "gamepad":
                        use gamepad_help


screen keyboard_help():

    vbox:
        spacing 12

        use help_entry(_("Enter"), _("Подтверждает выбор, активирует кнопки и продолжает диалог."))
        use help_entry(_("Пробел"), _("Продвигает реплики без выбора ответов."))
        use help_entry(_("Стрелки"), _("Перемещают фокус по меню и интерактивным экранам."))
        use help_entry(_("Esc"), _("Открывает игровое меню."))
        use help_entry(_("Ctrl"), _("Ускоряет пропуск текста, пока клавиша зажата."))
        use help_entry(_("Tab"), _("Включает постоянный режим пропуска."))
        use help_entry(_("Page Up"), _("Откатывает ход чтения назад."))
        use help_entry(_("Page Down"), _("Возвращает откат вперёд, если он доступен."))
        use help_entry("H", _("Скрывает интерфейс пользователя для просмотра сцены."))
        use help_entry("S", _("Делает снимок экрана."))


screen mouse_help():

    vbox:
        spacing 12

        use help_entry(_("Левый клик"), _("Подтверждает выбор и продвигает диалоги."))
        use help_entry(_("Правый клик"), _("Открывает игровое меню."))
        use help_entry(_("Клик колёсиком"), _("Скрывает интерфейс пользователя."))
        use help_entry(_("Колёсико вверх"), _("Откатывает чтение назад."))
        use help_entry(_("Колёсико вниз"), _("Возвращает откат вперёд, если он доступен."))


screen gamepad_help():

    vbox:
        spacing 12

        use help_entry(_("Правый триггер / A"), _("Подтверждает выбор и продолжает диалог."))
        use help_entry(_("Левый триггер / LB"), _("Откатывает чтение назад."))
        use help_entry(_("Правый бампер"), _("Возвращает откат вперёд."))
        use help_entry(_("Крестовина / стики"), _("Перемещают фокус по интерфейсу."))
        use help_entry(_("Старт / B"), _("Открывает игровое меню."))
        use help_entry(_("Y"), _("Скрывает интерфейс пользователя."))

        textbutton _("Калибровка") action GamepadCalibrate()


screen mechanics_help():

    vbox:
        spacing 16
        xfill True

        text _("ХАРАКТЕРИСТИКИ ЭВАНА"):
            style "premium_card_kicker"

        use help_entry(_("Аналитика"), _("Научные проверки, вскрытие архивов, диагностика, расчёты и технические сцены."))
        use help_entry(_("Эмпатия"), _("Доверие, мягкое убеждение, работа с паникой, сбор союзников и удержание экипажа от срыва."))
        use help_entry(_("Стойкость"), _("Тяжёлые операции, выматывающие слоты, удержание темпа и некоторые финальные технические задачи."))
        use help_entry(_("Авторитет"), _("Приказы, кризисная координация, жёсткое убеждение и командные решения под давлением."))
        use help_entry(_("Память"), _("Даёт бонус или штраф к сложным убеждениям и логическим выводам. Снижается между неделями, но может частично восстанавливаться отдыхом и аккуратной игрой."))
        use help_entry(_("Статы по неделям"), _("Характеристики не откатываются в начале новой недели. Их меняют только ваши действия, провалы убеждения и сюжетные штрафы."))

        text _("РОЛИ И ПРОВЕРКИ"):
            style "premium_card_kicker"

        use help_entry(_("Первая неделя"), _("Базовая версия экипажа. Она знакомит с кораблём и даёт стартовые ориентиры по ролям и характерам."))
        use help_entry(_("Поздние недели"), _("Начиная со 2-й недели роли пересобираются заново для конкретного прохождения. Это случайность с ограничениями, а не полностью хаотическая мешанина."))
        use help_entry(_("Ключевые окна"), _("Редкие сильные сочетания ролей появляются не всегда. Например, у Лены есть только одно позднее окно в неделях 3-5, где она реально способна вскрывать путь к кабине пилотов."))
        use help_entry(_("Проверка помощи"), _("Для успешной помощи обычно нужны подходящая роль персонажа, нужная характеристика Эвана и достаточная память."))
        use help_entry(_("Саботажные роли"), _("Некоторые версии персонажей не просто слабо помогают, а сознательно уводят сцену в провал или саботаж."))
        use help_entry(_("Сложные исходы"), _("Редкие концовки и тяжёлые квесты должны требовать хорошего маршрута по статам и правильного окна по ролям, но не становиться недостижимыми."))

        frame:
            style "help_entry_frame"

            vbox:
                spacing 10

                text _("КАК ЧИТАТЬ ВЫБОРЫ"):
                    style "premium_card_kicker"

                text _("Полоски характеристик и подсветка выборов показывают, какая сторона сборки Эвана сейчас важнее всего. Если выбор окрашен смешанным цветом, сцена обычно требует сразу несколько сильных сторон."):
                    style "help_entry_description"


screen help_entry(key_name, description):

    frame:
        style "help_entry_frame"

        hbox:
            spacing 22
            xfill True
            yminimum 60

            text key_name:
                style "help_entry_key"

            text description:
                style "help_entry_description"


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_tabs_frame is frame
style help_panel_frame is frame
style help_entry_frame is frame
style help_entry_key is text
style help_entry_description is text

style help_button:
    xpadding 18
    ypadding 10
    background Solid("#0d1b22")
    hover_background Solid("#17303a")
    selected_background Solid("#245566")

style help_button_text:
    font gui.interface_text_font
    size 22
    color "#aeb8bc"
    hover_color "#ffffff"
    selected_color "#ffffff"
    outlines [(1, "#020608aa", 0, 0)]

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

style help_tabs_frame:
    xfill True
    padding (18, 16)
    background Solid("#0b1920db")

style help_panel_frame:
    xfill True
    padding (22, 20)
    background Solid("#0b1920eb")

style help_entry_frame:
    xfill True
    padding (18, 16)
    background Solid("#102129")

style help_entry_key:
    xsize 255
    yalign 0.5
    font gui.interface_text_font
    size 22
    color "#68b6cc"
    outlines [(1, "#020608aa", 0, 0)]

style help_entry_description:
    xfill True
    yalign 0.5
    textalign 0.0
    font gui.interface_text_font
    size 21
    color "#e5edf0"
    outlines [(1, "#020608aa", 0, 0)]



################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    zorder 200

    style_prefix "confirm"

    add Solid("#02070bb0")

    frame:
        style "confirm_frame"
        at premium_panel_reveal

        vbox:
            spacing 26

            text _("ПОДТВЕРЖДЕНИЕ"):
                style "confirm_kicker"
                xalign 0.5

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            text _("Это действие влияет на состояние текущего цикла или интерфейса."):
                style "confirm_hint"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 26

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text
style confirm_kicker is text
style confirm_hint is text

style confirm_frame:
    xmaximum 760
    padding (38, 30)
    background Solid("#0b1920f2")
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    size 30
    color "#f5f8f9"
    outlines [(2, "#020608aa", 0, 0)]

style confirm_button:
    xpadding 30
    ypadding 12
    background Solid("#102129")
    hover_background Solid("#17303a")
    selected_background Solid("#245566")

style confirm_button_text:
    font gui.interface_text_font
    size 22
    color "#d7dddf"
    hover_color "#ffffff"
    selected_color "#ffffff"
    outlines [(1, "#020608aa", 0, 0)]

style confirm_kicker:
    font gui.interface_text_font
    size 16
    color "#68b6cc"
    outlines [(1, "#020608aa", 0, 0)]

style confirm_hint:
    font gui.interface_text_font
    size 18
    color "#93a7ae"
    outlines [(1, "#020608aa", 0, 0)]


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Пропускаю")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_4" action NullAction()
    key "mouseup_5" action NullAction()

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Показывает меню, если есть. Меню может показываться некорректно, если
        ## config.narrator_menu установлено на True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Пузырьковый экран ###########################################################
##
## Экран пузырьков используется для отображения диалога игроку при использовании
## речевых пузырьков. Экран пузырьков принимает те же параметры, что и экран
## say, должен создать отображаемый объект с id "what", и может создавать
## отображаемые объекты с id "namebox", "who" и "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}





default manifest_selected_index = 0
default manifest_show_bio = False
default player_track_index = 0
default choice_rollback_targets = []

init python:
    import renpy.store as store

    STAT_COLORS = {
        "analysis": "#f08c2e",
        "empathy": "#43a047",
        "resilience": "#d64545",
        "authority": "#3b82f6",
    }

    CHOICE_STAT_REQUIREMENTS = {
        "Сослаться на нарушение техрегламента и возможную служебную проверку": ("authority",),
        "Показать ей странный паттерн отказов и попросить второй взгляд инженера": ("analysis",),
        "Напомнить, что из-за одного неверного шлюза люди могут не успеть выйти в аварийный коридор": ("empathy",),
        "Показать, что диверсант уже репетирует маршрут через слабые точки безопасности": ("authority",),
        "Разложить перед ним повторяющиеся пики сбоев и совпадения по доступам": ("analysis",),
        "Сказать прямо, что без тихого штаба экипаж сорвётся в охоту друг на друга": ("empathy",),
        "Пообещать не сенсацию, а документированную цепочку доступа и мотива": ("analysis",),
        "Сказать, что без её канала шёпот победит нас раньше диверсанта": ("empathy",),
        "Надавить через ответственность перед экипажем и цену публичной ошибки": ("authority",),
        "Говорить как офицер: без оценки ручного манёвра нельзя готовить штурм мостика": ("authority",),
        "Дать ему схему питания и попросить оценить реальное окно для ручного входа": ("analysis",),
        "Напомнить, что без него в решающий момент за штурвал сядет первый выживший": ("empathy",),
        "Опереться на протокол: без нестандартного решения медблок встретит массовый срыв": ("authority",),
        "Показать, что астрий уже даёт воспроизводимый эффект и требует врачебного контроля": ("analysis",),
        "Сказать прямо, что кто-то должен удержать людей от распада, пока мы ломаем курс": ("empathy",),
        "Провести ремонт дренажных фильтров с Леной": ("analysis",),
        "Собрать жалобы пассажиров с Сарой": ("empathy",),
        "Проверить аптечки с Кенджи": ("analysis",),
        "Попросить Томаса проверить учебный симулятор": ("authority",),
        "Проверить контейнер с биообразцами вместе с Мирой": ("analysis",),
        "Собрать реакторные логи с Леной": ("analysis",),
        "Проверить пропавшие минуты записи с Маркусом": ("authority",),
        "Разобрать странный контейнер с Мирой": ("analysis",),
        "Попросить Томаса оценить резервный люк": ("authority",),
        "Сверить улики вместе с Кенджи": ("analysis",),
        "вскрыть квантовый архив мостика": ("analysis", "resilience"),
        "Попросить Лену разобрать аварийный насос": ("analysis",),
        "Попросить Кенджи проверить токсикологию воды": ("analysis",),
        "Собрать карты доступа вместе с Маркусом": ("authority",),
        "Провести тихий брифинг с Сарой": ("empathy",),
        "Проверить шлюзовой журнал с Леной": ("analysis",),
        "Попросить Маркуса проверить тайники безопасности": ("authority",),
        "Согласовать антикризисный протокол с Кенджи": ("empathy",),
        "Подготовить канал оповещения с Сарой": ("empathy",),
        "Сверить питание мостика с Леной": ("analysis",),
        "Собрать показания с Сарой": ("empathy",),
        "синхронизировать три конфликтующих контура питания": ("analysis", "resilience"),
        "Попросить Томаса оценить ручной манёвр": ("authority",),
        "Попросить Маркуса вскрыть оружейный тайник": ("authority",),
        "Попросить Кенджи подготовить нейростабилизатор": ("analysis",),
        "провести ложный манёвр для отвлечения диверсанта": ("authority", "analysis"),
        "Собрать финальный резерв с Хейзом": ("authority",),
        "вручную перепрошить навигационное ядро": ("analysis", "resilience"),
        "эвакуировать гражданский сектор перед штурмом": ("authority", "empathy"),
    }

    def stat_tint(stat_name):
        return STAT_COLORS.get(stat_name, "#8d99a0")

    def _hex_to_rgb(color):
        color = color.lstrip("#")
        return tuple(int(color[index:index + 2], 16) for index in (0, 2, 4))

    def _rgb_to_hex(rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    def _mix_colors(base_color, accent_color, accent_weight):
        base_rgb = _hex_to_rgb(base_color)
        accent_rgb = _hex_to_rgb(accent_color)
        return _rgb_to_hex(tuple(
            int((base_channel * (1.0 - accent_weight)) + (accent_channel * accent_weight))
            for base_channel, accent_channel in zip(base_rgb, accent_rgb)
        ))

    def choice_stat_tint(stats):
        if not stats:
            return None

        colors = [_hex_to_rgb(stat_tint(stat_name)) for stat_name in stats if stat_name in STAT_COLORS]
        if not colors:
            return None

        count = float(len(colors))
        blended = tuple(int(sum(color[channel] for color in colors) / count) for channel in range(3))
        return _rgb_to_hex(blended)

    def choice_plate_color(stats, weight=0.42, alpha="dd"):
        tint = choice_stat_tint(stats)
        if not tint:
            return None
        return _mix_colors("#10212b", tint, weight) + alpha

    def pm_record_choice_rollback_point():
        if renpy.in_rollback():
            return

        history = getattr(store, "_history_list", [])
        if not history:
            return

        identifier = getattr(history[-1], "rollback_identifier", None)
        if not identifier:
            return

        if (not store.choice_rollback_targets) or store.choice_rollback_targets[-1] != identifier:
            store.choice_rollback_targets.append(identifier)

    def pm_previous_choice_identifier():
        valid_identifiers = [
            identifier
            for identifier in store.choice_rollback_targets
            if renpy.get_identifier_checkpoints(identifier) is not None
        ]

        if not valid_identifiers:
            return None

        if renpy.get_screen("choice") is not None:
            return valid_identifiers[-2] if len(valid_identifiers) >= 2 else None

        return valid_identifiers[-1]

    PLAYER_TRACKS = [
        ("Основная тема", "audio/main_theme.mp3"),
        ("Тревожный контур", "audio/tension_theme.mp3"),
        ("Нулевая гравитация", "audio/ambient_theme.mp3"),
    ]

    def cycle_music_track(delta):
        global player_track_index
        if not PLAYER_TRACKS:
            return
        player_track_index = (player_track_index + delta) % len(PLAYER_TRACKS)

    def play_selected_track():
        if not PLAYER_TRACKS:
            return
        name, path = PLAYER_TRACKS[player_track_index]
        if renpy.loadable(path):
            renpy.music.play(path, channel="music", loop=True, fadein=0.5)
        else:
            renpy.notify("Трек '%s' пока не найден в папке game/audio." % name)

screen hud_stats():

    if not main_menu:
        $ memory_state_label = {"sharp": "ясная", "strained": "напряжённая", "fractured": "рваная"}.get(manifest_state.memory_tier(), "ясная")
        frame:
            xpos 0
            ypos 0
            xsize 350
            ysize 300
            background None

            vbox:
                spacing 6
                text "Эван Картер" size 22
                text "Память: [manifest_state.memory_stability] ([memory_state_label])" size 16
                text "Слоты: [manifest_state.week_time_spent]/[manifest_state.week_time_budget]" size 16

                hbox:
                    spacing 8
                    textbutton "Манифест" action ToggleScreen("manifest_panel")
                    textbutton "Плеер" action ToggleScreen("music_player_panel")

                text "Аналитика" size 14
                bar:
                    value StaticValue(manifest_state.stats["analysis"], 100)
                    xmaximum 320
                    left_bar Solid(stat_tint("analysis"))
                    right_bar Solid("#2a2a2a")

                text "Эмпатия" size 14
                bar:
                    value StaticValue(manifest_state.stats["empathy"], 100)
                    xmaximum 320
                    left_bar Solid(stat_tint("empathy"))
                    right_bar Solid("#2a2a2a")

                text "Стойкость" size 14
                bar:
                    value StaticValue(manifest_state.stats["resilience"], 100)
                    xmaximum 320
                    left_bar Solid(stat_tint("resilience"))
                    right_bar Solid("#2a2a2a")

                text "Авторитет" size 14
                bar:
                    value StaticValue(manifest_state.stats["authority"], 100)
                    xmaximum 320
                    left_bar Solid(stat_tint("authority"))
                    right_bar Solid("#2a2a2a")


screen music_player_panel():
    tag music_player_panel
    zorder 121

    frame:
        xpos 370
        yalign 0.02
        xsize 460
        ysize 250
        background Frame("gui/frame.png", 18, 18)

        vbox:
            spacing 10
            text "Плеер Эвана" size 28
            if PLAYER_TRACKS:
                text "Текущий трек: [PLAYER_TRACKS[player_track_index][0]]" size 18
                text "Управление темой сцены" size 14
                hbox:
                    spacing 8
                    textbutton "◀" action Function(cycle_music_track, -1)
                    textbutton "▶" action Function(cycle_music_track, 1)
                    textbutton "Play" action Function(play_selected_track)
                    textbutton "Pause" action PauseAudio("music")
            else:
                text "Список треков пуст." size 16
            textbutton "Закрыть" action Hide("music_player_panel")


screen top_info():

    if not main_menu:

        vbox:
            xalign 0.98
            yalign 0.02

            text "Цикл: [manifest_state.loop_count]":
                size 22
                color "#ffffff"
                outlines [(2, "#000000aa", 0, 0)]

            text "[PLAYER_TRACKS[player_track_index][0]]":
                size 20
                color "#cccccc"
                outlines [(2, "#000000aa", 0, 0)]


screen character_layer(who):

    zorder 100

    $ speaker_portrait = SPEAKER_PORTRAITS.get(who, None)

    if speaker_portrait and not renpy.variant("small"):
        add speaker_portrait:
            xpos 1960
            ypos 1080
            xanchor 1.0
            yanchor 1.0
            zoom 0.9


screen manifest_panel():
    tag manifest_panel
    modal True
    zorder 300

    $ cid, card = manifest_state.get_card_by_index(manifest_selected_index)
    $ records = list(reversed(manifest_state.history))
    $ manifest_panel_width = min(1550, config.screen_width - 80)
    $ manifest_panel_height = min(880, config.screen_height - 120)
    $ manifest_scroll_height = max(240, manifest_panel_height - 380)

    add Solid("#051015a8")

    button:
        xfill True
        yfill True
        background None
        action NullAction()

    frame:
        xalign 0.5
        yalign 0.5
        xsize manifest_panel_width
        ysize manifest_panel_height
        background Frame("gui/frame.png", 24, 24)

        vbox:
            spacing 14

            hbox:
                xfill True
                text "Passenger Manifest" size 36
                null width 30
                textbutton "Закрыть" action Hide("manifest_panel")

            text "Текущая неделя: [manifest_state.week_index], цикл: [manifest_state.loop_count]" size 18

            hbox:
                spacing 14
                textbutton "← Предыдущее досье" action SetVariable("manifest_selected_index", manifest_selected_index - 1)
                textbutton "Следующее досье →" action SetVariable("manifest_selected_index", manifest_selected_index + 1)
                textbutton "Изучить досье (биографии)" action ToggleVariable("manifest_show_bio")

            if card:
                frame:
                    background Frame("gui/frame.png", 18, 18)
                    xfill True
                    yminimum 220

                    vbox:
                        spacing 8
                        text "[card['name']]" size 30
                        text "Базовая роль: [card['base_role']]" size 18

                        if manifest_show_bio:
                            text "Биография: [card['bio_base']]" size 17
                            text "Важный поворот жизни: [manifest_state.get_public_life_path(card)]" size 17
                            text "Наблюдение Эвана: [manifest_state.get_public_trait(card)]" size 17

                        text "Текущая специальность: [manifest_state.get_public_role(card)]" size 20
                        text "Статус: [manifest_state.get_public_status(card)]" size 18

                if manifest_show_bio:

                    frame:
                        background Frame("gui/frame.png", 16, 16)
                        xfill True
                        yfill True   # <<< ВАЖНО (не фикс высота!)

                        has vbox

                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            xfill True
                            yfill True   # <<< КЛЮЧ

                            vbox:
                                spacing 8
                                xfill True
                                text "Предыдущие версии досье" size 24

                                for idx, rec in enumerate(records):
                                    $ rec_card = manifest_state.get_card_in_record(rec, cid)
                                    if rec_card:
                                        $ prev = records[idx+1] if idx + 1 < len(records) else None
                                        $ prev_card = manifest_state.get_card_in_record(prev, cid) if prev else None
                                        $ life_changed = prev_card and prev_card.get('life_path') != rec_card.get('life_path')
                                        $ trait_changed = prev_card and prev_card.get('trait') != rec_card.get('trait')
                                        text "Цикл #[rec['loop']] / Неделя [rec['week']]" size 18
                                        text "Биография: [rec_card['bio_base']]" size 16
                                        text "Поворот жизни: [manifest_state.format_with_underline_if_changed(manifest_state.get_public_life_path(rec_card), life_changed, rec['week'])]" size 16
                                        text "Отметка Эвана: [manifest_state.format_with_underline_if_changed(manifest_state.get_public_trait(rec_card), trait_changed, rec['week'])]" size 16
                                        text "Специальность в цикле: [manifest_state.get_manifest_role(rec, cid)]" size 16
                                        text "Статус в цикле: [manifest_state.get_public_status(rec_card)]" size 16
                                        text ""


init python:
    if "hud_stats" not in config.overlay_screens:
        config.overlay_screens.append("hud_stats")

################################################################################
## Мобильные варианты
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Раз мышь может не использоваться, мы заменили быстрое меню версией,
## использующей меньше кнопок, но больших по размеру, чтобы их было легче
## касаться.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:
        $ previous_choice_identifier = pm_previous_choice_identifier()

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Назад") action Rollback()
            textbutton _("Пред. выбор"):
                action (RollbackToIdentifier(previous_choice_identifier) if previous_choice_identifier else NullAction())
                sensitive previous_choice_identifier is not None
            textbutton _("След. выбор") action Skip(fast=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Меню") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
