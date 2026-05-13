import pygame
from sys import exit

pygame.init()
pygame.display.set_caption("Sokoban Mystery Game")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
win_font = pygame.font.Font(None, 80)

background = pygame.image.load('Python/img/background.png').convert()
background = pygame.transform.scale(background, (800, 600))

player_original = pygame.image.load('Python/img/player.png').convert_alpha()
player_original = pygame.transform.scale(player_original, (70, 40))
player_rect = player_original.get_rect(center=(400, 150))
current_player_surface = player_original 

box_surface = pygame.image.load('Python/img/box.png').convert_alpha()
box_surface = pygame.transform.scale(box_surface, (60, 40))

wall_surface = pygame.image.load('Python/img/wall.png').convert()
wall_surface = pygame.transform.scale(wall_surface, (200, 90))
wall_rect = wall_surface.get_rect(topleft=(300, 400)) 

hole_surface = pygame.image.load('Python/img/hole.png').convert_alpha()
hole_surface = pygame.transform.scale(hole_surface, (90, 60))

red_hole_surface = pygame.image.load('Python/img/hole_rouge.png').convert_alpha()
red_hole_surface = pygame.transform.scale(red_hole_surface, (90, 60))

box_rects = [
    box_surface.get_rect(center=(600, 400)),
    box_surface.get_rect(center=(250, 400)),
    box_surface.get_rect(center=(400, 100)),
    box_surface.get_rect(center=(350, 500)),
    box_surface.get_rect(center=(500, 500)),
]

holes = [
    hole_surface.get_rect(center=(100, 100)),
    hole_surface.get_rect(center=(700, 100)),
    hole_surface.get_rect(center=(100, 500)),
    hole_surface.get_rect(center=(700, 500)),
    hole_surface.get_rect(center=(400, 300)),
]

filled_holes = [] 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    speed = 3

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = speed
        current_player_surface = pygame.transform.rotate(player_original, -90)
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -speed
        current_player_surface = pygame.transform.rotate(player_original, 90)
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -speed
        current_player_surface = pygame.transform.rotate(player_original, 0)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = speed
        current_player_surface = pygame.transform.rotate(player_original, 180)

    player_rect.x += dx
    
    if player_rect.left < 0: player_rect.left = 0
    if player_rect.right > 800: player_rect.right = 800
    
    if player_rect.colliderect(wall_rect):
        if dx > 0: player_rect.right = wall_rect.left
        if dx < -0: player_rect.left = wall_rect.right

    for box in box_rects:
        if player_rect.colliderect(box):
            if dx > 0: box.left = player_rect.right
            if dx < 0: box.right = player_rect.left
            
            if box.left < 0: box.left = 0; player_rect.left = box.right
            if box.right > 800: box.right = 800; player_rect.right = box.left
                
            if box.colliderect(wall_rect):
                if dx > 0: box.right = wall_rect.left; player_rect.right = box.left
                if dx < 0: box.left = wall_rect.right; player_rect.left = box.right
                
            for other in box_rects:
                if box != other and box.colliderect(other):
                    if dx > 0: box.right = other.left; player_rect.right = box.left
                    if dx < 0: box.left = other.right; player_rect.left = box.right

    player_rect.y += dy
    
    if player_rect.top < 0: player_rect.top = 0
    if player_rect.bottom > 600: player_rect.bottom = 600

    if player_rect.colliderect(wall_rect):
        if dy > 0: player_rect.bottom = wall_rect.top
        if dy < 0: player_rect.top = wall_rect.bottom

    for box in box_rects:
        if player_rect.colliderect(box):
            if dy > 0: box.top = player_rect.bottom
            if dy < 0: box.bottom = player_rect.top
            
            if box.top < 0: box.top = 0; player_rect.top = box.bottom
            if box.bottom > 600: box.bottom = 600; player_rect.bottom = box.top

            if box.colliderect(wall_rect):
                if dy > 0: box.bottom = wall_rect.top; player_rect.bottom = box.top
                if dy < 0: box.top = wall_rect.bottom; player_rect.top = box.bottom

            for other in box_rects:
                if box != other and box.colliderect(other):
                    if dy > 0: box.bottom = other.top; player_rect.bottom = box.top
                    if dy < 0: box.top = other.bottom; player_rect.top = box.bottom

    for box in box_rects[:]:
        for hole in holes:
            if hole not in filled_holes:
                if abs(box.centerx - hole.centerx) < 15 and abs(box.centery - hole.centery) < 15:
                    box_rects.remove(box)
                    filled_holes.append(hole)

    screen.blit(background, (0, 0))
    
    for hole in holes:
        if hole in filled_holes:
            screen.blit(red_hole_surface, hole)
        else:
            screen.blit(hole_surface, hole)

    screen.blit(wall_surface, wall_rect)
    screen.blit(current_player_surface, player_rect)

    for box in box_rects:
        screen.blit(box_surface, box)

    pygame.draw.rect(screen, (0, 0, 0), player_rect, 2)

    text = font.render(f"Holes Filled: {len(filled_holes)}/{len(holes)}", True, (255, 255, 255))    
	

    for hole in holes:
        pygame.draw.rect(screen, (0, 0, 0), hole.inflate(10, 10), 2)

    for box in box_rects:
        pygame.draw.rect(screen, (0, 0, 0), box.inflate(10, 10), 2)

    if len(filled_holes) == len(holes):
        win_text = win_font.render("YOU WIN!", True, (0, 255, 0))
        text_rect = win_text.get_rect(center=(400, 300))
        pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(30, 30))
        screen.blit(win_text, text_rect)

    pygame.display.update()
    clock.tick(60)