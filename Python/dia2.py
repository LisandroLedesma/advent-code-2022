#PARTE 1
#Ref:
# A X = Rock
# B Y = Paper
# C Z = Scissors

# def match(me, rival):
#     if me == "X":
#         result = 1
#         if rival == "A":
#             result += 3
#         elif rival == "B":
#             result += 0
#         else:
#             result += 6
#     elif me == "Y":
#         result = 2
#         if rival == "A":
#             result += 6
#         elif rival == "B":
#             result += 3
#         else:
#             result += 0
#     else:
#         result = 3
#         if rival == "A":
#             result += 0
#         elif rival == "B":
#             result += 6
#         else:
#             result += 3

#     return result

# with open('input2.txt') as f:
#     lines = f.readlines()

#     totalScore = 0

#     for line in lines:
#         rival = line[0:1]
#         me = line[2:3]
#         totalScore += match(me, rival)
# print(totalScore)

#PARTE 2
#Ref:
# X = lose
# Y = draw
# Z = win

def match(me, rival):
    if rival == "A":
        if me == "X":
            result = 3 + 0
        elif me == "Y":
            result = 1 + 3
        else:
            result = 2 + 6
    elif rival == "B": 
        if me == "X":
            result = 1 + 0
        elif me == "Y":
            result = 2 + 3
        else:
            result = 3 + 6
    else:
        if me == "X":
            result = 2 + 0
        elif me == "Y":
            result = 3 + 3
        else:
            result = 1 + 6

    return result

with open('input2.txt') as f:
    lines = f.readlines()

    totalScore = 0

    for line in lines:
        rival = line[0:1]
        me = line[2:3]
        #print(match(me, rival))
        totalScore += match(me, rival)
print(totalScore)
