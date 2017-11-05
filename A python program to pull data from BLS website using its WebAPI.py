
#A python program to pull data from BLS website using its WebAPI



import requests
import json
#import prettytable
import csv

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['EIUCOCANZ321'],"startyear":"2012", "endyear":"2017"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
print(p.content)



json_data = json.loads(p.text)
#print(json_data)
seriesID = json_data['Results']['series'][0]['seriesID']
filename = seriesID+'.csv'



for series in json_data['Results']['series']:
    fields = ["seriesID", "year","periodName","period","value","footnotes"]
    
    seriess = series['data']
    with open(filename, 'w') as csvfile:
        
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(seriess)







#work more to display seriesID
#work to erase the [{}] of footnotes
