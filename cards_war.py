import random

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
        return temp_card
    
    def get_four_cards_from_player1(self):
        temp_cards=self.player1_deck[0:4]
        del self.player1_deck[0:4]
        return temp_cards
        
    
    def add_card_to_player1_deck(self,card):
        self.player1_deck.extend(card)
     
    
    def get_player1_deck_length(self):
        return len(self.player1_deck)    
    
    def get_a_card_from_player2(self):
        temp_card=self.player2_deck[0]
        self.player2_deck.pop(0)
        return temp_card
    
    def add_card_to_player2_deck(self,card):
        self.player2_deck.extend(card)

    def get_four_cards_from_player2(self):
        temp_cards = self.player2_deck[0:4]
        del self.player2_deck[0:4]
        return temp_cards
    
    def get_player2_deck_length(self):
        return len(self.player2_deck)
    
    def comapre_two_cards(self):
        if(self.player1_deck[0].number==self.player2_deck[0].number):
            return True
        else:
            return False
    
        
    
    
    def __str__(self):
        for card in self.player1_deck:
            print(card)
        return ''
    
class GameLogic():
    
    
    
    def check_if_deck_is_over(self, player):
        if (player.get_player1_deck_length() == 0 or player.get_player2_deck_length() == 0):
            return True
        else:
            return False



    def check_who_wins(self,player):
        if(player.get_player1_deck_length() > player.get_player2_deck_length()):
            print('player 1 wins')
            
        else:
            print('player 2 wins')
            
    def declare_war(self,player):
        if(player.get_player1_deck_length() >= 4 and player.get_player2_deck_length() >=4):
            self.player1_4_cards = player.get_four_cards_from_player1()
            self.player2_4_cards = player.get_four_cards_from_player2()
            
          
            
            while (self.player1_4_cards[len(self.player1_4_cards)-1].number == self.player2_4_cards[len(self.player2_4_cards)-1].number):
                if(player.get_player1_deck_length() >= 4 and player.get_player2_deck_length() >= 4):
                    self.player1_4_cards.extend(player.get_four_cards_from_player1())
                    self. player2_4_cards.extend(player.get_four_cards_from_player2())
                else:
                    if(player.get_player1_deck_length() > player.get_player2_deck_length()):
                        print('player 1 wins')
                        return False
                    else:
                        print('player 2 wins')
                        return False
         
            if(self.player1_4_cards[len(self.player1_4_cards)-1].number > self.player2_4_cards[len(self.player2_4_cards)-1].number):
                cards = self.player1_4_cards+self.player2_4_cards
                player.add_card_to_player1_deck(cards)
                return True
            else:
                cards = self.player1_4_cards + self.player2_4_cards
                player.add_card_to_player2_deck(cards)
                return True 
        else:
            self.check_who_wins(player)
            return False

        
    def compare_players_card(self,player):
        
        self.player1card = None
        self.player2card = None
        self.player1_deck_length = player.get_player1_deck_length()
        self.player2_deck_length = player.get_player2_deck_length()
        
        
        while True:
            if(player.comapre_two_cards()):
                continue_game=self.declare_war(player)
                if(continue_game):
                    if(self.check_if_deck_is_over(player)):
                        self.check_who_wins(player)
                        break
                    else:
                        continue
                else:
                    break
                
            self.player1card = player.get_a_card_from_player1()
            self.player2card = player.get_a_card_from_player2()
            
            print(self.player1card)
            print(self.player2card)
        
            
            if(self.player1card.number > self.player2card.number):
                cards=[self.player1card,self.player2card]
                player.add_card_to_player1_deck(cards);

            elif(self.player2card.number > self.player1card.number):
                cards = [self.player1card, self.player2card]
                player.add_card_to_player2_deck(cards)
                
            self.player1_deck_length = player.get_player1_deck_length()
            self.player2_deck_length = player.get_player2_deck_length()
            
            print('player 1 len::{}'.format(self.player1_deck_length))
            print('player 2 len::{}'.format(self.player2_deck_length))
                
            if(self.check_if_deck_is_over(player)):
                self.check_who_wins(player)
                break
    
if __name__ == '__main__':
    deck=Deck()
    deck.create_deck()
    player=Player()
    player.get_deck_and_divide(deck.get_deck_of_card())
    gml=GameLogic()
    gml.compare_players_card(player) 
    