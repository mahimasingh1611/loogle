import os
import re
config = {}
config["debug_level"] = "INFO"

def read_config(filename,delimiter):
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "" or re.findall("^#" , line):
                continue
            parts=line.split(delimiter, 1)
            key = parts[0].strip();
            value = parts[1].strip();
            if (key == "dirpath" or key == "filepath") :
                if config.get(key) is None:
                    config[key] = []
                config[key].append(value)
            else:
                config[key] = value

def collate_all_files():
    config["list_of_files"] = [];
    for dirpath in config["dirpath"]:
        dir_list = os.listdir(dirpath)
        for filepath in dir_list:
            config["list_of_files"].append(filepath)

def indexfiles():
    for f in config["list_of_files"]:
        print("indexing file: " + f)



filename = 'config.cfg'  
delimiter = ':'
read_config(filename, delimiter)
collate_all_files()
print(config)
indexfiles()
