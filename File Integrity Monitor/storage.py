import json


def storage(files_hashes_dictionnary, dir_to_analyze) :
    json_name = f"baseline_{dir_to_analyze}"
    with open(json_name, "w") as file :
        json.dump(files_hashes_dictionnary, file, indent=4)