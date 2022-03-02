import pygame
import pygame_menu
import sys
import random

pygame.init()
pol = 0 
total = 2
size = [505,632]
screen = pygame.display.set_mode(size) 
pygame.display.flip()
pygame.display.set_caption('2048')
total = pygame.font.SysFont('CALLIBRIA', 50)
CONST = 0
record = 0

def start_the_game():  
    global record

    if CONST == 3:
        
        blok = 135
        MARGIN = 5
        mas = [
            [0]*CONST,
            [0]*CONST,
            [0]*CONST
        ]
        shrift = 0
        xx,yy = 0,0
    
    if CONST == 4:
        blok = 100
        MARGIN = 5
        mas = [
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST
        ]
        shrift = 0
        xx,yy = 0,0

    if CONST == 5:
        blok = 80
        MARGIN = 4
        mas = [
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST
        ]
        shrift = -10
        xx,yy = 5,5

    if CONST == 6:
        blok = 67
        MARGIN = 3
        mas = [
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST
        ]
        shrift = -18
        xx,yy = 10,10

    if CONST == 7:
        blok = 60
        MARGIN = 2
        mas = [
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST,
            [0]*CONST
        ]
        shrift = -18
        xx,yy = 10,10

    n, ll, conez, ohki = 0, 0, 0, 0
    destvie, y = 0, 0 #отслживание действий ,для добавления рандомного блока
    
    while n != 2:
        a = random.randint(0, CONST -1 )
        b = random.randint(0, CONST -1)
        if mas[a][b] == 0:
            mas[a][b] = 2
            n += 1    
     
    def random_blok():#создания рандомного блока

        while True:
            i = random.randint(0, CONST-1)
            j = random.randint(0, CONST-1)
            rd = random.random()

            if mas[i][j] == 0:

                if rd <= 0.8:
                    mas[i][j] = 2
                    pygame.draw.rect(screen,(255,255,40),[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok])
                    con = pygame.font.SysFont('CALLIBRIA', 80)
                    text = con.render(f"{mas[i][j]}",15,(10,10,10))
                    screen.blit(text,(50 - xx + 20 + blok*j + MARGIN*(j+1),190+blok*i +  MARGIN*(i+1)))
                    break

                else:

                    mas[i][j] = 4
                    pygame.draw.rect(screen,(255,255,40),[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok])
                    con = pygame.font.SysFont('CALLIBRIA', 80)
                    text = con.render(f"{mas[i][j]}",15,(10,10,10))
                    screen.blit(text,(50 -xx + 20 + blok*j + MARGIN*(j+1),190+blok*i +  MARGIN*(i+1)))
                    break
                    
    def risovka_blok(collor,i,j): #рисовка блоков

        return (pygame.draw.rect(screen,collor,[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok]))

    while True:

        if conez == 1:
            break

        def text_shet(i,j): #создание счета игрового поля
            
            while True:
                #n -сдвиг влево ,k-шрифт
                if mas[i][j] <= 8:
                    k = 80 
                    n = 20
                    pygame.draw.rect(screen,(255,255,40),[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok])
                    break
                
                if mas[i][j] <= 64:
                    k = 80 
                    n = 10
                    pygame.draw.rect(screen,(255,150,0),[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok])
                    break
                
                if mas[i][j] < 1024:
                    k = 60 
                    n = 5
                    pygame.draw.rect(screen,(255,100,0),[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok])
                    break
                
                if mas[i][j] == 1024:
                    k = 50
                    n = 0
                    pygame.draw.rect(screen,(255,70,0),[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok])
                    break
                
                if mas[i][j] > 1024:
                    k = 50
                    n = 0
                    pygame.draw.rect(screen,(255,0,0),[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok])
                    break
                if mas[i][j] > 8000:
                    k = 5
                    n = 0
                    pygame.draw.rect(screen,(255,0,0),[40 + blok*j + MARGIN*(j+1),170+blok*i +  MARGIN*(i+1),blok,blok])
                    break
        
            con = pygame.font.SysFont('sss', k + shrift)
            text = con.render(f"{mas[i][j]}",15,(10,10,10))
            screen.blit(text,(50 - xx + n + blok*j + MARGIN*(j+1),190+blok*i +  MARGIN*(i+1))) 
        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if pygame.mouse.get_pos() >= (100,200):
                    if pygame.mouse.get_pos() <= (240,250):
                            start_the_game()

                if pygame.mouse.get_pos() >= (260,400):
                    if pygame.mouse.get_pos() <= (400,700):
                            conez = 1
                            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:#управление
                
                if ll == 1:
                    conez = 1
                
                if event.key == pygame.K_UP:
                    print(1)
                    n = 0
                    
                    while n != CONST-1:
                        
                        for row in range(CONST-1,0,-1):
                            for col in range(CONST):
                                
                                if mas[row][col] != 0:
                                   
                                    if mas[row - 1][col] == 0:
                                        destvie += 1
                                        mas[row - 1][col] = mas[row][col]
                                        mas[row][col] = 0
                                   
                                    if mas[row - 1][col] == mas[row][col]:
                                        mas[row - 1][col] += mas[row][col]
                                        mas[row][col] = 0
                                        mmax = 0
                                        for i in range(CONST):
                                            if max(mas[i]) > mmax:
                                                mmax = max(mas[i])
                                        if mmax <= 8:
                                            ohki += 4
                                        if mmax > 8 and mmax <= 64:
                                            ohki += 16
                                        if mmax > 64 and mmax <= 512:
                                            ohki += 32
                                        if mmax > 512 and mmax <= 1024:
                                            ohki += 64
                                        if mmax > 1024:
                                            ohki += 128
                                        destvie += 1
                        
                        n += 1
                    
                    if destvie > y:
                        y = destvie
                        random_blok()
                    
                    if record < ohki:
                        record = ohki
                
                elif event.key == pygame.K_DOWN:
                    
                    n = 0
                    
                    while n != CONST-1:
                        
                        for row in range(CONST-1):
                            for col in range(CONST):
                                
                                if mas[row][col] != 0:
                                    
                                    if mas[row + 1][col] == 0:
                                        mas[row + 1][col] = mas[row][col]
                                        mas[row][col] = 0
                                        destvie += 1
                                    
                                    if mas[row + 1][col] == mas[row][col]:
                                        mas[row + 1][col] += mas[row][col]
                                        mas[row][col] = 0
                                        destvie += 1
                                        
                                        mmax = 0
                                        for i in range(CONST):
                                            if max(mas[i]) > mmax:
                                                mmax = max(mas[i])
                                        if mmax <= 8:
                                            ohki += 4
                                        if mmax > 8 and mmax <= 64:
                                            ohki += 16
                                        if mmax > 64 and mmax <= 512:
                                            ohki += 32
                                        if mmax > 512 and mmax <= 1024:
                                            ohki += 64
                                        if mmax > 1024:
                                            ohki += 128
                        
                        n += 1
                    
                    if destvie > y:
                        y = destvie
                        random_blok()

                    if record < ohki:
                        record = ohki

                elif event.key == pygame.K_LEFT:
                    
                    n = 0
                    
                    while n != CONST-1:
                        
                        for row in range(CONST):
                            for col in range(CONST-1,0,-1):
                                
                                if mas[row][col] != 0:
                                    
                                    if mas[row][col-1] == 0:
                                        mas[row][col-1] = mas[row][col]
                                        mas[row][col] = 0
                                        destvie += 1
                                    
                                    if mas[row][col-1] == mas[row][col]:
                                        mas[row][col-1] += mas[row][col]
                                        mas[row][col] = 0
                                        destvie += 1
                                        
                                        mmax = 0
                                        for i in range(CONST):
                                            if max(mas[i]) > mmax:
                                                mmax = max(mas[i])
                                        if mmax <= 8:
                                            ohki += 4
                                        if mmax > 8 and mmax <= 64:
                                            ohki += 16
                                        if mmax > 64 and mmax <= 512:
                                            ohki += 32
                                        if mmax > 512 and mmax <= 1024:
                                            ohki += 64
                                        if mmax > 1024:
                                            ohki += 128

                        n += 1
                    if destvie > y:
                        y = destvie
                        random_blok()

                    if record < ohki:
                        record = ohki

                elif event.key == pygame.K_RIGHT:
                    
                    n = 0
                    
                    while n != CONST-1:
                        
                        for row in range(CONST):
                            for col in range(CONST-1):
                                
                                if mas[row][col] != 0:
                                    
                                    if mas[row][col+1] == 0:
                                        mas[row][col+1] = mas[row][col]
                                        mas[row][col] = 0
                                        destvie += 1
                                    
                                    if mas[row][col+1] == mas[row][col]:
                                        mas[row][col+1] += mas[row][col]
                                        mas[row][col] = 0
                                        destvie += 1
                                        
                                        mmax = 0
                                        for i in range(CONST):
                                            if max(mas[i]) > mmax:
                                                mmax = max(mas[i])
                                        if mmax <= 8:
                                            ohki += 4
                                        if mmax > 8 and mmax <= 64:
                                            ohki += 16
                                        if mmax > 64 and mmax <= 512:
                                            ohki += 32
                                        if mmax > 512 and mmax <= 1024:
                                            ohki += 64
                                        if mmax > 1024:
                                            ohki += 128
                        
                        n += 1

                    if record < ohki:
                        record = ohki
                    
                    if destvie > y:
                        y = destvie
                        random_blok()

        screen.fill((240,240,190)) #оксраска фона 
        pygame.draw.rect(screen,(220,170,0),[20,150,465,461])
        
        for i in range(CONST):#цикл на рисовку
            for j in range(CONST):
                risovka_blok((255,255,140), i, j)
                if mas[i][j] != 0:
                    text_shet(i,j)
        
        ma = 0 #проверка на возможный ход
        
        for i in range(CONST):
            for j in range(CONST):
                if mas[i][j] == 0:
                    ma += 1

        if ma == 0:
            
            for i in range(CONST):
                for j in range(CONST-1):
                    if mas[i][j] == mas[i][j+1]:
                        ma = 1
                        break
                if ma == 1:
                    break
            
            for i in range(CONST-1):
                for j in range(CONST):
                    
                    if mas[i][j] == mas[i+1][j]:
                        ma = 1
                        break
                
                if ma == 1:
                    break
            
            if ma == 0:

                pygame.draw.rect(screen,(0,0,0),[80,280,350,110])
                con = pygame.font.SysFont('CALLIBRIA', 56)
                text = con.render(f"{'Ты проиграл'}",35,(255,255,255))
                screen.blit(text,(130,310))
                start_button = pygame.draw.rect(screen,(20,20,105),(100,400,140,50))
                con1 = pygame.font.SysFont('CALLIBRIA', 38)
                text1 = con1.render(f"{'Ещё раз'}",20,(255,255,255))
                screen.blit(text1,(115,410))
                start_button1 = pygame.draw.rect(screen,(20,20,105),(250,400,140,50))
                con2 = pygame.font.SysFont('CALLIBRIA', 38)
                text2 = con2.render(f"{'Меню'}",20,(255,255,255))
                screen.blit(text2,(280,410))

        text = total.render(f" {'Ваш счет:'}",30,(10,10,10))
        screen.blit(text,(20,20))
        text = total.render(f" {ohki}",30,(10,10,10))
        screen.blit(text,(20,75))
        text = total.render(f" {'Рекорд:'}",20,(10,10,10))
        screen.blit(text,(250,20))
        text = total.render(f"{record}",40,(10,10,10))
        screen.blit(text,(260,75))
        pygame.display.flip()
def set_difficulty(value, difficulty):
    
    global CONST,pol
    
    CONST = list(value)
    CONST = list(CONST[0])
    CONST = CONST[-1]
    pol = CONST

menu = pygame_menu.Menu('2048', size[0], size[1], theme=pygame_menu.themes.THEME_DARK)                
menu.add.button('Играть', start_the_game)
menu.add.text_input('Имя игрока :', default='')
menu.add.selector('Выберите режим :', [('-',0),('3 x 3', 3),('4 x 4', 4), ('5 x 5', 5),('6 x 6', 6),('7 x 7', 7)], onchange=set_difficulty)
menu.add.button('Выйти', pygame_menu.events.EXIT)
menu.mainloop(screen)
