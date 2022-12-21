from random import shuffle

def prompt_for_teammate(cards, clue_word, number):
    allcards = []
    for l in cards.values():
        for card in l:
            allcards.append(card)
    shuffle(allcards)
    prompt = f"""You are playing the boardgame Codenames. You are the teammate.

Your clue word is "{clue_word}". You must guess {number} of words. All of these words need to be different.

The clue word relates to some of these words: {', '.join(allcards)}.

First, you have to guess only one word. You must not guess a word which is not in the game.

Your guess is: 
"""

    return prompt


def prompt_for_teammate_after_response(response):
    prompt = f"""{response}"""
    return prompt


def parse_teammate_response(response_text):
    tokens = [token for token in re.split(
        '[-, \n]', response_text) if token != '']
    return tokens[0]
