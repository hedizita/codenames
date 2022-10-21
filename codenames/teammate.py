def prompt_for_teammate_after_response(response):
  prompt = f"""{response}"""
  return prompt


def parse_teammate_response(response_text):
  tokens = [token for token in re.split('[-, \n]', response_text) if token!='']
  return tokens[0]