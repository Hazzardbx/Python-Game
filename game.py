import pygame
from pygame.locals import K_ESCAPE
from sys import exit

# Inicialização do Pygame
pygame.init()

# Inserir música
pygame.mixer.init()
pygame.mixer.music.load('super.mp3')
pygame.mixer.music.play(-1)

# Dicionário para armazenar os tipos de lixo e as imagens correspondentes
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

# Configuração da janela do jogo
screen = pygame.display.set_mode((1620, 1080))
pygame.display.set_caption('Trash_Trak')
clock = pygame.time.Clock()

# Definindo uma fonte
main_font = pygame.font.Font('font/SuperMario256.ttf', 30)

# Carregamento das imagens e definição dos objetos
bk_surface = pygame.image.load('graphics/bk.png')
icon = pygame.image.load('graphics/1.png')
text_surface = main_font.render('Find the hidden garbage', False, 'Brown')

mario_surface = pygame.image.load('graphics/2.png')
mario_original = mario_surface  # Armazena a imagem original
mario_rect = mario_surface.get_rect(topleft=(700, 500))
initial_mario_position = (700, 500)

# Lista para armazenar as imagens do lixo e suas posições
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

# Definindo uma fonte para a contagem regressiva
countdown_font = pygame.font.Font('font/SuperMario256.ttf', 100)

# Definindo o tempo inicial para a contagem regressiva
countdown_time = 3  # 3 segundos

# Loop de contagem regressiva
while countdown_time > 0:
    screen.fill((0, 0, 0))  # Preenche a tela com a cor preta

    # Renderiza o texto da contagem regressiva
    countdown_surface = countdown_font.render(str(countdown_time), False, 'White')
    screen.blit(countdown_surface, (800, 500))

    pygame.display.update()
    pygame.time.delay(1000)  # Aguarda 1 segundo
    countdown_time -= 1
    
# Variáveis para contar a quantidade de lixo apanhado
lixo_apanhado = 0

# Variável para armazenar a pontuação
score = 0

# Variável para a pontuação máxima
pontuacao_maxima = 11

# Defina uma velocidade inicial
speed = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario_rect.x -= speed
                # Inverte a imagem quando movendo para a esquerda
                mario_surface = pygame.transform.flip(mario_original, True, False)
            elif event.key == pygame.K_RIGHT:
                mario_rect.x += speed
                # Restaura a imagem original quando movendo para a direita
                mario_surface = mario_original
            elif event.key == pygame.K_UP:
                mario_rect.y -= speed
            elif event.key == pygame.K_DOWN:
                mario_rect.y += speed
                
            elif event.key == K_ESCAPE:  # Adicione esta verificação
                pygame.quit()
                exit()
 # Verifica se a pontuação atingiu a pontuação máxima
    if lixo_apanhado >= pontuacao_maxima:
        # Exibe a mensagem final
        final_surface = main_font.render("It's all clean!", False, 'Brown')
        screen.blit(final_surface, (580, 350))

        # Aguarda a entrada do jogador para reiniciar o jogo
        restart_surface = main_font.render("Press (R) to start again", False, 'White')
        screen.blit(restart_surface, (500, 500))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reinicia as variáveis
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

    # Garante que o Mario permanece dentro dos limites da tela
    mario_rect.x = max(0, min(mario_rect.x, 1620 - mario_rect.width))
    mario_rect.y = max(0, min(mario_rect.y, 1080 - mario_rect.height))

  # Verifica a colisão com o lixo e atualiza a pontuação
    for i, (image, position) in enumerate(images_and_rects):
        trash_rect = pygame.Rect(position, image.get_size())
        if mario_rect.colliderect(trash_rect) and lixo_apanhado <= len(images_and_rects):
            lixo_apanhado += 1
            score += 1
            print({lixo_apanhado})
            print(f"Score: {score}")
            images_and_rects[i] = (image, (-1000, -1000)) # Move o lixo fora da tela

    # Atualização da tela do jogo
    clock.tick(60)
    screen.blit(bk_surface, (0, 0))
    screen.blit(text_surface, (600, 200))
    
    score_surface = main_font.render(f"Score: {score}/{pontuacao_maxima}", False, 'White')
    screen.blit(score_surface, (10, 10))

    # Desenha as imagens do lixo
    for image, position in images_and_rects:
        rect = image.get_rect(topleft=position)
        screen.blit(image, rect.topleft)

    # Desenha o personagem principal
    screen.blit(mario_surface, mario_rect.topleft)
    
    

     # Verifica se a pontuação atingiu a pontuação máxima
    if lixo_apanhado >= pontuacao_maxima:
        # Exibe a mensagem final
        
        final_surface = main_font.render("Press (R) to start again/ to exit (ESC)", False, 'Brown')
        screen.blit(final_surface, (500, 350))
        

    pygame.display.set_icon(icon)
    pygame.display.update()


