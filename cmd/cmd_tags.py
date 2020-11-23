import os
import configparser as cp
import operations as ops

cfg = cp.ConfigParser()
cfg.read("config.ini")

FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]


def tags_command(args):
    if len(args) < 1:
        return "Please specify type oftag as follows, you lvl2 lee sin tower diver:\n `tags [champ/item].`"
    if args[0].lower().startswith("champ"):
        filepath = os.path.join(FILES_DIRECTORY, "champion_tags.json")
    elif args[0].lower().startswith("item"):
        filepath = os.path.join(FILES_DIRECTORY, "item_tags.json")
    else:
        return "Invalid tag type. Please search by `[champ]` or `[item]`."

    data = ops.get_data(filepath)
    result = "```md\n"
    for tag in data["tags"]:
        result+=f"* {tag}\n"
    result+="```"
    return result
    