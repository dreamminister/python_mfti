# task url: https://www.coursera.org/learn/programming-in-python/programming/nc6Ce/key-value-khranilishchie

import argparse
import json
import os
import tempfile

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")
    args = parser.parse_args()
    return args.key, args.val

def get_storage_path():
    return os.path.join(tempfile.gettempdir(), 'storage.data')

def storage_exists():
    storage_path = get_storage_path()
    return os.path.exists(storage_path)

def load_storage(path):
    storage = {}
    content = ""
    with open(path, 'r') as file:
        content = file.read()
    storage = json.loads(content)
    return storage

def dump_storage(path, storage_obj):
    with open(path, 'w') as outfile:
        json.dump(storage_obj, outfile)

def update_storage(key:str, value:str, storage:dict, storage_path:str) -> None:
    if key not in storage:
        storage[key] = value
    else:
        values = storage[key]
        values_list = [value]
        if isinstance(values, str):
            values_list.append(values)
        else:
            values_list.extend(values)

        storage[key] = list(set(values_list))
    
    print(f"({key}, {value}) has been added")
    
    dump_storage(storage_path, storage)

def print_values_by_key(key:str, storage:dict, storage_path:str) -> None:
    if key not in storage:
        print('None')
    else:
        values = storage[key]

        if isinstance(values, str):
            print(values)
        else:
            print(", ".join(values))

if __name__ == "__main__":
    
    storage = { }
    storage_path = get_storage_path()
    #print(storage_path)

    if storage_exists():
        storage = load_storage(storage_path)

    key, value = get_args()
        
    if not key and not value:
        print(f"Bad args: {key}, {value}")

    elif key and value:
        update_storage(key, value, storage, storage_path)

    elif key and not value:
        print_values_by_key(key, storage, storage_path)