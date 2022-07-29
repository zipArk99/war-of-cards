import random
from this import d

class Card():
    def __init__(self,suit,number):
        """
        Card Model To Create Cards 
        """
        self.suit=suit
        self.number=number
        
    def __str__(self):
        """
        To print Info about card 
        """
        return '({},{})'.format(self.suit,self.number)

class Deck():
    """ 
    class to create card deck and shuffle it
    """
    def __init__(self):
        self.deck=[]
        self.suits=['club','spead','diamond','hearts']
        self.rank=[2,3,4,5,6,7,8,9,10,11,12,13,14]  
        
    def create_deck(self):
        for suit in self.suits:
            for num in self.rank:
                self.deck.append(Card(suit, num))
        
    def get_deck_of_card(self):
        random.shuffle(self.deck)
        return self.deck
             
    def __str__(self):
        if self.deck != []:
            for i in self.deck:
                print(i)
            return '\nLength of Deck::{}'.format(len(self.deck))
        else:
            return 'List is empty'
        
class Player():
    """ 
    Player class
    """
    def __init__(self):       
        self.player1_deck=[]
        self.player2_deck=[]
    
    def get_deck_and_divide(self,deck):
        for num,card in enumerate(deck):
            if(num%2==0):
                self.player1_deck.append(card)
            else:
                self.player2_deck.append(card)
    
    def get_a_card_from_player1(self):
        temp_card=self.player1_deck[0]
        self.player1_deck.pop(0)
        print(len(self.player1_deck))
        return temp_card
    
    def get_four_cards_from_player1(self):
        temp_cards=self.player1_deck[0:4]
        del self.player1_deck[0:4]
        return temp_cards
        
    
    def add_card_to_player1_deck(self,card):
        self.player1_deck.append(card)
        print(len(self.player1_deck))
    
    def get_player1_deck_length(self):
        return len(self.player1_deck)
        
    
    def get_a_card_from_player2(self):
        temp_card=self.player2_deck[0]
        self.player2_deck.pop(0)
        print(len(self.player2_deck))
        return temp_card
    
    def add_card_to_player2_deck(self,card):
        self.player2_deck.append(card)
        print(len(self.player2_deck))

    def get_four_cards_from_player2(self):
        temp_cards = self.player2_deck[0:4]
        del self.player2_deck[0:4]
        return temp_cards
    
    def get_player2_deck_length(self):
        return len(self.player2_deck)
    
        
    
    
    def __str__(self):
        for card in self.player1_deck:
            print(card)
        return ''
    
class GameLogic():
    
    def declare_war(self,player):
        player1_4_cards = player.get_four_cards_from_player1()
        player2_4_cards = player.get_four_cards_from_player2()

        while player1_4_cards[len(player1_4_cards)-1] == player2_4_cards[len(player1_4_cards)-1]:
            if(player.get_player1_deck_length() >= 4 and player.get_player2_deck_length()>=4):
                player1_4_cards.append(player.get_four_cards_from_player1())
                player2_4_cards.append(player.get_four_cards_from_player2())
            else:
                if(player.get_player1_deck_length() > player.get_player2_deck_length()):
                    print('player 1 wins')
                else:
                    print('player 2 wins')
        if(player1_4_cards[len(player1_4_cards)-1] > player2_4_cards[len(player1_4_cards)-1]):
            player.add_card_to_player1_deck([player1_4_cards,player2_4_cards])
        else:
            player.add_card_to_player2_deck([player1_4_cards, player2_4_cards])


   
    
    def compare_players_card(self,player):
        player1card = player.get_a_card_from_player1()
        player2card = player.get_a_card_from_player2()
        print(player1card)
        print(player2card)
        if(player1card.number == player2card.number):
            self.declare_war(player)
            
        elif(player1card.number > player2card.number  ):
            player.add_card_to_player1_deck([player1card,player2card])
            
        elif(player2card.number > player1card.number):
            player.add_card_to_player2_deck([player1card,player2card])
    
        
            
    
    
if __name__ == '__main__':
    deck=Deck()
    deck.create_deck()
    player=Player()
    player.get_deck_and_divide(deck.get_deck_of_card())
    gml=GameLogic()
    gml.compare_players_card(player) 
    
    
    
    
    
    

            
        
        





       

       
        

    