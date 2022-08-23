#!/usr/bin/python3
strty = ""
for i in reversed(range(97, 123)):
     if (i % 2) == 0:
         strty += chr(i)
     else:
         strty += chr(i-32)
print("{}".format(strty), end="")
