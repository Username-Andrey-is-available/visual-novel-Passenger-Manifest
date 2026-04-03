label week_5_arc:
    scene bg corridor
    na "Неделя 5: правда о корабле."
    ev "Нужно пролезть в технический контур и добраться до архивов пилотской смены."
    ev "Кажется, я могу пробовать что-угодно, но... кто знает сколько у меня попыток."
    na "Кенджи ведёт утренние обходы, а Эван подписывает медицинские и архивные протоколы по смене."
    call w5_proof_scene from _call_w5_proof_scene


    call w5_pre_slots_scene from _call_w5_pre_slots_scene
    call w5_slot_1 from _call_w5_slot_1
    call w5_between_1_2_scene from _call_w5_between_1_2_scene
    call w5_slot_2 from _call_w5_slot_2
    call w5_between_2_3_scene from _call_w5_between_2_3_scene
    call w5_slot_3 from _call_w5_slot_3
    call w5_between_3_4_scene from _call_w5_between_3_4_scene
    call w5_slot_4 from _call_w5_slot_4
    call w5_between_4_5_scene from _call_w5_between_4_5_scene
    call w5_slot_5 from _call_w5_slot_5
    call w5_between_5_6_scene from _call_w5_between_5_6_scene
    call w5_slot_6 from _call_w5_slot_6
    call w5_between_6_7_scene from _call_w5_between_6_7_scene
    call w5_slot_7 from _call_w5_slot_7
    call w5_post_slots_scene from _call_w5_post_slots_scene
    call w5_quiet_corridor_scene from _call_w5_quiet_corridor_scene
    call w5_sabotage_report from _call_w5_sabotage_report

    if "dead_pilots" in manifest_state.evidence:
        na "После вскрытия кабины сомнений не остаётся: пилоты давно мертвы, а корабль ведёт чужой сценарий автопилота."
        ev "Нас заранее ведут к чёрной дыре."
    else:
        na "Я всё ближе к ответу, но без вскрытой кабины пилотов не хватает главного звена."
        ev "Кто-то слишком старательно держит меня подальше от той двери."
    return

label w5_quiet_corridor_scene:
    scene bg corridor
    tg "Слышишь?"
    ev "Ничего."
    tg "Вот именно. На работающем корабле так тихо не бывает."
    ev "Потому что часть секций давно мертва, а мы всё ещё изображаем штатный режим."
    tg "Я десять лет учил пилотов держать курс."
    tg "Впервые вижу корабль, который держит курс против людей на борту."
    ev "И всё равно мы его развернём."
    return

label w5_pre_slots_scene:
    scene bg corridor
    ev "Начинаю неделю с простого правила: каждое действие либо даёт улику, либо двигает нас к мостику."
    na "На служебных экранах мигают бытовые задачи — замена ламп, проверка фильтров, контроль давления в душевых."
    return

label w5_between_1_2_scene:
    scene bg technical
    ev "Между слотами просматриваю карту аварийных люков и пометки Лены на полях."
    ev "Почерк у неё такой же, как неделя: резкий, без украшений, только маршруты и риск."
    return

label w5_between_2_3_scene:
    scene bg canteen
    na "В короткий перерыв экипаж смотрит в досуговом модуле старый комедийный сериал про неуклюжих астронавтов."
    ev "Смеюсь вместе со всеми и думаю, как мало людям надо, чтобы на час перестать бояться."
    return

label w5_between_3_4_scene:
    scene bg corridor
    ev "Перед следующим слотом возвращаюсь в каюту и меняю батарею в наладоннике с архивами."
    ev "Смешно: в петле может сломаться всё, кроме необходимости вовремя заряжать технику."
    return

label w5_between_4_5_scene:
    scene bg technical
    $ pm_story_sfx("metallic_impact")
    na "Из глубины техотсека доносится короткий металлический удар, и несколько человек одновременно поднимают головы."
    ev "Любой звук кажется либо уликой, либо началом катастрофы. Обычно и тем, и другим."
    return

label w5_between_5_6_scene:
    scene bg corridor
    tg "Если опять не переведёшь дух, на мостик войдёт не лидер, а ходячий тремор."
    ev "Спасибо. Две минуты тишины — и дальше в отсек."
    return

label w5_between_6_7_scene:
    scene bg laboratory
    na "Лабораторный терминал медленно выгружает очередной фрагмент архива, полоска прогресса тянется мучительно долго."
    ev "Эти секунды ожидания меня так раздражают... я уже рядом!"
    return

label w5_post_slots_scene:
    scene bg corridor
    na "После серии решений Эван берёт в библиотеке книгу 'Домой через ночь' и читает главу в коридоре."
    ev "Так цвета означали ауры людей в глазах безликого! Значит, все люди из 'радуги'..."
    ev "Вот что значило 'фиолетовый, последний цвет', она должна стать последней жертвой."
    na "Эван захлопнул книгу."
    return

label w5_slot_1:
    menu:
        "Неделя 5 / Слот 1"
        "Техническая инфильтрация с Леной":
            $ manifest_state.take_action("w5_infiltration")
            scene bg technical
            if manifest_state.can_interact_with("lena"):
                if manifest_state.role_requirement_met("lena", ["engineer", "repair_key"]):
                    le "Дам тебе одиннадцать минут, пока датчики висят в диагностике."
                    le "На двенадцатой запищит всё. Даже совесть капитана."
                    $ manifest_state.add_ally_by_tag("technical")
                    ev "Тогда работаем быстро."
                else:
                    le "Я такую инфильтрацию не тяну. Контур слишком злой."
                    ev "Понял. Сорвёмся ещё на входе."
            else:
                na "Лена избегает вас; операция срывается до начала."
        "Официальный запрос капитану":
            $ manifest_state.take_action("w5_official")
            scene bg bridge
            ch "Доступ запрещён. Это вопрос командования."
            ch "Ещё один несанкционированный запрос, и я ограничу ваш протокол."
            ev "Понял, не дурак."
        "Научная рутина: анализ траектории":
            $ manifest_state.take_action("w5_trajectory")
            scene bg laboratory
            ev "Курс к чёрной дыре подправляют мелкими импульсами каждые восемь часов."
            ev "И у этих импульсов один и тот же почерк."
            $ manifest_state.register_evidence("microcourse_corrections")
        "вручную сверить резервные гироскопы":
            $ manifest_state.take_action("w5_quest_gyros")
            $ manifest_state.complete_quest("quest_09_gyros")
            $ manifest_state.register_evidence("gyro_bias")
            na "Квест выполнен: резервные гироскопы искусственно смещены на доли градуса."
            ev "Этого хватает, чтобы неделями вести корабль в ловушку и не палиться."
    return

label w5_slot_2:
    menu:
        "Неделя 5 / Слот 2"
        "Разговор с Томасом о ручном перехвате":
            $ manifest_state.take_action("w5_thomas")
            scene bg bridge
            if manifest_state.can_interact_with("thomas"):
                if manifest_state.role_requirement_met("thomas", ["veteran", "savior"]):
                    tg "Если доберёмся до мостика, я сяду за баранку. Но нужен полный контур питания."
                    tg "Один провал, и останемся в падении без права на коррекцию."
                    $ manifest_state.add_ally_by_tag("pilot")
                    ev "Значит, нужны два ключа: питание и доступ."
                else:
                    tg "Процедуру я знаю в теории. Руками такое не водил."
                    ev "Значит, пилотского ресурса в этой ветке не хватает."
            else:
                na "Томас не приходит на встречу и переводит разговор в формальный канал."
        "Разговор с Кенджи о вскрытии отчётов":
            $ manifest_state.take_action("w5_kenji")
            scene bg laboratory
            if manifest_state.can_interact_with("kenji"):
                kt "Следы токсина указывают: пилоты погибли задолго до последних служебных отметок."
                kt "По журналам тела не должны выглядеть так 'свежо'. Значит, отчёты правили руками."
                kt "Я сейчас-же сообщу Хейзу."
                $ manifest_state.register_evidence("pilot_toxin")
                ev "Спасибо. Я возьму на себя ответственность за обнаруженное и сам сообщу капитану, не отвлекайся от работы."
            else:
                na "Кенджи отказывается обсуждать с вами вскрытие без посредника."
        "Досуговый час в баре экипажа":
            $ manifest_state.take_action("w5_bar")
            scene bg canteen
            mr "Люди на грани. Ещё одна искра — и всё вспыхнет."
            mr "Мне нужен повод не вводить жёсткий режим безопасности."
            ev "Я дам тебе повод — но мне нужно время до конца недели."
    return

label w5_slot_3:
    menu:
        "Неделя 5 / Слот 3"
        "Сара помогает собрать хронологию":
            $ manifest_state.take_action("w5_timeline")
            scene bg canteen
            if manifest_state.can_interact_with("sarah"):
                sc "Я свела камеры, логи и доступы. Кто-то стирает последние сорок секунд каждого события."
                sc "Это не чистка следов. Это какой-то монтаж реальности под отчёт."
                $ manifest_state.register_evidence("log_wipes")
                $ manifest_state.add_ally_by_tag("ally_candidate")
            else:
                na "Сара избегает вас; хронология остаётся несобранной."
        "Маркус проводит обыск грузового сектора":
            $ manifest_state.take_action("w5_search")
            scene bg technical
            if manifest_state.can_interact_with("marcus"):
                mr "Нашёл оружие, которого не должно быть на пассажирском рейсе."
                mr "Если это всплывёт раньше срока, начнётся охота на ведьм."
                mr "Держи это в секрете."
                $ manifest_state.register_evidence("illegal_weapons")
                ev "Почему ты мне это сообщил..."
            else:
                na "Маркус уклоняется от совместного обыска."
        "Личная работа с Manifest":
            $ manifest_state.take_action("w5_manifest_refine")
            ev "Чем больше фактов, тем страшнее итог."
            ev "Но только фактами я пока и удерживаю себя от паники."
        "обнаружить источник поддельных биометрий":
            $ manifest_state.take_action("w5_quest_biometrics")
            $ manifest_state.complete_quest("quest_10_biometrics")
            $ manifest_state.register_evidence("biometric_spoof")
            na "Квест выполнен: найден генератор фальшивых биометрических подписей."
            ev "Кто-то заходил в ключевые зоны лицом людей, которых там не было."
    return

label w5_slot_4:
    menu:
        "Неделя 5 / Слот 4"
        "Прямо обвинить Миру":
            $ manifest_state.take_action("w5_blame_mira")
            if manifest_state.role_requirement_met("mira", ["alien"]) and ("second_observer" in manifest_state.evidence or "note_final_cycle" in manifest_state.evidence):
                $ manifest_state.register_evidence("mira_pressure_point")
                ev "Слишком много совпадений сходится на Мире. Она не та, кем себя выдаёт."
            else:
                $ manifest_state.adjust_stat("authority", -2)
                ev "Я давлю слишком рано и слышу насколько мои аргументы слабые."
                ev "Нет. Так нельзя. Иначе я принесу людям не расследование, а страх."
        "Подготовить тихую операцию на следующую неделю":
            $ manifest_state.take_action("w5_prepare_finale")
            ev "Нужны люди, которым я доверяю, и план на каждый шлюз."
            ev "Одна заминка, и нас запрут в переходе между отсеками."
        "Наблюдать за горизонтом событий":
            $ manifest_state.take_action("w5_horizon")
            ev "Край тьмы напоминает: времени больше не станет."
            ev "Вселенная не торгуется. Она просто закрывает окно."
        "синхронизировать три конфликтующих контура питания":
            $ manifest_state.take_action("w5_quest_power_sync")
            if manifest_state.meets_quest_requirements("quest_17_power_sync"):
                $ manifest_state.complete_quest("quest_17_power_sync")
                $ manifest_state.register_evidence("power_sync_map")
                na "Квест выполнен: силовые контуры сведены в единое окно на 27 секунд."
                ev "Математика адская: если любое реле опоздает на долю секунды, мостик погаснет в момент штурма."
            else:
                ev "Пытаюсь совместить контуры, но схема расползается на последнем этапе."
                ev "Нужно больше аналитики и выносливости. Иначе спалим резерв ещё до финала."
    return


label w5_sabotage_report:
    scene bg bridge
    na "Саботаж выходит на новый уровень: в системе жизнеобеспечения сменены приоритеты воздуха между палубами."
    ev "Я показываю капитану досье и цепочку допусков за последние циклы."
    ch "Что за несуразица, твой манифест неисправен."
    ch "У этих людей несовместимые профили. Один числится стажёром, а доступ у него как у инженера первой категории."
    ch "Как они вообще прошли проверку перед вылетом?"
    ch "Я взял вопрос на контроль, но если это какая-то шутка, то ты плохо меня знаешь, Эван."
    $ manifest_state.register_evidence("sabotage_air_priority")
    return


label w5_proof_scene:
    scene bg bridge
    ev "Томас терпит только конкретный запрос. Либо у меня есть внятная причина лезть в пилотскую часть, либо он меня сразу осадит."
    call generic_weekly_proof_scene("thomas", "Томас") from _call_generic_weekly_proof_scene_5
    return

label w5_slot_5:
    menu:
        "Неделя 5 / Слот 5"
        "Сверить питание мостика с Леной":
            call generic_role_quest(
                "w5_partner_bridge_power", "lena", "analysis", 63, "bridge_power_splice",
                "Лена матерится шёпотом, но собирает схему: кто-то тайно вшил мостик в контур, который можно вырубить с техпалубы.",
                "Схема разваливается на последнем узле, и у вас остаётся только догадка о диверсии.",
                "Лена не помогает: в каждом её движении чувствуется чужой расчёт."
            ) from _call_generic_role_quest_18
        "Собрать показания с Сарой":
            call generic_role_quest(
                "w5_partner_testimonies", "sarah", "empathy", 62, "crew_timeline_testimony",
                "Сара собирает свидетельства так, будто монтирует документалку: всё сходится в одну страшную линию.",
                "Люди слишком напуганы, и даже Сара не вытягивает из них цельную хронологию.",
                "Сара не помогает: она выбирает манипуляцию, а не честное свидетельство."
            ) from _call_generic_role_quest_19
    return

label w5_slot_6:
    menu:
        "Неделя 5 / Слот 6"
        "Попросить Томаса оценить ручной манёвр":
            call generic_role_quest(
                "w5_partner_manual_course", "thomas", "authority", 64, "manual_course_window",
                "Томас быстро рисует окно манёвра: 'двадцать семь секунд, сынок. Больше космос не даст'.",
                "Томас не удерживает расчёт до конца: без реального навыка манёвр остаётся красивой теорией.",
                "Томас не помогает. Сейчас он больше обуза, чем пилот спасения."
            ) from _call_generic_role_quest_20
        "Попросить Маркуса вскрыть оружейный тайник":
            call generic_role_quest(
                "w5_partner_armory", "marcus", "authority", 62, "armory_override",
                "Маркус действует жёстко и быстро: тайник открыт, и теперь у вас есть козырная карта тех, кто готовился к насилию заранее.",
                "Маркус не дотягивает до чистого вскрытия, и тайник остаётся запечатанным.",
                "Маркус не помогает — этот тайник для него ценнее правды."
            ) from _call_generic_role_quest_21
    return

label w5_slot_7:
    menu:
        "Неделя 5 / Слот 7"
        "Третий этап исследования астрия":
            jump w5_astrium_chain
        "Повторить сценарий штурма вслух":
            $ manifest_state.take_action("w5_rehearsal")
            ev "Проговариваю план по шагам. Голос дрожит только на слове 'если'."
        "Попросить Лену вскрыть кабину пилотов":
            call investigate_pilot_cabin_with_lena("w5_pilot_cabin_lena") from _call_investigate_pilot_cabin_with_lena_2
    return

label w5_astrium_chain:
    $ manifest_state.take_action("w5_astrium_stage3")
    $ manifest_state.set_logic_hint("Теперь нужно доказать, что полезное свойство астрия можно передать живому носителю, а не только технике.")
    menu:
        "Астрий / Шаг 5"
        "Сверить реакцию вещества с нейроэлектрическими пиками у человека":
            $ a5 = True
        "Проверить, не связан ли эффект только с гормональной реакцией на стресс, а не с памятью и личностью":
            $ a5 = False
    $ manifest_state.set_logic_hint("Если астрий выравнивает импульсы, последняя проверка — можно ли обменять это знание на доступ к саботёрам.")
    menu:
        "Астрий / Шаг 6"
        "Сделать вывод, что астрий экранирует краткие когнитивные искажения и ценен для тех, кто живёт на грани аномалии":
            $ a6 = True
        "Решить, что астрий всего лишь временно глушит симптомы и потому интересен только как дорогой седатив":
            $ a6 = False
    $ manifest_state.clear_logic_hint()
    if a5 and a6:
        $ manifest_state.advance_element_stage("Астрий кратко выравнивает когнитивные скачки и потому бесценен тем, кто балансирует между масками и ролями.")
        $ manifest_state.register_evidence("astrium_cognitive_buffer")
        ev "Теперь ясно, почему за ним охотятся. Астрий не лечит совесть, но удерживает личность от распада у самой аномалии."
    else:
        $ manifest_state.register_logic_chain(False)
        ev "Я опять выбираю красивое объяснение вместо точного."
    return
