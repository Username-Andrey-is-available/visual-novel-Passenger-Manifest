init python:
    def pm_delete_all_saves():
        removed = 0

        for filename in renpy.list_saved_games(regexp=r"^(\d+|auto|quick)-\d+$", fast=True):
            renpy.unlink_save(filename)
            removed += 1

        renpy.restart_interaction()

        if removed:
            renpy.notify("Все сохранения удалены.")
        else:
            renpy.notify("Сохранений не найдено.")
