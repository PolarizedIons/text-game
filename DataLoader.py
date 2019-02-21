from os import walk
from os import path
import json

DATA_DIR = './data'


def load():
    filenames = []
    for (_, _, filenames) in walk(path.join(DATA_DIR)):
        filenames.extend(filenames)
        break

    data = {}
    for file in set(filenames):
        loaded = loadfile(file)
        data[loaded['name']] = loaded
    
    return data



def loadfile(filename):
    with open(path.join(DATA_DIR, filename)) as f:
            print(f':: Loading {filename}')
            content = json.load(f)
    return normalize_file(content)

def normalize_file(file):
    normalized = {}
    
    normalized['name'] = get_key(file, 'name')
    
    normalized['navigation'] = {}
    for key, value in get_key(file, 'navigation').items():
        if type(value) == str:
            normalized['navigation'][key] = {
                'location': value
            }
        else:
            normalized['navigation'][key] = value
        
        if 'conditions' not in normalized['navigation'][key]:
            normalized['navigation'][key]['conditions'] = []
        
        if get_key(file, f'navigation.{key}.condition'):
            normalized['navigation'][key]['conditions'] = [get_key(file, f'navigation.{key}.condition')]
            normalized['navigation'][key].pop('condition')

    

    return normalized



def get_key(content, key):
    if type(content) != dict and (key or key not in content):
        return None
    key, *forward_key = key.split('.')
    content = content[key]

    if len(forward_key) == 0:
        return content
    
    return get_key(content, '.'.join(forward_key))


if __name__ == "__main__":
    print(load())