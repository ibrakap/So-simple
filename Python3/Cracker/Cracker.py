""" ibrakap tarafından ctf için yazılmış tooldur """
import sys
import base64
import hashlib
if sys.argv[1] == "-B64de":
 Base64de = sys.argv[2]
 print("Sonuç =",base64.b64decode(Base64de))
if sys.argv[1] == "-B64en":
 Base64en = sys.argv[2]
 Encode = base64.b64encode(Base64en.encode())
 print("Sonuç =",Encode)
if sys.argv[1] == "-md5en":
    print("Sonuç =",hashlib.md5(sys.argv[2].encode()).hexdigest())
