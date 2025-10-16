import csv
# score = 0
# opn csv File
# read house column
# add score
# print score

houses = {
    "Ravenclaw":0,
    "Gryffindor":0,
    "Slytherin":0,
    "Hufflepuff":0,
}

#file = open("houses.csv","r")
#file.close()

# with open("houses.csv","r") as file:
#     reader = csv.DictReader(file)
#   #  next(reader)
#     for row in reader:
#         house = row["House"]
#     #    houses[row[House]] +=1
#         houses[house] += 1
# for house in houses:
#     #print( houses[house] )
#     print(f"{house} : {houses[house]}")


with open("houses.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        house = row["House"].strip()   # remove spaces if any
        if house in houses:
            houses[house] += 1
        else:
            houses[house] = 1  # handle any unexpected house names

for house, count in houses.items():
    print(f"{house} : {count}")
