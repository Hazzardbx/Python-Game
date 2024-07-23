import pygame
from pygame.locals import K_ESCAPE
from sys import exit

# Initialize Pygame
pygame.init()

# Insert music
pygame.mixer.init()
pygame.mixer.music.load('super.mp3')
pygame.mixer.music.play(-1)

# Library to store the types of trash and their corresponding 
lixo_dict = {
    "lata": pygame.transform.scale(pygame.image.load('graphics/lata.png'), (60, 70)),
    "lata1": pygame.transform.scale(pygame.image.load('graphics/lata1.png'), (60, 70)),
    "garrafa": pygame.transform.scale(pygame.image.load('graphics/garrafa.png'), (60, 70)),
    "maca": pygame.transform.scale(pygame.image.load('graphics/maca.png'), (60, 70)),
    "papel1": pygame.transform.scale(pygame.image.load('graphics/papel1.png'), (50, 60)),
    "banana": pygame.transform.scale(pygame.image.load('graphics/banana.png'), (60, 70)),
    "ovo": pygame.transform.scale(pygame.image.load('graphics/ovo.png'), (60, 70)),
    "garrafa1": pygame.transform.scale(pygame.image.load('graphics/garrafa1.png'), (60, 70)),
    "papel": pygame.transform.scale(pygame.image.load('graphics/papel.png'), (50, 50)),
    "sumo": pygame.transform.scale(pygame.image.load('graphics/sumo.png'), (50, 60)),
    "papel2": pygame.transform.scale(pygame.image.load('graphics/papel2.png'), (70, 60)),
}

# Game config window
screen = pygame.display.set_mode((1620, 1080))
pygame.display.set_caption('Trash_Trak')
clock = pygame.time.Clock()

# Defining font
main_font = pygame.font.Font('font/SuperMario256.ttf', 30)

#  Loading images and objects definitions
bk_surface = pygame.image.load('graphics/bk.png')
icon = pygame.image.load('graphics/1.png')
text_surface = main_font.render('Find the hidden garbage', False, 'Brown')

mario_surface = pygame.image.load('graphics/2.png')
mario_original = mario_surface  # Armazena a imagem original
mario_rect = mario_surface.get_rect(topleft=(700, 500))
initial_mario_position = (700, 500)

# List to store "trash" pictures and their positions
images_and_rects = [
    (lixo_dict["lata"], (550, 700)),
    (lixo_dict["lata1"], (200, 650)),
    (lixo_dict["garrafa"], (1400, 100)),
    (lixo_dict["maca"], (200, 230)),
    (lixo_dict["papel1"], (1200, 700)),
    (lixo_dict["banana"], (600, 920)),
    (lixo_dict["ovo"], (980, 930)),
    (lixo_dict["garrafa1"], (150, 840)),
    (lixo_dict["papel"], (500, 450)),
    (lixo_dict["sumo"], (1510, 820)),
    (lixo_dict["papel2"], (1300, 900))
]

# Defining font for "countdown"
countdown_font = pygame.font.Font('font/SuperMario256.ttf', 100)

# Definining starting point(time) for countdown
countdown_time = 3  # 3 secs

# Loop de contagem regressiva
while countdown_time > 0:
    screen.fill((0, 0, 0))  # Fills screen with black color

    # Render countdown text
    countdown_surface = countdown_font.render(str(countdown_time), False, 'White')
    screen.blit(countdown_surface, (800, 500))

    pygame.display.update()
    pygame.time.delay(1000)  # Holds 1second
    countdown_time -= 1
    
# Variable to count acquired trash number
lixo_apanhado = 0

# Variable for the score
score = 0

# Variable for maximum score
pontuacao_maxima = 11

# Define starting velocity
speed = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario_rect.x -= speed
                # Inverts image when moving left
                mario_surface = pygame.transform.flip(mario_original, True, False)
            elif event.key == pygame.K_RIGHT:
                mario_rect.x += speed
                # Restores image to default (right) when moving back to the right side
                mario_surface = mario_original
            elif event.key == pygame.K_UP:
                mario_rect.y -= speed
            elif event.key == pygame.K_DOWN:
                mario_rect.y += speed
                
            elif event.key == K_ESCAPE: 
                pygame.quit()
                exit()
 # Checks if maximum score was reached
    if lixo_apanhado >= pontuacao_maxima:
        # Shows ending message
        final_surface = main_font.render("It's all clean!", False, 'Brown')
        screen.blit(final_surface, (580, 350))

        # Awaits player "trigger" to start game again
        restart_surface = main_font.render("Press (R) to start again", False, 'White')
        screen.blit(restart_surface, (500, 500))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Restarts variables
            lixo_apanhado = 0
            score = 0
            mario_rect.topleft = initial_mario_position
            
            images_and_rects = [
    (lixo_dict["lata"], (550, 700)),
    (lixo_dict["lata1"], (200, 650)),
    (lixo_dict["garrafa"], (1400, 100)),
    (lixo_dict["maca"], (200, 230)),
    (lixo_dict["papel1"], (1200, 700)),
    (lixo_dict["banana"], (600, 920)),
    (lixo_dict["ovo"], (980, 930)),
    (lixo_dict["garrafa1"], (150, 840)),
    (lixo_dict["papel"], (500, 450)),
    (lixo_dict["sumo"], (1510, 820)),
    (lixo_dict["papel2"], (1300, 900))
]

    # Sets limit for the character not to go through the window's limits
    mario_rect.x = max(0, min(mario_rect.x, 1620 - mario_rect.width))
    mario_rect.y = max(0, min(mario_rect.y, 1080 - mario_rect.height))

  # Checks colision with trash to update score
    for i, (image, position) in enumerate(images_and_rects):
        trash_rect = pygame.Rect(position, image.get_size())
        if mario_rect.colliderect(trash_rect) and lixo_apanhado <= len(images_and_rects):
            lixo_apanhado += 1
            score += 1
            print({lixo_apanhado})
            print(f"Score: {score}")
            images_and_rects[i] = (image, (-1000, -1000)) # Move o lixo fora da tela

    # Refreshes game window
    clock.tick(60)
    screen.blit(bk_surface, (0, 0))
    screen.blit(text_surface, (600, 200))
    
    score_surface = main_font.render(f"Score: {score}/{pontuacao_maxima}", False, 'White')
    screen.blit(score_surface, (10, 10))

    # Draws trash images
    for image, position in images_and_rects:
        rect = image.get_rect(topleft=position)
        screen.blit(image, rect.topleft)

    # Draws main character
    screen.blit(mario_surface, mario_rect.topleft)
    
    

     # Checks if maximum score was reached
    if lixo_apanhado >= pontuacao_maxima:
        # Shows end game message
        
        final_surface = main_font.render("Press (R) to start again/ to exit (ESC)", False, 'Brown')
        screen.blit(final_surface, (500, 350))
        

    pygame.display.set_icon(icon)
    pygame.display.update()


