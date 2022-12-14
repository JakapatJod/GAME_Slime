import pygame
from pygame.locals import *
from pygame import mixer
import time
import os
from os import path

t0 = time.time()
x = 0
adwwdasfwess = 0
pygame.init()


dt = 0
clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 750

list_score = []

tile_size = 50
game_over = 0

main_menu = True
topscore = []

second = 1
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Super Slime Tournament")

icon = pygame.image.load("images/blob.png")
pygame.display.set_icon(icon)
bg = pygame.image.load("images/sky.png")
dirt = pygame.image.load("images/dirt.png")
grass = pygame.image.load("images/platform.png")
load_player = pygame.image.load("images/blob.png")
start_img = pygame.image.load("images/start_btn.png")
exit_img = pygame.image.load("images/exit_btn.png")
restart_img = pygame.image.load("images/restart_btn.png")

player = pygame.transform.scale(load_player,(45,37))
mixer.music.load("sounds/Corona320bit.wav")



font_color=(34,139,34)
font_obj=pygame.font.Font("font/2005_iannnnnCPU.ttf",60)
font_time = pygame.font.SysFont("font/2005_iannnnnCPU.ttf",60)
white = (255, 255, 255)
red = (255,0,0)

if os.path.exists('highscore.txt'):
    open_file = open('highscore.txt')
    bar = 0
    for un in open_file:
        bar = bar + 1
    open_file2 = open('highscore.txt')
    for un2 in range(bar):
        read_score = open_file2.readline().replace('\n','')
    
        list_score.append(read_score)
    
    list_score = sorted(list_score)
else:
    list_score = [0,0,0,0,0]
    


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

class World():
    def __init__(self, data):
        self.tile_list= []

        #class odject
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    ghost = Enemy(col_count * tile_size, row_count * tile_size)
                    blob_group.add(ghost)
                if tile == 4:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size//2))
                    lava_group.add(lava)
                if tile == 5:
                    door = Door(col_count * tile_size, row_count * tile_size)
                    door_group.add(door)
                if tile == 6:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                    platform_group.add(platform)
                if tile == 7:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                    platform_group.add(platform)
                
                col_count += 1
            row_count += 1
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ghost.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        
        self.move_counter += 1
        if self.move_counter > 50:
            self.move_direction *= -1
            self.move_counter *= -1

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/platform.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size//2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("images/exit.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        main_menu = True


        

# 1= ?????????     # 6 = ???????????????????????????????????????
# 2= ????????????    # 7 = ??????????????????????????????????????????
# 3= ???????????????
# 4= ????????????
# 5= ???????????????
world_data = [ 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],   
[1, 0, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
[1, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 3, 0, 0, 0, 1],   
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 1],  
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],  
[1, 0, 2, 0, 0, 6, 0, 0, 2, 0, 0, 6, 0, 0, 1, 1], 
[1, 2, 1, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1, 1],
]

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        #get cilck
        pos = pygame.mouse.get_pos()

        #chech clicked:
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        screen.blit(self.image, self.rect)
        
        return action
        

class Player():
    def __init__(self, x, y):
        self.reset(x, y)
        
    def update(self, game_over , ):
        dx = 0
        dy = 0 
        col_thresh = 20

        if game_over == 0:
            # ??????????????????????????????
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                dx -= 5
            if keys[pygame.K_d]:
                dx += 5   
            if keys[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -15 
                self.jumped = True
            if keys[pygame.K_SPACE] == False and self.in_air == False:
                self.jumped = False
            
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            self.in_air = True
            for tile in world.tile_list:
                # ?????????????????????????????????
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # ??????????????????????????????
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y < 0 :
                        dy = tile[1].bottom - self.rect.top
                    elif self.vel_y >= 0 :
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1
            
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
            
            if pygame.sprite.spritecollide(self, door_group, False):
                game_over = -2
            
            for platform in platform_group:
                #?????????????????????????????? X
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #?????????????????????????????? Y
                if platform.rect.colliderect(self.rect.x , self.rect.y + dy, self.width, self.height):
                    #?????????????????? platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    #??????????????? platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

                
            self.rect.x += dx
            self.rect.y += dy 
        elif game_over == -1:
            if self.rect.y > 200:
                self.rect.y -= 5
                self.rect.x -= 15
             

        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        
        return game_over
    def reset(self, x, y,):
        load_player = pygame.image.load("images/blob.png")
        self.image = pygame.transform.scale(load_player,(45,37))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = True
        mixer.music.play()
        

player = Player(100, screen_height - 130)

platform_group = pygame.sprite.Group()
blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()

world = World(world_data)

#?????? button
restart_button = Button(screen_width // 2-70, screen_height // 2+100, restart_img)
start_button = Button(screen_width // 2 -350, screen_height // 2 , start_img)
exit_button = Button(screen_width // 2 + 100, screen_height // 2 , exit_img)




        
        


run = True

#?????????????????????

while run:
    
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    if game_over == 0:
        t1 = time.time()
        dt = t1 - t0
        dt = format(dt,'.0f')
    if main_menu == True:
        draw_text('HIGHSCORE 1 : ' + list_score[0], font_obj, white, (screen_width // 2) - 150, (screen_height // 2) - 350)
        draw_text('HIGHSCORE 2 : ' + list_score[1], font_obj, white, (screen_width // 2) - 150, (screen_height // 2) - 300)
        draw_text('HIGHSCORE 3 : ' + list_score[2], font_obj, white, (screen_width // 2) - 150, (screen_height // 2) - 250)
        draw_text('HIGHSCORE 4 : ' + list_score[3], font_obj, white, (screen_width // 2) - 150, (screen_height // 2) - 200)
        draw_text('HIGHSCORE 5 : ' + list_score[4], font_obj, white, (screen_width // 2) - 150, (screen_height // 2) - 150)
        if exit_button.draw():
            run = False

        if start_button.draw():
            main_menu = False
            t0 = t1
    
    else:
        world.draw()
        game_over = player.update(game_over)
        
        if game_over == 0:
            blob_group.update()
            platform_group.update()   
            

            

        
        blob_group.draw(screen)
        lava_group.draw(screen)
        door_group.draw(screen)
        platform_group.draw(screen)

        if game_over == -1:

            draw_text('YOU LOSE WITH TIME :' +(format(dt)), font_obj, red, (screen_width // 2) + -200, (screen_height // 2)- 50)
            mixer.music.stop()     
            
            if restart_button.draw():
                player.reset(100, screen_height - 130)
                game_over = 0
                t0 = t1
                main_menu = True
                

               

        if game_over == -2:
            
                
            draw_text('YOU WIN WITH TIME :' +(format(dt)), font_obj, font_color, (screen_width // 2) + -200, (screen_height // 2)- 50)
            
            
            mixer.music.stop()
            
            if restart_button.draw():
                player.reset(100, screen_height - 130)
                game_over = 0
                t0 = t1
                main_menu = True
                list_score.append(dt)
                list_score = sorted(list_score)
                
                open_file3 = open('highscore.txt','w')


                for un3 in range(bar):
                    open_file3.write(list_score[un3]+'\n')
                open_file3.close()
                #print(list_score)

                
        count = font_obj.render("Time : "+(format(dt)),0,font_color)
        screen.blit(count,(300,50))
        

        pygame.time.delay(0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        pygame.display.set_mode((screen_width,screen_height),pygame.FULLSCREEN)
    if keys[pygame.K_ESCAPE]:
        exit()

    pygame.display.update()
pygame.quit()
