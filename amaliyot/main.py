import json
with open("tests (2).json","r") as j_file:
    p_file=json.load(j_file)
s=0
while True:
    print(s+1,"- Salov\n",p_file[s]["question"])
    answers = (p_file[s]['answers'])
    variantlar = ["A", "B", "C", "D"]
    i = 0
    for answer in answers:
            print(F"{variantlar[i]}) {answer['key']}")
            i += 1

    tanlov = input(">>>> .. ")
    javoblar = []
    for answer in answers:
            javoblar.append(answer["isTrue"])
    if tanlov == "A" and javoblar[0] == True:
            print("Javob to'gri")
    elif tanlov == "B" and javoblar[1] == True:
            print("Javob to'gri")
    elif tanlov == "C" and javoblar[2] == True:
            print("Javob to'gri")
    elif tanlov == "D" and javoblar[3] == True:
            print("Javob to'gri")
    else:
            print("Javob Xato")

    s+=1
    if s==10:
        break

