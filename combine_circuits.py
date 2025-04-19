import sys
import json
from utils import reformat_json

def or_binary_strings(a: str, b: str) -> str:
    # Pad the shorter string with '0's on the left
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    return ''.join('1' if x == '1' or y == '1' else '0' for x, y in zip(a, b))

def replaceTileData(circuit, x, y, bitstream):
    for tile in circuit['tiledata']:
        if tile['x'] == x and tile['y'] == y:
            tile['bitstream'] = bitstream
            
def combine_via_or(circuit1json, circuit2json, newcircuitjson):
    circuit1 = json.load(open(circuit1json))
    circuit2 = json.load(open(circuit2json))
    newcircuit = circuit1.copy()
    num_tiles = len(circuit1['tiledata'])
    for tile in circuit1['tiledata']:
        for tile2 in circuit2['tiledata']:
            #if they are the same tile, then do stuff.
            if tile['x'] == tile2['x'] and tile['y'] == tile2['y']:
                # print('tile',tile)
                # print('tile2',tile2)
                num_lines = min(len(tile['bitstream']), len(tile2['bitstream']))
                newbitstream = []
                for i in range(num_lines):
                    newstring = or_binary_strings(tile['bitstream'][i], tile2['bitstream'][i])
                    newbitstream.append(newstring)
                replaceTileData(newcircuit, tile['x'], tile['y'], newbitstream)
    json.dump(newcircuit, open(newcircuitjson, 'w+'))
    reformat_json(newcircuitjson)
    

if len(sys.argv) < 4:
    raise ValueError("Not enough arguments")
combine_via_or(sys.argv[1], sys.argv[2], sys.argv[3])