import random

suits= { 'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks= { 'Two','Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values= { 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return (f"{self.rank} of {self.suit} rank {self.value}")

class Deck:

    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        deck_cards=''
        for card in self.deck:
            deck_cards+="\n"+str(card)
        return deck_cards

    def deal(self):
        return self.deck.pop()

class Player:

    def __init__(self,name):
        self.name=name
        self.player_hand=[]

    def remove_one(self):
        return self.player_hand.pop(0)

    def add_one(self,cards):
        if type(cards)==type([]):
            self.player_hand.extend(cards)
        else:
            self.player_hand.append(cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.player_hand)}"


if __name__=="__main__":


    play_again=True
    while play_again:
        print("COMPUTER VS COMPUTER")
        player1=Player("player1")
        player2=Player("player2")
        deck=Deck()
        deck.shuffle()
        for i in range(26):
            player1.add_one(deck.deal())
            player2.add_one(deck.deal())
        game_size=5
        game_on=True
        round=0
        while game_on:
            round+=1
            print(f"Round {round}")
            if len(player1.player_hand)== 0:
                print(f"{player1.name} out of cards \n Game Over \n {player2.name} wins")
                game_on=False
                break

            if len(player2.player_hand)== 0:
                print(f"{player2.name} out of cards \n Game Over \n {player1.name} wins")
                game_on=False
                break
            
            player1_cards_on_table=[]
            player2_cards_on_table=[]

            player1_cards_on_table.append(player1.remove_one())
            player2_cards_on_table.append(player2.remove_one())

            war=True

            while war:

                if player1_cards_on_table[-1].rank > player2_cards_on_table[-1].rank:
                    player1.add_one(player1_cards_on_table)
                    player1.add_one(player2_cards_on_table)
                    war=False
                    break

                if player2_cards_on_table[-1].value > player1_cards_on_table[-1].value:
                    player2.add_one(player1_cards_on_table)
                    player2.add_one(player2_cards_on_table)
                    war=False
                    break

                else:
                    print("WAARRR!!!!")

                    if len(player1.player_hand) < game_size:
                        print(f"{player1.name} doesn't have enough cards to continue war\nGame Over!\n{player2.name} wins")
                        game_on=False
                        break

                    if len(player2.player_hand) < game_size :
                        print(f"{player2.name} doesn't have enough cards to continue war\nGame Over!\n{player1.name} wins")
                        game_on=False
                        break

                    else:
                        for i in range(game_size):
                            player1_cards_on_table.append(player1.remove_one())
                            player2_cards_on_table.append(player2.remove_one())
        while True:
            try:
                cont_game=input("Simulate game again ? Y/N")
                if cont_game[0]=='y' or cont_game[0]=='Y':
                    play_again=True
                    break
                if cont_game[0]=='n' or cont_game[0]=='N':
                    play_again=False
                    break
            except:
                print("wrong input try again")
