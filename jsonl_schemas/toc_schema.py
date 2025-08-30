import json

def save_jsonl(filepath, data_list):
    with open(filepath, "w", encoding="utf-8") as f:
        for item in data_list:
            json.dump(item, f)
            f.write("\n")
