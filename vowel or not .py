ch=input("enter the charachter :")
if (ch == "a" or ch == "A" or ch == "e" or ch == "E" or ch == "i" or ch == "I" or ch == "o" or ch == "O" or ch == "u" or ch == "U"):
    print("vowels")
elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
    print("consonants")
else:
    print("invalid")