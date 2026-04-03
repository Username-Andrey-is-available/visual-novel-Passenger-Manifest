label week_2_arc:
    scene bg corridor
    na "Неделя 2: повтор."
    ev "Я проснулся в тот же понедельник. Та же каюта. Тот же сигнал подъёма."
    ev "Лена снова злится на третий шлюз. Кендзи снова собирает недоспавших. Сара снова шутит про кашу."
    ev "Это не дежавю. Неделя пошла по второму кругу."
    ev "В конце прошлой мы упали в чёрную дыру. Я помню удар, тревогу, смерть. А теперь всё началось заново."
    ev "Значит, мы застряли во временной петле."
    ev "Никто вокруг этого не видит. Для них идёт обычная рабочая неделя."
    ev "Я не проснулся!?"
    na "Кенджи проводит медобход и отчёты по давлению, служба снабжения пересчитывает аптечки."
    call w2_proof_scene from _call_w2_proof_scene

    call w2_pre_slots_scene from _call_w2_pre_slots_scene
    call w2_slot_1 from _call_w2_slot_1
    call w2_between_1_2_scene from _call_w2_between_1_2_scene
    call w2_slot_2 from _call_w2_slot_2
    call w2_between_2_3_scene from _call_w2_between_2_3_scene
    call w2_slot_3 from _call_w2_slot_3
    call w2_between_3_4_scene from _call_w2_between_3_4_scene
    call w2_slot_4 from _call_w2_slot_4
    call w2_between_4_5_scene from _call_w2_between_4_5_scene
    call w2_slot_5 from _call_w2_slot_5
    call w2_between_5_6_scene from _call_w2_between_5_6_scene
    call w2_slot_6 from _call_w2_slot_6
    call w2_between_6_7_scene from _call_w2_between_6_7_scene
    call w2_slot_7 from _call_w2_slot_7
    call w2_post_slots_scene from _call_w2_post_slots_scene
    call w2_loop_monologue from _call_w2_loop_monologue
    call w2_midnight_lab_talk from _call_w2_midnight_lab_talk
    call w2_pilot_cabin_attempt from _call_w2_pilot_cabin_attempt
    return

label w2_loop_monologue:
    scene bg observation
    ev "К концу второго дня я перебираю совпадения и понимаю главное: словами петлю не доказать."
    ev "Для остальных это будут обрывки тревоги, странные догадки и я, который помнит то, чего ещё не было."
    ev "Скажу это вслух без доказательств в руках — меня спишут раньше, чем я дойду до мостика."
    ev "Доказательств, ага."
    return

label w2_midnight_lab_talk:
    scene bg laboratory
    ev "Ночью лаборатория звучит иначе. Даже вентиляторы будто шепчут."
    kt "Ты снова здесь. Третья ночь подряд."
    ev "Если бы ты знал..."
    kt "Как здоровье, ничего не беспокоит?"
    ev "Папки выпадают из шкафа."
    kt "Ммм?"
    return

label w2_proof_scene:
    scene bg technical
    ev "Прежде чем просить Лену о странных проверках, мне нужно подать это как обычную инженерную перестраховку."
    call generic_weekly_proof_scene("lena", "Лена") from _call_generic_weekly_proof_scene_2
    return

label w2_pre_slots_scene:
    scene bg corridor
    ev "Перед первым выбором сверяю расписание палуб: семь слотов, десятки людей и вторая попытка на ту же неделю."
    na "За иллюминаторами плывёт пылевой рукав, а внутри корабля начинается обычная рабочая карусель."
    return

label w2_between_1_2_scene:
    scene bg corridor
    ev "Пока лифт ползёт к жилому ярусу, я успеваю записать три гипотезы и вычеркнуть две."
    $ pm_story_impact("lift_stop", pause=0.14, stop_after=True, duck_music=False)
    na "В межзвёздной работе важна не скорость рук, а скорость отказа от плохих идей."
    return

label w2_between_2_3_scene:
    scene bg canteen
    na "В досуговом блоке кто-то играет в настольный симулятор посадки, споря о том, кто сорвёт стыковку первым."
    ev "Их смех звучит как маленький бунт против паники. Я цепляюсь за этот звук."
    return

label w2_between_3_4_scene:
    scene bg corridor
    ev "Перед следующим слотом захожу в каюту на пять минут и умываюсь ледяной водой."
    ev "Если выглядишь собранно, людям проще поверить, что план вообще существует."
    return

label w2_between_4_5_scene:
    scene bg observation
    na "У обзорного стекла две стюардессы обсуждают один и тот же анекдот теми же словами, что и на прошлой неделе."
    ev "Петля повторяет бытовые сцены так тщательно."
    ev "А тут и повторять нечего, одно и тоже."
    return

label w2_between_5_6_scene:
    scene bg corridor
    na "Пока я иду к следующему отсеку, служебный дрон везёт контейнеры с медикаментами по уже знакомой траектории."
    $ pm_story_impact("drone_pass", pause=0.16, stop_after=True, duck_music=False)
    ev "Даже техника повторяет маршрут почти без отклонений. Цикл сидит глубже человеческой памяти."
    return

label w2_between_6_7_scene:
    scene bg laboratory
    kt "Ты снова смотришь на часы так, будто пытаешься поймать их на лжи."
    ev "Потому что начинаю верить: врут не часы, а сама последовательность событий."
    return

label w2_post_slots_scene:
    scene bg canteen
    na "После слотов Эван идёт в тихую читальню и выбирает книгу: 'Психология изоляции в дальних рейсах'."
    ev "Читаю одну главу и понимаю: половина советов написана для тех, кто не застрял во временной петле."
    return

label w2_slot_1:
    menu:
        "Неделя 2 / Слот 1"
        "Сравнить прошлые и текущие досье":
            $ manifest_state.take_action("w2_compare_manifest")
            $ manifest_state.register_evidence("manifest_shift")
            ev "Имена те же. Роли другие. Это не ошибка базы."
            ev "Похоже, меняется сама реальность, а не запись о ней."
        "Проверить научные логи аномалии":
            $ manifest_state.take_action("w2_science")
            ev "Сигнатура чёрной дыры повторяет прошлую неделю, но со сдвигом по фазе."
            ev "Если соберу больше измерений, начну предсказывать пики."
        "Сделать вид, что ничего не происходит":
            $ manifest_state.take_action("w2_mask")
            ev "Если расскажу всё сразу, меня спишут как нестабильного."
            ev "Иногда молчание — тоже стратегия."
    return

label w2_slot_2:
    menu:
        "Неделя 2 / Слот 2"
        "Поговорить с Сарой как с журналистом-расследователем":
            $ manifest_state.take_action("w2_sarah")
            scene bg canteen
            if manifest_state.role_requirement_met("sarah", ["investigator", "ally"]):
                $ manifest_state.add_ally_by_tag("ally_candidate")
                sc "Если у тебя правда есть какая-то закономерность, я помогу превратить её в доказательство."
                sc "Люди верят историям. Решения всё равно принимают по фактам. Дай мне факты."
                ev "Договорились. Я дам тебе факты, ты дашь им голос."
            else:
                sc "Я не могу дать этой истории форму, которой поверят. Сейчас у меня нет для этого ни канала, ни опоры."
                ev "Значит, в этой ветке я остаюсь без её голоса."
        "Проверить камеры технического отсека":
            $ manifest_state.take_action("w2_cameras")
            $ manifest_state.register_evidence("camera_blindspots")
            ev "Слепые зоны появляются строго перед авариями."
            ev "Для случайности это слишком аккуратно."
        "Час отдыха в гидропонном саду":
            $ manifest_state.take_action("w2_rest")
            ms "Растения не спорят с реальностью. Люди — постоянно."
            ms "Наверное, поэтому растения переживают катастрофы спокойнее нас."
            ev "Жаль, у нас нет их терпения."
        "восстановить удалённый фрагмент журнала":
            $ manifest_state.take_action("w2_quest_log_restore")
            $ manifest_state.complete_quest("quest_03_log_restore")
            $ manifest_state.register_evidence("restored_log_fragment")
            ev "Квест выполнен: из удалённого лога всплыл незарегистрированный доступ к мостику."
            ev "Имя пустое. Метка времени — ровно на аварии."
    return

label w2_slot_3:
    menu:
        "Неделя 2 / Слот 3"
        "Попытка заранее предупредить капитана":
            $ manifest_state.take_action("w2_warn_captain")
            scene bg bridge
            ch "Вы устали. Возьмите отгул."
            ch "Без проверяемых данных я не меняю протокол рейса."
            ev "Понял."
        "Смена с Кенджи: анализ нейростресса экипажа":
            $ manifest_state.take_action("w2_medical")
            scene bg laboratory
            $ manifest_state.register_evidence("stress_cluster")
            kt "Пики тревоги возникают в одни и те же часы у разных людей."
            kt "Будто корабль синхронизирован с внешним импульсом."
            ev "Записываю это как косвенный индикатор цикла."
        "Дискуссия с Томасом о протоколах мостика":
            $ manifest_state.take_action("w2_bridge_access")
            scene bg bridge
            tg "Без разрешения капитана в кабину пилотов не пройти."
    return

label w2_slot_4:
    menu:
        "Неделя 2 / Слот 4"
        "Задержаться у обзорного иллюминатора":
            $ manifest_state.take_action("w2_cosmos")
            scene bg observation
            ev "Звёзды будто стоят на месте, хотя мы должны лететь."
            ev "Наверное, так и выглядит космос, когда перестаёшь доверять времени."
        "Провести вечер с командой в досуговом модуле":
            $ manifest_state.take_action("w2_leisure")
            scene bg canteen
            mr "Люди шутят громче, когда боятся."
            mr "Слишком тихий отсек опаснее шумного."
            ev "Тогда шум пусть будет признаком жизни."
            ev "Но вы ведь все чего-то боитесь. Чего же я ещё не знаю..."
        "Скрытая проверка служебных ключей":
            $ manifest_state.take_action("w2_keys")
            $ manifest_state.register_evidence("bridge_key_gap")
            ev "Один мастер-ключ зарегистрирован, но ни к кому не привязан."
            ev "Невидимый ключ для невидимого пользователя."
        "провести закрытый брифинг для пассажиров":
            $ manifest_state.take_action("w2_quest_briefing")
            $ manifest_state.complete_quest("quest_04_briefing")
            na "Квест выполнен: паника просела, пассажиры получили понятное объяснение рисков."
            ev "На короткой дистанции доверие иногда важнее полной правды."
        "вскрыть квантовый архив мостика":
            $ manifest_state.take_action("w2_quest_quantum_archive")
            if manifest_state.meets_quest_requirements("quest_14_quantum_archive"):
                $ manifest_state.complete_quest("quest_14_quantum_archive")
                $ manifest_state.register_evidence("bridge_quantum_archive")
                na "Квест выполнен: архив открылся только после трёхфакторной синхронизации с медблоком."
                ev "Кто-то спрятал резервные протоколы так глубоко, будто боялся не поиска, а неоднократного поиска."
            else:
                ev "Запускаю вскрытие, но процесс упирается в проверку компетенций."
                ev "Не хватает аналитики и внутренней собранности, чтобы дожать взлом."
    return

label w2_slot_5:
    menu:
        "Неделя 2 / Слот 5"
        "Собрать реакторные логи с Леной":
            call generic_role_quest(
                "w2_partner_reactor", "lena", "analysis", 60, "reactor_access_gap",
                "Лена нервно шутит, но вытаскивает из системы нужный журнал: кто-то получил инженерный доступ в обход штатного допуска.",
                "Проверка срывается: Лена теряет нить и оставляет только хаотичный набор логов без доказательной силы.",
                "Лена не помогает. Внятного объяснения не будет."
            ) from _call_generic_role_quest_5
        "Проверить пропавшие минуты записи с Маркусом":
            call generic_role_quest(
                "w2_partner_security_gap", "marcus", "authority", 58, "security_gap_scheme",
                "Маркус молча выстраивает схему слепых зон и признаёт: кто-то слишком аккуратно обходит штатную безопасность.",
                "Маркус собирает не ту последовательность, и пропавшие минуты так и остаются набором досадных дыр.",
                "Маркус не собирается помогать: он уходит в скрытность вместо сотрудничества."
            ) from _call_generic_role_quest_6
        "Снова перечитать логи аномалии в одиночку":
            $ manifest_state.take_action("w2_repeat_research")
            ev "Одиночество полезно уже тем, что не спорит со мной вслух."
    return

label w2_slot_6:
    menu:
        "Неделя 2 / Слот 6"
        "Разобрать странный контейнер с Мирой":
            call generic_role_quest(
                "w2_partner_mira_samples", "mira", "analysis", 59, "mira_sample_shift",
                "Мира осторожно ведёт вас по протоколу и будто случайно роняет фразу: некоторые образцы 'помнят' прошлые циклы.",
                "Мира выбирает безопасный маршрут проверки, и вы упираетесь в половину данных без финального вывода.",
                "Мира не помогает. Её спокойствие слишком похоже на контролируемую дистанцию."
            ) from _call_generic_role_quest_7
        "Попросить Томаса оценить резервный люк":
            call generic_role_quest(
                "w2_partner_service_hatch", "thomas", "authority", 60, "service_hatch_map",
                "Томас ругается по-стариковски, но находит способ открыть сервисный люк на мостике.",
                "Томас знает теорию, однако на практике не производит рабочую схему.",
                "Томас не помогает — от него остаются только красивые слова о протоколах."
            ) from _call_generic_role_quest_8
        "Дать себе час тишины":
            $ manifest_state.take_action("w2_rest_quiet")
            ev "Тишина на корабле. Почему мне так беспокойно."
    return

label w2_slot_7:
    menu:
        "Неделя 2 / Слот 7"
        "Сверить улики вместе с Кенджи":
            call generic_role_quest(
                "w2_partner_medical_pattern", "kenji", "analysis", 61, "circadian_pulse_pattern",
                "Кенджи выводит красивую, почти пугающую таблицу: всплески тревоги у экипажа синхронны с гравитационными пиками.",
                "Кенджи осторожничает и не дотягивает до жёсткого вывода; остаётся только вероятность.",
                "Кенджи не идёт в помощь: он держится на безопасной дистанции от истины."
            ) from _call_generic_role_quest_9
        "Переписать все выводы начисто":
            $ manifest_state.take_action("w2_clean_notes")
            ev "Если я не выстрою мысли на бумаге, скоро они начнут спорить друг с другом прямо у меня в голове."
    return


label w2_pilot_cabin_attempt:
    scene bg bridge
    ev "К концу второй недели я всё-таки иду к кабине пилотов: если курс повторяется, надо менять его у источника."
    na "На двери горит красный индикатор допуска. Пилоты — Алик Хартманн и Нельсон Стюарт — по-прежнему не выходят в общий контур."
    ev "У меня нет доступа. Ладно. Тогда через безопасность."
    scene bg corridor
    mr "Я проверил замок. Без капитанского уровня я туда не войду, даже если очень захочу."
    ev "Значит, просим Хейза открыть кабину официально."
    scene bg bridge
    ch "Не мешайте пилотам выполнять их работу. Это прямой приказ."
    ch "Уходите."
    ev "Именно после этого приказа я окончательно понимаю: правда сидит по ту сторону двери."
    return
