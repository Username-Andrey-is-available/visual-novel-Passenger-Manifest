# Passenger Manifest — динамическое состояние и системная архитектура.

init -4 python:
    import random
    import copy

    class ManifestState(object):
        """
        Единый state-container.
        Хранит состояние петли, досье, отношения, улики и флаги концовок.
        """
        def __init__(self):
            self.reset_all()

        def reset_all(self):
            self.week_index = 1
            self.day_index = 1
            self.loop_count = 0
            self.memory_stability = 100
            self.week_time_budget = 0
            self.week_time_spent = 0
            self.week_actions = []
            self.week_slots_total = 7
            self.current_logic_text = ""
            self.proofed_this_week = set()
            self.interaction_denials = {}
            self.secret_element_shared = False
            self.element_stage = 0
            self.element_insight = None
            self.completed_quests = set()
            self.alien_exposed = False
            self.mira_detained = False
            self.false_accusation = False
            self.self_sacrifice = False
            self.timeout_reached = False
            self.logic_chain_failed = False
            self.logic_chain_success = 0
            self.final_plan = None
            self.truth_flags = set()
            self.allies = set()
            self.evidence = set()
            self.manifest = {}
            self.history = []
            self.manifest_studied_weeks = set()
            self.manifest_studied_cycles = set()
            self.blocked_characters = set()
            self.mira_alien_locked = False
            self.pilot_cabin_blocked = False
            self.pilot_cabin_opened = False
            self.captain_execution = False
            self.dictator_cell = False
            self.thomas_took_controls = False
            self.asteroid_crash = False
            self.escaped_black_hole = False
            self.stats = {
                "analysis": 50,
                "empathy": 50,
                "resilience": 50,
                "authority": 50,
            }

        def export_progress_snapshot(self):
            return copy.deepcopy(vars(self))

        def import_progress_snapshot(self, snapshot):
            if not isinstance(snapshot, dict):
                return

            self.__dict__.clear()
            self.__dict__.update(copy.deepcopy(snapshot))

        def progress_marker(self):
            return (
                self.loop_count,
                self.week_index,
                len(self.history),
                len(self.completed_quests),
                len(self.evidence),
                len(self.truth_flags),
                len(self.allies),
            )

        def sync_progress(self):
            pm_sync_runtime_progress()

        def set_runtime_flag(self, attr, value=True):
            setattr(self, attr, value)
            self.sync_progress()

        def roll_new_week(self, forced_seed=None):
            """
            Генерирует новую версию реальности:
            те же персонажи, но другие варианты личностей/ролей.
            """
            self.loop_count += 1
            self.week_index = min(self.loop_count, 6)
            self.day_index = 1
            self.memory_stability = max(20, self.memory_stability - 8)
            self.stats["authority"] = 50
            self.start_week_planning(self.week_slots_total)
            self.proofed_this_week = set()
            self.interaction_denials = {}
            self.current_logic_text = ""

            rng = random.Random(forced_seed if forced_seed is not None else self.loop_count)
            current_manifest = {}
            for cid, cdata in CHARACTER_POOL.items():
                if self.loop_count == 1:
                    variant = cdata["variants"][0]
                else:
                    variant = rng.choice(cdata["variants"])

                public_variant = variant
                if cid == "mira":
                    human_variants = [item for item in cdata["variants"] if item["code"] != "alien"]
                    if self.week_index >= 4 and not self.mira_alien_locked:
                        variant = next(item for item in cdata["variants"] if item["code"] == "alien")
                    if variant["code"] == "alien":
                        self.mira_alien_locked = True
                        public_variant = rng.choice(human_variants)
                    elif self.mira_alien_locked:
                        public_variant = variant
                        variant = next(item for item in cdata["variants"] if item["code"] == "alien")

                current_manifest[cid] = {
                    "name": cdata["display_name"],
                    "base_role": cdata["base_role"],
                    "bio_base": cdata.get("bio_base", ""),
                    "active_role": variant["role"],
                    "variant_code": variant["code"],
                    "trait": variant["trait"],
                    "life_path": variant.get("life_path", ""),
                    "tags": list(variant["tags"]),
                    "public_role": public_variant["role"],
                    "public_trait": public_variant["trait"],
                    "public_life_path": public_variant.get("life_path", variant.get("life_path", "")),
                    "public_status": "неизвестно" if cid == "mira" and self.mira_alien_locked and not self.alien_exposed else "подтверждено",
                }
            self.manifest = current_manifest
            self.history.append({
                "loop": self.loop_count,
                "week": self.week_index,
                "manifest": current_manifest,
            })
            self.sync_progress()

        def start_week_planning(self, budget):
            self.week_slots_total = budget
            self.week_time_budget = budget
            self.week_time_spent = 0
            self.week_actions = []

        def can_take_action(self, cost=1):
            return (self.week_time_spent + cost) <= self.week_time_budget

        def memory_tier(self):
            if self.memory_stability >= 80:
                return "sharp"
            if self.memory_stability >= 55:
                return "strained"
            return "fractured"

        def memory_bonus(self):
            tier = self.memory_tier()
            if tier == "sharp":
                return 4
            if tier == "strained":
                return 0
            return -5

        def can_recall(self, threshold=60):
            return self.memory_stability >= threshold

        def get_memory_fragment(self):
            if self.loop_count <= 1:
                return None

            sharp_fragments = {
                2: "Я помню холод металла за минуту до падения. Значит, конец недели уже когда-то лежал у меня в руках.",
                3: "Перед глазами вспыхивает чужая фраза о версиях реальности. Я ещё не доказал её, но уже боюсь, что она верна.",
                4: "На секунду я снова вижу наблюдательную палубу и лицо, которое знало о петле больше моего.",
                5: "Память приносит не образ, а дверь: кабина пилотов, слишком тихая для живых людей внутри.",
                6: "Я помню сразу несколько финалов. Это не помогает выбрать проще, но помогает понять цену ошибки.",
            }

            strained_fragments = {
                2: "Что-то в конце прошлой недели было не только страшным, но и знакомым. Память ещё держит форму, но уже теряет детали.",
                3: "Я помню, что одна из моих гипотез уже почти сходилась. Хуже всего — не помнить, какая именно.",
                4: "Кто-то уже смотрел на меня так, будто тоже был здесь раньше. Я не удерживаю лицо, только ощущение.",
                5: "Есть важная дверь, к которой я всё время опаздываю мысленно на несколько секунд.",
                6: "Финал уже был, просто не в этой версии. Мне нужно удержать хотя бы самую прочную нить.",
            }

            fractured_fragments = {
                2: "Повтор уже начался, но память рвётся на обрывки. Я знаю больше, чем могу сформулировать.",
                3: "В голове остаётся не вывод, а только тревога, что однажды я уже ошибался именно здесь.",
                4: "Кто-то важный скрывается за знакомым контуром, но память отдаёт лишь пустой силуэт.",
                5: "Я почти вспоминаю правду о корабле и тут же теряю её, как сон при резком пробуждении.",
                6: "Финальные недели наслаиваются друг на друга, и мне приходится выбирать, какой своей памяти доверять.",
            }

            tier = self.memory_tier()
            if tier == "sharp":
                return sharp_fragments.get(self.week_index)
            if tier == "strained":
                return strained_fragments.get(self.week_index)
            return fractured_fragments.get(self.week_index)

        def set_logic_hint(self, text):
            if not text:
                self.current_logic_text = ""
                return

            tier = self.memory_tier()
            if tier == "sharp":
                self.current_logic_text = text
            elif tier == "strained":
                self.current_logic_text = text + " Держись за факты: память уже начинает смазывать переходы."
            else:
                self.current_logic_text = "Мысль ускользает. Опираться можно только на самые жёсткие факты: " + text

        def clear_logic_hint(self):
            self.current_logic_text = ""

        def register_week_proof(self, cid):
            if cid:
                self.proofed_this_week.add(cid)
                self.interaction_denials.pop(cid, None)
                self.sync_progress()

        def needs_weekly_proof(self, cid):
            return self.week_index >= 3 and cid and cid not in self.proofed_this_week

        def mark_interaction_denial(self, cid, denied):
            if cid:
                self.interaction_denials[cid] = denied
                if denied:
                    self.block_character(cid)
                self.sync_progress()

        def interaction_allowed_after_failed_proof(self, cid):
            seed = (self.loop_count * 37) + self.week_index + sum(ord(ch) for ch in cid)
            denied = random.Random(seed).random() < 0.5
            self.mark_interaction_denial(cid, denied)
            return not denied

        def character_is_hostile_role(self, cid):
            card = self.manifest.get(cid, {})
            tags = set(card.get("tags", []))
            return bool(tags & {"antagonistic", "criminal", "corporate", "threat"}) or card.get("variant_code") in {"saboteur", "smuggler", "spy", "fanatic", "suspected_saboteur"}

        def can_offer_help(self, cid):
            return (not self.character_is_hostile_role(cid)) or self.secret_element_shared

        def get_role_factor(self, cid):
            role_weights = {
                "engineer": 0.9, "repair_key": 0.95, "intern": 0.35, "saboteur": 0.0,
                "guardian": 0.8, "paranoid": 0.45, "smuggler": 0.0, "suspects_evan": 0.4,
                "surgeon": 0.9, "incompetent": 0.35, "anomaly_scientist": 0.9, "believer": 0.75,
                "investigator": 0.85, "panic": 0.4, "spy": 0.0, "ally": 0.8,
                "veteran": 0.9, "fraud": 0.25, "alcoholic": 0.2, "savior": 0.95,
                "leader": 0.8, "dictator": 0.35, "secret_keeper": 0.55, "suspected_saboteur": 0.0,
                "quiet_researcher": 0.7, "fanatic": 0.0, "mathematician": 0.85, "alien": 0.6,
            }
            return role_weights.get(self.manifest.get(cid, {}).get("variant_code"), 0.5)

        def resolve_partner_quest(self, quest_code, cid, stat=None, difficulty=55, reward=None):
            factor = self.get_role_factor(cid)
            stat_value = self.stats.get(stat, 50) if stat else 50
            score = stat_value * 0.45 + factor * 55 + self.memory_bonus()
            if not self.can_offer_help(cid):
                score = 0
            success = score >= difficulty
            if success:
                self.completed_quests.add(quest_code)
                if reward:
                    self.register_evidence(reward)
                self.sync_progress()
            return success

        def advance_element_stage(self, insight):
            self.element_stage += 1
            self.element_insight = insight
            if self.element_stage >= 4:
                self.secret_element_shared = True
            self.sync_progress()

        def adjust_stat(self, stat, delta):
            if stat in self.stats:
                self.stats[stat] = max(0, min(100, self.stats[stat] + delta))

        def apply_action_effects(self, action_code):
            if not action_code:
                return

            # Ребаланс: 24 решения за игру. Чтобы стабильно дойти от 50 до квест-порогов 68-72,
            # профильный выбор должен давать заметный импакт (+4), а компромисс — ощутимую цену (-2).
            action_profiles = {
                "analysis": [
                    "science", "research", "scan", "archive", "trajectory", "predict", "lab", "manifest",
                    "compare", "timeline", "evidence", "truth", "log", "camera", "keys", "beacons", "gyros",
                    "biometric", "power_sync", "bridge_code", "nav_reflash", "autopilot", "memory_test",
                ],
                "empathy": [
                    "social", "podcast", "briefing", "rest", "morale", "qa", "sarah", "bar", "leisure",
                    "medical", "kenji", "mira", "cosmos", "earth_records", "faceoff",
                ],
                "resilience": [
                    "night", "gym", "horizon", "infiltration", "assault", "sleep", "shift", "tail",
                    "search", "thrusters", "reserve_sacrifice", "prevent", "cargo", "spacewalk",
                ],
                "authority": [
                    "bridge", "captain", "security", "public", "team", "evac", "official", "prepare",
                    "warn", "expose", "silent", "pilot", "engineer", "info", "locks", "blame",
                ],
            }

            tradeoffs = {
                "analysis": "empathy",
                "empathy": "analysis",
                "resilience": "empathy",
                "authority": "resilience",
            }

            for stat, tokens in action_profiles.items():
                if any(token in action_code for token in tokens):
                    self.adjust_stat(stat, 3)
                    self.adjust_stat(tradeoffs[stat], -1)

            if "sleep" in action_code or "rest" in action_code:
                self.memory_stability = min(100, self.memory_stability + 3)
                self.adjust_stat("resilience", 2)
                self.adjust_stat("authority", -1)
            elif any(token in action_code for token in ["night", "infiltration", "quest", "assault"]):
                self.memory_stability = max(15, self.memory_stability - 3)

            if any(token in action_code for token in ["diary", "journal", "earth_records", "manifest_recheck", "final_breath", "rehearsal"]):
                self.memory_stability = min(100, self.memory_stability + 2)

            if any(token in action_code for token in ["astrium", "truth", "faceoff", "contact_saboteurs", "public_expose", "mira_casefile"]):
                self.memory_stability = max(15, self.memory_stability - 2)

        def take_action(self, action_code, cost=1):
            if not self.can_take_action(cost):
                self.timeout_reached = True
                self.sync_progress()
                return False
            self.week_time_spent += cost
            self.week_actions.append(action_code)
            self.apply_action_effects(action_code)
            self.sync_progress()
            return True

        def quest_requirements(self):
            return {
                "quest_14_quantum_archive": {"analysis": 60, "resilience": 45},
                "quest_17_power_sync": {"analysis": 68, "resilience": 55},
                "quest_18_decoy_maneuver": {"authority": 58, "analysis": 55},
                "quest_19_nav_reflash": {"analysis": 72, "resilience": 60},
                "quest_20_civilian_evac": {"authority": 62, "empathy": 52},
            }

        def meets_quest_requirements(self, quest_code):
            req = self.quest_requirements().get(quest_code, {})
            for stat, threshold in req.items():
                if self.stats.get(stat, 0) < threshold:
                    return False
            return True

        def register_logic_chain(self, success):
            if success:
                self.logic_chain_success += 1
            else:
                self.logic_chain_failed = True

        def complete_quest(self, quest_code):
            self.completed_quests.add(quest_code)
            pm_mark_flow_flag(quest_code)
            self.sync_progress()

        def add_ally_by_tag(self, tag):
            self.allies.add(tag)
            pm_mark_flow_flag("ally:" + tag)
            self.sync_progress()

        def register_evidence(self, code):
            self.evidence.add(code)
            pm_mark_flow_flag(code)
            self.sync_progress()

        def reveal_alien(self):
            self.alien_exposed = True
            pm_mark_flow_flag("alien_exposed")
            self.sync_progress()

        def detain_mira(self):
            self.reveal_alien()
            self.mira_detained = True
            self.block_character("mira")
            self.register_evidence("mira_detained")
            self.sync_progress()

        def commit_final_plan(self, plan):
            self.final_plan = plan
            self.sync_progress()

        def apply_truth_flag(self, flag):
            self.truth_flags.add(flag)
            pm_mark_flow_flag(flag)
            self.sync_progress()

        def get_manifest_role(self, loop_record, cid):
            manifest = loop_record.get("manifest", {})
            card = manifest.get(cid)
            if not card:
                return "—"
            if card.get("variant_code") == "alien" and not self.alien_exposed:
                return card.get("public_role", card.get("base_role", "—"))
            return card.get("active_role", "—")

        def get_public_role(self, card):
            if not card:
                return "—"
            if card.get("variant_code") == "alien" and not self.alien_exposed:
                return card.get("public_role", card.get("base_role", "—"))
            return card.get("active_role", "—")

        def get_public_trait(self, card):
            if not card:
                return "—"
            if card.get("variant_code") == "alien" and not self.alien_exposed:
                return "Статус: неизвестно. Мира держится слишком ровно и не даёт зацепиться за детали."
            return card.get("trait", "—")

        def get_public_life_path(self, card):
            if not card:
                return "—"
            if card.get("variant_code") == "alien" and not self.alien_exposed:
                return card.get("public_life_path", card.get("life_path", "—"))
            return card.get("life_path", "—")

        def get_public_status(self, card):
            if not card:
                return "—"
            if card.get("variant_code") == "alien" and not self.alien_exposed:
                return card.get("public_status", "неизвестно")
            return "подтверждено"

        def mark_manifest_reviewed(self):
            self.manifest_studied_weeks.add(self.week_index)
            self.manifest_studied_cycles.add(self.loop_count)
            self.sync_progress()

        def reviewed_manifest_this_week(self):
            return self.loop_count in self.manifest_studied_cycles

        def block_character(self, cid):
            if cid:
                self.blocked_characters.add(cid)
                self.sync_progress()

        def can_interact_with(self, cid):
            return cid not in self.blocked_characters

        def fail_convince_character(self, cid):
            self.adjust_stat("analysis", -1)
            self.adjust_stat("empathy", -1)
            self.adjust_stat("authority", -2)
            self.block_character(cid)
            self.sync_progress()

        def role_requirement_met(self, cid, required_codes):
            card = self.manifest.get(cid, {})
            return card.get("variant_code") in required_codes


        def get_character_ids(self):
            return list(self.manifest.keys())

        def get_card_by_index(self, idx):
            ids = self.get_character_ids()
            if not ids:
                return None, {}
            safe_idx = idx % len(ids)
            cid = ids[safe_idx]
            return cid, self.manifest.get(cid, {})

        def get_card_in_record(self, record, cid):
            return record.get("manifest", {}).get(cid)

        def format_with_underline_if_changed(self, text, changed, week):
            if week >= 2 and changed and text:
                return "{u}%s{/u}" % text
            return text or "—"

        def evaluate_ending(self):
            if self.dictator_cell:
                return "ending_cell"

            if self.asteroid_crash:
                return "ending_asteroids"

            if self.escaped_black_hole:
                return "escape"

            if self.captain_execution:
                return "endless_loop"

            if self.self_sacrifice or self.final_plan == "sacrifice":
                return "sacrifice"

            if self.false_accusation:
                return "paranoia"

            if self.stats["analysis"] < 32 and self.stats["authority"] < 38:
                return "ending_breakdown"

            if self.stats["empathy"] < 30 and self.stats["authority"] < 45:
                return "ending_crew_split"

            if self.stats["resilience"] < 34 and self.memory_stability < 40:
                return "ending_memory_crash"

            if self.logic_chain_failed and self.logic_chain_success == 0:
                return "paranoia"

            if self.final_plan == "hesitate":
                return "endless_loop"

            truth_rules = ENDING_RULES["truth"]
            if self.final_plan == "assault" and all(flag in self.truth_flags for flag in truth_rules["requires_truth_flags"]):
                return "truth"

            escape_rules = ENDING_RULES["escape"]
            coordinated_assault = all(tag in self.allies for tag in escape_rules["requires_allies"])
            sabotage_ceasefire_path = (
                "technical" in self.allies
                and "pilot" in self.allies
                and "saboteur_ceasefire" in self.evidence
                and ("bridge_override_code" in self.evidence or "nav_core_reflashed" in self.evidence)
            )

            if self.final_plan == "assault" and self.alien_exposed and (coordinated_assault or sabotage_ceasefire_path):
                return "escape"

            alien_rules = ENDING_RULES["alien_victory"]
            if (not self.alien_exposed) and len(self.allies) <= alien_rules["max_allies"] and self.final_plan != "sacrifice":
                return "alien_victory"

            return "endless_loop"


    def pm_progress_marker_from_snapshot(snapshot):
        if not isinstance(snapshot, dict):
            return (-1, -1, -1, -1, -1, -1, -1)

        return (
            snapshot.get("loop_count", 0),
            snapshot.get("week_index", 0),
            len(snapshot.get("history", []) or []),
            len(snapshot.get("completed_quests", set()) or set()),
            len(snapshot.get("evidence", set()) or set()),
            len(snapshot.get("truth_flags", set()) or set()),
            len(snapshot.get("allies", set()) or set()),
        )


    def pm_sync_runtime_progress(reset=False):
        if "manifest_state" not in globals():
            return

        snapshot = manifest_state.export_progress_snapshot()

        if reset:
            persistent.pm_manifest_state_snapshot = snapshot
            renpy.save_persistent()
            return

        existing = getattr(persistent, "pm_manifest_state_snapshot", None)
        if existing is None or pm_progress_marker_from_snapshot(snapshot) >= pm_progress_marker_from_snapshot(existing):
            persistent.pm_manifest_state_snapshot = snapshot
            renpy.save_persistent()


    def pm_restore_runtime_progress():
        if "manifest_state" not in globals():
            return

        snapshot = getattr(persistent, "pm_manifest_state_snapshot", None)
        if not isinstance(snapshot, dict):
            return

        if pm_progress_marker_from_snapshot(snapshot) > manifest_state.progress_marker():
            manifest_state.import_progress_snapshot(snapshot)


    class NarrativeDirector(object):
        """
        Оркестратор сценария.
        Управляет недельными арками, гейтами улик и переходами к финалу.
        """
        WEEK_BEATS = {
            1: ["normal_flight", "minor_incidents", "black_hole_reveal", "ship_destruction"],
            2: ["deja_vu", "manifest_shift", "first_failed_bridge_attempt", "pilot_cabin_denied"],
            3: ["future_knowledge", "pilot_cabin_breakin", "autopilot_truth"],
            4: ["second_observer_hint", "paranoia_phase", "alien_hunt_start"],
            5: ["tech_deck_infiltration", "dead_pilots_reveal", "autopilot_truth"],
            6: ["ally_selection", "traitor_exposure", "bridge_assault", "final_choice"],
        }

        def __init__(self, state):
            self.state = state

        def current_week_beats(self):
            return self.WEEK_BEATS.get(self.state.week_index, [])


default manifest_state = ManifestState()
init python:
    config.after_load_callbacks.append(pm_restore_runtime_progress)
