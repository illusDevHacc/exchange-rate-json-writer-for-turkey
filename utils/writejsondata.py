from json import dumps

def writedata(content:dict):
    with open("kur.json","w",encoding="utf-8") as file:
        file.write(dumps(content,indent=6,ensure_ascii=False))