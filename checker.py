from infer import infer

test = open('./data/testing.txt', 'r')

correct = 0
incorrect = 0
total = 0

for line in test:
    name, sex = line.strip().split(' ')
    male, female, inference = infer(name)

    if inference == 'u':
        continue

    if inference == sex:
        correct = correct + 1

    else:
        incorrect = incorrect + 1

    total = total + 1
    print(total)

print("Correct: " + str((correct/total)*100) + "%")
print("Incorrect: " + str((incorrect/total)*100) + "%")

test.close()
