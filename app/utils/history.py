import json 

def get_review():
    try:
        with open("./resources/json/history.json") as file:
            history = json.load(file)
    except FileNotFoundError:
        with open("./resources/json/history.json",'w') as file:
            history = {"yes":0,"no":0}
            json.dump(history, file)
    return history

def add_review(result:bool):
    history = get_review()
    if result: 
        history['yes'] = int(history.get('yes'))+1
    else:
        history['no'] = int(history.get('no'))+1
    with open("./resources/json/history.json", 'w') as fp:
        json.dump(history, fp)