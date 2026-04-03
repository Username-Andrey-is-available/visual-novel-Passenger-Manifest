init -7 python:
    FLOWCHART_WEEKS = [
        {
            "title": "Неделя 1",
            "subtitle": "Первый провал",
            "nodes": [
                {"key": "anomaly_spectrum", "label": "Спектр аномалии", "kind": "evidence", "description": "Первый научный след гравитационного искажения."},
                {"key": "shared_dreams", "label": "Общие сны", "kind": "evidence", "description": "Пассажиры начинают видеть одно и то же падение."},
                {"key": "decoded_noise_pattern", "label": "Шум как сигнал", "kind": "quest", "description": "Помехи в датчиках перестают выглядеть случайными."},
                {"key": "black_hole_fall", "label": "Падение в сингулярность", "kind": "critical", "description": "Aurora впервые срывается в чёрную дыру."},
            ],
        },
        {
            "title": "Неделя 2",
            "subtitle": "Повтор и сдвиг",
            "nodes": [
                {"key": "manifest_shift", "label": "Сдвиг манифеста", "kind": "critical", "description": "Имена те же, роли уже другие."},
                {"key": "camera_blindspots", "label": "Слепые зоны", "kind": "evidence", "description": "Камеры темнеют именно перед важными сбоями."},
                {"key": "restored_log_fragment", "label": "Восстановленный лог", "kind": "quest", "description": "Из архивов всплывает незарегистрированный доступ к мостику."},
                {"key": "stress_cluster", "label": "Кластер тревоги", "kind": "evidence", "description": "Тревожность экипажа синхронна с внешним импульсом."},
            ],
        },
        {
            "title": "Неделя 3",
            "subtitle": "Эксперименты",
            "nodes": [
                {"key": "predictive_success", "label": "Предсказание сбоев", "kind": "choice", "description": "Эван учится опережать детерминированные сбои."},
                {"key": "autopilot_model_drift", "label": "Дрифт автопилота", "kind": "evidence", "description": "Навигационная модель обучается на ложных приоритетах."},
                {"key": "mira_versions_hypothesis", "label": "Гипотеза Миры", "kind": "critical", "description": "Петля может быть не откатом времени, а сдвигом реальностей."},
                {"key": "memory_discrepancy_matrix", "label": "Тест памяти", "kind": "quest", "description": "У части экипажа появляются невозможные воспоминания."},
                {"key": "astrium_origin", "label": "Происхождение астрия", "kind": "quest", "description": "Материал напрямую связан с полем аномалии."},
            ],
        },
        {
            "title": "Неделя 4",
            "subtitle": "Второй наблюдатель",
            "nodes": [
                {"key": "second_observer", "label": "Кто-то помнит тоже", "kind": "critical", "description": "Мира даёт понять, что Эван не единственный с памятью о циклах."},
                {"key": "false_alert_source", "label": "Источник ложных тревог", "kind": "evidence", "description": "Нервозность экипажа кто-то разгоняет намеренно."},
                {"key": "encrypted_thread", "label": "Зашифрованная переписка", "kind": "evidence", "description": "На борту работает скрытая координация."},
                {"key": "assault_kit_ready", "label": "Комплект штурма", "kind": "quest", "description": "Собран набор для прохода к мостику."},
                {"key": "note_final_cycle", "label": "Записка из другой ветки", "kind": "critical", "description": "Подсказка на финальный цикл переживает обычный сброс."},
                {"key": "astrium_conductive_property", "label": "Свойство астрия", "kind": "quest", "description": "Материал способен гасить краткие энергетические дрожания."},
            ],
        },
        {
            "title": "Неделя 5",
            "subtitle": "Правда о корабле",
            "nodes": [
                {"key": "dead_pilots", "label": "Мёртвые пилоты", "kind": "critical", "description": "Кабина вскрыта, а внутри давно нет живого управления."},
                {"key": "pilot_toxin", "label": "Следы сокрытия", "kind": "evidence", "description": "Отчёты о пилотах подделывались вручную."},
                {"key": "power_sync_map", "label": "Карта питания мостика", "kind": "quest", "description": "Штурм получает рабочее энергетическое окно."},
                {"key": "biometric_spoof", "label": "Поддельные биометрии", "kind": "evidence", "description": "Ключевые зоны посещали чужими лицами."},
                {"key": "mira_pressure_point", "label": "Фокус на Мире", "kind": "choice", "description": "Подозрение на Миру перестаёт быть пустой паникой."},
                {"key": "astrium_cognitive_buffer", "label": "Астрий и личность", "kind": "quest", "description": "Материал удерживает сознание от распада в поле аномалии."},
            ],
        },
        {
            "title": "Неделя 6",
            "subtitle": "Финальная петля",
            "nodes": [
                {"key": "ally:technical", "label": "Инженеры на вашей стороне", "kind": "choice", "description": "Техконтур готов к проходу."},
                {"key": "ally:pilot", "label": "Пилот готов к перехвату", "kind": "choice", "description": "Есть кому сесть за ручной вектор."},
                {"key": "ally:ally_candidate", "label": "Инфоканалы под контролем", "kind": "choice", "description": "Штурм прикрыт от паники."},
                {"key": "mira_note_confession", "label": "Признание Миры", "kind": "critical", "description": "Инопланетный наблюдатель раскрывается и встаёт в центр финала."},
                {"key": "mira_detained", "label": "Мира под арестом", "kind": "critical", "description": "Хейз и Маркус принимают досье и изолируют Миру до конца операции."},
                {"key": "bridge_override_code", "label": "Код мостика", "kind": "quest", "description": "Дверь можно открыть не силой, а правом доступа."},
                {"key": "nav_core_reflashed", "label": "Перепрошивка ядра", "kind": "quest", "description": "Навигационное ядро подчиняется новому сценарию."},
                {"key": "astrium_secret_complete", "label": "Секрет астрия завершён", "kind": "critical", "description": "Последний козырь против диверсии и петли."},
                {"key": "mission_cover_story", "label": "Истинная цель рейса", "kind": "critical", "description": "Саботёр признаёт, что пассажирский рейс был ширмой для миссии с астрием."},
                {"key": "saboteur_ceasefire", "label": "Снятие диверсии", "kind": "choice", "description": "После раскрытия секрета астрия один из диверсантов убирает внутренние ловушки с маршрута."},
                {"key": "ending_truth", "label": "Истина о петле", "kind": "ending", "description": "Эван понимает, что менялись не записи, а сами версии реальности."},
                {"key": "ending_alien", "label": "Инопланетная победа", "kind": "ending", "description": "Неостановленный наблюдатель уводит Aurora в чужой сценарий."},
                {"key": "ending_paranoia", "label": "Паранойя", "kind": "ending", "description": "Неверное обвинение рвёт команду до встречи с чёрной дырой."},
                {"key": "ending_sacrifice", "label": "Цена спасения", "kind": "ending", "description": "Курс спасён ценой жизни Эвана в техническом отсеке."},
                {"key": "ending_breakdown", "label": "Когнитивный срыв", "kind": "ending", "description": "Память и причинность ломаются раньше финального штурма."},
                {"key": "ending_crew_split", "label": "Раскол экипажа", "kind": "ending", "description": "Команда распадается на лагеря и теряет шанс на общий манёвр."},
                {"key": "ending_memory_crash", "label": "Обвал памяти", "kind": "ending", "description": "Ключевая нить выпадает, и петля захлопывается вслепую."},
                {"key": "ending_asteroids", "label": "Астероидное поле", "kind": "ending", "description": "Побег от сингулярности приводит Aurora в новую катастрофу."},
                {"key": "ending_cell", "label": "Комната-тюрьма", "kind": "ending", "description": "Капитан лишает Эвана и свободы, и доступа к Manifest."},
                {"key": "ending_escape", "label": "Выход из петли", "kind": "ending", "description": "Корабль уходит от чёрной дыры совместным выбором."},
                {"key": "ending_loop", "label": "Петля замкнулась", "kind": "ending", "description": "Истина оказалась близко, но не удержалась."},
            ],
        },
    ]

    def pm_mark_flow_flag(flag):
        if not flag:
            return
        flags = set(getattr(persistent, "flow_flags", set()) or set())
        flags.add(flag)
        persistent.flow_flags = flags
        renpy.save_persistent()

    def pm_collect_flow_flags():
        flags = set(getattr(persistent, "flow_flags", set()) or set())

        if "manifest_state" in globals():
            state = manifest_state
            flags.update(state.evidence)
            flags.update(state.completed_quests)
            flags.update(state.truth_flags)
            flags.update("ally:" + tag for tag in state.allies)

            if state.alien_exposed:
                flags.add("alien_exposed")
            if state.false_accusation:
                flags.add("false_accusation")
            if state.self_sacrifice:
                flags.add("ending_sacrifice")
            if state.escaped_black_hole:
                flags.add("ending_escape")
            if state.captain_execution or state.dictator_cell or state.asteroid_crash:
                flags.add("ending_loop")

        return flags

    def pm_flow_progress():
        total = sum(len(week["nodes"]) for week in FLOWCHART_WEEKS)
        unlocked = sum(1 for week in FLOWCHART_WEEKS for node in week["nodes"] if node["key"] in pm_collect_flow_flags())
        return unlocked, total

    def pm_flow_color(kind, unlocked):
        palette = {
            "choice": ("#8d99a0", "#f1b640"),
            "evidence": ("#64808a", "#1aa7e6"),
            "quest": ("#607b88", "#2897c5"),
            "critical": ("#7b7388", "#66d7ff"),
            "ending": ("#8c6d72", "#ff7b7b"),
        }
        locked, active = palette.get(kind, ("#6c7a80", "#1aa7e6"))
        return active if unlocked else locked

    def pm_delete_all_saves():
        removed = 0
        for filename, _extra, _time, _screenshot in renpy.list_saved_games(regexp=r".*", fast=True):
            renpy.unlink_save(filename)
            removed += 1

        renpy.restart_interaction()

        if removed:
            renpy.notify("Все сохранения удалены.")
        else:
            renpy.notify("Сохранений не найдено.")
