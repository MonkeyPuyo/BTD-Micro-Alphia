# what helps this code run

import pygame

pygame.init()

# the screen size and how we load the pictures
screen = pygame.display.set_mode((700, 520))

#the font we load
font = pygame.font.SysFont('roboto', 52)



map=pygame.image.load("map.jpg")
map=pygame.transform.scale(map, (700,520))
D_S=pygame.image.load("D_S.png")
D_S=pygame.transform.scale(D_S, (100,100))
D_M=pygame.image.load("D_M.png")
D_M=pygame.transform.scale(D_M, (60,60))

        
# where all the magic happens

active = True

is_draggable = True
dart_loc = (600, 3)

#starting amount of money
money= 1000

#everything will be tracked by frame
while active:
    
    text = font.render(str(money), True, (232, 228, 11))

 # how we pick up the monkey & drag it & money management

    mouse_loc = pygame.mouse.get_pos()
    for event in pygame.event.get():
        print(event)


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if is_draggable:
                money -= 200
            is_draggable = not is_draggable

    if money <200:
        is_draggable=False

    #perfect for debug
    # if event.type == pygame.MOUSEBUTTONDOWN:
        # print("clicked!")
    # if event.button == 1:
        # print("and it's the left button")
    
    if event.type == pygame.QUIT:
        active = False

    #if D_M is placed

    #where all the characters load and where they are
    screen.blit(map,(0,0))
    screen.blit(D_S,(600,3))
    screen.blit(D_M,(dart_loc))
    screen.blit(text, (0, 0))
    #other code about the mouse
    print(mouse_loc)

    if is_draggable:
        dart_loc = mouse_loc



    pygame.display.flip()
