from random import sample

def generate_codewords_board(words, blue = 4 , red = 4, neutral = 4, bomb = 1): # 13
  word_cards = sample(words, blue + red + neutral + bomb)
  board_cards = {}
  board_cards['blue'] = word_cards[:blue] #9 blue cards
  board_cards['red'] = word_cards[blue:blue+red] #8 red cards
  board_cards['neutral'] = word_cards[blue+red:blue+red+neutral] # remaining are neutral
  board_cards['bomb'] = word_cards[blue+red+neutral:]
  return board_cards