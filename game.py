from cap import Shape, Colour, Card, Player
from random import shuffle

def get_colour():
    print("The colour options are:")
    colours = list(Colour)
    for i, colour in enumerate(colours, start=1):
        print(f"{i}. {colour.name}")
    option = int(input("Which colour do you want? "))
    return colours[option - 1]

def get_shape():
    print("The shape options are:")
    shapes = list(Shape)
    for i, shape in enumerate(shapes, start=1):
        print(f"{i}. {shape.name}")
    option = int(input("Which shape do you want? "))
    return shapes[option - 1]

def get_number():
    return int(input("Enter a number from 1-4 (inclusive): "))

def ask_question(player):
    print("Which question would you like to ask?")
    print("1. How many cards with a certain colour?")
    print("2. How many cards with a certain shape?")
    print("3. How many cards with a certain number?")
    print("4. How many cards with a certain colour and number?")
    print("5. How many cards with a certain shape and number?")
    print("6. How many cards with a certain colour and shape?")
   
    option = input("Which option would you like? ")

    if option == "1":
        colour = get_colour()
        count = player.how_many_colour(colour)
        print(f"The player has {count} cards with colour {colour}.")
    elif option == "2":
        shape = get_shape()
        count = player.how_many_shape(shape)
        print(f"The player has {count} cards with shape {shape}.")
    elif option == "3":
        number = get_number()
        count = player.how_many_number(number)
        print(f"The player has {count} cards with number {number}.")
    elif option == "4":
        colour = get_colour()
        number = get_number()
        count = player.how_many_colour_number(colour, number)
        print(f"The player has {count} cards with colour {colour} and number {number}.")
    elif option == "5":
        shape = get_shape()
        number = get_number()
        count = player.how_many_shape_number(shape, number)
        print(f"The player has {count} cards with shape {shape} and number {number}.")
    elif option == "6":
        colour = get_colour()
        shape = get_shape()
        count = player.how_many_colour_shape(colour, shape)
        print(f"The player has {count} cards with colour {colour} and shape {shape}.")
    else:
        print("That is not an option, try again.")
        ask_question(player)

def guess_card(player, guessed_cards):
    colour = get_colour()
    shape = get_shape()
    number = get_number()
    card = Card(colour, shape, number)
   
    if player.has_card(card):
        return card
    else:
        print(f"The player does not have the card {card}.")
        return None

def play(player):
    print("Welcome to Sleuth!")
   
    questions_asked = 0
    incorrect_guesses = 0
    guessed_cards = []

    while len(guessed_cards) < 3:
        print("Would you like to:")
        print("1. Ask a question.")
        print("2. Guess a card.")
        option = input("Which option would you like? ")
       
        if option == "1":
            questions_asked += 1
            ask_question(player)
        elif option == "2":
            card_guessed = guess_card(player, guessed_cards)
            if card_guessed:
                if card_guessed in guessed_cards:
                    print(f"The player has the card {card_guessed}.")
                    print("But you already knew that.")
                else:
                    print(f"The player has the card {card_guessed}.")
                    print("Good guess!")
                    guessed_cards.append(card_guessed)
            else:
                incorrect_guesses += 1
        else:
            print("That is not an option, try again.")

    print("Congratulations!")
    print(f"It took you {questions_asked} questions and {incorrect_guesses} incorrect guesses.")
    print(f"The player's hand was: {', '.join(map(str, player.hand))}")

if __name__ == "__main__":
    deck = []
    for colour in Colour:
        for shape in Shape:
            for number in range(1, 5):
                deck.append(Card(colour, shape, number))
    shuffle(deck)
    play(Player(deck[0:3]))
