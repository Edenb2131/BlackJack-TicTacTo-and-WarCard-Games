import random

types = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Card class icludes : type(heart etc'), rank, and some value
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

    def __init__(self, name):
        self.all_cards = []
        self.name = name

    def add_one(self, new_card):
        #extend is a way addint more then 1 thing(maybe we pass in a list)
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)

    def remove_one(self):
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# Setting up a new game

player_one = Player("one")
player_two = Player("two")

new_deck = Deck()
new_deck.shuffle()

# len(new_deck.all_card)/2 = 26
for x in range(26):
    player_one.add_one(new_deck.deal_one())
    player_two.add_one(new_deck.deal_one())


# Game Logic:

round_num = 0
game_on = True

while game_on:

    round_num+= 1
    print(f"this is round: {round_num}")
    #check to see if someone wins
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_one(player_one_cards)
            player_one.add_one(player_two_cards)
            at_war = False


        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_one(player_one_cards)
            player_two.add_one(player_two_cards)
            at_war = False



        else:
            print('WAR!')

            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            # First check to see if player has enough cards
            # Check to see if a player is out of cards:

            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break


            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False

                break

            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
