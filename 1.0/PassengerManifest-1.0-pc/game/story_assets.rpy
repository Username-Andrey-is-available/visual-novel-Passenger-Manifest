init -6 python:
    # Future-proof asset map: the game keeps working with fallbacks until you add the files.
    STORY_VISUALS = {
        "black_hole_fall": "images/cg/black_hole_fall.png",
        "pilot_cabin_reveal": "images/cg/pilot_cabin_reveal.png",
        "mira_reveal": "images/cg/mira_reveal.png",
        "bridge_assault": "images/cg/bridge_assault.png",
        "escape_maneuver": "images/cg/escape_maneuver.png",
        "sacrifice_switch": "images/cg/sacrifice_switch.png",
        "loop_reset": "images/cg/loop_reset.png",
        "bridge_alert": "images/backgrounds/bridge_alert.png",
        "observation_anomaly": "images/backgrounds/observation_anomaly.png",
        "corridor_alert": "images/backgrounds/corridor_alert.png",
        "technical_alert": "images/backgrounds/technical_alert.png",
    }

    STORY_SFX = {
        "ui_confirm": "audio/sfx/ui/menu_confirm.mp3",
        "ui_back": "audio/sfx/ui/menu_back.ogg",
        "black_hole_fall": "audio/sfx/events/black_hole_fall.ogg",
        "loop_reset": "audio/sfx/events/loop_reset_hit.mp3",
        "dead_pilots_reveal": "audio/sfx/events/dead_pilots_reveal.mp3",
        "mira_reveal": "audio/sfx/events/mira_reveal.mp3",
        "captain_gunshots": "audio/sfx/events/captain_gunshots.mp3",
        "final_breach": "audio/sfx/events/final_breach.ogg",
        "light_flicker": "audio/sfx/ship/light_flicker.ogg",
        "deck_vibration": "audio/sfx/ship/deck_vibration.ogg",
        "metallic_impact": "audio/sfx/ship/metallic_impact.ogg",
        "airlock_open": "audio/sfx/ship/airlock_open.ogg",
        "alarm_short": "audio/sfx/ship/alarm_short.ogg",
        "ominous_hum": "audio/sfx/ship/ominous_hum.ogg",
        "lift_stop": "audio/sfx/ship/lift_stop.ogg",
        "drone_pass": "audio/sfx/ship/drone_pass.ogg",
    }

    def pm_story_image(key, fallback=None):
        path = STORY_VISUALS.get(key)
        if path and renpy.loadable(path):
            return path

        candidates = []

        if renpy.loadable(key):
            candidates.append(key)

        if "/" not in key:
            if "." in key:
                candidates.extend([
                    "images/cg/{}".format(key),
                    "images/backgrounds/{}".format(key),
                ])
            else:
                candidates.extend([
                    "images/cg/{}.png".format(key),
                    "images/backgrounds/{}.png".format(key),
                    "images/cg/{}".format(key),
                    "images/backgrounds/{}".format(key),
                ])

        for candidate in candidates:
            if renpy.loadable(candidate):
                return candidate

        if fallback:
            return fallback

        return key

    def pm_story_sfx(key, channel="sound", loop=False, relative_volume=1.0):
        path = STORY_SFX.get(key)
        if path and renpy.loadable(path):
            renpy.sound.play(
                path,
                channel=channel,
                loop=loop,
                relative_volume=relative_volume,
            )

    def pm_return_to_main_menu():
        renpy.full_restart(transition=config.end_game_transition)
