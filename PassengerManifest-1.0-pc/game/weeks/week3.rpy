label week_3_arc:
    scene bg corridor
    na "Неделя 3: эксперименты."
    ev "Я уже знаю что делать."
    ev "Но я обязан соблюсти рабочие процессы. Для кого-то мои действия могут показаться преступлением."
    na "Кенджи проводит медобход по пассажирским палубам, Лена закрывает журнал обслуживания реактора."
    call w3_proof_scene from _call_w3_proof_scene


    call w3_pre_slots_scene from _call_w3_pre_slots_scene
    call w3_slot_1 from _call_w3_slot_1
    call w3_between_1_2_scene from _call_w3_between_1_2_scene
    call w3_slot_2 from _call_w3_slot_2
    call w3_between_2_3_scene from _call_w3_between_2_3_scene
    call w3_slot_3 from _call_w3_slot_3
    call w3_between_3_4_scene from _call_w3_between_3_4_scene
    call w3_slot_4 from _call_w3_slot_4
    call w3_between_4_5_scene from _call_w3_between_4_5_scene
    call w3_slot_5 from _call_w3_slot_5
    call w3_between_5_6_scene from _call_w3_between_5_6_scene
    call w3_slot_6 from _call_w3_slot_6
    call w3_between_6_7_scene from _call_w3_between_6_7_scene
    call w3_slot_7 from _call_w3_slot_7
    call w3_post_slots_scene from _call_w3_post_slots_scene
    call w3_mess_hall_scene from _call_w3_mess_hall_scene
    call w3_sabotage_report from _call_w3_sabotage_report
    call w3_logic_chain from _call_w3_logic_chain

    na "Я меняю отдельные эпизоды недели, но упрямый вектор остаётся тем же."
    ev "Петля не ломается от локальных побед. Она требует удара по самому курсу."
    $ manifest_state.register_evidence("causality_redistribution")
    return

label w3_mess_hall_scene:
    scene bg canteen
    sc "Опять холодный ужин? Это уже диагноз, а не график."
    ev "Это уже грамотное распределение бедствия по часам."
    sc "Тогда добавь в расписание нормальную еду."
    return

label w3_pre_slots_scene:
    scene bg technical
    ev "Открываю недельный план как операционный лист: промахнуться нельзя."
    na "В техническом отсеке пахнет озоном и машинным маслом — привычный запах жизни на дальнем рейсе."
    return

label w3_between_1_2_scene:
    scene bg corridor
    ev "Может посмотреть какой-нибудь фильм? Времени много появилось. Ха."
    return

label w3_between_2_3_scene:
    scene bg canteen
    na "У автомата с напитками Эван спорит с Томасом о том, какая музыка лучше для ночной вахты."
    tg "Ставь джаз, приятель. Под него руки реже дурят."
    ev "Не люблю старьё."
    tg "Ну хоть scorpions..."
    ev "Пожалуй послушаю новый альбом от gemini, спродюссировал gemini, люди нужны вообще?"
    return

label w3_between_3_4_scene:
    scene bg observation
    ev "Между слотами зависаю у звёзд и прогоняю дыхание по схеме Кендзи."
    na "Пять вдохов, пять выдохов — и снова в бой."
    return

label w3_between_4_5_scene:
    scene bg corridor
    na "По общему каналу снова звучит та же фраза стюарда о задержке ужина — слово в слово, как в прошлом цикле."
    return

label w3_between_5_6_scene:
    scene bg technical
    mr "Чего так несёшься, помедленней, док, я уже думаю, не из-за тебя ли я тут."
    ev "Ты даже не представляешь... как мы все опаздываем."
    return

label w3_between_6_7_scene:
    scene bg canteen
    na "В столовой пахнет разогретым супом и озоном от неисправного автомата."
    ev "Самые земные запахи здесь почему-то сильнее всего напоминают, какая у ошибки цена."
    return

label w3_post_slots_scene:
    scene bg corridor
    na "Перед ночным брифингом Эван берёт в медиатеке старую аудиокнигу о первых экспедициях к Юпитеру."
    ev "Слушаю её десять минут в пустом коридоре и впервые за день думаю не об очередной 'смерти'."
    return

label w3_slot_1:
    menu:
        "Неделя 3 / Слот 1"
        "Научный эксперимент: предсказать микросбои":
            $ manifest_state.take_action("w3_predict")
            ev "Три прогноза. Три попадания."
            ev "Значит, хотя бы часть системы можно посчитать."
            $ manifest_state.register_evidence("predictive_success")
        "Попытаться предотвратить первую аварию лично":
            $ manifest_state.take_action("w3_prevent")
            ev "В этот раз секцию C мы удержали."
            ev "Для них это случайность. Для меня — уже выбор."
        "Пропустить смену ради сна":
            $ manifest_state.take_action("w3_sleep")
            ev "Без сна я ничего не добьюсь."
            ev "А если поплывёт фокус, память о прошлых неделях превратится в шум."
        "проверить нейросеть автопилота":
            $ manifest_state.take_action("w3_quest_autopilot_ai")
            $ manifest_state.complete_quest("quest_05_autopilot_ai")
            $ manifest_state.register_evidence("autopilot_model_drift")
            na "Квест выполнен: модель автопилота учат на ненормальных параметрах."
            ev "Кто-то скармливает ей чужие приоритеты."
    return

label w3_slot_2:
    menu:
        "Неделя 3 / Слот 2"
        "Разговор с Маркусом о сценариях угроз":
            $ manifest_state.take_action("w3_marcus")
            scene bg corridor
            if manifest_state.can_interact_with("marcus"):
                mr "Если ты прав, нужен кризисный штаб. Тихий, без толпы."
                mr "Но без прямой улики я людей легально не соберу."
                ev "Тогда я добуду улики."
            else:
                na "Маркус сухо кивает и уходит в другой отсек. Он явно избегает вас."
        "Разговор с Мирой о математике аномалий":
            $ manifest_state.take_action("w3_mira_math")
            scene bg laboratory
            if manifest_state.can_interact_with("mira"):
                ms "Петля... возможно, вообще не про время."
                ms "Может, ты не назад идёшь, Эван. Может, просто соскальзываешь в соседнюю ветвь."
                $ manifest_state.register_evidence("mira_versions_hypothesis")
                ev "Красивая гипотеза."
            else:
                ms "Формально говоря... сейчас не лучшее время."
        "Архивная рутина и фиксация отличий":
            $ manifest_state.take_action("w3_archive")
            ev "Сухая работа держит голову на месте. Таблица не спорит."
            ev "Я верю только цифрам."
    return

label w3_slot_3:
    menu:
        "Неделя 3 / Слот 3"
        "Совместная смена с Леной в реакторном отсеке":
            $ manifest_state.take_action("w3_lena_shift")
            scene bg technical
            if manifest_state.can_interact_with("lena"):
                if manifest_state.role_requirement_met("lena", ["engineer", "repair_key"]):
                    le "Могу протащить тебя в обход блокировки мостика. Но это уже на грани."
                    le "Если спалимся, нас снимут со смены и закроют."
                    $ manifest_state.add_ally_by_tag("technical")
                    ev "Я собрал достаточно причин это сделать."
                else:
                    le "Я... не тяну такой обход. Только базовую диагностику, не больше."
                    ev "Понял. Без сильного инженера этот заход сейчас мёртвый."
            else:
                na "Лена избегает вас и переводится на параллельную смену."
                ev "Может, надо было дожимать её раньше. Поздно."
        "Запись подкаста Сары о жизни в перелёте":
            $ manifest_state.take_action("w3_sarah_podcast")
            scene bg canteen
            if manifest_state.can_interact_with("sarah"):
                sc "Людям нужны не только сводки. Им нужны живые голоса."
                sc "Как только они перестают слышать друг друга, экипаж превращается в толпу."
                ev "Тогда этот выпуск полезнее половины приказов."
            else:
                na "Сара отменяет запись и отвечает лишь коротким служебным сообщением."
        "Лекция Эвана для пассажиров о чёрных дырах":
            $ manifest_state.take_action("w3_public_talk")
            scene bg canteen
            ev "Наука иногда сбивает панику. Если у страха есть язык, его легче держать."
            ev "Я говорю про горизонты событий, а у людей в глазах один вопрос: успеем ли?"
        "собрать сигнатуры с аварийных маяков":
            $ manifest_state.take_action("w3_quest_beacons")
            $ manifest_state.complete_quest("quest_06_beacons")
            $ manifest_state.register_evidence("beacon_echo")
            na "Квест выполнен: аварийные маяки дают эхо ещё до команды."
            ev "Будто всё знает о бедствии заранее."
        "провести двойной слепой тест памяти экипажа":
            $ manifest_state.take_action("w3_quest_memory_test")
            $ manifest_state.complete_quest("quest_15_memory_test")
            $ manifest_state.register_evidence("memory_discrepancy_matrix")
            na "Квест выполнен: у шести человек воспоминания о вчерашнем дне статистически невозможны."
            ev "Петля трогает не только события. Она правит биографию на ходу."
    return

label w3_slot_4:
    menu:
        "Неделя 3 / Слот 4"
        "Ночная вахта в лаборатории":
            $ manifest_state.take_action("w3_lab")
            scene bg laboratory
            ev "Шум пространства звучит как сердце перед срывом."
            ev "Я ловлю каждую волну так, будто снимаю пульс у тяжёлого пациента."
        "Проверка грузового трюма":
            $ manifest_state.take_action("w3_cargo")
            scene bg technical
            $ manifest_state.register_evidence("unlogged_crate")
            mr "Есть контейнеры без нормальной маркировки."
            mr "И кто-то очень старается, чтобы мы не лезли именно сюда."
            ev "Тогда тем более стоит."
        "Личный досуг: старые записи о Земле":
            $ manifest_state.take_action("w3_earth_records")
            ev "Память о доме держит лучше транквилизатора."
            ev "Вот накоплю денег, вернусь на родную планету и..."
            ev "и... зашью лицо игрушке..."
            ev "В глазах потемнело."
            ev "Что это было? Лицо, Игрушка? Это я вообще сказал?!"
    return


label w3_sabotage_report:
    scene bg bridge
    na "К концу недели срывается подача охлаждения в сектор B: кто-то вручную изменил очередность клапанов."
    ev "Я собираю досье по доступам и иду к капитану."
    ch "Этого списка людей не должно быть рядом с критическим контуром."
    ch "Это трибунал!"
    ch "..."
    ch "Ждите указаний, Эван. Порядок я наведу сам."
    $ manifest_state.register_evidence("sabotage_cooling_b")
    return

label w3_logic_chain:
    scene bg corridor
    ev "Мне нужна не интуиция. Нужна цепочка причин."
    $ manifest_state.set_logic_hint("Ищу истину через наблюдения: сначала опора, потом допустимый вывод.")
    menu:
        "Шаг 1: что является самой надёжной опорой?"
        "Повторяемые приборные аномалии":
            $ w3_step1 = "data"
        "Ощущения дежавю":
            $ w3_step1 = "feeling"

    $ manifest_state.set_logic_hint("Теперь выбираю истину сам: удобная версия может быть ошибкой, но иногда альтернативный вывод допустим.")
    menu:
        "Шаг 2: какой вывод следует из этого?"
        "Меняются версии реальности, а манифест это фиксирует":
            $ w3_step2 = "reality_variants"
        "Кто-то просто подменяет файлы в архиве":
            $ w3_step2 = "fake_archive"

    $ manifest_state.clear_logic_hint()
    if w3_step1 == "data" and w3_step2 == "reality_variants":
        $ manifest_state.register_logic_chain(True)
        ev "Цепочка сходится. Я держусь за данные, а не за страх."
    else:
        $ manifest_state.register_logic_chain(False)
        $ manifest_state.apply_truth_flag("logic_false")
        ev "Я где-то ошибся. Цепочка ломается. Я опять тянусь к удобной версии вместо правды."
    return


label w3_proof_scene:
    scene bg corridor
    ev "Маркус понимает только ясный риск. Если мне нужна его помощь, говорить придётся языком безопасности, не одержимости."
    call generic_weekly_proof_scene("marcus", "Маркус") from _call_generic_weekly_proof_scene_3
    return

label w3_slot_5:
    menu:
        "Неделя 3 / Слот 5"
        "Попросить Лену разобрать аварийный насос":
            call generic_role_quest(
                "w3_partner_pump", "lena", "analysis", 61, "pump_failure_origin",
                "Лена резко срывает защитную панель и находит искусственно ослабленный узел: это уже не сбой, а чья-то рука.",
                "Лена допускает одну ошибку за другой, и насос так и остаётся капризной загадкой без твёрдой причины.",
                "Лена не помогает: по её действиям видно, что насос ей выгоднее оставить умирающим."
            ) from _call_generic_role_quest_10
        "Попросить Кенджи проверить токсикологию воды":
            call generic_role_quest(
                "w3_partner_toxicology", "kenji", "analysis", 60, "water_toxicology_clearance",
                "Кенджи находит в следах воды компонент, которого не должно быть в гражданском контуре вообще.",
                "Исследование даёт только слабый намёк: данных недостаточно для обвинения.",
                "Кенджи слишком занят, чтобы помочь, доводы не слушает."
            ) from _call_generic_role_quest_11
    return

label w3_slot_6:
    menu:
        "Неделя 3 / Слот 6"
        "Собрать карты доступа вместе с Маркусом":
            call generic_role_quest(
                "w3_partner_access_cards", "marcus", "authority", 59, "security_card_branch",
                "Маркус выстраивает схему так чётко, будто всегда ждал подобного кризиса: доступы не совпадают с должностями.",
                "Карта доступа получается рваной; подозрения есть, но маршрута диверсанта всё ещё нет.",
                "Маркус не помогает: сейчас он сам часть проблемы, а не решение."
            ) from _call_generic_role_quest_12
        "Провести тихий брифинг с Сарой":
            call generic_role_quest(
                "w3_partner_briefing", "sarah", "empathy", 58, "crew_message_frame",
                "Сара находит правильный тон для людей.",
                "Сара перегибает драму, и часть экипажа лишь сильнее нервничает.",
                "Сара не помогает: сейчас ей ближе шум, чем доверие."
            ) from _call_generic_role_quest_13
    return

label w3_slot_7:
    menu:
        "Неделя 3 / Слот 7"
        "Исследовать крошку элемента 'Астрий'":
            jump w3_astrium_chain
        "Сверить манифест с прошлыми выводами":
            $ manifest_state.take_action("w3_diary_chain")
            ev "Я записываю мысль, от которой мороз по коже: петля сохраняет не факты, а структуру выбора. Стал ли я ближе к правде?.."
        "Попросить Лену вскрыть кабину пилотов":
            call investigate_pilot_cabin_with_lena("w3_pilot_cabin_lena") from _call_investigate_pilot_cabin_with_lena
    return

label w3_astrium_chain:
    $ manifest_state.take_action("w3_astrium_stage1")
    $ manifest_state.set_logic_hint("Астрий: сначала нужно доказать, что образец не метеоритный мусор, а продукт аномалии.")
    menu:
        "Астрий / Шаг 1"
        "Сверить спектр с пылевым шлейфом у чёрной дыры":
            $ a1 = True
        "Сначала проверить, не совпадает ли спектр с техногенным шлаком реактора":
            $ a1 = False
    $ manifest_state.set_logic_hint("Если спектр внеземной, второй опорой должна стать реакция материала на гравитационное поле.")
    menu:
        "Астрий / Шаг 2"
        "Поместить образец в модель локального гравитационного градиента":
            $ a2 = True
        "Проверить только термическое сжатие, возможно, это редкий промышленный кристалл":
            $ a2 = False
    $ manifest_state.clear_logic_hint()
    if a1 and a2:
        $ manifest_state.advance_element_stage("Астрий рождается только вблизи аномалии и меняет отклик под гравитационным сжатием.")
        $ manifest_state.register_evidence("astrium_origin")
        ev "Если цепочка верна, астрий не просто редкий. Он буквально 'запоминает' давление искривлённого пространства."
    else:
        $ manifest_state.register_logic_chain(False)
        ev "Я делаю удобное предположение и теряю научную опору. С астрией так нельзя."
    return
