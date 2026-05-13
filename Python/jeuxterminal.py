from pynput import keyboard
import os
import subprocess

pos = [1, 1]
boxes = [[2, 3], [5, 7], [7, 2], [8, 8], [1, 7]]
existences = [[6, 0], [6, 1], [6, 2], [6, 3]]
checkpoints = [[2, 1], [0, 9], [11, 0], [11, 9], [5, 5] ]

WIDTH = 10
HEIGHT = 12

def draw_map():
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

    if all(box in checkpoints for box in boxes):
        print("Congratulations! You've won the game!")
        return

    
    print("╔" + "══" * WIDTH + "╗")
    
    for y in range(HEIGHT):
        row_str = "║"
        for x in range(WIDTH):
            p = [y, x]
            if p == pos:
                char = " P"
            elif p in boxes:
                char = " □"
            elif p in existences:
                char = " █"
            elif p in checkpoints:
                char = ". "
            else:
                char = "  "
            row_str += char
        print(row_str + "║")
        
    print("╚" + "══" * WIDTH + "╝")
    print("\n[WASD / Arrows] Move  |  [ESC] Quit")

def move(dy, dx):
    new_p = [pos[0] + dy, pos[1] + dx]

    if not (0 <= new_p[0] < HEIGHT and 0 <= new_p[1] < WIDTH) or new_p in existences or new_p in checkpoints:
        return

    if new_p in boxes:
        new_box = [new_p[0] + dy, new_p[1] + dx]    
    

        if (0 <= new_box[0] < HEIGHT and 0 <= new_box[1] < WIDTH) and \
           new_box not in existences and new_box not in boxes:
            boxes.remove(new_p)
            boxes.append(new_box)

        # if the box in the checkpoint, remove it from the game
        elif new_p in checkpoints:
            boxes.remove(new_p) 
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
    if key == keyboard.Key.esc:
        return False

draw_map()
with keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True) as listener:
    listener.join()