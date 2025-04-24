import matplotlib.pyplot as plt
import matplotlib.patches as patches
import json

dark_colors = ['#1b1f3b', '#2e3a1f', '#3a1f2e', '#2f1f1f', '#1f2f2f', '#1f1f2f',
               '#2a2f1f', '#1f2f1f', '#2f1f2a', '#1f1f1f', '#2e1f1b', '#1b2e1f']

light_colors = ['#4c5a9d', '#7aa235', '#c061a0', '#e85a5a', '#5ad3d1', '#5a5ae8',
                 '#bcd35a', '#61e85a', '#e85ac2', '#bbbbbb', '#dd845a', '#5ae884']

def draw_colored_grid(tile_instructions):
    """
    Draws a grid where specific tiles are colored individually.

    Parameters:
        tile_instructions (list of tuples): Each tuple should be (x, y, color)
    """
    if not tile_instructions:
        print("No tiles to draw.")
        return

    # Determine grid bounds
    xs, ys = zip(*[(x, y) for x, y, _ in tile_instructions])
    max_x, max_y = max(xs), max(ys)

    # Setup plot
    fig, ax = plt.subplots(figsize=(max_x + 2, max_y + 2))

    # Draw tiles
    for x, y, color in tile_instructions:
        rect = patches.Rectangle((x, y), 1, 1, edgecolor='gray', facecolor=color)
        ax.add_patch(rect)

    # Draw full grid
    ax.set_xlim(0, max_x + 1)
    ax.set_ylim(0, max_y + 1)
    ax.set_aspect('equal')
    ax.set_xticks(range(max_x + 2))
    ax.set_yticks(range(max_y + 2))
    ax.grid(True)

    plt.title("Custom Tile Grid")
    plt.xlabel("X")
    plt.ylabel("Y")
    # plt.show()
    plt.savefig('fpga.png')
    print('finished drawing')

def assignColors(tile_types:list) -> dict:
    color = {}
    length = min(len(tile_types), len(dark_colors), len(light_colors))
    for i in range(length):
        color[tile_types[i]] = {'used':dark_colors[i], 'unused':light_colors[i]}
    return color
        
    
def drawFPGATiles(data):
    colors = assignColors(data['tile_types'])
    todraw = []
    for tile in data['usedtiles']:
        if 'x' in tile.keys() and 'y' in tile.keys() and 'tiletype' in tile.keys():
            x = int(tile['x'])
            y = int(tile['y'])
            tile_type = tile['tiletype']
            color = colors[tile_type]['used']
            todraw.append((x,y,color))
    for tile in data['unusedtiles']:
        if 'x' in tile.keys() and 'y' in tile.keys() and 'tiletype' in tile.keys():
            x = int(tile['x'])
            y = int(tile['y'])
            tile_type = tile['tiletype']
            color = colors[tile_type]['unused']
            todraw.append((x,y,color))
    draw_colored_grid(todraw)
# Example usage:
if __name__ == "__main__":
    jsondata = json.load(open('output1.json'))
    drawFPGATiles(jsondata)


