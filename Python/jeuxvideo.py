import pygame
from sys import exit

pygame.init()
pygame.display.set_caption("Sokoban Mystery Game - Numbers Edition")

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
win_font = pygame.font.Font(None, 80)

bg_tile = pygame.image.load('Python/img/background.png').convert()
background = pygame.Surface((800, 600))
for x in range(0, 800, 64):
    for y in range(0, 600, 64):
        background.blit(bg_tile, (x, y))

player_sheet = pygame.image.load('Python/img/player.png').convert_alpha()
player_frames = []
for i in range(11):
    frame = player_sheet.subsurface(pygame.Rect(i * 32, 0, 32, 32))
    player_frames.append(pygame.transform.scale(frame, (50, 40)))

player_images = {
    'right': player_frames[0],
    'left': pygame.transform.flip(player_frames[0], True, False),
}

player_rect = pygame.Rect(400, 150, 50, 50)
current_player_surface = player_images['right']

box_surface = pygame.image.load('Python/img/box.png').convert_alpha()
box_surface = pygame.transform.scale(box_surface, (50, 50))

wall_tile = pygame.image.load('Python/img/wall.png').convert()  
wall_surface = pygame.Surface((200, 90))
for x in range(0, 200, 16):
    for y in range(0, 90, 16):
        wall_surface.blit(wall_tile, (x, y))
wall_rect = wall_surface.get_rect(topleft=(300, 400))

hole_sheet = pygame.image.load('Python/img/hole.png').convert_alpha()  
hole_surface = pygame.transform.scale(hole_sheet.subsurface(pygame.Rect(0, 0, 48, 48)), (60, 60))

red_hole_sheet = pygame.image.load('Python/img/hole_rouge.png').convert_alpha()  
red_hole_surface = pygame.transform.scale(red_hole_sheet.subsurface(pygame.Rect(0, 0, 48, 48)), (60, 60))

box_positions = [(600, 400), (250, 400), (400, 100), (350, 230), (600, 300)]
hole_positions = [(100, 100), (700, 100), (100, 500), (700, 500), (400, 300)]
numbers = [1, 2, 3, 4, 5]

boxes = []
for i in range(5):
    boxes.append({'rect': box_surface.get_rect(center=box_positions[i]), 'num': numbers[i]})

holes = []
for i in range(5):
    holes.append({'rect': hole_surface.get_rect(center=hole_positions[i]), 'num': numbers[i]})

filled_holes = []

def can_move_box(current_box, dx, dy, all_boxes):
    temp_rect = current_box.copy()
    temp_rect.x += dx
    temp_rect.y += dy
    
    if temp_rect.colliderect(wall_rect): return False
    if temp_rect.left < 0 or temp_rect.right > 800 or temp_rect.top < 0 or temp_rect.bottom > 600: return False
    
    for other in all_boxes:
        if current_box != other['rect'] and temp_rect.colliderect(other['rect']):
            return False
    return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    speed = 3

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx, current_player_surface = speed, player_images['right']
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx, current_player_surface = -speed, player_images['left']
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = speed

    shift_pressed = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
    prev_player_rect = player_rect.copy()

    player_rect.x += dx

    if player_rect.left < 0: player_rect.left = 0
    if player_rect.right > 800: player_rect.right = 800

    if player_rect.colliderect(wall_rect):
        if dx > 0: player_rect.right = wall_rect.left
        elif dx < 0: player_rect.left = wall_rect.right

    colliding_boxes_x = [b for b in boxes if player_rect.colliderect(b['rect'])]
    
    if len(colliding_boxes_x) > 1:
        if dx > 0: player_rect.right = colliding_boxes_x[0]['rect'].left 
        elif dx < 0: player_rect.left = colliding_boxes_x[0]['rect'].right
    else:
        for b in colliding_boxes_x:
            if can_move_box(b['rect'], dx, 0, boxes):
                if dx > 0: b['rect'].left = player_rect.right
                elif dx < 0: b['rect'].right = player_rect.left
            else:
                if dx > 0: player_rect.right = b['rect'].left
                elif dx < 0: player_rect.left = b['rect'].right

    actual_dx = player_rect.x - prev_player_rect.x
    if shift_pressed and actual_dx != 0 and len(colliding_boxes_x) == 0:
        for b in boxes:
            same_row = b['rect'].bottom > prev_player_rect.top and b['rect'].top < prev_player_rect.bottom
            if actual_dx > 0:
                behind = abs(b['rect'].right - prev_player_rect.left) <= abs(actual_dx)
            else:
                behind = abs(b['rect'].left - prev_player_rect.right) <= abs(actual_dx)
            if same_row and behind and can_move_box(b['rect'], actual_dx, 0, boxes):
                b['rect'].x += actual_dx
                break

    prev_player_rect_y = player_rect.copy()
    player_rect.y += dy

    if player_rect.top < 0: player_rect.top = 0
    if player_rect.bottom > 600: player_rect.bottom = 600

    if player_rect.colliderect(wall_rect):
        if dy > 0: player_rect.bottom = wall_rect.top
        elif dy < 0: player_rect.top = wall_rect.bottom

    colliding_boxes_y = [b for b in boxes if player_rect.colliderect(b['rect'])]

    if len(colliding_boxes_y) > 1:
        if dy > 0: player_rect.bottom = colliding_boxes_y[0]['rect'].top 
        elif dy < 0: player_rect.top = colliding_boxes_y[0]['rect'].bottom
    else:
        for b in boxes:
            if player_rect.colliderect(b['rect']):
                if can_move_box(b['rect'], 0, dy, boxes):
                    if dy > 0: b['rect'].top = player_rect.bottom
                    elif dy < 0: b['rect'].bottom = player_rect.top
                else:
                    if dy > 0: player_rect.bottom = b['rect'].top
                    elif dy < 0: player_rect.top = b['rect'].bottom 

    actual_dy = player_rect.y - prev_player_rect_y.y
    if shift_pressed and actual_dy != 0 and len(colliding_boxes_y) == 0:
        for b in boxes:
            same_col = b['rect'].right > prev_player_rect_y.left and b['rect'].left < prev_player_rect_y.right
            if actual_dy > 0:
                behind = abs(b['rect'].bottom - prev_player_rect_y.top) <= abs(actual_dy)
            else:
                behind = abs(b['rect'].top - prev_player_rect_y.bottom) <= abs(actual_dy)
            if same_col and behind and can_move_box(b['rect'], 0, actual_dy, boxes):
                b['rect'].y += actual_dy
                break
        
    for b in boxes[:]:
        for h in holes:
            if h['rect'] not in filled_holes:
                if abs(b['rect'].centerx - h['rect'].centerx) < 20 and abs(b['rect'].centery - h['rect'].centery) < 20:
                    if b['num'] == h['num']:
                        boxes.remove(b)
                        filled_holes.append(h['rect'])
                        break

    screen.blit(background, (0, 0))
    for h in holes:
        if h['rect'] in filled_holes:
            screen.blit(red_hole_surface, h['rect'])
        else:
            screen.blit(hole_surface, h['rect'])
        h_num = font.render(str(h['num']), True, (0, 0, 0))
        screen.blit(h_num, h_num.get_rect(center=h['rect'].center))

    screen.blit(wall_surface, wall_rect)

    for b in boxes:
        screen.blit(box_surface, b['rect'])
        b_num = font.render(str(b['num']), True, (0, 0, 0))
        screen.blit(b_num, b_num.get_rect(center=b['rect'].center))
    
    screen.blit(current_player_surface, player_rect)

    if len(filled_holes) == len(holes):
        win_text = win_font.render("YOU WIN!", True, (0, 255, 0))
        tr = win_text.get_rect(center=(400, 300))
        pygame.draw.rect(screen, (0, 0, 0), tr.inflate(30, 30))
        screen.blit(win_text, tr)

    pygame.draw.rect(screen, (0, 0, 0), wall_rect.inflate(4, 4), 2) 
    pygame.draw.rect(screen, (0, 0, 0), player_rect.inflate(4, 4), 2)
    for b in boxes:
        pygame.draw.rect(screen, (0, 0, 0), b['rect'].inflate(4, 4), 2)
    for h in holes:
        pygame.draw.rect(screen, (0, 0, 0), h['rect'].inflate(4, 4), 2)

    pygame.display.update()
    clock.tick(60)