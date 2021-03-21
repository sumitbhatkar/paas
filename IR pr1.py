print("Name :- SHRADDHA JAMASHETTI\nRoll No :- T081\nClass :- T.Y.C.S")
def check(term,li):
    for i in range(0,len(li)):
        if term in li:
            return 1
        else:
            return 0

str1=[item for item in input("Enter 1st String:").split()]
str2=[item for item in input("Enter 2nd String:").split()]
term=str(input("Enter a term:"))
print("Vector :",check(term,str1),check(term,str2))
