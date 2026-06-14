import json
import os


def storage(files_hashes_dictionnary, dir_to_analyze) :

    json_name = f"baseline_{dir_to_analyze}"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, json_name)
    with open(path, "w") as file :
        json.dump(files_hashes_dictionnary, file, indent=4)