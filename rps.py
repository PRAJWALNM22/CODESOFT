import random
you=0
sys=0
flag=1
while(flag):
    n=int(input("\n press 0 for rock \n press 1 for paper \n press 2 for scissor \n enter your choice : "))
    m=random.randint(0,2)
    if n>=0 and n<3:
        
        if n==m:
            print("DRAW")
        elif n==0 and m==2:
            print("YOU WINS")
            you+=1
        elif n==2 and m==0:
            print("SYSTEM WINS")
            sys+=1
        elif n>m:
            print("SYSTEM WINS")
            sys+=1
        elif m>n:
            print("YOU WINS")
            you+=1
        print(f"your score is {you} : {sys}")
    else:
        print("enter a valid number")
    s1=input("DO YOU WONNA CONTINUE!(y/n)")
    if s1=="n":
        flag=0
if you>sys:
    print("FINALLY YOU WON")
elif sys>you:
    print("FINALLY SYSTEM WON")
else:
    print("FINALLY ITS A DRAW")

