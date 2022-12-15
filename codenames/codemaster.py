import re


def prompt_for_codemaster(cards, team):
    opponent = {'red': 'blue', 'blue': 'red'}
    prompt = f"""You are playing Codenames, you are the Codemaster.
Find clue word that is related to words from Group A but not related to words from Group B or the Bomb words or the Neutral words.

Group A: {', '.join(cards[team])}.
Group B: {', '.join(cards[opponent[team]])}.
Neutral: {', '.join(cards['neutral'])}.
Bomb words: {', '.join(cards['bomb'])}.

The clue word must not be the same as any of the words in the Group A, Group B, Neutral or Bomb.
You also give a number between 1 and 3, this is the number of words your clue relates to from group A.

Your response (clue word and number separated by comma):"""
    return prompt


def parse_codemaster_response(response_text):
    match = re.match(r'\s*(\b[\w-]+\b)[,;\s]+(\b\d+\b)', response_text)
    s1, s2 = match.groups()
    s2 = int(s2)
    return s1, int(s2)
