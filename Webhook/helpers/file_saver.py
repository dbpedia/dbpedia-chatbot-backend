from datetime import datetime
import json

class file_saver():

    def __init__(self):
        print("File Saver initialized")

    def save_json(self, json_object):
        path = './' + datetime.now().strftime("%m-%d-%Y_%H-%M-%S") + '.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(json_object, f, ensure_ascii=False, indent=4)