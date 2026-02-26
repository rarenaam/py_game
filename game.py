import pygame
import tkinter as tk

root = tk.Tk()
root.withdraw()
winx, winy = root.winfo_screenwidth(), root.winfo_screenheight()
print(winx, winy)

pygame.init()

winx2, winy2 = 1920, 720
win = pygame.display.set_mode((winx, winy))

background_colours = [(255, 255, 255),(200, 200, 200), (173, 216, 230), (245, 245, 220), (255, 255, 180), (50, 50, 50), (20, 20, 70), (0, 0, 0), (0, 50, 0), (50, 0, 50) ]
current_background = 0

colour_player1 = (255, 125, 125)
colour_player2 = (125, 255, 255)
colour_player3 = (125, 255, 255)


player_toggle_31 = 0
player_toggle_12 = 0
player_toggle_23 = 0

x1 = 50
y1 = 50
width1 = 30
height1 = 60
speed1 = 4
speed_boost1 = 8

x2 = 50
y2 = 50
width2 = 30
height2 = 60
speed2 = 4
speed_boost2 = 8

x3 = 50
y3 = 50
width3 = 30
height3 = 60
speed3 = 4
speed_boost3 = 8

cooldown_touch = 1000 #ms
last_touch_time = -cooldown_touch

sprint_cooldown = 5000
sprint_time = 1500
last_sprint_time1 = 0
last_sprint_time2 = 0
last_sprint_time3 = 0

#rectangle
rect_x = winx/2
rect_y = winy/2
rect_width = 200
rect_height = 100

def invert_colour(colour):
    r, g, b = colour
    return 255 - r, 255 - g, 255 - b

def touch_function(x11,x22,y11,y22,width11,height11):
    return x11-x22<width11 and y11-y22<height11 and x22-x11<width11 and y22-y11<height11

#def movement(w,a,s,d,shift, x, y, speedM, speed_boost, last_sprint_time):
    #if Keys[pygame.K_up]:
     #   y -= speedM
   # if Keys[pygame.K_a]:
   #     x -= speedM
    #if Keys[pygame.K_s]:
      #  y += speedM
 #   if Keys[pygame.K_d]:
      #  x += speedM
    #if Keys[pygame.K_shift] and current_time - last_sprint_time >= sprint_cooldown:
        #speedM = speed_boost
        #last_sprint_time = current_time
    #if current_time >= last_sprint_time + sprint_time:
      #  speedM = 4

def buiten_scherm(x,y):
    if y < 0:
        y = 0
    if y > winy - height1:
        y = winy - height1
    if x < 0:
        x = 0
    if x > winx - width1:
        x = winx - width1
    return x,y

def in_rect(x,y):
    if rect_y <= y <= rect_y + rect_height:
        if x <= rect_width - width1:
            x = rect_width - width1
    return x, y



font = pygame.font.Font(None, 50)
text_colour = invert_colour(background_colours[current_background])

player_toggle = 0

run = True
clock = pygame.time.Clock()
speed = 4
while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():

        #quit button
        if event.type == pygame.QUIT:
            run = False

        #change background colour
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_background = (current_background + 1) % len(background_colours)
                text_colour = invert_colour(background_colours[current_background])

    #check out of screen
    x1, y1 = buiten_scherm(x1, y1)
    x2, y2 = buiten_scherm(x2, y2)
    x3, y3 = buiten_scherm(x3, y3)

    #check in rect
    x1, y1 = in_rect(x1, y1)
    x2, y2 = in_rect(x2, y2)
    x3, y3 = in_rect(x3, y3)



    touch_this_frame = False

    #check for touching player 1 and 2
    touching = touch_function(x1, x2, y1, y2, width1, height1)
    if touching and current_time - last_touch_time >= cooldown_touch and not touch_this_frame:
        touch = "True"
        Btouch = True
        touch_this_frame = True
        player_toggle_12 = 1 - player_toggle_12
        if player_toggle != 2:
            if player_toggle_12 == 1:
                player_toggle = 0
            elif player_toggle_12 == 0:
                player_toggle = 1
            last_touch_time = current_time
        else:
            touch = "False"
            Btouch = False

    # check for touching player 2 and 3
    touching = touch_function(x2, x3, y2, y3, width1, height1)
    if touching and current_time - last_touch_time >= cooldown_touch and not touch_this_frame:
        touch = "True"
        Btouch = True
        touch_this_frame = True
        player_toggle_23 = 1 - player_toggle_23
        if player_toggle != 0:
            if player_toggle_23 == 1:
                player_toggle = 1
            elif player_toggle_23 == 0:
                player_toggle = 2
            last_touch_time = current_time
        else:
            touch = "False"
            Btouch = False

    # check for touching player 3 and 1
    touching = touch_function(x3, x1, y3, y1, width1, height1)
    if touching and current_time - last_touch_time >= cooldown_touch and not touch_this_frame:
        touch = "True"
        Btouch = True
        touch_this_frame = True
        player_toggle_31 = 1 - player_toggle_31
        if player_toggle != 1:
            if player_toggle_31 == 1:
                player_toggle = 2
            elif player_toggle_31 == 0:
                player_toggle = 0
            last_touch_time = current_time
        else:
            touch = "False"
            Btouch = False


    if player_toggle == 0:
        colour_player2 = (255, 0, 0)
        colour_player1 = text_colour
        colour_player3 = (0, 0, 255)
    elif player_toggle == 1:
        colour_player1 = (0, 255, 0)
        colour_player2 = text_colour
        colour_player3 = (0, 0, 255)
    elif player_toggle == 2:
        colour_player3 = text_colour
        colour_player2 = (255, 0, 0)
        colour_player1 = (0, 255, 0)

    #player 1 movement
    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_w]:
        y1 -= speed1
    if Keys[pygame.K_y]:
        cooldown_touch += 100
    if Keys[pygame.K_a]:
        x1 -= speed1
    if Keys[pygame.K_s]:
        y1 += speed1
    if Keys[pygame.K_d]:
        x1 += speed1
    if Keys[pygame.K_LSHIFT] and current_time - last_sprint_time1 >= sprint_cooldown:
        speed1 = speed_boost1
        last_sprint_time1 = current_time
    if current_time >= last_sprint_time1 + sprint_time:
        speed1 = 4

    #player 2 movement
    if Keys[pygame.K_i]:
        y2 -= speed2
    if Keys[pygame.K_j]:
        x2 -= speed2
    if Keys[pygame.K_k]:
        y2 += speed2
    if Keys[pygame.K_l]:
        x2 += speed2
    if Keys[pygame.K_b] and current_time - last_sprint_time2 >= sprint_cooldown:
        speed2 = speed_boost2
        last_sprint_time2 = current_time
    if current_time >= last_sprint_time2 + sprint_time:
        speed2 = 4


    #player 3 movement
    Keys = pygame.key.get_pressed()
    if Keys[pygame.K_KP8]:
        y3 -= speed3
    if Keys[pygame.K_KP4]:
        x3 -= speed3
    if Keys[pygame.K_KP5]:
        y3 += speed3
    if Keys[pygame.K_KP6]:
        x3 += speed3
    if Keys[pygame.K_KP_ENTER] and current_time - last_sprint_time3 >= sprint_cooldown:
        speed3 = speed_boost3
        last_sprint_time3 = current_time
    if current_time >= last_sprint_time3 + sprint_time:
        speed3 = 4

    win.fill(background_colours[current_background])
    pygame.draw.rect(win, colour_player1, (x1, y1, width1, height1))
    pygame.draw.rect(win, colour_player2, (x2, y2, width2, height2))
    pygame.draw.rect(win, colour_player3, (x3, y3, width3, height3))

    pygame.draw.rect(win, text_colour, (winx/2, winy/2, 100, 100))

    text_surface = font.render(f"player touch: {touch}, player_toggle: {player_toggle}",True,text_colour)
    win.blit(text_surface,(50,50))
    pygame.display.update()

pygame.quit()
