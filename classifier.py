#classifying the cards with a different class
import pygame

# ignore this importing images 
#list 
my_deck = []

# ok heres where the class actually starts 

class CardDeck:
#appending the cards, their images, and integers to a list so i can access the cards and their elements in my main class 
    def __init__(self, num, imglink):
        self.num = num
        self.imglink = imglink

    @staticmethod
    def load_cards():
        my_deck = []
        for i in range(1, 5):
            if i == 1:
                for x in range(1, 14):
                    club_img = pygame.image.load(f"War_Card_Game/{x}c.png")
                    card = CardDeck(x, club_img)
                    my_deck.append(card)
            elif i == 2:
                for x in range(1, 14):
                    heart_img = pygame.image.load(f"War_Card_Game/{x}h.png")
                    card = CardDeck(x, heart_img)
                    my_deck.append(card)
            elif i == 3:
                for x in range(1, 14):
                    spade_img = pygame.image.load(f"War_Card_Game/{x}s.png")
                    card = CardDeck(x, spade_img)
                    my_deck.append(card)
            elif i == 4:
                for x in range(1, 14):
                    diamond_img = pygame.image.load(f"War_Card_Game/{x}d.png")
                    card = CardDeck(x, diamond_img)
                    my_deck.append(card)
        return my_deck


CardDeck.load_cards()
