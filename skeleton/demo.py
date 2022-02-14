import pygame, sys, random

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

#Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

#Game Variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7
score_time = None
current_time = 0

#Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 24)

while True:
	#Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            
    #Ball Animation
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        #Reset ball
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_x = 7 * random.choice((1,-1))
        ball_speed_y = 7 * random.choice((1,-1))
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        #Reset ball
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_x = 7 * random.choice((1,-1))
        ball_speed_y = 7 * random.choice((1,-1))
        
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        ball_speed_x *= -1
    if ball.colliderect(opponent) and ball_speed_x < 0:
        ball_speed_x *= -1

    #Player Animation
    player.y += player_speed
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if player.top <= 0:
        player.top = 0

    #Opponent AI
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))



    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (610, 350))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (580, 350))	

    # Updating the window 
    pygame.display.flip()
    clock.tick(60)
