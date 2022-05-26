import random

types = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}


class Card:
    def __init__(self, type, rank):
        self.type = type
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.type

class Deck:
    #making a list with all 52 cards in a deck
    def __init__(self):
        self.all_cards = []
        for type in types:
            for rank in ranks:
                self.all_cards.append(Card(type , rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

print("Welcome to the Israel's best BLACK-JACK mechine!")

#setting up the game
player = Player("eden", int(input("How much money you have ?")))
deck = Deck()
deck.shuffle()

game_on = True

while game_on:


    if int(player.balance) <= 0:
        print("Sorry, you wasted all your money!")
        game_on = False
        break


    #checking the input
    while True:
        player_bet = int(input("How much money you want to bet?"))
        if player_bet > player.balance:
            print(f"You cant bet less then your balance! your balancw is : {player.balance} $")
        else:
            break

    player_cards = [deck.deal_one(), deck.deal_one()]
    dealer_cards = [deck.deal_one(), deck.deal_one()]

    #showing the dealer hand
    print(f"The dealers card are: {dealer_cards[0]} and an hidden one")

    # showing your hand
    print(f"Your cards are: {player_cards[0]} and {player_cards[1]}")


    while True:
        player_sum = 0
        dealer_sum = 0
        player_fail = False
        for card in player_cards:
            player_sum += card.value

        #check if Ace
        if player_sum < 21 and player_cards[0].rank == 'Ace' or player_cards[1].rank == 'Ace':
            print("Ace was found!")
            player_sum -= 10

        print(f"your sum is: {player_sum}")

        if player_sum > 21:
            print("you lose!")
            player.balance -= player_bet
            player_fail = True
            break

        answer = input("Do you wish to hit or stay ?")
        if answer.lower() == 'hit':
            player_cards.append(deck.deal_one())
            print("your new card is : {}".format(player_cards[-1]))
        else:
            break

    print(f"The dealers card are: {dealer_cards[0]} and {dealer_cards[1]}")
    for card in dealer_cards:
        dealer_sum += card.value
    print(f"The dealers sum is: {dealer_sum}")

    # need to add a while loop until dealers cards are more the 17
    while True and player_fail is False:
        if dealer_sum <= 17:
            print("dealer draw another card!")
            dealer_cards.append(deck.deal_one())
            dealer_sum += dealer_cards[-1].value
            print(f"dealer draw : {dealer_cards[-1]} and his sum is: {dealer_sum}")
        else:
            break

    if dealer_sum > 21:
        print("The player has won!")
        player.balance += player_bet


    elif player_sum > dealer_sum and player_sum <= 21:
        print("The player has won!")
        player.balance += player_bet


    elif player_sum < dealer_sum:
        print("The dealer has won!")
        player.balance -= player_bet

    elif player_sum == dealer_sum:
        print("its a tie!")

    print(f"hey {player.name}! Your balance is: {player.balance}")

    answer = input("Do you want to play again ?")
    if answer.lower() != 'yes':
        game_on = False
        print("Thx!")
        break

print(f"hey {player.name}! Your balance is: {player.balance}")










