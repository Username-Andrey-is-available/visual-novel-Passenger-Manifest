label week_6_arc:
    scene bg corridor
    na "Неделя 6: финальная петля."
    ev "Снова семь слотов. На всё меня уже не хватит."
    ev "Это не финал истории. Это экзамен на всё, что я успел собрать раньше."
    na "Медик проверяет аварийные аптечки, служба снабжения пересчитывает кислородные маски по секциям."
    call w6_proof_scene from _call_w6_proof_scene


    call w6_pre_slots_scene from _call_w6_pre_slots_scene
    call w6_slot_1 from _call_w6_slot_1
    call w6_between_1_2_scene from _call_w6_between_1_2_scene
    call w6_slot_2 from _call_w6_slot_2
    call w6_between_2_3_scene from _call_w6_between_2_3_scene
    call w6_slot_3 from _call_w6_slot_3
    call w6_between_3_4_scene from _call_w6_between_3_4_scene
    call w6_slot_4 from _call_w6_slot_4
    call w6_between_4_5_scene from _call_w6_between_4_5_scene
    call w6_slot_5 from _call_w6_slot_5
    call w6_between_5_6_scene from _call_w6_between_5_6_scene
    call w6_slot_6 from _call_w6_slot_6
    call w6_between_6_7_scene from _call_w6_between_6_7_scene
    call w6_slot_7 from _call_w6_slot_7
    call w6_post_slots_scene from _call_w6_post_slots_scene
    call w6_pre_assault_briefing from _call_w6_pre_assault_briefing
    call w6_truth_logic_chain from _call_w6_truth_logic_chain

    call w6_final_decision from _call_w6_final_decision
    return

label w6_mira_jump_scare:
    show expression pm_story_image("mira_reveal", "images/backgrounds/captains bridge.png") as mira_jump_scare
    $ pm_story_impact("mira_reveal", pause=1.8)
    hide mira_jump_scare
    return

label w6_pre_assault_briefing:
    scene expression pm_story_image("bridge_alert", "images/backgrounds/captains bridge.png")
    $ pm_story_impact("alarm_short", pause=0.18, stop_after=True)
    ch "Я не обязан вам верить, Эван."
    ch "Но я обязан дать кораблю шанс, если шанс настоящий."
    ev "Шанс есть только если команда сработает как один контур."
    if "technical" in manifest_state.allies:
        le "Инженеры готовы. Если никто не начнёт импровизировать в щите."
    else:
        ev "Инженерного запаса почти нет. Любой сбой в шлюзах будем проходить на чистом нерве."
    if "pilot" in manifest_state.allies:
        tg "Пилот готов. Дайте мне руль, а не поминки."
    else:
        ev "С ручным перехватом хуже всего: права на пробный манёвр у нас не будет."
    if "ally_candidate" in manifest_state.allies:
        sc "Каналы вычищены, паника ужата. Окно маленькое, но живое."
    else:
        ev "Инфоканалы останутся шумными. Значит, штурм должен быть ещё быстрее."
    if manifest_state.can_interact_with("marcus") and manifest_state.can_offer_help("marcus"):
        mr "Безопасность прикроет тылы на три минуты. Больше не удержу."
    else:
        ev "Тылы никто полностью не закроет. Придётся держать темп, пока коридоры ещё наши."
    if "saboteur_ceasefire" in manifest_state.evidence:
        mr "И ещё странность: внутреннее противодействие исчезло. Будто кто-то сам увёл людей с маршрута."
        ev "Значит, канал сработал. Кто-то по ту сторону решил дожить до правды."
    ev "Три минуты — это вечность, если никто не начнёт спорить."
    if manifest_state.mira_detained:
        ch "Мира под изоляцией. Она ни с кем не может говорить без сопровождения Маркуса."
        mr "Если врёт, решётка удержит. Если нет, проверим уже после манёвра."
    elif manifest_state.alien_exposed and manifest_state.can_interact_with("mira"):
        ms "И всё это ничто, если кто-то дрогнет в последнюю секунду."
    ev "Тогда не дрогнем."
    return

label w6_pre_slots_scene:
    scene bg corridor
    ev "Неделя начинается как обычная смена: отчёты, подписи, датчики. Только ставки теперь абсолютные."
    na "В коридорах пахнет антисептиком и горячим пластиком — экипаж готовит аварийные наборы на случай штурма."
    return

label w6_between_1_2_scene:
    scene bg corridor
    ev "После первого слота я иду через жилой модуль: люди молча расступаются и кивают, будто уже знают, что времени мало."
    ev "Такое молчаливое доверие тяжелее любого приказа."
    return

label w6_between_2_3_scene:
    scene bg canteen
    na "В редкий спокойный момент Эван заходит в комнату отдыха, где на экране идёт запись земного океана."
    ev "Смотрю на волны две минуты и думаю только об одном: снова услышать настоящий ветер, а не вентиляцию."
    return

label w6_between_3_4_scene:
    scene bg corridor
    ev "Перед следующим слотом проверяю список в кармане: имена, задачи, время входа в каждый отсек."
    ev "Когда страх зашкаливает, три чёткие строки работают лучше любой речи."
    return

label w6_between_4_5_scene:
    scene bg bridge
    na "На мостике никто не повышает голос, но напряжение висит в воздухе плотнее дыма."
    return

label w6_between_5_6_scene:
    scene bg technical
    ms "Последний шанс договориться с теми, кто прятался в тени, всегда похож на прыжок без поручней."
    ev "Значит, прыгну с открытыми глазами."
    return

label w6_between_6_7_scene:
    scene bg corridor
    na "Перед последним слотом корабль повторяет знакомый низкий гул."
    $ pm_story_impact("ominous_hum", pause=0.2, duck_music=False)
    na "Тот самый звук, который Эван слышал каждый цикл."
    ev "Одни и те же звуки. Одни и те же слова. Не собираюсь привыкать."
    return

label w6_post_slots_scene:
    scene bg corridor
    na "Прежде чем идти на штурм, Эван прослушивает давно забытую песню классика прошлого десятилетия."
    na "'...мы за рулём своего катафалка...' в самый раз."
    return

label w6_slot_1:
    menu:
        "Неделя 6 / Слот 1"
        "Собрать инженерную группу":
            $ manifest_state.take_action("w6_engineer_team")
            scene bg technical
            if manifest_state.can_interact_with("lena"):
                if manifest_state.role_requirement_met("lena", ["engineer", "repair_key"]):
                    $ manifest_state.add_ally_by_tag("technical")
                    le "Я вскрою внешнюю блокировку, если Маркус удержит коридор."
                    le "Но после этого легального режима у нас уже не будет."
                    ev "Легальный режим у нас закончился ещё на первой неделе."
                else:
                    le "Я этот контур не вскрою. Опыта не хватит."
                    ev "Без опытного инженера штурм сразу проседает."
            else:
                na "Лена не выходит на связь и избегает участия в группе."
        "Собрать пилотскую группу":
            $ manifest_state.take_action("w6_pilot_team")
            scene bg bridge
            if manifest_state.can_interact_with("thomas"):
                if manifest_state.role_requirement_met("thomas", ["veteran", "savior"]):
                    $ manifest_state.add_ally_by_tag("pilot")
                    tg "Дайте мне ручной вектор, и шанс у нас будет."
                    ev "Питание беру на себя."
                else:
                    tg "Теорию дам. Вживую такой перехват не потяну."
                    ev "Я снова ошибся."
            else:
                na "Томас держится на дистанции и не входит в штурмовую группу."
        "Собрать информационную группу":
            $ manifest_state.take_action("w6_info_team")
            scene bg canteen
            if manifest_state.can_interact_with("sarah"):
                if manifest_state.role_requirement_met("sarah", ["investigator", "ally"]):
                    $ manifest_state.add_ally_by_tag("ally_candidate")
                    sc "Я уведу пассажирские каналы в сторону и сниму панику с маршрута."
                    sc "Пока люди слушают меня, у вас будет тихое окно для штурма."
                    ev "Это окно может оказаться нашим единственным."
                else:
                    sc "Я не соберу для тебя управляемый эфир. Слишком много шума, слишком мало доверия."
                    ev "Без правильного голоса в инфоканалах штурм снова останется один на один с паникой."
            else:
                na "Сара не подключается к инфоканалам по вашему запросу."
    return

label w6_slot_2:
    menu:
        "Неделя 6 / Слот 2"
        "Проверить все ключевые улики перед штурмом":
            $ manifest_state.take_action("w6_evidence_review")
            scene bg laboratory
            if "dead_pilots" in manifest_state.evidence:
                ev "Факт смерти пилотов подтверждён. Сомнений больше нет."
                ev "Теперь это не теория заговора. Это цепочка преступления."
                ev "Убийца всё ещё на корабле, но он не преследует цель убить меня, возможно, он не знает то, что знаю я."
            else:
                ev "Доказательств всё ещё не хватает, а времени почти не осталось."
        "Поговорить с Мирой наедине":
            $ manifest_state.take_action("w6_mira_faceoff")
            scene bg observation
            if manifest_state.mira_detained:
                ev "Поздно. После ареста Мира говорит только через стекло и под запись."
                ev "Значит, следующую правду придётся добывать уже не доверием, а протоколом."
            elif manifest_state.can_interact_with("mira"):
                if "mira_pressure_point" in manifest_state.evidence and ("second_observer" in manifest_state.evidence or "note_final_cycle" in manifest_state.evidence):
                    if manifest_state.can_recall(56):
                        ms "Ты больше не ищешь странность, Эван. Ты ищешь форму, в которой меня можно предъявить людям."
                        ev "Мне нужна не форма. Мне нужна правда. Что ты знаешь о целях рейса?"
                        ms "Тогда запомни: в другой ветви ты пришёл ко мне на семь минут позже и умер раньше, чем понял, что спрашиваешь не человека."
                        ev "Такого разговора ещё не было, никогда не было. В этой ветви мы впервые..."
                        ms "А я и не говорю про эту."
                        $ manifest_state.register_evidence("mira_verbal_tell")
                    else:
                        ms "Ты почти дошёл до правильного вопроса. Жаль только, что память в тебе держится хуже, чем у самой петли."
                        ev "Я чувствую, что она проговорилась. Но не удерживаю, на каком слове треснула маска."
                else:
                    ms "Ты ищешь предателя... хотя, может быть, ищешь выжившего."
                    ms "И вопрос не в том, кто я. Вопрос — зачем тебе правда именно сейчас."
            else:
                ms "Вероятно, пока нам лучше не продолжать."
        "Укрепить мораль команды":
            $ manifest_state.take_action("w6_morale")
            scene bg canteen
            ev "Если люди не верят друг другу, никакой план не сработает."
            ev "Даю короткий брифинг: страх признаём, курс меняем, действуем вместе."
    return

label w6_slot_3:
    menu:
        "Неделя 6 / Слот 3"
        "Передать досье на Миру Хейзу и Маркусу":
            $ manifest_state.take_action("w6_mira_casefile")
            scene bg bridge
            if all(flag in manifest_state.evidence for flag in ["second_observer", "note_final_cycle", "mira_pressure_point", "mira_verbal_tell"]):
                ev "У меня не догадка, а цепочка: записка, повторяющаяся память, невозможная реплика и совпадение роли с паттерном наблюдателя."
                ch "Мира Шоу, до конца операции вы переходите под охрану."
                call w6_mira_jump_scare from _call_w6_mira_jump_scare
                $ manifest_state.detain_mira()
                ev "Что это было?"
            elif len([flag for flag in ["second_observer", "note_final_cycle", "mira_pressure_point", "mira_verbal_tell"] if flag in manifest_state.evidence]) >= 2:
                ev "У меня есть совпадения, но не хватает..."
                ch "Тогда это ещё не арест. Только наблюдение."
                $ manifest_state.adjust_stat("authority", -1)
            else:
                $ manifest_state.set_runtime_flag("false_accusation")
                mr "После такого люди начнут видеть чудовище в каждом тихом лице."
                ev "Я уже слышу, как ошибка расходится по кораблю быстрее фактов."
        "Раскрыть Миру публично и заставить говорить":
            $ manifest_state.take_action("w6_public_expose")
            scene bg bridge
            call w6_mira_jump_scare from _call_w6_mira_jump_scare_1
            if manifest_state.mira_detained:
                ev "Поздно. Теперь её держит не толпа, а изоляционная дверь."
            elif "mira_pressure_point" in manifest_state.evidence and "second_observer" in manifest_state.evidence and ("mira_verbal_tell" in manifest_state.evidence or "note_final_cycle" in manifest_state.evidence):
                $ manifest_state.reveal_alien()
                mr "Теперь назад пути нет."
                mr "Либо мы удержим порядок, либо корабль рухнет в хаос раньше манёвра."
                if "note_final_cycle" in manifest_state.evidence and manifest_state.role_requirement_met("mira", ["alien"]):
                    ev "Мира, у меня есть записка: 'В финальном цикле смотри не на роли, а на повторяющийся выбор'. Это твоё?"
                    ms "Да. Я оставила её в другой версии, где ты не успевал меня услышать."
                    ms "Я пришла сюда как наблюдатель. Но теперь тоже хочу выйти из петли."
                    $ manifest_state.register_evidence("mira_note_confession")
            else:
                $ manifest_state.set_runtime_flag("false_accusation")
                ch "Вы только что вывели экипаж к пропасти без моста между словами и доказательствами."
                mr "Порядок после такого держится не на доверии, а на страхе."
        "Назвать подозреваемого (без проверки)":
            $ manifest_state.take_action("w6_blind_accusation")
            scene bg bridge
            $ manifest_state.set_runtime_flag("false_accusation")
            ch "Вы только что раскололи экипаж."
            ev "Я понимаю цену этой ошибки."
            ch "Нет, не понимаете! Ожидайте."
        "Скрыть расследование до последнего":
            $ manifest_state.take_action("w6_silent")
            scene bg corridor
            ev "Секретность даёт шанс на манёвр, но лишает поддержки."
            ev "Иногда тихая операция выигрывает у громкой правды. На коротком отрезке."
        "активировать резервный код мостика":
            $ manifest_state.take_action("w6_quest_bridge_code")
            $ manifest_state.complete_quest("quest_11_bridge_code")
            $ manifest_state.register_evidence("bridge_override_code")
            na "Квест выполнен: резервный код мостика восстановлен из старого бэкапа."
            ev "Теперь дверь можно открыть не силой, а правом доступа."
        "провести ложный манёвр для отвлечения диверсанта":
            $ manifest_state.take_action("w6_quest_decoy_maneuver")
            if manifest_state.meets_quest_requirements("quest_18_decoy_maneuver"):
                $ manifest_state.complete_quest("quest_18_decoy_maneuver")
                $ manifest_state.register_evidence("decoy_route_uploaded")
                na "Квест выполнен: в систему загружен ложный курс, который должен вынудить противника раскрыться."
                ev "Если расчёт верен, диверсант полезет в ближайшие пять минут и покажет точку доступа."
            else:
                ev "Ложный манёвр не запускается: экипаж не воспринимает команду как достоверную."
                ev "Мне не хватает авторитета и точности, чтобы провернуть такую операцию."
    return

label w6_slot_4:
    menu:
        "Неделя 6 / Слот 4"
        "Финальная научная проверка":
            $ manifest_state.take_action("w6_truth_research")
            scene bg laboratory
            ev "Фиксирую все несостыковки и готовлю окончательный вывод."
            ev "Теперь истина зависит от того, свяжу ли я факты правильно."
        "Сфокусироваться только на спасении":
            $ manifest_state.take_action("w6_focus_escape")
            scene bg bridge
            ev "Сейчас — траектория и питание мостика."
        "Самопожертвование как резервный план":
            $ manifest_state.take_action("w6_reserve_sacrifice")
            scene bg technical
            ev "Если всё остальное провалится, я замкну контур вручную."
            ev "Лучше одна жизнь в отсеке, чем сотня в сингулярности."
        "синхронизировать аварийные двигатели":
            $ manifest_state.take_action("w6_quest_thrusters")
            $ manifest_state.complete_quest("quest_12_thrusters")
            $ manifest_state.register_evidence("thruster_sync")
            na "Квест выполнен: аварийные двигатели синхронизированы на импульс выхода."
            ev "Если команда дойдёт до мостика, у нас будет реальный манёвр, а не жест отчаяния."
        "вручную перепрошить навигационное ядро":
            $ manifest_state.take_action("w6_quest_nav_reflash")
            if manifest_state.meets_quest_requirements("quest_19_nav_reflash"):
                $ manifest_state.complete_quest("quest_19_nav_reflash")
                $ manifest_state.register_evidence("nav_core_reflashed")
                na "Квест выполнен: ядро приняло прошивку только после ручного подтверждения в трёх отсеках."
                ev "Это был риск: ещё одна ошибка, и система сожгла бы резервный модуль без права восстановления."
            else:
                ev "Перепрошивка обрывается на втором отсеке: я не удерживаю темп и точность."
                ev "Для такой операции нужны максимум аналитики и стойкости, а их пока не хватает."
    return

label w6_final_decision:
    scene expression pm_story_image("bridge_assault", "images/backgrounds/captains bridge.png")
    menu:
        "Последнее решение Эвана"
        "Пожертвовать собой и отключить навигацию":
            $ manifest_state.commit_final_plan("sacrifice")
            $ manifest_state.set_runtime_flag("self_sacrifice")
            $ manifest_state.complete_quest("quest_13_last_switch")
            ev "Я остаюсь у ручного рубильника."
            ev "Пусть эта петля закончится на мне, но не на корабле."
        "Идти в кабину с командой и менять курс":
            $ manifest_state.commit_final_plan("assault")
            $ pm_story_impact("final_breach", pause=0.24, stop_after=True)
            if all(tag in manifest_state.allies for tag in ["technical", "pilot", "ally_candidate"]):
                ev "Команда собрана. Идём до конца."
            elif "saboteur_ceasefire" in manifest_state.evidence and "technical" in manifest_state.allies and "pilot" in manifest_state.allies:
                ev "Команда неполная, но кто-то из тени убрал сопротивление с маршрута."
                ev "Для уверенности этого мало. Но уже достаточно, чтобы риск стал ставкой, а не безумием."
            else:
                ev "Команда неполная. Шанс есть, но он ниже."
                ev "Каждый недостающий человек — это минус один шаг в коридоре к спасению."
        "Сомневаться до последнего":
            $ manifest_state.commit_final_plan("hesitate")
            ev "Один шаг промедления, и петля закрывается снова."
            ev "Но даже в сомнении есть правда: я всё ещё человек, а не робот."
        "эвакуировать гражданский сектор перед штурмом":
            $ manifest_state.commit_final_plan("evacuate")
            if manifest_state.meets_quest_requirements("quest_20_civilian_evac"):
                $ manifest_state.complete_quest("quest_20_civilian_evac")
                na "Квест выполнен: гражданские переброшены в защищённые отсеки."
                ev "Если операция сорвётся, хотя бы пассажиры не попадут под перекрёстный огонь."
            else:
                ev "Пытаюсь начать эвакуацию, но люди не слушаются и цепляются за семьи."
                ev "Не хватает авторитета и эмпатии, чтобы провести их через панику без потерь."
    return


label w6_truth_logic_chain:
    scene bg laboratory
    $ manifest_state.set_logic_hint("Финальный вывод: каждое суждение должно продолжать предыдущее, а не спорить с ним.")
    menu:
        "Логическая цепочка: шаг 1"
        "Манифест не врёт сам по себе: он фиксирует сдвиг между версиями одной и той же недели":
            $ w6_logic_1 = "versions"
        "Манифест используют как инструмент отбора, подсовывая экипажу только нужные роли":
            $ w6_logic_1 = "archive"

    $ manifest_state.set_logic_hint("Последний шаг: выбрать истину о людях. Ошибка здесь сломает финал, но часть выводов может быть морально допустимой альтернативой.")
    menu:
        "Логическая цепочка: шаг 2"
        "Значит, люди одни и те же по имени, но с разными ветками личности":
            $ w6_logic_2 = "personality_branches"
        "Значит, поле не меняет людей полностью, а выталкивает их в крайние версии самих себя":
            $ w6_logic_2 = "all_false"

    $ manifest_state.clear_logic_hint()
    if w6_logic_1 == "versions" and w6_logic_2 == "personality_branches":
        if manifest_state.can_recall(58):
            $ manifest_state.register_logic_chain(True)
            $ manifest_state.apply_truth_flag("all_versions_real")
            $ manifest_state.apply_truth_flag("manifest_consistency")
            ev "Вывод сходится: я видел разные версии одних и тех же людей."
        else:
            $ manifest_state.register_logic_chain(True)
            $ manifest_state.apply_truth_flag("partial_truth")
            ev "Я почти удерживаю истину, но память рвёт связку между фактами."
            ev "Я знаю, что версии реальны. Не знаю только, хватит ли мне целостности дотащить это до финала."
    else:
        $ manifest_state.register_logic_chain(False)
        $ manifest_state.apply_truth_flag("logic_false")
        ev "Цепочка ломается. Я что-то упустил."
    return


label w6_proof_scene:
    scene bg laboratory
    ev "Если попрошу Кендзи о нестандартной помощи без рабочей причины, он решит, что я уже сорвался."
    call generic_weekly_proof_scene("kenji", "Кендзи") from _call_generic_weekly_proof_scene_6
    return

label w6_slot_5:
    menu:
        "Неделя 6 / Слот 5"
        "Попросить Кенджи подготовить нейростабилизатор":
            call generic_role_quest(
                "w6_partner_stabilizer", "kenji", "analysis", 63, "neuro_stabilizer_ready",
                "Кенджи собирает протокол на основе астрия так, будто всё утро ждал именно этой невозможной задачи.",
                "Протокол не дотягивает до боевого режима: формула есть, а надёжности нет.",
                "Кенджи не помогает. Без доверия медицинская часть финала осыпается."
            ) from _call_generic_role_quest_22
        "Выяснить, кто на борту охотится за астрием":
            if manifest_state.secret_element_shared:
                $ manifest_state.take_action("w6_astrium_bargain")
                if manifest_state.mira_detained:
                    scene bg bridge
                    if manifest_state.can_recall(54):
                        mr "Мы вскрыли её датапад. Прямых имён нет, но один маршрут повторяется снова и снова."
                        ch "Сервисные роли, грузовые отсеки и астрий в одной линии. Это не кража образца, а операция по извлечению."
                        $ manifest_state.register_evidence("astrium_buyer_profile")
                        ev "Значит, диверсанты везли не случайную добычу. Им нужен был именно этот материал и именно эта аномалия."
                    else:
                        mr "В датападе слишком много совпадений, но ты сейчас держишь их в голове как осколки, не как схему."
                        ev "Я вижу куски маршрута, но не связываю их в одну цель. Пока нет."
                elif manifest_state.can_interact_with("mira"):
                    scene bg observation
                    if manifest_state.can_recall(54):
                        ms "Ты всё ещё думаешь, что астрий нужен им как трофей."
                        ms "Нет. Им нужен не сам кристалл, а его способность удерживать личность у края распада."
                        ms "Скажи это тем, кто прячется в сервисных ролях, и один из них наконец перестанет лгать о цели рейса."
                        $ manifest_state.register_evidence("astrium_buyer_profile")
                        ev "Значит, это мой пропуск к людям, которые до сих пор скрывают саботаж на Aurora."
                    else:
                        ms "Ты дошёл до края ответа..."
                        ev "Я слышу, что астрий кому-то нужен не как трофей, но теряю связку между целью и людьми."
                else:
                    ev "Секрет астрия у меня есть. Адресата для следующего шага пока нет."
            else:
                $ manifest_state.take_action("w6_astrium_bargain_fail")
                ev "Без полной цепочки по астрию я не могу торговать тем, чего сам не понимаю."
    return

label w6_slot_6:
    menu:
        "Неделя 6 / Слот 6"
        "Связаться с саботёрами через секрет астрия":
            $ manifest_state.take_action("w6_contact_saboteurs")
            scene bg technical
            if manifest_state.secret_element_shared and "astrium_buyer_profile" in manifest_state.evidence:
                $ manifest_state.set_logic_hint("Если выхожу на диверсантов, нужно предложить не шантаж, а сделку, и назвать их мотив точнее, чем они сами привыкли о нём говорить.")
                menu:
                    "Как открыть канал к диверсантам?"
                    "Предложить секрет астрия в обмен на правду о миссии":
                        $ s1 = True
                    "Прижать их угрозой трибунала и пообещать назвать имена капитану":
                        $ s1 = False
                menu:
                    "Что сказать о цели диверсии?"
                    "Назвать астрий страховкой для тех, кого аномалия стирает изнутри":
                        $ s2 = True
                    "Назвать астрий ценным минералом для продажи":
                        $ s2 = False
                $ manifest_state.clear_logic_hint()
                if s1 and s2:
                    ev "Я не обвиняю. Я предлагаю сделку: секрет астрия в обмен на один честный разговор о настоящей задаче рейса."
                    na "Закрытый служебный канал долго молчит, а потом открывает тонкую голосовую дорожку без подписи."
                    $ manifest_state.register_evidence("saboteur_channel_open")
                    ev "Канал открыт. Значит, на последнем шаге исследования я смогу дожать эту правду до признания."
                else:
                    ev "Я выбираю тон, после которого со мной не торгуются, а просто рвут соединение."
                    na "В ответ приходит только короткий импульс глушилки. Кто бы ни сидел на том конце, он снова уходит в тень."
            else:
                ev "Мне нечего предложить. В ответ только мёртвая тишина."
        "Собрать финальный резерв с Хейзом":
            call generic_role_quest(
                "w6_partner_command_reserve", "hayes", "authority", 62, "captain_reserve_order",
                "Хейз сжимает челюсть, но подписывает резервный приказ. Впервые капитан играет не против времени, а вместе с вами.",
                "Хейз не доводит решение до приказа: сомнение съедает последние минуты.",
                "Хейз не помогает — он слишком тесно сплетён с саботажем и скрытностью."
            ) from _call_generic_role_quest_23
    return

label w6_slot_7:
    menu:
        "Неделя 6 / Слот 7"
        "Завершить исследование астрия":
            jump w6_astrium_chain
        "Собрать себя перед финалом":
            $ manifest_state.take_action("w6_final_breath")
            ev "Делаю медленный вдох и напоминаю себе: истина тоже выбор, но не каждый выбор истинен."
        "Попросить Лену вскрыть кабину пилотов":
            call investigate_pilot_cabin_with_lena("w6_pilot_cabin_lena") from _call_investigate_pilot_cabin_with_lena_3
    return

label w6_astrium_chain:
    $ manifest_state.take_action("w6_astrium_stage4")
    $ manifest_state.set_logic_hint("Финальная цепочка по астрию: 1) назвать его полезное свойство; 2) решить, кому и зачем отдавать этот секрет.")
    menu:
        "Астрий / Шаг 7"
        "Сделать вывод, что астрий стабилизирует энергетику и кратко удерживает личность от распада в поле аномалии":
            $ a7 = True
        "Сделать вывод, что астрий усиливает фокус оператора, но выжигает всех, кто рядом, и потому годится только как инструмент превосходства":
            $ a7 = False
    $ manifest_state.set_logic_hint("Последний выбор — не факт, а истина, которую Эван готов принять: делиться секретом ради спасения или спрятать его.")
    menu:
        "Астрий / Шаг 8"
        "Поделиться секретом, чтобы получить доступ к диверсантам и повернуть их мотив против петли":
            $ a8 = True
        "Сохранить секрет, а диверсантов попытаться вытащить на страхе и силе":
            $ a8 = False
    $ manifest_state.clear_logic_hint()
    if a7 and a8:
        $ manifest_state.advance_element_stage("Секрет астрия — его стабилизирующий эффект — можно обменять на диалог даже с теми, кто строил диверсию.")
        $ manifest_state.register_evidence("astrium_secret_complete")
        ev "Логика замкнулась. Истина неприятная, но рабочая: иногда путь к спасению идёт не через наказание, а через правильно предложенный секрет."
        if "saboteur_channel_open" in manifest_state.evidence and manifest_state.can_recall(55):
            python:
                saboteur_name = None
                for sid in ["lena", "marcus", "sarah", "hayes"]:
                    if manifest_state.role_requirement_met(sid, ["saboteur", "smuggler", "spy", "suspected_saboteur"]):
                        saboteur_name = manifest_state.manifest.get(sid, {}).get("name", sid)
                        break
            na "Канал оживает сразу, будто собеседник ждал не слов, а именно этого вывода."
            if saboteur_name:
                na "Голос искажён помехами, но я всё равно узнаю его: [saboteur_name]."
            na "\"Вот зачем нас сюда отправили, доктор. Не спасать пассажиров — доставить астрий к аномалии и проверить, сколько личностей он удержит до распада.\""
            na "\"Командование знало маршрут. Пассажирский рейс был ширмой, шумом, идеальным прикрытием для опыта, который нельзя было вести на военном борту.\""
            na "\"Мы должны были привезти образцы и свидетелей. Но, по всей видимости, без тебя, мы не выйдем из петли.\""
            $ manifest_state.register_evidence("mission_cover_story")
            $ manifest_state.register_evidence("saboteur_ceasefire")
            $ manifest_state.apply_truth_flag("mission_cover_real")
            ev "Значит, чёрная дыра была не ошибкой маршрута. Её включили в миссию ещё до посадки первого пассажира."
        elif "saboteur_channel_open" in manifest_state.evidence:
            na "Канал оживает, но смысл уходит быстрее, чем слова успевают сцепиться друг с другом."
            ev "Я понимаю только главное: на том конце признаются не в локальном саботаже, а в чём-то большем. Но не удерживаю, в чём именно."
    elif a7:
        $ manifest_state.register_logic_chain(True)
        ev "Свойство астрия я понял верно. Но решил скрыть его — это не ошибка логики, а другой моральный выбор. Со своей ценой."
        if "saboteur_channel_open" in manifest_state.evidence:
            na "Закрытый канал ждёт ещё несколько секунд и умирает. Я понимаю: шанс на честное признание я только что похоронил сам."
    else:
        $ manifest_state.register_logic_chain(False)
        ev "Я выбрал удобную жестокость вместо точного вывода. Такая 'истина' приведёт только к новому витку."
    return
