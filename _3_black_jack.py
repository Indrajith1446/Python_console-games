import random

suits = {"Hearts","Diamonds","Clubs","Spades"}
ranks = {'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace'}
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    
    def __str__(self):
        return (self.rank+" of "+self.suit+" value "+str(self.value))

class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        cardstr=""
        for card in self.deck:
            cardstr+="\n"+str(card)
        return cardstr

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
    
    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value-=10
            self.aces-=1

class Chips:
    
    def __init__(self):
        self.total = 100  
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    
    while True:

        try:
            chips.bet=int(input("Enter the amount of bet"))
        except ValueError:
            print("Enter a number. Try again")
        else:
            if chips.total < chips.bet:
                print(f"Sorry bet amount cannot exceed {chips.total}")
            else:
                print(f"Bet set for amount {chips.bet}")
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 
    
    while True:
        inp=input("Hit or Stand ? enter h/s ")
        if inp[0].lower()== 'h':
            print("Player choose to hit ")
            hit(deck,hand)
        
        elif inp[0].lower()== 's':
            print("Player choose to stand")
            playing=False
        
        else:
            print("Sorry unidentified input try again")
            continue

        break

def show_some(player,dealer):
    print("\nDealers Hand")
    print("*******")
    print("",dealer.cards[1])
    print("\nPlayers Hand",*player.cards,sep="\n")
    
def show_all(player,dealer):
    print("\nDealers Hand",*dealer.cards,sep="\n")
    print("Dealer value:",dealer.value)
    print("\nPlayers Hand",*player.cards,sep="\n")
    print("Player value:",player.value)

def player_busts(player,dealer,chips):
    print("Player loses")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer looses")
    chips.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.win_bet()
    
def push(player,dealer):
    print("Dealer and players on tie")

if __name__=="__main__":

    while True:

        print("Welcome to BlackJack")
        
        deck= Deck()
        deck.shuffle()

        player=Hand()
        player.add_card(deck.deal())
        player.add_card(deck.deal())

        dealer=Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
            
        player_chips=Chips()

        take_bet(player_chips)
        
        show_some(player,dealer)
        
        while playing:  
            
            hit_or_stand(deck,player)
            
            show_some(player,dealer)

            if player.value>21:
                player_busts(player,dealer,player_chips)
                break

        if player.value <=21:
            
            while dealer.value<17:
                hit(deck,dealer)
        
            show_all(player ,dealer)

            if dealer.value>21:
                dealer_busts(player,dealer,player_chips)
            
            elif dealer.value>player.value:
                dealer_wins(player,dealer,player_chips)

            elif dealer.value<player.value:
                player_wins(player,dealer,player_chips)

            else:
                push(player,dealer)

        print(f"Player wins with chips {player_chips.total}")

        cont=input("\nPlay another hand? Enter 'y' or 'n' ")
        if cont[0].lower()=='y':
            playing=True
            continue
        else:
            print("\nThank you Game ENDED\n")
            break
        