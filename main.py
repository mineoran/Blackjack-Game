import random
import os    #You could import os and then at the top of your script run os.system('cls')

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def total_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
#We wrote this line because the Ace has two different values. 11 and 1. 
    cards.remove(11)
    cards.append(1)
  return sum(cards)

""" Create a function called compare() and pass in the your_score and computer_score. 
If the computer and your both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. 
If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses.
If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins. """

def compare(your_score, computer_score):
  if your_score > 21 and computer_score > 21:
    return "You went over. You lose"
  if your_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "Lose, opponent has Blackjack "
  elif your_score == 0:
    return "Win with a Blackjack "
  elif your_score > 21:
    return "You went over. You lose "
  elif computer_score > 21:
    return "Computer went over. You win "
  elif your_score > computer_score:
    return "You win "
  else:
    return "You lose "

def play_game():
  user_cards = []
  computer_cards = []
  game_over = False

  for deck in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not game_over:
    user_score = total_score(user_cards)
    computer_score = total_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = total_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

play_game()