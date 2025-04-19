import json
import sys

def reformat_json(file_path, indent=4):
    """Reads a JSON file, reformats it with proper indentation, and overwrites it."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Load JSON data

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=indent)  # Overwrite with formatted JSON

        print(f"Reformatted JSON saved to {file_path}")
    except Exception as e:
        print(f"Error: {e}")


def updateJson(data, jsonfile):
    json.dump(data, open(jsonfile, 'w+'))

def identifyUsediles(data: dict, jsonoutput = None):
    tiles = data['tiledata']
    usedtiles = []
    unusedtiles=[]
    for tile in tiles:
        if 'bitstream' in tile.keys():
            rawbitstream = ''.join(tile['bitstream'])
            if '1' in rawbitstream:
                tile['used'] = True
                
                t = {}
                t['tiletype'] = tile['tiletype']
                if 'x' in tile.keys():
                    t['x'] = tile['x']
                if 'y' in tile.keys():
                    t['y'] = tile['y']
                usedtiles.append(t)
            else:
                tile['used'] = False
                
                t = {}
                t['tiletype'] = tile['tiletype']
                if 'x' in tile.keys():
                    t['x'] = tile['x']
                if 'y' in tile.keys():
                    t['y'] = tile['y']
                unusedtiles.append(t)
    newdata = data.copy()
    newdata['usedtiles'] = usedtiles
    newdata['unusedtiles'] = unusedtiles
    data = newdata
    if jsonoutput is not None:
        updateJson(data=newdata, jsonfile=jsonoutput)
        reformat_json(jsonoutput)
    return usedtiles, unusedtiles

if __name__ == '__main__':
    jsondata = json.load(open('output.json'))
    ret = identifyUsediles(jsondata, 'output1.json')
    print('used: ',ret[0])
    print('unused: ', ret[1])