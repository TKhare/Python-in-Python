
import pygame
import sys
import random
import time
 

#Pygame Init
check_errors = pygame.init()
if check_errors[1] > 0:
	print('%d errors occured: exiting...',check_errors[1])
	sys.exit()
else:
	print('Successful Initialization!')

#Display Surface
playerSurface = pygame.display.set_mode((720,500))

#Tab Caption
pygame.display.set_caption('Snake4Godz by Tejas')
time.sleep(10)

#Colors
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
grey = pygame.Color(217, 217, 217) #background
blue = pygame.Color(0, 0, 255) 
brown = pygame.Color(104, 58, 9) #food

#Game Variables

	#FramesPerSecond Controller
fpsController = pygame.time.Clock()  

	#Important Variables
snakePosition = [360,250]
snakeBody = [[360,250], [350,250]]
foodPos = [random.randrange(1,72)*10,random.randrange(1,50)*10]
foodSpawn = True

	#Direction
direction = 'RIGHT'
changeto = direction

#Game Over :(
def gameOver():
        Font1 = pygame.font.SysFont('monaco', 72)
        goSurface = Font1.render('Game Over!', True, red)
        gorect = goSurface.get_rect()
        gorect.midtop = (360, 15)
        playerSurface.blit(goSurface,gorect)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    

#MLG Main Logic of Game
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit
			sys.exit
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'): #ASCII value of D
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'): #ASCII value of A
				changeto = 'LEFT'

			if event.key == pygame.K_UP or event.key == ord('w'): #ASCII value of W
				changeto = 'UP'

			if event.key == pygame.K_DOWN or event.key == ord('s'): #ASCII value of S
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))

	if changeto=='RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	
	if changeto=='LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'

	if changeto=='UP' and not direction == 'DOWN':
		direction = 'UP'


	if changeto=='DOWN' and not direction == 'UP':
		direction = 'DOWN'

	if direction == 'RIGHT':
		snakePosition[0] += 10

	if direction == 'LEFT':
		snakePosition[0] -= 10

	if direction == 'DOWN':
		snakePosition[1] += 10

	if direction == 'UP':
		snakePosition[1] -= 10

#Snake Body
	snakeBody.insert(0, list(snakePosition))
	if snakePosition[0] == foodPos[0] and snakePosition[1] == foodPos[1]:
		foodSpawn = False
	else:
		snakeBody.pop()
       
	#Food Spawn
	if foodSpawn == False:
		foodPos = [random.randrange(1,72)*10,random.randrange(1,50)*10]
	foodSpawn = True
   
	playerSurface.fill(grey)
	
	for pos in snakeBody:
		pygame.draw.rect(playerSurface, green, pygame.Rect(pos[0],pos[1],10,10))
	
	pygame.draw.rect(playerSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
#Boundary Death
	if snakePosition[0] > 710 or snakePosition[0] < 10:
		gameOver()
	if snakePosition[1] > 490 or snakePosition[1] < 10:
		gameOver()
	for segment in snakeBody[1:]:
		if snakePosition[0] == segment[0] and snakePosition[1] == segment[1]:
			gameOver()

	pygame.display.flip()
	fpsController.tick(25)
