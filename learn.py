from metrics import allMetrics
from combine import combine
import json

training_file = open('./training.json', 'w')
source_file = open('./data/training.txt', 'r')

training = {
    "female":{},
    "male":{},
    "maleCount":0,
    "femaleCount":0
}

def learn (name, sex):
    nameCount = allMetrics(name)

    if sex == "female":
        training["femaleCount"] = training["femaleCount"] + 1
    else:
        training["maleCount"] = training["maleCount"] + 1

    for i in nameCount:
        if i not in training[sex]:
            training[sex][i] = 0
        
        training[sex][i] = training[sex][i]+1



i = 0
for line in source_file:
    cleaned_line = line.strip()
    line_arr = cleaned_line.split(' ')

    name = line_arr[0]
    sex = ''

    if line_arr[1] == 'm':
        sex = 'male'
    else:
        sex = 'female'

    learn(name, sex)

    i = i + 1
    print(i)




json.dump(training, training_file, indent=1)

source_file.close()
training_file.close()