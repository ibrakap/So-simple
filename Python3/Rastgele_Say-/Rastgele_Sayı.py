import random

ilk_r = int(input("İlk sayıyı girin:"))
son_r = int(input("Son sayıyı girin:"))
mixer = random.randint(ilk_r,son_r)
user_i = int(input("Tahmini sayıyı girin:"))

if user_i == mixer:
    print("Tebrikler! Sayıyı doğru bildiniz")
else:
    print("Üzgünüm yanlış cevap\nSayı {} olacaktı".format(mixer))
