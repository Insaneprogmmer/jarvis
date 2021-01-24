import json

with open('jarvis.json') as f:
    data = json.load(f)

command = 'tell me time'


def abc(command):
    for a in data["intents"]:
        for b in a["pattern"]:
            if command == b:
                result = str(a['answer'])[1:-1]
                return result


founder = abc(command)

if 'what is time' in founder:
    print("done")
