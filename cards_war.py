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
    def __init__(self):
        
        self.deck=[]
        self.suits=['club','spead','diamond','hearts']
        self.rank=[2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']  
        
    def create_deck(self):
        for suit in self.suits:
            for num in self.rank:
                self.deck.append(Card(suit, num))
                
    def shuffle_deck(self):
        random.shuffle(self.deck)
                
    def get_deck_of_card(self):
        return self.deck
                  
    def __str__(self):
        if self.deck != []:
            for i in self.deck:
                print(i)
            return '\nLength of Deck::{}'.format(len(self.deck))
        else:
            return 'List is empty'
            
            
deck1=Deck()
deck1.create_deck()
deck1.shuffle_deck()
print(deck1)
            
        
        





       

       
        

    