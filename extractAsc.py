import json

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

def extractASCFile(filename, outfile = 'output.json'):
    file = open(filename)
    asclines = file.readlines()
    
    ascdata = []
    tempdata = {}
    key = ''
    #loop through lines and record the data
    for line in asclines:
        if line[0] == '.':
            if len(tempdata) > 0: 
                ascdata.append(tempdata)
                tempdata = {}
            words = line.split()
            tempdata['tilename'] = words[0][1:]
            if(len(words)>1):
                tempdata['x'] = words[1]
            if(len(words)>2):    
                tempdata['y'] = words[2]
            tempdata['bitstream'] = []
        else:
            tempdata['bitstream'].append(line.strip())
    jsondata = {'ascdata': ascdata}
    with open(outfile, 'w+') as ofile:
        json.dump(jsondata, ofile)
    reformat_json(outfile)
    
if __name__ == '__main__':
    extractASCFile('blink182.asc')