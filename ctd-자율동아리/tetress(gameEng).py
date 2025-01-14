# -*- coding:cp949 -*-
import pygame
import sys
import random

gameBoard = [
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]


blockset = [
        [[2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
         [2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[3,3,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,3,0,0,3,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [3,3,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,3,0,0,3,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,4,4,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,4,0,0,0,4,4,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,4,4,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,4,0,0,0,4,4,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[5,0,0,0,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [5,5,0,0,5,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [5,5,5,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,5,0,0,0,5,0,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,0,6,0,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [6,0,0,0,6,0,0,0,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [6,6,6,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [6,6,0,0,0,6,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[0,7,0,0,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [7,0,0,0,7,7,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [7,7,7,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,7,0,0,7,7,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        [[8,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [8,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [8,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [8,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]]



def trun_check(x,y,gameBoard,blockset,box_num,box_turn):
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if gameBoard[j+y][i+x] == 1 or gameBoard[j+y][i+x] == 9:
                if blockset[box_num][(box_turn+1)%4][i*4+j] != 0:
                    return True     
            j = j + 1
        i = i + 1
    return False

def box_input(x,y,gameBoard,blockset,box_num,box_turn):
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if 0 != blockset[box_num][box_turn][i*4+j]:
                gameBoard[j+y][i+x] = 1     
            j = j + 1
        i = i + 1
    return gameBoard

def down_rect_check(y,x,gameBoard,blockset,box_num,box_turn):
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if blockset[box_num][box_turn][j*4+i] != 0:
               if gameBoard[i+y+1][j+x] != 0:
                 return True
            j = j + 1
        i = i + 1
    return False

def right_rect_check(y,x,gameBoard,blockset,box_num,box_turn):
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if blockset[box_num][box_turn][j*4+i] != 0:
               if gameBoard[i+y+1][j+x+1] != 0:
                 return True
            j = j + 1
        i = i + 1
    return False

def left_rect_check(y,x,gameBoard,blockset,box_num,box_turn):
    i = 0
    while i <= 3:
        j = 0
        while j <= 3:
            if blockset[box_num][box_turn][j*4+i] != 0:
               if gameBoard[i+y][j+x-1] != 0:
                 return True
            j = j + 1
        i = i + 1
    return False

def box_drow(y,x,gameBoard,blockset,box_num,box_turn,screen,font):
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if blockset[box_num][box_turn][j*4+i] != 0:
                set_string(screen,font,j+x,i+y)
            j = j + 1
        i = i + 1
        
def set_string(screen,font,x,y):
    text = font.render(u"*", True, (255, 255, 255))
    screen.blit(text,(20*x, y*20) ,text.get_rect())

def draw_gameBoard(gameBoard,screen,font):
    x = 0
    while x < 19:
        y = 0
        while y < 16:
            if gameBoard[x][y] != 0:
                set_string(screen,font,y,x)
            y = y + 1
        x = x + 1
        
def dowm_line(gameBoard,v):
    x = v
    while x > 0:    
        y = 0 
        while y < 10:
            
            gameBoard[x][y+4] = gameBoard[x-1][y+4]
                
                
            y = y + 1
        x = x - 1
    return gameBoard

def check_line(gameBoard,x):
    y = 0
    while y < 11:
        if gameBoard[x][y+3] == 0:
            return False
        y = y + 1
    return True

def delete_line(gameBoard,x):
    y = 0
    while y < 10:
        gameBoard[x][y+4] = 0
        y = y + 1

def die_line(gameBoard):
   
    x = 0
    while x < 15:
        if check_line(gameBoard,x) == True:
            delete_line(gameBoard,x)
            gameBoard = dowm_line(gameBoard,x)
        x = x + 1
    return gameBoard

def array_chekc(gameBoard):
    x = 0
    while x < 12:
        y = 0
        while y < 16:
            if gameBoard[x+4][y] != 9:
                y = 0
                x = x + 1
            y = y + 1
        
        x = x + 1

def Main(gameBoard):
    x = 5
    y = 0
    box_turn = 0
    
    pygame.init()

    screen = pygame.display.set_mode((600, 360))
    font = pygame.font.SysFont("test.ttf", 70)

    
    text = font.render(u"▩", True, (255, 255, 255))
    
    bock = font.render(u"□", True, (255, 255, 255))

    box_num = random.randint(0, 6)
    
    i = 0
    while True:
        i = i + 1
        if (i%500) == 0:
            if down_rect_check(y,x,gameBoard,blockset,box_num,box_turn%4) == False:
                    y = y + 1
                    gameBoard = die_line(gameBoard)
                    
            if down_rect_check(y,x,gameBoard,blockset,box_num,box_turn%4) == True:
                    gameBoard = box_input(x,y,gameBoard,blockset,box_num,box_turn%4)
                    gameBoard = die_line(gameBoard)
                    x = 5
                    y = 0
                    box_turn = 1
                    box_num =  random.randint(0, 6)
                            
        for event in pygame.event.get():
             # 이벤트를 처리하는 부분
                
            if pygame.KEYDOWN == event.type:
                if event.key == pygame.K_DOWN:
                    if down_rect_check(y,x,gameBoard,blockset,box_num,box_turn%4) == False:
                        gameBoard = die_line(gameBoard)
                        y = y + 1
                        gameBoard = die_line(gameBoard)
                        
                    if down_rect_check(y,x,gameBoard,blockset,box_num,box_turn%4) == True:
                        
                        gameBoard = box_input(x,y,gameBoard,blockset,box_num,box_turn%4)
                        x = 5
                        y = 0
                        box_turn = 1
                        box_num =  random.randint(0, 6)

                if event.key == pygame.K_RIGHT:
                    if right_rect_check(y,x,gameBoard,blockset,box_num,box_turn%4) == False:
                        x = x + 1


                if event.key == pygame.K_LEFT:
                    if left_rect_check(y,x,gameBoard,blockset,box_num,box_turn%4) == False:
                        x = x - 1
                
                    
                if event.key == pygame.K_UP:
                    if trun_check(x,y,gameBoard,blockset,box_num,box_turn) == False:
                        box_turn = box_turn + 1
                    
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.exit()
                return
        screen.fill((0, 0, 0))

        box_drow(y,x,gameBoard,blockset,box_num,box_turn%4,screen,font)

        draw_gameBoard(gameBoard,screen,font)

        #set_string(screen,font,x,y)

        
        pygame.display.flip()

Main(gameBoard)
