#!/usr/bin/python3
import random

while True:
 try:
  number1 = random.randint(0,1000000)
  number2 = random.randint(0,1000000)
  summ = number1 + number2
  print("{} + {} = ?".format(number1,number2))
  inputt = int(input("İşlemin sonucunu girin:"))
  if inputt == summ:
   print("Tebrikler sonuç doğru ...")
  else:
   print("Tekrar deneyiniz ...")
 except ValueError:
  print("String ve diğer tipler girilemez!")
 except:
  print("Hata")
