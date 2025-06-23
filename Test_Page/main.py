

while True:
    tanlov=int(input("""
    Kim millioner bo'lishni xohlaydi ?
    1 ==>> O'yin
    2 ==>> Reting
    
    0 ==>> Tugatish ... 
    """))
    if tanlov==0:
        print("Xayr salomat bo'ling!!")
        break
    elif tanlov==2:
        print("Natejalar")
        import json
        with open("users.json") as j_file:
            p_file=json.load(j_file)
        print("|  Name    |  Played  |  Reting  |")
        for user in p_file:
            print(F'|  {user["name"]}   |    {user["play"]}  |      {user["reting"]}')


