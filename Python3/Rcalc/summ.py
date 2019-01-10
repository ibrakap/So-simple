import random
while True:
    try:
        mark = ["+","-","*","/"]
        rand_mark = random.choice(mark)
        summ = "{} {} {}".format(random.randint(0,2000),rand_mark,random.randint(0,2000))
        calc = eval("{}".format(summ))
        inp = int(input("{} =".format(summ)))
        if inp == calc:
            print("Tebrikler sonucunuz doğru")
        else:
            print("Sonucunuz yanlış doğru sonuç {} olmalıydı".format(calc))
    except:
        pass
