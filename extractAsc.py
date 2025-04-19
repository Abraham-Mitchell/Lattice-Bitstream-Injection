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

def processSymData(line, data:list) -> None:
    dataentry = {}
    words = line.split()
    if len(words) > 1:
        dataentry['number'] =  words[1]
        if len(words) > 2:
            dataentry['value'] = words[2]
            data.append(dataentry)
    return
    
def extractASCFile(filename, outfile = 'output.json'):
    file = open(filename)
    asclines = file.readlines()
    
    tiledata = []
    symdata = []
    comments = []
    device = []
    tile_types = []
    tempdata = {}
    key = ''
    #loop through lines and record the data
    for line in asclines:
        if '.sym' in line:
            processSymData(line, symdata)
            continue
        if '.comment' in line:
            comments.append(line)
            continue
        if '.device' in line:
            device.append(line)
            continue
        if line[0] == '.':
            if len(tempdata) > 0: 
                tiledata.append(tempdata)
                tempdata = {}
            words = line.split()
            tempdata['tiletype'] = words[0][1:]
            if tempdata['tiletype'] not in tile_types:
                tile_types.append(tempdata['tiletype'])
            if(len(words)>1):
                tempdata['x'] = words[1]
            if(len(words)>2):    
                tempdata['y'] = words[2]
            tempdata['bitstream'] = []
        else:
            tempdata['bitstream'].append(line.strip())
    jsondata = {'tiledata': tiledata, 'symdata':symdata, 'tile_types':tile_types}
    with open(outfile, 'w+') as ofile:
        json.dump(jsondata, ofile)
    reformat_json(outfile)
    
if __name__ == '__main__':
    # extractASCFile('blink182.asc')
    print(sys.argv)
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
        if len(sys.argv) > 2:
            extractASCFile(inputfile, outfile=sys.argv[2])
        else:
            extractASCFile(inputfile)