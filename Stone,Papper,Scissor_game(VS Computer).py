import random
win={"Scissor":"Paper","Paper":"Stone","Stone":"Scissor"}
cmpc,pc=0,0
l=["Scissor","Paper","Stone"]
n=int(input("Enter the total no. of points match: "))
while True:
    i=input("Enter your choice out of Stone,Paper or Scissor: ")
    cmp=l[random.randint(0,2)]
    print("Computer:-",cmp," You:-",i)
    if cmp!=i:
        if cmp==win[i]:
            pc+=1
        else:
            cmpc+=1
    if cmpc==n or pc==n:
        break
    print("Points:- Computer:",cmpc," You:",pc)
if cmpc>pc:
    print("Computer Wins")
    print("Points:- Computer:",cmpc," You:",pc)
else:
    print("You Win")
    print("Points:- Computer:",cmpc," You:",pc)