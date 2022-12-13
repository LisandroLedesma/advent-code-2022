#Alternativas para abrir el archivo

# f = open("demofile.txt", "r")
# print(f.read())

# with open('readme.txt') as f:
#     lines = f.readlines()
#Usando el segundo enfoque no es necesario el close()

#PARTE 1
# f = open("input1.txt", "r")
# lines = f.readlines()
# elfCalories = 0
# maxCalories = 0

# for i in range(0, len(lines)):
#     if lines[i] != '' and lines[i] != '\n':
#         elfCalories += int(lines[i])
    
#     if lines[i] == '\n' or i == len(lines)-1:
#         if elfCalories > maxCalories:
#             maxCalories = elfCalories
#         elfCalories = 0
# f.close()
# print(maxCalories)

# The EOF char is an empty string

# TODO: refactorizar este monstruo

#PARTE 2
f = open("input1.txt", "r")
lines = f.readlines()
elfCalories = 0
caloriesList = []
caloriesTop = []
totalTop = 0

for i in range(0, len(lines)):
    if lines[i] != '' and lines[i] != '\n':
        elfCalories += int(lines[i])
    
    if lines[i] == '\n' or i == len(lines)-1:
        caloriesList.append(elfCalories)
        elfCalories = 0

f.close()
print(sum(sorted(caloriesList, reverse=True)[:3]))