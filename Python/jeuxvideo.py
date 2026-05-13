import pygame 
from sys import exit

pygame.init()
pygame.display.set_caption("Player Game") 

screen = pygame.display.set_mode((800 , 600))
Clock = pygame.time.Clock()

test_surface = pygame.image.load('Python/img/background.png').convert()
test_surface = pygame.transform.scale(test_surface, (800, 600))

player_surface = pygame.image.load('Python/img/player.png').convert_alpha()
player_rect = player_surface.get_rect(center = (400, 300)) 

box_surface = pygame.image.load('Python/img/box.png').convert_alpha()
box_surface = pygame.transform.scale(box_surface, (60, 40))

box_rect = [
    box_surface.get_rect(center = (600, 400)), 
    box_surface.get_rect(center = (200, 400)),
    box_surface.get_rect(center = (400, 200)), 
    box_surface.get_rect(center = (300, 500)),
    box_surface.get_rect(center = (500, 500)), 
]

font = pygame.font.Font(None , 40)
debug_font = pygame.font.Font(None , 25)
text_surface = font.render("Hello World", True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                player_rect.x += 10
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: 
                player_rect.x -= 10
            if event.key == pygame.K_UP or event.key == pygame.K_w: 
                player_rect.y -= 10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                player_rect.y += 10

    screen.blit(test_surface, (0, 0))
    screen.blit(text_surface, (300, 50))
    
    screen.blit(player_surface, player_rect)
    pygame.draw.rect(screen, (0, 255, 0), player_rect, 2)

    for box in box_rect:
        screen.blit(box_surface, box)
        pygame.draw.rect(screen, (255, 0, 0), box, 2)
        
        size_text = debug_font.render(f"{box.width}x{box.height}", True, (255, 255, 0))
        screen.blit(size_text, (box.x, box.y - 20))

    collision = False
    for box in box_rect:
        if player_rect.colliderect(box):
            collision = True
            break
            
    if collision:
        text_surface = font.render("Collision Detected!", True, (255, 0, 0))
    else:
        text_surface = font.render("Hello World", True, (255, 255, 255))

    pygame.display.update()
    Clock.tick(60)