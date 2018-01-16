import pygame

DISPLAY = (800, 1000)
RIVER_WIDTH = 400
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
CHARACTER_SIZE = 40
GREY = (122, 122, 122)
YELLOW = (122,255,0)
ORANGE = (255,122,0)

def MC():
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface_M = myfont.render('M', False, RED)
    textsurface_C = myfont.render('C', False, RED)
    # print(DISPLAY[0]/2-RIVER_WIDTH/2,0,DISPLAY[0]/2+RIVER_WIDTH/2,DISPLAY[1])
    gameDisplay = pygame.display.set_mode(DISPLAY)

    no_of_missionaries = 3
    no_of_cannibals = 3
    mouse_pressed = False
    river_crossed = False
    boat_load = []
    boatM = 0
    boatC = 0
    break_flag = False
    gamePlay = True
    while (True):
        gameDisplay.fill(YELLOW)
        mouse_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break_flag = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = True
        if break_flag == True:
            break
        pygame.display.set_caption("Missionaries and Cannibal")

        gameDisplay.fill(BLUE, rect=(DISPLAY[0] // 2 - RIVER_WIDTH // 2, 0, RIVER_WIDTH, DISPLAY[1]))
        #     pygame.draw.circle(gameDisplay,(255,0,0),(20,20),20)



        for i in range(no_of_missionaries-(not river_crossed)*boatM):
            rect = pygame.draw.rect(gameDisplay, ORANGE,(RIVER_WIDTH / 4, DISPLAY[1] / 4 + 2 * i * CHARACTER_SIZE, CHARACTER_SIZE, CHARACTER_SIZE))
            gameDisplay.blit(textsurface_M, (RIVER_WIDTH / 4, DISPLAY[1] / 4 + 2 * i * CHARACTER_SIZE))
            if mouse_pressed == True and len(boat_load)<2 and river_crossed == False and gamePlay:
                if rect.collidepoint(mouse_pos):
                    boatM+=1
                    boat_load.append('M')


        for i in range(no_of_cannibals-(not river_crossed)*boatC):
            rect = pygame.draw.rect(gameDisplay, BLACK, (RIVER_WIDTH / 4, DISPLAY[1] / 4 + 2 * i * CHARACTER_SIZE + 8 * CHARACTER_SIZE, CHARACTER_SIZE, CHARACTER_SIZE))
            gameDisplay.blit(textsurface_C, (RIVER_WIDTH / 4, DISPLAY[1] / 4 + 2 * i * CHARACTER_SIZE + 8 * CHARACTER_SIZE))
            if mouse_pressed == True and len(boat_load)<2 and river_crossed == False and gamePlay:

                if rect.collidepoint(mouse_pos):
                    boat_load.append('C')
                    boatC+=1


        for i in range(3 - no_of_missionaries - river_crossed*boatM):
            rect = pygame.draw.rect(gameDisplay, ORANGE, (DISPLAY[0] - RIVER_WIDTH / 4 - CHARACTER_SIZE, DISPLAY[1] / 4 + 2 * i * CHARACTER_SIZE, CHARACTER_SIZE, CHARACTER_SIZE))
            gameDisplay.blit(textsurface_M, (DISPLAY[0] - RIVER_WIDTH / 4 - CHARACTER_SIZE, DISPLAY[1] / 4 + 2 * i * CHARACTER_SIZE))
            if mouse_pressed == True and len(boat_load)<2 and river_crossed and gamePlay:
                if rect.collidepoint(mouse_pos):
                    boatM+=1
                    boat_load.append('M')


        for i in range(3 - no_of_cannibals - river_crossed*boatC):
            rect = pygame.draw.rect(gameDisplay, BLACK, (DISPLAY[0] - RIVER_WIDTH / 4 - CHARACTER_SIZE, DISPLAY[1] / 4 + 2 * i * CHARACTER_SIZE + 8 * CHARACTER_SIZE,CHARACTER_SIZE, CHARACTER_SIZE))
            gameDisplay.blit(textsurface_C, (DISPLAY[0] - RIVER_WIDTH / 4 - CHARACTER_SIZE, DISPLAY[1] / 4 + 2 * i * CHARACTER_SIZE + 8 * CHARACTER_SIZE))
            if mouse_pressed == True and len(boat_load)<2 and river_crossed and gamePlay:
                if rect.collidepoint(mouse_pos):
                    boat_load.append('C')
                    boatC=1
        count = 0
        removed = False
        if river_crossed == False:
            boat_rect = pygame.draw.rect(gameDisplay, GREY, (RIVER_WIDTH / 2,DISPLAY[1]/2-CHARACTER_SIZE, CHARACTER_SIZE, 4*CHARACTER_SIZE))
            for i in boat_load:
                print(i)
                if i == 'M':
                    rect = pygame.draw.rect(gameDisplay, ORANGE, (RIVER_WIDTH / 2, DISPLAY[1] / 2 -CHARACTER_SIZE+ 3*count*CHARACTER_SIZE, CHARACTER_SIZE,CHARACTER_SIZE))
                    gameDisplay.blit(textsurface_M, (RIVER_WIDTH / 2, DISPLAY[1] / 2 -CHARACTER_SIZE+ 3*count*CHARACTER_SIZE))
                    if mouse_pressed == True and gamePlay:
                        if rect.collidepoint(mouse_pos):
                            boatM-=1
                            boat_load.pop(count)
                            removed = True

                else:
                    rect = pygame.draw.rect(gameDisplay, BLACK, (RIVER_WIDTH / 2, DISPLAY[1] / 2 -CHARACTER_SIZE+ 3*count*CHARACTER_SIZE,CHARACTER_SIZE, CHARACTER_SIZE))
                    gameDisplay.blit(textsurface_C, (RIVER_WIDTH / 2, DISPLAY[1] / 2 -CHARACTER_SIZE+ 3*count*CHARACTER_SIZE))
                    if mouse_pressed == True and gamePlay:
                        if rect.collidepoint(mouse_pos) and gamePlay:
                            boatC-=1
                            boat_load.pop(count)
                            removed = True

                count+=1

        else:
            boat_rect = pygame.draw.rect(gameDisplay, GREY, (DISPLAY[0]-RIVER_WIDTH / 2 - CHARACTER_SIZE,DISPLAY[1]/2-CHARACTER_SIZE, CHARACTER_SIZE, 4*CHARACTER_SIZE))
            for i in boat_load:
                print(i)
                if i == 'M':
                    rect = pygame.draw.rect(gameDisplay, ORANGE, (DISPLAY[0]-RIVER_WIDTH / 2-CHARACTER_SIZE, DISPLAY[1] / 2 -CHARACTER_SIZE+ 3*count*CHARACTER_SIZE, CHARACTER_SIZE,CHARACTER_SIZE))
                    gameDisplay.blit(textsurface_M, (DISPLAY[0]-RIVER_WIDTH / 2 -CHARACTER_SIZE, DISPLAY[1] / 2 -CHARACTER_SIZE+ 3*count*CHARACTER_SIZE))
                    if mouse_pressed == True and gamePlay:
                        if rect.collidepoint(mouse_pos):
                            boatM-=1
                            boat_load.pop(count)
                            removed = True

                else:
                    rect = pygame.draw.rect(gameDisplay, BLACK, (DISPLAY[0]-RIVER_WIDTH / 2 - CHARACTER_SIZE, DISPLAY[1] / 2 -CHARACTER_SIZE+ 3*count*CHARACTER_SIZE,CHARACTER_SIZE, CHARACTER_SIZE))
                    gameDisplay.blit(textsurface_C, (DISPLAY[0]-RIVER_WIDTH / 2 - CHARACTER_SIZE, DISPLAY[1] / 2 -CHARACTER_SIZE+ 3*count*CHARACTER_SIZE))
                    if mouse_pressed == True and gamePlay:
                        if rect.collidepoint(mouse_pos):
                            boatC-=1
                            boat_load.pop(count)
                            removed = True
                count+=1

        if mouse_pressed == True:
            if boat_rect.collidepoint(mouse_pos) and len(boat_load)>0 and removed == False and gamePlay:
                if river_crossed == False:
                    no_of_missionaries-= boatM
                    no_of_cannibals-= boatC
                else:
                    no_of_missionaries+= boatM
                    no_of_cannibals+= boatC

                river_crossed = not river_crossed

        print(no_of_cannibals,no_of_missionaries)

        if no_of_cannibals== 0 and no_of_missionaries == 0 and gamePlay :
            message = "You Won"
            gamePlay = False
            mouse_pressed = False

        elif(no_of_cannibals>no_of_missionaries and no_of_missionaries!=0 or (3-no_of_cannibals)>(3-no_of_missionaries) and (3-no_of_missionaries)!=0) and gamePlay:
            gamePlay = False
            message = "Cannibals ate Missionaries"
            mouse_pressed = False

        if gamePlay == False:

            textsurface = myfont.render(message, False, RED)
            gameDisplay.blit(textsurface,(DISPLAY[0]/2-5*len(message),DISPLAY[1]/2))
            textsurface1 = myfont.render("Click To Restart",False, RED)
            gameDisplay.blit(textsurface1,(DISPLAY[0]/2-5*len(message),DISPLAY[1]/2+40))

            if mouse_pressed == True:
                print("Hello World")
                pygame.quit()
                MC()
                quit()


        pygame.display.update()



MC()
