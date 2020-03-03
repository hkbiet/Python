import csv
import json #for saving the created dictionary as a JSON file



result = {} #dictionary for formatting json file

pathin = 'movies.csv' #path to input csv

with open(pathin, 'r') as f:
    reader = csv.reader(f)
    for item in reader:
        #the second column is used for keys, the third column is split into list of genres
        result[item[1]] = item[2].split('|') 
f.close()

pathout = 'result.json' #path for output json

with open(pathout, 'w') as file_handle:
    #write dictionary to json file
    file_handle.write(json.dumps(result, indent=4))
file_handle.close()





