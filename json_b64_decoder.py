#!/usr/bin/env python3
import argparse
import base64
import json

from os import read
description = "json_b64_decoder - A basic base64 decoder for JSON where the key is plain text and the body is base64 encoded."

def get_key_values_from_json(file, key = None):
    read_file = open(file, 'r')
    json_file = json.load(read_file)

    return json_file[key] if (key is not None) else json_file

def decode_value(data):
    try:
        return base64.b64decode(data)
    except:
        return data
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-i', help="json file input", required=True, type=str)
    parser.add_argument('-k', help="specific key to decode", type=str)
    args = parser.parse_args()
    file = args.i
    key = args.k

    needed_json = get_key_values_from_json(file, key)
    json_keys = needed_json.keys()
    json_keys.sort()
    
    for k in json_keys:
        print(k + " :: " + decode_value(needed_json[k]))