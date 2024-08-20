import random
import time

valid_play = ("y", "n")
play = ""

cards = [
    "2c",
    "3c",
    "4c",
    "5c",
    "6c",
    "7c",
    "8c",
    "9c",
    "10c",
    "Jc",
    "Qc",
    "Kc",
    "Ac",
    "2d",
    "3d",
    "4d",
    "5d",
    "6d",
    "7d",
    "8d",
    "9d",
    "10d",
    "Jd",
    "Qd",
    "Kd",
    "Ad",
    "2s",
    "3s",
    "4s",
    "5s",
    "6s",
    "7s",
    "8s",
    "9s",
    "10s",
    "Js",
    "Qs",
    "Ks",
    "As",
    "2h",
    "3h",
    "4h",
    "5h",
    "6h",
    "7h",
    "8h",
    "9h",
    "10h",
    "Jh",
    "Qh",
    "Kh",
    "Ah",
]

card_values = {
    "2c": 2,
    "3c": 3,
    "4c": 4,
    "5c": 5,
    "6c": 6,
    "7c": 7,
    "8c": 8,
    "9c": 9,
    "10c": 10,
    "Jc": 10,
    "Qc": 10,
    "Kc": 10,
    "Ac": 11,
    "2d": 2,
    "3d": 3,
    "4d": 4,
    "5d": 5,
    "6d": 6,
    "7d": 7,
    "8d": 8,
    "9d": 9,
    "10d": 10,
    "Jd": 10,
    "Qd": 10,
    "Kd": 10,
    "Ad": 11,
    "2s": 2,
    "3s": 3,
    "4s": 4,
    "5s": 5,
    "6s": 6,
    "7s": 7,
    "8s": 8,
    "9s": 9,
    "10s": 10,
    "Js": 10,
    "Qs": 10,
    "Ks": 10,
    "As": 11,
    "2h": 2,
    "3h": 3,
    "4h": 4,
    "5h": 5,
    "6h": 6,
    "7h": 7,
    "8h": 8,
    "9h": 9,
    "10h": 10,
    "Jh": 10,
    "Qh": 10,
    "Kh": 10,
    "Ah": 11,
}


def calculate_hand_value(hand):
    value = 0
    aces = 0

    for card in hand:
        card_value = card_values[card]
        value += card_value
        if card.startswith("A"):
            aces += 1
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value


# Ask if the player wants to play
while play not in valid_play:
    play = input("Welcome. Would you like to play blackjack? (y/n): ")
    if play not in valid_play:
        print("Invalid answer")
    elif play == "n":
        quit()

balance = 0

# Get the deposit amount
while balance <= 0:
    deposit = input("How much would you like to deposit?: $")
    if deposit.isdigit():
        balance += int(deposit)
        print(f"Your playable balance is ${balance}")
    else:
        print("Please enter a valid amount.")

while balance > 0:
    # Get the bet amount
    bet = 0
    while bet <= 0 or bet > balance:
        bet = input(f"Your balance is ${balance}. How much would you like to bet?: $")
        if bet.isdigit():
            bet = int(bet)
            if bet > balance:
                print(f"You cannot bet more than your balance of ${balance}.")
            elif bet <= 0:
                print("Please enter a positive amount.")
        else:
            print("Please enter a valid amount.")

    balance -= bet
    print(f"You bet ${bet}. Remaining balance: ${balance}")

    # Shuffle and deal cards
    random.shuffle(cards)
    dealer_cards = random.sample(cards, 2)
    player_cards = random.sample(cards, 2)
    dealer_value = calculate_hand_value(dealer_cards)
    player_value = calculate_hand_value(player_cards)

    print(f"The Dealers's cards are {dealer_cards} and their value is {dealer_value}.")
    time.sleep(2)
    print(f"The Player's cards are {player_cards} and their value is {player_value}.")
    time.sleep(2)

    if dealer_value == 21:
        print("Dealer has Blackjack! You lose.")
        continue
    if player_value == 21:
        print("Player has Blackjack! You win!")
        balance += bet * 2.5
        continue

    # Player's turn
    while player_value < 21:
        valid_ans1 = ("a", "b")
        ans1 = ""
        while ans1 not in valid_ans1:
            ans1 = input(
                f"Your card value is {player_value}. Would you like to Hit or Stand? \n(a) HIT \n(b) STAND\nYour Choice: "
            )
        if ans1 == "a":
            hit = random.sample(cards, 1)[0]
            player_cards.append(hit)
            player_value = calculate_hand_value(player_cards)
            print(f"Your cards are {player_cards} and their value is {player_value}")
            if player_value > 21:
                print("You bust! The Dealer wins.")
                break
        elif ans1 == "b":
            print(f"Player chooses to stand. Your card value is {player_value}.")
            break

    # Dealer's turn
    if player_value <= 21:
        while dealer_value < 18:
            hit = random.sample(cards, 1)[0]
            dealer_cards.append(hit)
            dealer_value = calculate_hand_value(dealer_cards)
            print(
                f"Dealer's cards are {dealer_cards} and their value is {dealer_value}."
            )
            time.sleep(2)
            if dealer_value > 21:
                print("Dealer busts! You win.")
                balance += bet * 2
                break

    # Determine winner if both player and dealer are under 21
    if player_value <= 21 and dealer_value <= 21:
        if player_value > dealer_value:
            balance += bet * 2
            print(f"You win! Your balance is now ${balance}.")
        elif player_value < dealer_value:
            print(f"You lose! Your balance is now ${balance}.")
        else:
            balance += bet
            print(f"It's a tie! You get your bet back. Your balance is ${balance}.")

    # Check if player wants to continue or quit
    play = ""
    while play not in valid_play:
        play = input("Do you want to play again? (y/n): ")
        if play == "n":
            quit()
