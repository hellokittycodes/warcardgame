import pygame
from classifier import CardDeck
import random 

pygame.init()
screen = pygame.display.set_mode((900,500))
pygame.display.set_caption('WAR')
clock = pygame.time.Clock() 
pygame.font.init()  

#this will come in handy for later - these are instructions on how to use the game, blitting text instructions on the screen 
my_font_1 = pygame.font.SysFont('Comic Sans MS', 30)
my_font_2= pygame.font.SysFont('Comic Sans MS', 30)
my_font_3 = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font_1.render('Click To Generate Two Cards. Press Space To Take Them Off The Screen.', False, (0, 0, 0))
text_surface_1 = my_font_2.render('You', False, (0, 0, 0))
text_surface_2 = my_font_3.render('Computer', False, (0, 0, 0))


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

#_________________________________________________________________

## button parameters 
b_w = 600
b_h = 50
b_color = (0, 0, 0) #red 
b_textcolor = (255, 255, 255) #white 
font = pygame.font.SysFont("Arial", 12)
b_surface = pygame.Surface((b_w, b_h))
text = font.render("Hello, and Welcome to War! Click To Generate Cards and Press Space + Click To Play Again", True, b_textcolor) 
text_rect = text.get_rect(center=(b_w // 2, b_h // 2))
b_surface.blit(text, text_rect)
 
#_______________________________________________________________
# update text in the function to display the result of war 

def update(screen, fstring):
    b_w = 600
    b_h = 50
    b_color = (0, 0, 0)  # Red
    b_textcolor = (255, 255, 255)  # White
    font = pygame.font.SysFont("Arial", 12)
    text = font.render(fstring, True, b_textcolor)
    
    # Calculate the center position of the text
    text_x = (screen.get_width() - text.get_width()) // 2
    text_y = (screen.get_height() - text.get_height()) // 2
    
    screen.fill(b_color, (0, 450, 900, 50))  # Clear the previous text
    screen.blit(text, (text_x, text_y))

  
#_________________________________________________________________
## FUNCTIONS 
# utilizing my "update" function 

def win_button(screen): 
  update(screen, "You Won!")

def lose_button(screen): 
  update(screen, "You Lost!")

def tie_button(screen) : 
  update(screen, "You Tied!")
  
def blank_button(screen):
    update(screen, 'Click')
  
#_________________________________________________________________
# ...

# Define variables to track round outcomes
ROUND_OUTCOME_WIN = 1
ROUND_OUTCOME_LOSE = 2
ROUND_OUTCOME_TIE = 3
round_outcome = None

# ...

#update  
running = True


while running:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            cover = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            clicked = False
            cover = True
            round_outcome = None
            
    key = pygame.key.get_pressed()
        
    screen.fill((20, 137, 40))
    # Draw all elements
    # Update everything here
    screen.blit(cover_One, (270, 150))
    screen.blit(cover_Two, (470, 150))
    screen.blit(text_surface, (100,50))
    screen.blit(text_surface_2, (500,355))
    screen.blit(text_surface_1, (320,355))

    if cover == False:
        screen.fill((20, 137, 40))
        screen.blit(text_surface, (100,50))
        screen.blit(text_surface_2, (500,355))
        screen.blit(text_surface_1, (320,355))
        

    if not clicked:
    
        rand_Blit_1 = random.choice(my_deck)
        rand_Blit_2 = random.choice(my_deck)
        current_Card_1 = rand_Blit_1.imglink
        current_Card_2 = rand_Blit_2.imglink

    # if your number is bigger, smaller, or the same, correlating it to the expected outcome


    # displaying round outcome on the screen
    if round_outcome == ROUND_OUTCOME_WIN:
        win_button(screen)
    elif round_outcome == ROUND_OUTCOME_LOSE:
        lose_button(screen)
    elif round_outcome == ROUND_OUTCOME_TIE:
        tie_button(screen)
    elif round_outcome == None:
        blank_button(screen)

    ## if you click then the card covers will disappera 
    if event.type == pygame.MOUSEBUTTONDOWN and clicked == False: 
        clicked = True 
        cover = False 

    if clicked:
        current_Card_1 = current_Card_1 = rand_Blit_1.imglink
        current_Card_2 = current_Card_2 = rand_Blit_2.imglink
        screen.blit(current_Card_1, (290, 190))
        screen.blit(current_Card_2, (500, 182))

        if rand_Blit_1.num > rand_Blit_2.num:
            round_outcome = ROUND_OUTCOME_WIN
        elif rand_Blit_1.num < rand_Blit_2.num:
            round_outcome = ROUND_OUTCOME_LOSE
        elif rand_Blit_1.num == rand_Blit_2.num: 
            round_outcome = ROUND_OUTCOME_TIE
        else:
            round_outcome = None

     # cards disappear when you press space key
 
    pygame.display.update() 
    clock.tick(60)

# ...
