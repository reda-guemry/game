import pygame
from sys import exit

pygame.init()
pygame.display.set_caption("Player Game")

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

background = pygame.image.load('Python/img/background.png').convert()
background = pygame.transform.scale(background, (800, 600))

player_surface = pygame.image.load('Python/img/player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface, (90, 60))
player_rect = player_surface.get_rect(center=(400, 300))

box_surface = pygame.image.load('Python/img/box.png').convert_alpha()
box_surface = pygame.transform.scale(box_surface, (60, 40))

box_rects = [
    box_surface.get_rect(center=(600, 400)),
    box_surface.get_rect(center=(200, 400)),
    box_surface.get_rect(center=(400, 200)),
    box_surface.get_rect(center=(300, 500)),
    box_surface.get_rect(center=(500, 500)),
]

font = pygame.font.Font(None, 40)


# ================= MAIN LOOP =================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    dx, dy = 0, 0

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = 3
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -3
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -3
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = 3

    player_rect.x += dx
    
    if player_rect.left < 0: player_rect.left = 0
    if player_rect.right > 800: player_rect.right = 800

    for box in box_rects:
        if player_rect.colliderect(box):
            if dx > 0: box.left = player_rect.right
            if dx < 0: box.right = player_rect.left
            
            if box.left < 0: 
                box.left = 0
                player_rect.left = box.right
            if box.right > 800: 
                box.right = 800
                player_rect.right = box.left
                
            for other_box in box_rects:
                if box != other_box and box.colliderect(other_box):
                    if dx > 0: 
                        box.right = other_box.left
                        player_rect.right = box.left
                    if dx < 0: 
                        box.left = other_box.right
                        player_rect.left = box.right

    player_rect.y += dy
    
    if player_rect.top < 0: player_rect.top = 0
    if player_rect.bottom > 600: player_rect.bottom = 600

    for box in box_rects:
        if player_rect.colliderect(box):
            if dy > 0: box.top = player_rect.bottom
            if dy < 0: box.bottom = player_rect.top
            
            if box.top < 0: 
                box.top = 0
                player_rect.top = box.bottom
            if box.bottom > 600: 
                box.bottom = 600
                player_rect.bottom = box.top

            for other_box in box_rects:
                if box != other_box and box.colliderect(other_box):
                    if dy > 0: 
                        box.bottom = other_box.top
                        player_rect.bottom = box.top
                    if dy < 0: 
                        box.top = other_box.bottom
                        player_rect.top = box.bottom
      
    screen.blit(background, (0, 0))

    screen.blit(player_surface, player_rect)
    pygame.draw.rect(screen, (0, 255, 0), player_rect, 2)

    for box in box_rects:
        screen.blit(box_surface, box)
        pygame.draw.rect(screen, (255, 0, 0), box, 2)

    collision = any(player_rect.colliderect(box) for box in box_rects)

    if collision:
        text_surface = font.render("Collision Detected!", True, (255, 0, 0))
    else:
        text_surface = font.render("Hello World", True, (255, 255, 255))

    screen.blit(text_surface, (250, 50))

    pygame.display.update()
    clock.tick(60)