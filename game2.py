import pygame

pygame.init()
screen_width= 600
screen_height=500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("You welcome on my Game")
runing= True

def display_text():
    systemFonts= pygame.font.SysFont("impact", 30) #declaring font
    systemFonts = systemFonts.render("RectGame", True, "black", "orange") # render a font and text
    systemFontRect= systemFonts.get_rect()
    systemFontRect = (screen_width / 2, screen_height / 2)
    screen.blit(systemFonts, systemFontRect)

while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display_text()
    pygame.display.update()
    