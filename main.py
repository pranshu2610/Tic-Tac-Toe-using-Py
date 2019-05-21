def display():
    print(ground[0][0]+'\t|'+ground[0][1]+'\t|'+ground[0][2])
    print('-----------------------')
    print(ground[1][0]+'\t|'+ground[1][1]+'\t|'+ground[1][2])
    print('-----------------------')
    print(ground[2][0]+'\t|'+ground[2][1]+'\t|'+ground[2][2])
    print('\n')

def checkwin(Sym):
    condition=[]
    for i in range(3):
        condition.append(Sym)
    data=['','','']
    #row-win
    for i in range(3):
        data[i]=ground[0][i]
    if data==condition:
        print(Sym+' is winner')
        exit()
    for i in range(3):
        data[i]=ground[1][i]
    if data==condition:
        print(Sym+' is winner')
        exit()
    for i in range(3):
        data[i]=ground[2][i]
    if data==condition:
        print(Sym+' is winner')
        exit()

    #col-win
    for i in range(3):
        data[i]=ground[i][0]
    if data==condition:
        print(Sym+' is winner')
        exit()
    for i in range(3):
        data[i]=ground[i][1]
    if data==condition:
        print(Sym+' is winner')
        exit()
    for i in range(3):
        data[i]=ground[i][2]
    if data==condition:
        print(Sym+' is winner')
        exit()

    #dia-win
    for i in range(3):
        data[i]=ground[i][i]
    if data==condition:
        print(Sym+' is winner')
        exit()
    for i in range(3):
        data[i]=ground[2-i][i]
    if data==condition:
        print(Sym+' is winner')
        exit()

def computer(sel, com):
    import random
    stat=len(sel)
    comsel=random.randint(0,(stat-1))
    compos=str(sel[int(comsel)])
    sel.remove(compos)
    for i in range(3):
        for j in range(3):
            if ground[i][j]==compos:
                ground[i][j]=com
    display()
    checkwin(com)

def playermove(sel, player):
    position=input()
    sel.remove(position)
    for i in range(3):
        for j in range(3):
            if ground[i][j]==position:
                ground[i][j]=player
    display()
    checkwin(player)


ground=[['LTop', 'MTop', 'RTop'], ['LCen', 'MCen', 'RCen'], ['LBot', 'MBot', 'RBot']]
sel=[]
for i in range(3):
    for j in range(3):
        sel.append(ground[i][j])

print("Welcome to Tic Tac Toe Game:\n")
display()
print("What you want to be X or O?")
player=input()
player=player.upper()
if player== 'X':
    com='O'
elif player== 'O':
    com='X'

if player== 'X':
    print("Your Turn!\nEnter the Position:")
    playermove(sel, player)


print("Computer Turn!\n")
computer(sel, com)
print("Your Turn!\nEnter the Position:")
playermove(sel, player)
print("Computer Turn!\n")
computer(sel, com)
print("Your Turn!\nEnter the Position:")
playermove(sel, player)
print("Computer Turn!\n")
computer(sel, com)
print("Your Turn!\nEnter the Position:")
playermove(sel, player)
print("Computer Turn!\n")
computer(sel, com)
print("Your Turn!\nEnter the Position:")
playermove(sel, player)
print("Computer Turn!\n")
computer(sel, com)
print("Your Turn!\nEnter the Position:")
playermove(sel, player)
