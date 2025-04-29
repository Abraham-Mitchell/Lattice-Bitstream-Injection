import json
import sys

def get_tile_by_coordinates(tiledata, x, y):
    x, y = str(x), str(y)  # ensure both are strings
    for tile in tiledata:
        if tile.get("x") == x and tile.get("y") == y:
            return tile
    return None


def json2asc(infile, outfile):
    circuit = json.load(open(infile))
    lines = []
    lines.append('.comment')
    for device_line in circuit['device']:
        lines.append(device_line.strip())
        
    y_is_valid = True
    y = 0
    while(y_is_valid and y<100):
        x_is_valid = True
        x = 0
        while(x_is_valid and x<100):
            tile = get_tile_by_coordinates(circuit['tiledata'], x, y)
            if tile is not None:
                lines.append('.'+str(tile['tiletype']) + ' ' + str(x) + ' ' + str(y))
                for bitline in tile['bitstream']:
                    lines.append(bitline)
                lines.append('\n')
            x+=1
        y += 1
        
    for sym_line in circuit['symdata']:
        lines.append(sym_line)        
    out = open(outfile, 'w+')
    finallines = '\n'.join(lines)
    out.write(finallines)
    

    
# json2asc('combined.json', 'combined.asc')
if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise ValueError("not enough arguments")
    json2asc(sys.argv[1], sys.argv[2])
