import os
import configparser as cp
import operations as ops

cfg = cp.ConfigParser()
cfg.read("config.ini")

FILES_DIRECTORY = cfg["DEFAULT"]["files_directory"]


def items_command(args):
    if len(args) < 1:
        return "Please specify item tag(s) as follows, you uncultured swine:\n `items [tag1 tag2 tag3...]`"
    
    filepath = os.path.join(FILES_DIRECTORY, "items.json")
    data = ops.get_data(filepath)
    

    items = list(set([v["name"] for v in data.values()
        if ops.has_intersection(v["tags"], args)]))
    chunks = [items[x:x+25] for x in range(0, len(items),25)]
    
    results = []
    for items in chunks:
        result = "```md\n"
        for i in items:
            result+=f"* {i}\n"
        result+="```"
        results.append(result)
    return results
    