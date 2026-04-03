label week_4_arc:
    scene bg corridor
    na "Неделя 4: второй наблюдатель."
    ev "Кто-то произносит фразу, которую можно сказать только с памятью о прошлых циклах."
    ev "После этого любой взгляд уже звучит как проверка."
    na "Медик снова проходит по каютам, фиксируя скачки тревожности и бессонницу."
    call w4_proof_scene from _call_w4_proof_scene


    call w4_pre_slots_scene from _call_w4_pre_slots_scene
    call w4_slot_1 from _call_w4_slot_1
    call w4_between_1_2_scene from _call_w4_between_1_2_scene
    call w4_slot_2 from _call_w4_slot_2
    call w4_between_2_3_scene from _call_w4_between_2_3_scene
    call w4_slot_3 from _call_w4_slot_3
    call w4_between_3_4_scene from _call_w4_between_3_4_scene
    call w4_slot_4 from _call_w4_slot_4
    call w4_between_4_5_scene from _call_w4_between_4_5_scene
    call w4_slot_5 from _call_w4_slot_5
    call w4_between_5_6_scene from _call_w4_between_5_6_scene
    call w4_slot_6 from _call_w4_slot_6
    call w4_between_6_7_scene from _call_w4_between_6_7_scene
    call w4_slot_7 from _call_w4_slot_7
    call w4_post_slots_scene from _call_w4_post_slots_scene
    call w4_observation_deck_dialogue from _call_w4_observation_deck_dialogue
    call w4_found_note from _call_w4_found_note
    call w4_sabotage_report from _call_w4_sabotage_report

    na "Подозрения множатся. Любой разговор может быть ловушкой."
    ev "Если я ошибусь с выводом, корабль взорвётся от страха раньше сингулярности."
    return

label w4_observation_deck_dialogue:
    scene expression pm_story_image("observation_anomaly", "images/backgrounds/observation dome.png")
    ms "Смотри. Видишь этот свет у края?"
    ev "Гравитационное линзирование."
    ms "Я называю это местом, где правда ломается раньше всего."
    ev "Ты говоришь так, будто уже не в первый раз это видишь."
    ms "А если так и есть, ты сможешь с этим жить?"
    ev "Смогу, если это выведет людей отсюда."
    ms "Тогда не ищи чудовище в одном лице. Иногда чудовище — это сам способ выбирать."
    return

label w4_pre_slots_scene:
    scene bg corridor
    ev "Перед первым слотом глушу личный канал: сегодня лишний шум может стоить решения."
    na "По служебной сети идут обычные сообщения — ремонт фильтров, график питания, просьба вернуть чужой гаечный ключ."
    return

label w4_between_1_2_scene:
    scene bg corridor
    ev "Лифт зависает на полминуты между палубами, и я слышу, как в шахте гудят силовые кабели."
    ev "Корабль звучит как огромный организм, который тоже устал от этой недели."
    return

label w4_between_2_3_scene:
    scene bg canteen
    na "В столовой устраивают 'тихий час': вместо новостей включают запись дождя с Земли."
    ev "Пару минут слушаю и вспоминаю, как пахнет мокрый асфальт после ливня."
    return

label w4_between_3_4_scene:
    scene bg corridor
    ev "Перед следующим слотом срываюсь в спорт-модуль: три подхода, холодная вода, тишина."
    ev "Тело должно напомнить голове, что мы ещё живы. А значит, ещё выбираем."
    return

label w4_between_4_5_scene:
    scene bg canteen
    sc "Знаешь, что страшнее слухов? Когда люди уже о меню шепчутся."
    ev "Тогда мне надо успеть раньше шёпота. Как только он станет нормой, корабль уйдёт панике."
    return

label w4_between_5_6_scene:
    scene bg corridor
    $ pm_story_sfx("light_flicker")
    na "Световая дорожка аварийного выхода на секунду вспыхивает ярче обычного и снова гаснет до штатного режима."
    ev "Система будто моргает мне в ответ. Терпеть не могу, когда техника начинает намекать."
    return

label w4_between_6_7_scene:
    scene bg observation
    na "За стеклом медленно плывёт искажённое сияние линзирования, а в отражении Эван на миг кажется самому себе старше на несколько циклов."
    ev "Я уже не различаю, где усталость, а где память о смертях, которых формально ещё не было."
    return

label w4_post_slots_scene:
    scene bg corridor
    na "После слотов Эван забирает из обменной полки тонкий роман о полярной экспедиции."
    ev "Читаю сцену про снежную бурю и думаю: космос и лёд одинаково не прощают беспечность."
    return

label w4_slot_1:
    menu:
        "Неделя 4 / Слот 1"
        "Точечные интервью по досье":
            $ manifest_state.take_action("w4_interviews")
            ev "На одни и те же вопросы в каждом цикле отвечают по-разному."
            ev "Люди будто те же. А внутренняя сборка уже другая."
        "Сканирование микрогравитационных флуктуаций":
            $ manifest_state.take_action("w4_scan")
            $ manifest_state.register_evidence("observer_phase_shift")
            ev "Кто-то лезет в паттерн ещё до того, как он проявится."
            ev "Это не реакция. Это упреждение."
        "Отдых в спорт-модуле":
            $ manifest_state.take_action("w4_gym")
            tg "Иногда выживает не самый умный. Выживает тот, кто дольше держит темп."
            tg "Сначала дыхание. Потом решения. Иначе сгоришь раньше финиша."
            ev "Принял. На этой неделе мне нужен холодный пульс."
    return

label w4_slot_2:
    menu:
        "Неделя 4 / Слот 2"
        "Прямой разговор с Мирой":
            $ manifest_state.take_action("w4_mira_direct")
            scene bg laboratory
            if manifest_state.can_interact_with("mira"):
                ms "Вероятно, память о прошлых неделях... не только у тебя."
                ms "А если точнее, всё зависит от того, кто спрашивает."
                $ manifest_state.register_evidence("second_observer")
                ev "Опять в сторону. Прямого ответа я не дождусь, да?"
            else:
                ms "Я бы воздержалась от разговора на личные темы."
        "Секретная встреча с Сарой":
            $ manifest_state.take_action("w4_secret_meeting")
            scene bg canteen
            if manifest_state.can_interact_with("sarah"):
                sc "Ошибёмся с подозреваемым — экипаж сорвётся."
                sc "Мне нужен не слух. Мне нужна цепочка: факт, мотив, доступ, повтор."
                $ manifest_state.add_ally_by_tag("ally_candidate")
                ev "Соберём. Иначе нас порвут ещё до штурма мостика."
            else:
                na "Сара игнорирует приглашение на встречу и отвечает только через редакционный канал."
        "Медицинская рутина с Кенджи":
            $ manifest_state.take_action("w4_med_routine")
            scene bg laboratory
            if manifest_state.can_interact_with("kenji"):
                kt "Люди плохо выдерживают хроническую неопределённость."
                kt "Им нужен хотя бы контур плана. Иначе начнутся срывы."
                ev "План есть. Неясно только, успею ли я его развернуть."
            else:
                na "Кенджи ограничивается формальным отчётом и уходит к пациентам."
        "изолировать канал ложных тревог":
            $ manifest_state.take_action("w4_quest_false_alert")
            $ manifest_state.complete_quest("quest_07_false_alert")
            $ manifest_state.register_evidence("false_alert_source")
            ev "Квест выполнен: найден узел, который подбрасывает фальшивые тревоги."
            ev "Кто-то специально разгоняет нервозность экипажа."
    return

label w4_slot_3:
    menu:
        "Неделя 4 / Слот 3"
        "Помочь Лене с закрытыми шлюзами":
            $ manifest_state.take_action("w4_locks")
            scene bg technical
            if manifest_state.can_interact_with("lena"):
                if manifest_state.role_requirement_met("lena", ["engineer", "repair_key"]):
                    le "Кто-то руками переписал приоритет доступа."
                    le "Я могу вернуть контроль, но мы всплывём в журнале как лампочка."
                    $ manifest_state.register_evidence("manual_lock_override")
                    $ manifest_state.add_ally_by_tag("technical")
                    ev "Пусть светимся. Тише уже не будет."
                else:
                    le "Я такие шлюзы пока не трогаю. Слишком легко всё уронить."
                    ev "Понял. Без опытного инженера тут не пройти."
            else:
                na "Лена вас избегает; техническая помощь недоступна."
        "Совещание безопасности с Маркусом":
            $ manifest_state.take_action("w4_security")
            scene bg corridor
            if manifest_state.can_interact_with("marcus"):
                mr "Либо у нас диверсант, либо система учится на наших страхах."
                mr "Оба варианта дрянь. Но первый хотя бы можно арестовать."
                ev "Если найдём, кого именно."
            else:
                na "Маркус закрывает канал связи без комментариев."
        "Пассажирский вечер вопросов о космосе":
            $ manifest_state.take_action("w4_qa")
            scene bg canteen
            ev "О звёздах говорить легче, чем о шансах умереть."
            ev "Иногда разговор о Вселенной удерживает людей от внутреннего распада."
    return

label w4_slot_4:
    menu:
        "Неделя 4 / Слот 4"
        "Попробовать скрытую слежку":
            $ manifest_state.take_action("w4_tail")
            $ manifest_state.register_evidence("maintenance_route_pattern")
            ev "Один маршрут повторяется вне расписания."
            ev "Ходят туда, где камеры всегда отстают на секунду."
        "Задокументировать все несоответствия в Manifest":
            $ manifest_state.take_action("w4_manifest_report")
            ev "Таблица уже похожа на карту подозрений."
            ev "Я отмечаю не только действия, но и странные паузы между ними."
        "Пауза и сон":
            $ manifest_state.take_action("w4_sleep")
            ev "Без этой паузы я начну видеть врага в каждом лице."
            ev "А это самый быстрый путь к ошибке с оружием."
        "перехватить личную переписку диверсанта":
            $ manifest_state.take_action("w4_quest_message_trace")
            $ manifest_state.complete_quest("quest_08_message_trace")
            $ manifest_state.register_evidence("encrypted_thread")
            ev "Квест выполнен: поймана зашифрованная цепочка сообщений в бортовой сети."
            ev "Теперь бы понять, пишет это человек или только хорошая имитация человека."
        "собрать аварийный комплект для штурма мостика":
            $ manifest_state.take_action("w4_quest_assault_kit")
            $ manifest_state.complete_quest("quest_16_assault_kit")
            $ manifest_state.register_evidence("assault_kit_ready")
            ev "Квест выполнен: собран комплект, которого официально не бывает на пассажирских рейсах."
            ev "Если дойдём до шлюза мостика, он решит, будем мы ломать дверь или зайдём тихо."
    return


label w4_found_note:
    scene bg laboratory
    na "Возвращаясь с обзорной палубы, я замечаю в кармане аварийного костюма сложенную записку без подписи."
    ev "Бумага настоящая. Кто-то специально оставил след, который не сотрётся вместе с терминалами."
    na "Внутри всего одна строка: 'В финальном цикле смотри не на должности, а на повторяющийся выбор'."
    $ manifest_state.register_evidence("note_final_cycle")
    ev "Наконец у меня есть зацепка, которая переживает неделю и не держится только на чужих словах."
    return


label w4_sabotage_report:
    scene bg bridge
    na "В середине недели в грузовом отсеке исчезают фильтры воды, а аварийный запас оказывается подменён."
    ev "Я приношу капитану досье с сопоставлением маршрутов доступа и сменных листов."
    ch "По бумагам эти люди должны обслуживать гражданский модуль, а не стратегический склад."
    ch "Как их вообще допустили к экспедиции?"
    ev "Люди каждый цикл будто смещены относительно самих себя. Без манифеста мы слепы."
    $ manifest_state.register_evidence("sabotage_water_filters")
    return


label w4_proof_scene:
    scene bg canteen
    ev "Сара полезет в грязную историю только если я подам её как рабочую зацепку, а не личную манию."
    call generic_weekly_proof_scene("sarah", "Сара") from _call_generic_weekly_proof_scene_4
    return

label w4_slot_5:
    menu:
        "Неделя 4 / Слот 5"
        "Проверить шлюзовой журнал с Леной":
            call generic_role_quest(
                "w4_partner_airlock", "lena", "analysis", 62, "airlock_rewrite_trace",
                "Лена хмыкает: 'ну да, кто-то правил шлюз как кривой черновик'. След вмешательства становится явным.",
                "Журнал уходит в циклическую ошибку, и чистого доказательства вы так и не вытаскиваете.",
                "Лена не помогает: по реакции видно, что ей выгоднее оставить шлюзовые следы спутанными."
            ) from _call_generic_role_quest_14
        "Попросить Маркуса проверить тайники безопасности":
            call generic_role_quest(
                "w4_partner_stashes", "marcus", "authority", 61, "security_stash_route",
                "Маркус находит спрятанный набор пропусков и мрачно бросает: это уже подготовка к долгой игре, не к одной аварии.",
                "Обыск даёт только старый хлам и раздражение. Тайник остаётся ненайденным.",
                "Маркус не помогает: он предпочитает прикрывать следы, а не вскрывать их."
            ) from _call_generic_role_quest_15
    return

label w4_slot_6:
    menu:
        "Неделя 4 / Слот 6"
        "Согласовать антикризисный протокол с Кенджи":
            call generic_role_quest(
                "w4_partner_crisis_protocol", "kenji", "empathy", 60, "medical_crisis_protocol",
                "Кенджи собирает протокол так, будто лечит сам корабль: коротко, точно.",
                "Протокол выходит слишком расплывчатым.",
                "Кенджи не помогает — союзника в медблоке из него не выходит."
            ) from _call_generic_role_quest_16
        "Подготовить канал оповещения с Сарой":
            call generic_role_quest(
                "w4_partner_broadcast", "sarah", "empathy", 61, "broadcast_template",
                "Сара делает сообщение живым и честным: не истерика, а план действий.",
                "Сара уходит в драму, и текст больше пугает людей, чем собирает их.",
                "Сара не помогает. Сейчас ей выгоднее шум, а не управляемый эфир."
            ) from _call_generic_role_quest_17
    return

label w4_slot_7:
    menu:
        "Неделя 4 / Слот 7"
        "Продолжить исследование астрия":
            jump w4_astrium_chain
        "Собрать мысли перед сном":
            $ manifest_state.take_action("w4_journal_rest")
            ev "Я вслух повторяю простую вещь: подозрение — не доказательство.."
        "Попросить Лену вскрыть кабину пилотов":
            call investigate_pilot_cabin_with_lena("w4_pilot_cabin_lena") from _call_investigate_pilot_cabin_with_lena_1
    return

label w4_astrium_chain:
    $ manifest_state.take_action("w4_astrium_stage2")
    $ manifest_state.set_logic_hint("Астрий уже признан продуктом аномалии. Теперь нужно понять, с чем именно он связывается в системе корабля.")
    menu:
        "Астрий / Шаг 3"
        "Проверить, меняет ли он проводимость при контакте с охлаждающим контуром":
            $ a3 = True
        "Проверить, не гасит ли он сигнал как любой хороший экранный композит":
            $ a3 = False
    $ manifest_state.set_logic_hint("Если материал влияет на проводимость, последним шагом ищу полезный эффект, а не просто красивый феномен.")
    menu:
        "Астрий / Шаг 4"
        "Измерить, стабилизирует ли он скачки энергии в резонансном поле":
            $ a4 = True
        "Проверить, не накапливает ли он заряд и не выдаёт ли это ложную картину стабильности":
            $ a4 = False
    $ manifest_state.clear_logic_hint()
    if a3 and a4:
        $ manifest_state.advance_element_stage("Астрий может выравнивать краткие энергетические скачки, если попасть в его резонансное окно.")
        $ manifest_state.register_evidence("astrium_conductive_property")
        ev "Вывод складывается: астрий не просто красивый минерал."
    else:
        $ manifest_state.register_logic_chain(False)
        ev "Я опять ухожу в эффектность и теряю цепочку."
    return
