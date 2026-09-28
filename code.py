import random

trute=""
c=1
x=1
y=0
#While typing 'prox' i realized how bad my variable names are
prox=[]
cads=[]

class card:
    def __init__(self, suit, number):
        self.number = number
        self.suit = suit

for i in range (52):
    if c <=4:
        y+=1
    if c > 4:
        y=1
        x+=1
        c=1
    if y == 1:
        trute = "Spades"
    elif y == 2:
        trute = "Clovers"
    elif y == 3:
        trute = "Hearts"
    elif y == 4:
        trute = "Diamonds"
    #ITS SO BEAUTIFUL
    newcard=card(trute,x)
    cads.append(newcard)
    #I LOVE IT AS IF IT WERE MY OWN CHILD
    c+=1

random.shuffle(cads)
midpoint = len(cads) //2
deck1 = cads[:midpoint]
deck2 = cads[midpoint:]

input("INTERNAL LOGIC FINISHED: STARTING PROGRAM: ")

while len(deck1) >0 and len(deck2) > 0:
    print("You are holding the" , deck1[0].number , " of " , deck1[0].suit, end="") 
    input(" ")
    print("Your opponent is holding the" , deck2[0].number , " of " , deck2[0].suit)
    if deck1[0].number < deck2[0].number:
        print("\nYou lost\n")
        deck2.append(deck2.pop(0))
        deck2.append(deck1.pop(0))
    elif deck1[0].number > deck2[0].number:
        print("\nYou win!!!\n")
        deck1.append(deck1.pop(0))
        deck1.append(deck2.pop(0))
    elif deck1[0].number == deck2[0].number:
        deck1.append(deck1.pop(0))
        deck2.append(deck2.pop(0))
        print("\nYou are at WAR\n")
        print("You are holding the" , deck1[0].number , " of " , deck1[0].suit, end="") 
        input(" ")
        print("Your opponent is holding the" , deck2[0].number , " of " , deck2[0].suit)
        if deck1[0].number < deck2[0].number:
            print("\nYou lost\n")
            #I could just for i in range 3 but i think if i get another error i'll get DEATHLY ill
            deck2.append(deck1.pop(0))
            deck2.append(deck1.pop(0))
            deck2.append(deck1.pop(0))
        elif deck1[0].number > deck2[0].number:
            print("\nYou win!!!\n")
            deck1.append(deck2.pop(0))
            deck1.append(deck2.pop(0))
            deck1.append(deck2.pop(0))
        elif deck1[0].number == deck2[0].number:
            print("\nDouble War\n")
            #I really dont wanna do double wars tonight
            break
