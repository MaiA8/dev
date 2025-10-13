from cs50 import get_int
scores = [72, 73, 33]

#print(f"Average: {(scores[0] + scores[1] + scores[2])/3}")

#print(f"Average {sum(scores)/3}")

#print(f"Average{sum(scores)/len(scores)}")

scores = []
for i in range(3):
    score = get_int("score: ")
#    scores.append(score)
    scores += [score]

print(f"Average{sum(scores)/len(scores)}")


