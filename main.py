# imports
import pygame, os, sys

# center pygame window on display
# technique found at https://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# initialize pygame
pygame.init()

# constants
WIDTH = 400
HEIGHT = 300
FPS = 4

# RGB colors
white = (255, 255, 255)
black = (0, 0, 0)

# variables
image_count = 0 # counter for images
clock = pygame.time.Clock() # clock object
running = True
timer = 0

# load images into pygame
my_images = [
pygame.image.load('./assets/sherry_1.png'),
pygame.image.load('./assets/sherry_2.png'),
pygame.image.load('./assets/sherry_3.png'),
pygame.image.load('./assets/sherry_4.png')
]

# changes size of all images to fit screen
for i in range(len(my_images)):
  my_images[i] = pygame.transform.scale(my_images[i], (150, 150))

# set Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flower :)")
WINDOW.fill(white)

# set up your font
font = pygame.font.Font('./fonts/Montserrat-Light.ttf', 12)

# create your text
text = font.render('growth is growth, no matter how small.', True, black, white)
textRect = text.get_rect()

creds = font.render('Artist: Delaney Sherry',True, black,white)
credsRect = text.get_rect()
creds2 = font.render('Programmers: Lucia D',True, black,white)
credsRect2 = text.get_rect()
creds3 = font.render('& Gin N',True, black,white)
credsRect3 = text.get_rect()
# position the text
textRect.center = (275, 100)

credsRect.center = (275, 200)
credsRect2.center = (275, 215)
credsRect3.center = (275, 230)
# display text
WINDOW.blit(text, textRect)
WINDOW.blit(creds, credsRect)
WINDOW.blit(creds2, credsRect2)
WINDOW.blit(creds3, credsRect3)
pygame.display.flip()

# draw shape function
def drawShape():
  global my_images
  global image_count
  if (image_count == 4):
     image_count = 0
  WINDOW.blit(my_images[image_count], (0, 100))
  pygame.display.flip()
  image_count += 1
  
# main animation Loop that will run for 10 seconds
while running and timer < 50:

  # upadate screen according to FPS value
  clock.tick(FPS)

  # update timer
  timer += 1

  # check if "X" is clicked by user 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()

  # call to drawShape function
  drawShape()