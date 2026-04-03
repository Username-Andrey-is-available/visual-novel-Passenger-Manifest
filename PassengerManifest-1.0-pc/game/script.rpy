# Passenger Manifest — основной роутер сюжета.

define ev = Character('Доктор Эван Картер', color="#b8e6ff")
define le = Character('Лена')
define mr = Character('Маркус')
define kt = Character('Кендзи')
define sc = Character('Сара')
define tg = Character('Томас')
define ch = Character('Капитан Хейз')
define ms = Character('Мира')
define na = Character(None)

label start:
    $ manifest_state.reset_all()
    $ choice_rollback_targets = []
    $ pm_sync_runtime_progress(reset=True)
    $ pm_stop_story_sound()
    $ pm_play_regular_music(force=True)
    jump prologue

label prologue:
    scene bg aurora
    na "ISV Aurora. Межзвёздный пассажирский корабль."
    ev "Я доктор Эван Картер. Архивист, наблюдатель, человек с дурной привычкой всё записывать."
    ev "Моя работа проста: вести Passenger Manifest, ловить отклонения, складывать чужие жизни в аккуратное досье."
    ev "Очередной дальний рейс. Тихий график, предсказуемая рутина, сотни историй, которые не должны были стать моими."
    ev "Тогда мне казалось, что это будет обычная неделя. Просто ещё одна."
    jump week_loop

label week_loop:
    if manifest_state.loop_count >= 6:
        jump finale

    $ manifest_state.roll_new_week()
    $ pm_stop_story_sound()
    $ pm_play_regular_music()
    scene bg aurora
    if manifest_state.loop_count == 1:
        na "Неделя [manifest_state.week_index]."
    else:
        na "Неделя [manifest_state.week_index]. Цикл [manifest_state.loop_count]."
        $ pm_story_impact("loop_reset", pause=0.18, stop_after=True)
    call loop_refrain_scene from _call_loop_refrain_scene
    call show_manifest_snapshot from _call_show_manifest_snapshot
    call week_dispatch from _call_week_dispatch

    if manifest_state.week_index < 6:
        if manifest_state.loop_count == 1:
            na "Неделя завершена. За иллюминаторами вспыхивает сингулярность."
        else:
            na "Неделя завершена. Впереди — сингулярность и очередной откат."
        jump week_loop

    jump finale

label show_manifest_snapshot:
    na "Досье недели:"
    python:
        for cid, card in manifest_state.manifest.items():
            renpy.say(None, "• {} — {}".format(card["name"], manifest_state.get_public_role(card)))
    return


label loop_refrain_scene:
    scene bg corridor
    le "Третий шлюз опять тупит. Ладно, сейчас вправлю ему мозги."
    kt "Утренний обход, всё как всегда. Кто не спал — ко мне. До обеда."
    sc "Если на этом рейсе случится что-то интереснее каши, я должна увидеть это первой."
    if manifest_state.loop_count == 1:
        ev "Обычное утро на Aurora. Те же голоса, тот же ритм, та же деловая суета."
    else:
        ev "Они снова говорят то же самое. Для них это утро обычное. Для меня — уже нет."
        $ memory_fragment = manifest_state.get_memory_fragment()
        if memory_fragment:
            ev "[memory_fragment]"
    return

label generic_weekly_proof_scene(cid, display_name):
    scene bg corridor
    $ helper_verb = "помогла" if cid in ["lena", "sarah", "mira"] else "помог"
    $ proof_hint_prefix = "Подбираю аргументацию" if manifest_state.loop_count % 2 else "Формулирую обоснование"

    if manifest_state.week_index == 2 and cid == "lena":
        $ intro_text = "[display_name], мне нужен твой взгляд на шлюзы. Если я зря дёргаюсь — это просто лишняя проверка. Если нет, кто-то уже щупает корабль на слабое место."
        $ manifest_state.set_logic_hint("%s: Лена лучше всего слышит технический риск, цену аварии и конкретику по контурам." % proof_hint_prefix)
        menu:
            "Как попросить Лену о нестандартной проверке?"
            "Сослаться на нарушение техрегламента и возможную служебную проверку":
                $ approach_stat = "authority"
                $ approach_text = "Если этот шлюз опять врёт журналу, под проверку пойдём не только мы. Поднимут всю техпалубу."
            "Показать ей странный паттерн отказов и попросить второй взгляд инженера":
                $ approach_stat = "analysis"
                $ approach_text = "Отказы слишком ровные для случайности. Мне нужен человек, который отличит чужую руку от обычного износа."
            "Напомнить, что из-за одного неверного шлюза люди могут не успеть выйти в аварийный коридор":
                $ approach_stat = "empathy"
                $ approach_text = "Если здесь рванёт разгерметизация, на формальности никто смотреть не будет. Я прошу помочь раньше, чем за это заплатят люди."

    elif manifest_state.week_index == 3 and cid == "marcus":
        $ intro_text = "[display_name], мне нужно, чтобы ты [helper_verb] с одной схемой."
        $ manifest_state.set_logic_hint("%s: Маркус уважает язык риска, маршрутов и предсказуемых последствий." % proof_hint_prefix)
        menu:
            "Как втянуть Маркуса в расследование?"
            "Показать, что диверсант уже репетирует маршрут через слабые точки безопасности":
                $ approach_stat = "authority"
                $ approach_text = "Если я прав, это не странности. Это уже готовый проход через твои сектора."
            "Разложить перед ним повторяющиеся пики сбоев и совпадения по доступам":
                $ approach_stat = "analysis"
                $ approach_text = "Смотри не на меня. Смотри на совпадения."
            "Сказать прямо, что без тихого штаба экипаж сорвётся в охоту друг на друга":
                $ approach_stat = "empathy"
                $ approach_text = "Если мы не дадим людям хоть какое-то чувство контроля, они сами назначат виноватых раньше фактов."

    elif manifest_state.week_index == 4 and cid == "sarah":
        $ intro_text = "[display_name], мне нужно, чтобы ты [helper_verb] превратить это в зацепку, а не в ещё один шёпот по столовой."
        $ manifest_state.set_logic_hint("%s: Сара лучше всего реагирует на историю с ценой ошибки, проверяемыми фактами и человеческой ставкой." % proof_hint_prefix)
        menu:
            "Как убедить Сару влезть в дело?"
            "Пообещать не сенсацию, а документированную цепочку доступа и мотива":
                $ approach_stat = "analysis"
                $ approach_text = "Мне не нужен заголовок. Мне нужен человек, который отличает монтаж страха от факта."
            "Сказать, что без её канала шёпот победит нас раньше диверсанта":
                $ approach_stat = "empathy"
                $ approach_text = "Люди уже живут слухами. Если ты не дашь им форму правды, они выберут форму паники."
            "Надавить через ответственность перед экипажем и цену публичной ошибки":
                $ approach_stat = "authority"
                $ approach_text = "Если мы назовём не то имя, корабль рванёт изнутри. Мне нужен человек, который выдержит удар, а не раскрутит его."

    elif manifest_state.week_index == 5 and cid == "thomas":
        $ intro_text = "[display_name], мне нужна не теория. Мне нужен тот момент, где человек ещё может вырвать штурвал у автоматики."
        $ manifest_state.set_logic_hint("%s: Томас включается, когда слышит язык реального пилотирования, окна манёвра и цену промедления." % proof_hint_prefix)
        menu:
            "Как подвести Томаса к опасной помощи?"
            "Говорить как офицер: без оценки ручного манёвра нельзя готовить штурм мостика":
                $ approach_stat = "authority"
                $ approach_text = "Мне нужен не совет из учебника. Мне нужна твоя подпись под тем, возможен ли живой перехват вообще."
            "Дать ему схему питания и попросить оценить реальное окно для ручного входа":
                $ approach_stat = "analysis"
                $ approach_text = "Я принёс цифры. Скажи, есть ли в этой схеме место для живого пилота."
            "Напомнить, что без него в решающий момент за штурвал сядет первый выживший":
                $ approach_stat = "empathy"
                $ approach_text = "Если ты в это не войдёшь, в решающий момент за штурвал сядет не лучший. Просто самый упрямый."

    elif manifest_state.week_index == 6 and cid == "kenji":
        $ intro_text = "[display_name], мне нужно, чтобы ты [helper_verb] с задачей, которая на бумаге не должна существовать."
        $ manifest_state.set_logic_hint("%s: Кендзи отвечает на клиническую аргументацию, доказуемый риск и моральную цену бездействия." % proof_hint_prefix)
        menu:
            "Как убедить Кендзи в финальной помощи?"
            "Опереться на протокол: без нестандартного решения медблок встретит массовый срыв":
                $ approach_stat = "authority"
                $ approach_text = "Если мы войдём без подготовки, пациентов не останется."
            "Показать, что астрий уже даёт воспроизводимый эффект и требует врачебного контроля":
                $ approach_stat = "analysis"
                $ approach_text = "Мне нужен врач, а не человек веры. Я вижу эффект, но без тебя не пойму, где кончается наука и начинается самообман."
            "Сказать прямо, что кто-то должен удержать людей от распада, пока мы ломаем курс":
                $ approach_stat = "empathy"
                $ approach_text = "Я иду спасать корабль. Ты — людей внутри него. Без тебя это будет катастрофа."



    $ intro_text = intro_text.replace("[display_name]", display_name).replace("[helper_verb]", helper_verb)
    $ proof_success_text = "%s недовольно морщится, но кивает: этого хватает, чтобы включиться в дело без лишних вопросов." % display_name
    $ proof_retry_text = "%s не в восторге, это видно сразу. Но дверь пока не захлопывает." % display_name
    $ proof_fail_text = "%s отступает на шаг и даёт понять: в это он не полезет." % display_name
    $ manifest_state.clear_logic_hint()
    ev "[intro_text]"
    ev "[approach_text]"
    $ score = manifest_state.stats.get(approach_stat, 50) + int(manifest_state.get_role_factor(cid) * 8) + manifest_state.memory_bonus()
    if score >= 60:
        $ manifest_state.register_week_proof(cid)
        $ manifest_state.adjust_stat(approach_stat, 1)
        na "[proof_success_text]"
    else:
        $ manifest_state.fail_convince_character(cid)
        if manifest_state.interaction_allowed_after_failed_proof(cid):
            na "[proof_retry_text]"
        else:
            na "[proof_fail_text]"
    return

label generic_role_quest(quest_code, partner_cid, stat_name, difficulty, reward_code, success_text, failure_text, sabotage_text, required_codes=None, sabotage_codes=None):
    if manifest_state.needs_weekly_proof(partner_cid):
        $ partner_name = manifest_state.manifest.get(partner_cid, {}).get('name', partner_cid)
        call generic_weekly_proof_scene(partner_cid, partner_name) from _call_generic_weekly_proof_scene
    if not manifest_state.can_interact_with(partner_cid):
        na "Контакт сорван: персонаж держит дистанцию и не выходит на смену вместе с вами."
        return
    $ manifest_state.take_action(quest_code)
    $ quest_outcome = manifest_state.resolve_partner_quest(quest_code, partner_cid, stat_name, difficulty, reward_code, required_codes, sabotage_codes)
    if quest_outcome == "success":
        $ renpy.say(narrator, success_text)
    elif quest_outcome == "sabotage":
        $ renpy.say(narrator, sabotage_text)
    else:
        $ renpy.say(narrator, failure_text)
    return

label investigate_pilot_cabin_with_lena(action_code):
    if manifest_state.needs_weekly_proof("lena"):
        $ partner_name = manifest_state.manifest.get("lena", {}).get('name', "Лена")
        call generic_weekly_proof_scene("lena", partner_name) from _call_generic_weekly_proof_scene_1
    if not manifest_state.can_interact_with("lena"):
        na "Лена держится от вас подальше, и попытка добраться до кабины пилотов срывается ещё до техотсека."
        return
    $ manifest_state.take_action(action_code)
    if not manifest_state.role_requirement_met("lena", ["engineer", "repair_key"]):
        le "Без нужного допуска я эту дверь не трону. Либо нас завернут по доступу, либо тревога взвоет раньше замка."
        ev "Без 'правильной' Лены я опять упираюсь в металл, пломбы и чужой приказ не лезть к пилотам."
        return

    scene bg technical
    le "В сервисном контуре есть окно. Короткое. Если идём — то прямо сейчас."
    ev "Веди. Мне нужен ответ раньше, чем капитан опять закроет всё приказом."
    $ pm_story_impact("airlock_open", pause=0.18, stop_after=True, duck_music=False)
    scene expression pm_story_image("pilot_cabin_reveal", "images/backgrounds/captains bridge.png")
    $ manifest_state.set_runtime_flag("pilot_cabin_opened")
    $ manifest_state.register_evidence("dead_pilots")
    $ manifest_state.register_evidence("autopilot_override")
    $ manifest_state.register_evidence("autopilot_blackhole_course")
    na "Дверь пилотской кабины отходит в сторону."
    $ pm_story_impact("dead_pilots_reveal", pause=0.24)
    na "Внутри — два тела: Алик Хартманн и Нельсон Стюарт. Они мертвы уже давно."
    ev "Значит, всё это время нас вёл не живой пилот."
    ev "Автопилот с самого начала тянул Aurora прямо в чёрную дыру."
    ev "Пытаюсь перебить курс вручную. Система даже не делает вид, что слушается."

    if manifest_state.role_requirement_met("hayes", ["secret_keeper", "suspected_saboteur"]):
        ch "Без вас миссию завершать неудобнее. Но переживу."
        na "Капитан появляется слишком быстро, будто ждал именно здесь."
        na "Выстрел..."
        $ pm_story_impact("captain_gunshots", pause=0.28, stop_after=True)
        na "...звучит коротко."
        $ manifest_state.set_runtime_flag("captain_execution")
        jump finale

    scene bg corridor
    ev "Остаётся одно: дотащить Томаса до управления, пока курс ещё можно сломать вручную."
    scene bg bridge
    if manifest_state.stats["authority"] >= 55:
        tg "Если ставишь на это своё имя — я сяду за штурвал."
        $ manifest_state.set_runtime_flag("thomas_took_controls")
        if manifest_state.role_requirement_met("thomas", ["fraud", "alcoholic"]):
            $ manifest_state.set_runtime_flag("asteroid_crash")
        else:
            $ manifest_state.set_runtime_flag("escaped_black_hole")
        jump finale
    else:
        ch "Доктор, вы зашли слишком далеко. Это не ваш мостик. И не ваш приказ."
        if manifest_state.role_requirement_met("hayes", ["dictator"]):
            ch "Раз слова до вас не доходят, досидите рейс за решёткой."
            $ manifest_state.set_runtime_flag("dictator_cell")
            jump finale
        ev "Без авторитета я могу только смотреть, как капитан выдавливает нас обратно из кабины."
        return


label week_dispatch:
    if manifest_state.week_index == 1:
        call week_1_arc from _call_week_1_arc
    elif manifest_state.week_index == 2:
        call week_2_arc from _call_week_2_arc
    elif manifest_state.week_index == 3:
        call week_3_arc from _call_week_3_arc
    elif manifest_state.week_index == 4:
        call week_4_arc from _call_week_4_arc
    elif manifest_state.week_index == 5:
        call week_5_arc from _call_week_5_arc
    elif manifest_state.week_index == 6:
        call week_6_arc from _call_week_6_arc
    return

label finale:
    $ pm_stop_story_sound()
    $ pm_play_regular_music()
    $ ending = manifest_state.evaluate_ending()

    if ending == "escape":
        jump ending_escape
    elif ending == "alien_victory":
        jump ending_alien
    elif ending == "paranoia":
        jump ending_paranoia
    elif ending == "sacrifice":
        jump ending_sacrifice
    elif ending == "truth":
        jump ending_truth
    elif ending == "ending_breakdown":
        jump ending_breakdown
    elif ending == "ending_crew_split":
        jump ending_crew_split
    elif ending == "ending_memory_crash":
        jump ending_memory_crash
    elif ending == "ending_asteroids":
        jump ending_asteroids
    elif ending == "ending_cell":
        jump ending_cell
    else:
        jump ending_loop

label ending_escape:
    $ pm_mark_flow_flag("ending_escape")
    scene expression pm_story_image("escape_maneuver", "images/backgrounds/ISV Aurora.png")
    na "Концовка: Ушли от чёрной дыры."
    if "mission_cover_story" in manifest_state.evidence:
        na "Перед самым манёвром правда успевает вскрыться: весь рейс изначально был ширмой для доставки астрия к аномалии."
        ev "Мы вытаскиваем корабль не из честной экспедиции. Из аккуратно упакованного преступления."
    if "saboteur_ceasefire" in manifest_state.evidence:
        na "Часть сопротивления гаснет изнутри: диверсанты снимают собственные ловушки, как только понимают, что их тайная цель уже названа вслух."
    na "Томас берёт управление на себя и выводит Aurora с заранее заданного курса."
    ev "Мы не побеждаем красиво. Мы просто вырываем у петли корабль. И живых."
    jump ending_complete

label ending_alien:
    $ pm_mark_flow_flag("ending_alien")
    scene expression pm_story_image("ending_alien")
    na "Инопланетная победа."
    na "Нераскрытый наблюдатель перехватывает контроль и уводит корабль к неизвестной системе."
    ev "Я выжил. И стал свидетелем чужого начала."
    jump ending_complete

label ending_paranoia:
    $ pm_mark_flow_flag("ending_paranoia")
    scene expression pm_story_image("ending_paranoia")
    na "Паранойя."
    na "Неверное обвинение запускает вооружённый конфликт между отсеками."
    ev "Aurora умирает раньше, чем успевает долететь до чёрной дыры."
    jump ending_complete

label ending_sacrifice:
    $ pm_mark_flow_flag("ending_sacrifice")
    scene expression pm_story_image("ending_sacrifice")
    na "Цена спасения."
    ev "Я вручную рублю навигационный контур и запираю секцию изнутри."
    na "Корабль меняет курс. Эван остаётся в техническом отсеке навсегда."
    jump ending_complete

label ending_loop:
    $ pm_mark_flow_flag("ending_loop")
    scene expression pm_story_image("ending_loop")
    na "Вечная петля."
    na "Я снова и снова подхожу к истине слишком близко, и цикл закрывается раньше спасения."
    ev "Каждый раз мне кажется, что я уже почти дошёл. Каждый раз — почти."
    jump ending_complete

label ending_truth:
    $ pm_mark_flow_flag("ending_truth")
    scene expression pm_story_image("truth")
    na "Скрытая концовка: Истина."
    ev "Досье не врали. Врали мои ожидания. Менялись не записи — менялись сами версии реальности."
    if "mission_cover_story" in manifest_state.evidence:
        na "И есть вторая правда, куда более человеческая и потому страшная: командование знало, куда отправляет Aurora."
        na "Пассажирский рейс был прикрытием. Астрий — целью. Чёрная дыра — частью эксперимента, а не ошибкой прокладки курса."
        ev "Значит, петлю держала не одна аномалия. Её с самого начала подпирала чужая воля. Чужое знание. Чужая готовность платить не своими жизнями."
    na "Passenger Manifest — Незавершён."
    jump ending_complete


label ending_breakdown:
    $ pm_mark_flow_flag("ending_breakdown")
    scene expression pm_story_image("black")
    na "Досрочная плохая концовка: Когнитивный срыв."
    ev "Я теряю нить причин и запираюсь в архиве среди пустых карточек."
    na "Команда остаётся без координации, и корабль уходит в ловушку без сопротивления."
    jump ending_complete

label ending_crew_split:
    $ pm_mark_flow_flag("ending_crew_split")
    scene expression pm_story_image("black")
    na "Досрочная плохая концовка: Раскол экипажа."
    na "Недоверие между отсеками перерастает в конфликт за доступ к ресурсам."
    ev "Я вижу, как команда рвётся на лагеря. И уже не могу стянуть её обратно."
    jump ending_complete

label ending_memory_crash:
    $ pm_mark_flow_flag("ending_memory_crash")
    scene expression pm_story_image("black")
    na "Досрочная плохая концовка: Обвал памяти."
    ev "Я помню, что что-то было важным. Но не могу собрать это в порядок."
    na "Петля захлопывается, а решения принимаются наугад."
    jump ending_complete


label ending_asteroids:
    $ pm_mark_flow_flag("ending_asteroids")
    scene expression pm_story_image("ending_asteroids")
    na "Плохая концовка: Астероидное поле."
    na "Томас садится за управление, но его 'версия' в этом цикле не справляется с реальным пилотированием."
    ev "Aurora уходит от чёрной дыры только затем, чтобы погибнуть в камнях."
    jump ending_complete

label ending_cell:
    $ pm_mark_flow_flag("ending_cell")
    scene expression pm_story_image("black")
    na "Худшая концовка: Комната-тюрьма."
    ch "Сидите здесь, доктор. И думайте о дисциплине."
    na "Капитан запирает вас без Manifest и без доступа к сети. День повторяется, цикл повторяется, а выйти уже не получится никогда."
    ev "Бесконечное время. Те же стены. Те же часы..."
    ev "Бесконечное время. Те же стены. Те же часы..."
    ev "Бесконечное время. Те же стены. Те же часы..."
    ev "Кто я?"
    jump ending_complete

label ending_complete:
    window hide
    $ renpy.block_rollback()
    $ pm_return_to_main_menu()
    return
