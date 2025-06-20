from amaliyot import Pen

while True:
    tanlov=int(input("""
    1 ==>> Yozish
    2 ==>> O'qish
    3 ==>> CHiq
    4 ==>> Energy
    0 ==>> Tugatish ... 
    """))
    if tanlov==0:
        print("Xayr salomat bo'ling 😊😊 !!!")
        break
    elif tanlov==1:
        pass
    elif tanlov==2:
        file = open("ruchka.txt", "r")
        r1=Pen()
        r1.my_read(file)
    elif tanlov==3:
        pass
    elif tanlov==4:
        pass
    else:
        print("Siz to'g'ri menyuni tanlamadingiz")