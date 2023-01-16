import json
from codenames import prompt_for_codemaster


with open("rounds_easy.json", "r") as f:
    lines = f.readlines()

with open("rounds_medium.json", "r") as f:
    lines += f.readlines()

with open("rounds_hard.json", "r") as f:
    lines += f.readlines()


completions = []


for line in lines:
    data = json.loads(line)
    if not data["winning"]:
        for i in range(len(data["prompts"])-1):
            completions.append({"prompt": data["prompts"][i], "completion": data["responses"][i]})
    else:
        completions.append({"prompt":prompt_for_codemaster(data["cards"], "blue"), "completion" : data["clue_word"] + "," + str(data["number"])})
        for i in range(len(data["prompts"])):
            completions.append({"prompt": data["prompts"][i], "completion": data["responses"][i]})
            


with open("finetune.jsonl", "w+") as f:
    for completion in completions:
        f.write(json.dumps(completion) +'\n')

