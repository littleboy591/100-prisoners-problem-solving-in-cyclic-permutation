import pygame
import random
import math

import pygame.camera

pygame.init()
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

#box list
box_no= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
box_no_inside = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]






#Shuffle button
shuffle = False
shuffle_but = pygame.Rect((20,420,100,50))
shuffle_color = (255,255,255)

#Go button
go_but = pygame.Rect((550,20,100,50))
go_color = (255,255,255)
send_pr = False

#next prisinor button
next_but = pygame.Rect((550,120,100,50))
next_col = (255,255,255)

#previos prisinor button
prev_but = pygame.Rect((550,220,100,50))
prev_col = (255,255,255)



#Variables for the main ^\/_-EVENT-_\/^
loop_length = 0
pr_x = 20
pr_y = 30
prisinor_no = 1
pr_pos = 1
no_pr_pass = 0
some_con = True
pass_or_fail = ""

#main loop

run = True
while run:
    screen.fill((0,0,0))
    
    prisinor = pygame.Rect((pr_x,pr_y,20,20))

    pygame.draw.rect(screen,(255,0,0),(10,10,500,400),width=5)

    pos = pygame.mouse.get_pos()

    #button
    
    pygame.draw.rect(screen,(shuffle_color),shuffle_but)
    screen.blit(pygame.font.SysFont('consolas',24).render("Shuffle",True,(0,0,0)),(25,433))
    
    if shuffle_but.collidepoint(pos):
        shuffle_color = (220,220,220)
        if pygame.mouse.get_pressed()[0]:
            shuffle_color = (200,200,200)
        else:
            shuffle_color = (220,220,220)
    else:
        shuffle_color = (255,255,255)

    #previos prisinor button

    pygame.draw.rect(screen,(prev_col),prev_but)
    screen.blit(pygame.font.SysFont('consolas',20).render("Prev pr.",True,(0,0,0)),(557,237))

    if prev_but.collidepoint(pos):
        prev_col = (220,220,220)
        if pygame.mouse.get_pressed()[0]:
            prev_col = (200,200,200)
        else:
            prev_col = (220,220,220)
    else:
        prev_col = (255,255,255)


    #boxes
    for row in range(6):
        for col in range(6):
            pygame.draw.rect(screen,(255,255,255),(col*80+20,row*60+30,50,50))
            no_of_box= pygame.font.SysFont('consolas',20).render(str(box_no[row*6+col]),True,(0,0,0))
            screen.blit(no_of_box,(col*80+30,row*60+30))
            
            if shuffle == True:
                random.shuffle(box_no_inside)
            no_in_box= pygame.font.SysFont('consolas',15).render(str(box_no_inside[row*6+col]),True,(255,0,0))
            screen.blit(no_in_box,(col*80+40,row*60+55))



    #Prisinors' time to test thier luck (:-)
    pygame.draw.rect(screen,go_color,go_but)
    screen.blit(pygame.font.SysFont('consolas',20).render("send pr.",True,(0,0,0)),(556,33))

    if go_but.collidepoint(pos):
        go_color = (220,220,220)
        if pygame.mouse.get_pressed()[0]:
            go_color = (200,200,200)
        else:
            go_color= (220,220,220)
    else:
        go_color = (255,255,255)
        
    if send_pr:
        pygame.draw.rect(screen,(0,0,255),prisinor)
        pr_pos = box_no_inside[pr_pos-1]
        loop_length += 1

        pr_y = (math.floor(pr_pos/6)*60+30)
        pr_x = ((pr_pos-(math.floor(pr_pos/6)*6)-1)*80+20)


        if prisinor_no == pr_pos:
            send_pr = False
            if some_con:
                if loop_length <= 18:
                    no_pr_pass += 1  
                    pass_or_fail = "PASS"
                else:
                    pass_or_fail = "FAIL"

            some_con = False
            
            
            

    pygame.draw.rect(screen,next_col,next_but)
    screen.blit(pygame.font.SysFont('consolas',20).render("Next pr.",True,(0,0,0)),(555,133))

    if next_but.collidepoint(pos):
        next_col = (220,220,220)
        if pygame.mouse.get_pressed()[0]:
            next_col = (200,200,200)
        else:
            next_col= (220,220,220)
    else:
        next_col = (255,255,255)


    shuffle = False

    # Terminal
    pygame.draw.rect(screen,(255,255,255),(700,30,280,550),width=5)
    screen.blit(pygame.font.SysFont('consolas',25,bold=True).render("TERMINAL",True,(255,255,255)),(780,10))
    screen.blit(pygame.font.SysFont('consolas',15,bold=True).render("Prisinor no. "+str(prisinor_no)+" going...",True,(255,255,255)),(730,50))
    screen.blit(pygame.font.SysFont('consolas',15,bold=True).render(str(pass_or_fail),True,(255,255,255)),(920,50))
    screen.blit(pygame.font.SysFont('consolas',15,bold=True).render("Loop length : "+str(loop_length),True,(255,255,255)),(730,65))
    screen.blit(pygame.font.SysFont('consolas',15,bold=True).render("No. of prisinors passed : "+str(no_pr_pass),True,(255,255,255)),(730,80))
    
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if shuffle_but.collidepoint(pos):
                    prisinor_no = 1
                    pr_pos=  1
                    shuffle = True
                    no_pr_pass = 0
                if go_but.collidepoint(pos):
                    send_pr = True
                    loop_length = 0
                if next_but.collidepoint(pos):
                    some_con = True
                    prisinor_no += 1
                    pr_pos = prisinor_no
                    pass_or_fail = ""
                    if prisinor_no >= 37:
                        prisinor_no = 36
                        pr_pos = prisinor_no

                if prev_but.collidepoint(pos):
                    some_con = True
                    prisinor_no -= 1
                    pr_pos = prisinor_no
                    pass_or_fail = ""
                    if prisinor_no <= 0:
                        prisinor_no = 1
                        pr_pos = prisinor_no



    clock.tick(60)
    pygame.display.update()

pygame.quit()