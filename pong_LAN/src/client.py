import pygame
from network import Network
from player import Player




def redrawWindow(player, player2, ball, field, win):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    ball.draw(win)
    field.draw(win)
    font_ = pygame.font.Font("dialog_font.ttf", 18)
    text = font_.render(f'{field.score}', False, (0, 0, 0))
    win.blit(text, (340, 10))
    pygame.display.update()
    
    
def main():
    run = True
    n = Network()
    pygame.font.init()
    width = 700
    height = 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Client")

    p = n.getp()
    clock= pygame.time.Clock()
    while run:
        clock.tick(60)
        p2, ball,field= n.send(p)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            n.send(True)
            
        p.move()      
        redrawWindow(p, p2, ball,field, win)
main()