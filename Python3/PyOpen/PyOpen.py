import sys

try:
 for arg in sys.argv[1:]:
  print("-----------------"+"Dosyanız:",arg,"----------------\n")
  Myfile = open(arg,"r")
  Read = Myfile.read()
  print(Read)
  Myfile.close()
  print("------------------------Bitiş------------------")
 if not sys.argv[1:]:
  print(""" Bu program ibrakap tarafından yazılmıştır ve unlicence ile dağıtılır
Kullanım:
$python rcat.py 1.dosya 2.dosya .... sonsuz dosya
Usage:
$python PyOpen.py [files] [files] [...]
only $python rcat.py
open help page""")
except FileNotFoundError:
 print(""">>>Dosyanızın veya" dosyalarınızın adlarını yanlış girdiniz kontrol edin ve tekrar deneyin<<<""")
