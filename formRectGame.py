import pygame
import random

pygame.init()

screen_width= 600
screen_height= 400

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Giant Game")
clock = pygame.time.Clock()

player = pygame.Rect(0,40, 50,50)
player_distance = 10
score = 0
lives = 5

enemy = pygame.Rect(screen_width - 40,40, 15,15)
enemy_distance = 2
enemy_velocity = 0.5

def display_score():
    systemFonts= pygame.font.SysFont("impact", 30) #declaring font
    systemFonts = systemFonts.render(f"Score : {score}", True, "white") # render a font and text
    systemFontRect= systemFonts.get_rect()
    systemFontRect = (screen_width-systemFontRect.width, 0)
    screen.blit(systemFonts, systemFontRect)

def lives_text():
    livesFont=pygame.font.SysFont("impact", 30)
    livesFont = livesFont.render(f"Lives : {lives}", True, "white")
    livesFont_rect= livesFont.get_rect()
    livesFont_rect = (0, 0)
    screen.blit(livesFont, livesFont_rect)

def game_over_text():
    game_over=pygame.font.SysFont("impact", 70)
    game_over = game_over.render("GAME OVER", True, "darkred")
    game_over_rect= game_over.get_rect()
    game_over_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(game_over, game_over_rect)

def resume_playing():
    resume_continue=pygame.font.SysFont("arial", 20)
    resume_continue = resume_continue.render("Press 'space' to Continue", True, "darkred")
    resume_continue_rect= resume_continue.get_rect()
    resume_continue_rect.center = (screen_width / 2, screen_height / 2 + 40 )
    screen.blit(resume_continue, resume_continue_rect)

# def ending_game():

        
def draw():
    screen.fill("skyblue")
    pygame.draw.rect(screen, ("darkgreen"), player)
    pygame.draw.rect(screen, ("darkred"), enemy)

def player_move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_distance
    if keys[pygame.K_RIGHT] and player.x < 70:
        player.x += player_distance
    if keys[pygame.K_UP] and player.y > 40:
        player.y -= player_distance
    if keys[pygame.K_DOWN] and player.y < screen_height-player.height:
        player.y += player_distance

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    draw()
    lives_text()
    display_score()
    # enemy_move()
    player_move()

    # limit enemy on hiting x-axis
    if enemy.x < 0:
        enemy.x = screen_width + 100
        enemy.y = random.randint(40, screen_height - enemy.height)
        lives -= 1
        enemy_velocity -= 1
    else:
        enemy.x -= enemy_distance*enemy_velocity

    # collision check
    if enemy.colliderect(player):
        enemy.x = screen_width-enemy.width
        enemy.y = random.randint(40, screen_height - enemy.height)
        enemy_velocity += 1
        score += 1
    if lives == 0:
        enemy.x = 0
        enemy.y = 1000
        game_over_text()
        resume_playing()

        keyPress = pygame.key.get_pressed()
        if keyPress[pygame.K_SPACE]:
            lives = 6
            score = 0

    pygame.display.update()
    clock.tick(60)