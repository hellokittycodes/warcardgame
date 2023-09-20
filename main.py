import pygame
from classifier import CardDeck
import random 

pygame.init()
screen = pygame.display.set_mode((900,500))
pygame.display.set_caption('WAR')
clock = pygame.time.Clock() 

#boolean
clicked = False 

#img size
DFLT_IMG_SZ = (150,200)

#cover 
cover = True 


#card cover img loads
cover_One = pygame.image.load('War_Card_Game/card_cover.png')
cover_Two = pygame.image.load('War_Card_Game/card_cover.png')


#scaling the image
cover_One = pygame.transform.scale(cover_One, DFLT_IMG_SZ)
cover_Two = pygame.transform.scale(cover_Two, DFLT_IMG_SZ)


#current Card var 
current_Card_1 = None 
current_Card_2 = None

#list 
list = []

#carddeckloadcards
my_deck = CardDeck.load_cards()

#___________________________________________________________________________________

## button parameters 
b_w = 600
b_h = 50
b_color = (0, 0, 0) #red 
b_textcolor = (255, 255, 255) #black 
font = pygame.font.SysFont("Arial", 12)
b_surface = pygame.Surface((b_w, b_h))
text = font.render("Hello, and Welcome to War! Click To Generate Cards and Press Space + Click To Play Again", True, b_textcolor) 
text_rect = text.get_rect(center=(b_w // 2, b_h // 2))
b_surface.blit(text, text_rect)
three_card_count = None 

#___________________________________________________________________________________
## FUNCTIONS 

def win_button(): 
  text = font.render("You Won!", True, b_textcolor) 
  screen.blit(b_surface, (150,400))


def lose_button(): 
  text = font.render("You Lost!", True, b_textcolor) 
  screen.blit(b_surface, (150,400)) 

def tie_button() : 
  text = font.render("You Tied!", True, b_textcolor) 
  screen.blit(b_surface, (150,400)) 
  
#___________________________________________________________________________________



#update  
running = True
while running :
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False 
  key = pygame.key.get_pressed()
 
  screen.fill((20,137,40)) 
  pygame.display.update() 

  # draw all elements
  # update everything here 
  screen.blit(cover_One, (270, 150))
  screen.blit(cover_Two, (470, 150))

  
  if cover == False : 
    screen.fill((20,137,40))

  
  rand_Blit_1 = random.choice(my_deck)
  rand_Blit_2 = random.choice(my_deck)
  
  if rand_Blit_1.num > rand_Blit_2.num : 
    win_button() 
    b_surface.blit(text, text_rect)
  elif rand_Blit_1.num < rand_Blit_2.num : 
    lose_button() 
    b_surface.blit(text, text_rect)
  elif rand_Blit_1.num == rand_Blit_2.num :
    tie_button() 
    b_surface.blit(text, text_rect)

  if event.type == pygame.MOUSEBUTTONDOWN and clicked == False : 
    clicked = True 
    cover = False 
    current_Card_1 = rand_Blit_1.imglink
    current_Card_2 = rand_Blit_2.imglink 
    
  if clicked :
    screen.blit(current_Card_1, (290, 190))
    screen.blit(current_Card_2, (500, 182))

  

  
  if key[pygame.K_SPACE] : 
    clicked = False 

  pygame.display.update() 
  clock.tick(60)

## randomized cards showing 
## boolean clicked = True
## if click then screen.blit(random.choice(list)), clicked = False
## if clicked = False then stop screen blitting or whatever
