from pynput import keyboard 
import os

pos = [0, 0]
boxes = [[2, 3], [5, 5], [7, 2], [8, 8], [1, 7]]
existences = [[6, 0], [6, 1], [6, 2], [6, 3]]

def draw_map():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(10):
        row = []
        for x in range(10):
            p = [y, x]
            if p == pos: row.append('P')
            elif p in boxes: row.append('B')
            elif p in existences: row.append('-')
            else: row.append(' ')
        print(" ".join(row))

def move(dy, dx):
    new_p = [pos[0] + dy, pos[1] + dx]

    if not (0 <= new_p[0] <= 9 and 0 <= new_p[1] <= 9) or new_p in existences:
        return

    if new_p in boxes:
        new_box = [new_p[0] + dy, new_p[1] + dx]
        
        if (0 <= new_box[0] <= 9 and 0 <= new_box[1] <= 9) and \
           new_box not in existences and new_box not in boxes:
            boxes.remove(new_p)
            boxes.append(new_box)
        else:
            return 

    pos[0], pos[1] = new_p[0], new_p[1]

def on_press(key):
    moves = {
        'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1),
        keyboard.Key.up: (-1, 0), keyboard.Key.down: (1, 0),
        keyboard.Key.left: (0, -1), keyboard.Key.right: (0, 1)
    }
    
    k = key.char if hasattr(key, 'char') else key
    if k in moves:
        dy, dx = moves[k]
        move(dy, dx)
        draw_map()

def on_release(key):
    if key == keyboard.Key.esc: return False

draw_map()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()






