#!/usr/bin/python3

message = input("Bir şeyler girin:")
add = ""

i = 0
while i <= len(message):
 add = add + message[i]
 i = i+1
 print(add)
 if i >= len(message):
  break
