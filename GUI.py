import pygame as py
import sys
import numpy as np

# Initialize Pygame
py.init()

# Set up display
screen = py.display.set_mode((800, 480))
py.display.set_caption('My First Pygame Program')

# Set up color
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)


# draw number in 
def draw_number_in_matrix_3x(number,x,y,width,sizefont,color):
    font  = py.font.SysFont(None,sizefont)
    number_surf = font.render(str(number), True, color)
    number_rect = number_surf.get_rect(center=((x + (width // 2)), (y + (width // 2))))
    screen.blit(number_surf, number_rect)



# draw matrix 3x

def draw_matrix_3x(x,y,width,n,array):
    for i in range(n+1):
        py.draw.line(screen, black, (x, y + i * width), (x + 3 * width, y + i * width), 2)
        py.draw.line(screen, black, (x + i * width, y), (x + i * width, y + 3 * width), 2)
    l = x
    k = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == -1:
                draw_number_in_matrix_3x('',x,y,width,30,black)
            else:
                draw_number_in_matrix_3x(array[i][j],x,y,width,30,black) 
            k = k + 1
            x = x + width
            if k%n == 0:
                y = y + width
                x = l
                k = 0
# Save cell empty
def save_empty(array,x,y,width,n):
    l = x
    k = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == -1:
                return (x,y) 
            k = k + 1
            x = x + width
            if k%n == 0:
                y = y + width
                x = l
                k = 0

# 1: left
# 2: right
# 3: up
# 4: down 

# Move cells
def handle(array,x,y,width,n,stable):
    print(array)
    x_empty,y_empty = save_empty(array,x,y,width,n)
    #print(x_empty,y_empty)
    for i in range(len(array)):
        for j in range(len(array[i])):
            # print("=====")
            # print(array[i][j],i,j)
            # print("=====")
            #if array[i][j] == -1: print(i,j)
            if array[i][j] == -1:
                #print(i,j,stable)
                if stable == 1 and j+1<n:
                    draw_number_in_matrix_3x(array[i][j+1],x_empty,y_empty,width,30,black)
                    draw_number_in_matrix_3x('',x_empty-width,y_empty,width,30,black)
                    array[i][j] = array[i][j+1]
                    array[i][j+1] = -1
                    x_empty = x_empty-width
                    return
                elif stable == 2 and j-1>=0: 
                    draw_number_in_matrix_3x(array[i][j-1],x_empty,y_empty,width,30,black)
                    draw_number_in_matrix_3x('',x_empty+width,y_empty,width,30,black)
                    array[i][j] = array[i][j-1]
                    array[i][j-1] = -1
                    x_empty = x_empty+width
                    return
                elif stable == 3 and i+1<n:
                    draw_number_in_matrix_3x(array[i+1][j],x_empty,y_empty,width,30,black)
                    draw_number_in_matrix_3x('',x_empty,y_empty+width,width,30,black)
                    array[i][j] = array[i+1][j]
                    array[i+1][j] = -1
                    y_empty = y_empty+width
                    return
                elif stable == 4 and i-1>=0:
                    #print(i,j,100)
                    draw_number_in_matrix_3x(array[i-1][j],x_empty,y_empty,width,30,black)
                    draw_number_in_matrix_3x('',x_empty,y_empty-width,width,30,black)
                    array[i][j] = array[i-1][j]
                    array[i-1][j] = -1
                    y_empty = y_empty-width
                    return
    #print (array)








        
        
        

        




# check button and draw button
font = py.font.SysFont(None, 25)
def draw_button(text,x, y, width, height, inactive_color, active_color):
    mouse = py.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        py.draw.rect(screen, active_color, (x, y, width, height))
    else:
        py.draw.rect(screen, inactive_color, (x, y, width, height))
    text_surf = font.render(text, True, white)
    text_rect = text_surf.get_rect(center=((x + (width // 2)), (y + (height // 2))))
    screen.blit(text_surf, text_rect)

def check_stable_button(x, y, width, height):
    mouse = py.mouse.get_pos()
    click = py.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        if click[0] == 1:
            return True
    return False



# load image
image = py.image.load('D:\DAI HOC DUNG HOC DAI\THIRD\HK1\AI\week2\megaphone.png')

#load music
py.mixer.music.load('D:\DAI HOC DUNG HOC DAI\THIRD\HK1\AI\week2\DLTTAD.mp3')  # Thay thế 'background_music.mp3' bằng tên tệp của bạn
py.mixer.music.set_volume(0.1)  # Thiết lập âm lượng (0.0 đến 1.0)
py.mixer.music.play(-1)  # Phát nhạc nền lặp lại vô hạn (-1)
#volume = 0.5

# check button
check_play = False
check_music = False

# array 
Goal = np.array([
    [1,2,3],
    [4,6,5],
    [7,-1,8]
    ])
Begin = np.array(
        [[1,2,3],
         [4,8,6],
         [7,5,-1]])
# loop 
while True:

    for event in py.event.get():
        
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        keys = py.key.get_pressed()
        if keys[py.K_LEFT] and check_play == True:
            handle(Begin,100,100,90,3,1)
            
            #print("mũi tên trái được nhấn")
        if keys[py.K_RIGHT] and check_play == True:
            handle(Begin,100,100,90,3,2)
           
        if keys[py.K_UP] and check_play == True:
            handle(Begin,100,100,90,3,3)
            
            #print(Begin)
        if keys[py.K_DOWN] and check_play == True:
            #print("xin chao")
            handle(Begin,100,100,90,3,4)
            
            
        if check_stable_button(300, 130, 200, 80) and check_play == False:
            check_play = True
            #screen.fill(white)
            print("click")
        if check_stable_button(300, 250, 200, 80) and check_play == False:
            py.quit()
            sys.exit()
        if check_stable_button(650,400,100,60):
            check_play = False
            print("click back")
        if check_stable_button(20,10,80,80) and check_music == False:
            py.mixer.music.pause()
            check_music = True
            print("music")
        elif check_stable_button(20,10,80,80) and check_music == True:
            check_music = False
            py.mixer.music.unpause()
            

    

        
    screen.fill(white)
    screen.blit(image, (20, 10))
    

    if check_play == False:
        draw_button("Play", 300, 130, 200, 80, blue, red)
        draw_button("Exit", 300, 250, 200, 80, blue, red)
       

    else: 
        draw_button('Back',650,400,100,60,blue,red)
        draw_matrix_3x(100,100,90,3,Begin)
        draw_matrix_3x(430,100,90,3,Goal)
        draw_number_in_matrix_3x("Goal State",500,10,90,30,black)
        if np.array_equal(Begin, Goal):
                draw_number_in_matrix_3x("You Win!!!",300,10,90,30,red)
    
    
    
    
    py.display.flip()

  
    
