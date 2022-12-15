import codenames
from codenames.codemaster import prompt_for_codemaster
import openai


cards = codenames.generate_codewords_board(codenames.EASY_WORDS, 3, 3, 3, 1)
codemaster_prompt = prompt_for_codemaster(cards, "blue")


response = openai.Completion.create(
            model="text-davinci-003",
            prompt=codemaster_prompt,
            temperature=0.7,
            max_tokens=6,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
)

clue_word, number = codenames.parse_codemaster_response(response['choices'][0]['text'])
print(clue_word, number)