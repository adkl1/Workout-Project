import pygame
from sys import exit

#intialize the pygame
pygame.init()

#create is screen
screen = pygame.display.set_mode((1800,1000))

#the clock
clock = pygame.time.Clock()

#Title Background and Icon
pygame.display.set_caption("Daily Plan")
icon = pygame.image.load("workoutProject/workoutProjectGit/muscleIcon.png").convert_alpha()
pygame.display.set_icon(icon)
background = pygame.image.load("workoutProject/workoutProjectGit/background.jpg").convert_alpha()

#buttons
daily_plan_button = pygame.Rect(650,500,500,100)
options_button = pygame.Rect(650,650,500,100)
back_button = pygame.Rect(20,930,200,50)
routin_button = pygame.Rect(1250,400,500,100)
workout_sch_button = pygame.Rect(1250,250,500,100)
workout_file_path_button = pygame.Rect(350,265,700,100)
routin_file_path_button = pygame.Rect(350,450,700,100)
#text
font = pygame.font.Font(None, 50)
def draw_text(text,font,color,surface,x,y):
    '''
    fuction for immidatley drawing a text on secfuce
    '''
    text_obj = font.render(text,1,color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(text_obj,text_rect)

workout_file_path = "c:/python/workoutplan.txt"
routin_file_path = "c:/python/workoutplan.txt"
def change_text(text):
    while True:
        #exit on screen close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #mouse input
        mx, my = pygame.mouse.get_pos()
        if options_button.collidepoint((mx,my)):
            if click:
                options_menu()
        if daily_plan_button.collidepoint((mx,my)):
            if click:
                daily_menu()
                
        click = False
        pygame.display.update()
        clock.tick(60)

#main game loop
def main_loop():
    '''
    function for running the main menu screen
    input: none
    output: none
    '''
    click = False
    while True:
        #exit on screen close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #mouse input
        mx, my = pygame.mouse.get_pos()
        if options_button.collidepoint((mx,my)):
            if click:
                options_menu()
        if daily_plan_button.collidepoint((mx,my)):
            if click:
                daily_menu()

        #add images
        screen.blit(background,(0,0))
        pygame.draw.rect(screen,(0,0,0),options_button)
        draw_text("Options",font,(255,255,255),screen,830,675)
        pygame.draw.rect(screen,(0,0,0),daily_plan_button)
        draw_text("Daily Menu",font,(255,255,255),screen,820,530)
        draw_text("Main Menu", font,(0,0,0),screen,800,40)

        #loop necesities
        click = False
        pygame.display.update()
        clock.tick(60)

def options_menu():
    '''
    function for running the option menu screen
    input: none
    output: none
    '''
    running = True
    global workout_file_path
    click_on_text = False
    while running:
        click = False
        #exit on screen close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not click_on_text:
                    running = False
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_ESCAPE:
                    click_on_text = False
                elif click_on_text and len(workout_file_path) < 30:
                    if event.unicode.isalpha() or event.unicode == "/" or event.unicode == ".":
                        workout_file_path += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        workout_file_path = workout_file_path[:-1]
                elif event.key == pygame.K_BACKSPACE:
                        workout_file_path = workout_file_path[:-1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    click_on_text = False
                    
        #mouse input
        mx, my = pygame.mouse.get_pos()
        if back_button.collidepoint((mx,my)):
            if click:
                running = False #leave menu
        if workout_file_path_button.collidepoint((mx,my)):
            if click:
                click_on_text = not click_on_text
        
        #add images
        screen.blit(background,(0,0))
        draw_text("Options Menu", font,(0,0,0),screen,800,40)
        pygame.draw.rect(screen,(0,0,0),back_button)
        draw_text("Back",font,(255,255,255),screen,77,937)
        #workout file field
        pygame.draw.rect(screen,(0,0,0),workout_file_path_button)
        draw_text("Workout File Path: ",font,(0,0,0),screen,20,300)
        draw_text(workout_file_path,font,(255,255,255),screen,370,300)
        #routine file field
        pygame.draw.rect(screen,(0,0,0),routin_file_path_button)
        draw_text("Routin File Path: ",font,(0,0,0),screen,20,475)
        draw_text(routin_file_path,font,(255,255,255),screen,370,475)

        #loop necesities
        pygame.display.update()
        clock.tick(60)

def daily_menu():
    '''
    function for running the daily menu screen
    input: none
    output: none
    '''
    running = True
    while running:
        click = False
        #exit on screen close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True #leave menu

        #mouse input
        mx, my = pygame.mouse.get_pos()
        if back_button.collidepoint((mx,my)):
            if click:
                running = False

        #add images
        screen.blit(background,(0,0))
        draw_text("Daily Menu", font,(0,0,0),screen,800,40)
        pygame.draw.rect(screen,(0,0,0),back_button)
        draw_text("Back",font,(255,255,255),screen,77,937)
        pygame.draw.rect(screen,(0,0,0),routin_button)
        draw_text("Daily Routine",font,(255,255,255),screen,1385,425)
        pygame.draw.rect(screen,(0,0,0),workout_sch_button)
        draw_text("Daily Workout",font,(255,255,255),screen,1385,280)
        

        #loop necesities
        pygame.display.update()
        clock.tick(60)

main_loop()
