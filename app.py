path = ["./css/style.css", "./css/resp.css" , "./js/script.js" , "./js/changes.js", "./data.json"]

def encrypt(data) -> str:
    newData = ""
    for i in data:
        newData += chr(ord(i) - 1)
    return newData

for i in range(len(path)):
    with open(path[i], "r") as f:
        data = f.read()
        newData = encrypt(data)
    with open(path[i], "w") as f:
        f.write(newData)