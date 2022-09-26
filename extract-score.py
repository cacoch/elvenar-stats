#!/usr/bin/env python


# extract elvenar score

import json

filename = 'buen.json'

with open(filename, 'r') as f:
    data = json.load(f)

data = data[0]

responseData = data['responseData'] 
contributors = responseData['contributors']

for el in contributors:
    name = el['player']['name']
    score = el['score']
    print(name, score)

#print(responseData)
