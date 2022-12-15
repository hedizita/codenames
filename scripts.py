import codenames
from codenames.codemaster import prompt_for_codemaster

cards = codenames.generate_codewords_board(codenames.EASY_WORDS, 3, 3, 3, 1)
prompt_for_codemaster(cards, "blue")
