#Program to compute cars' fuel mileages


import csv
a=open("2015FEGuide.csv",'r')
i=csv.DictReader(a)
def avg(n,Cyl,HwyFE):
    mil=0
    c=0
    for element in range (len(Cyl)):
        if Cyl[element]==n:
            mil+=int(HwyFE[element])
            c=c+1
    avg=mil/c
    return avg
def max_mil(n):
    mil_list=[]
    for row in i:
        if row[8]==n:
            mil_list.append(row)
    max_mil=max(mil_list)
    return max_mil
def min_mil(n):
    mil_list=[]
    for row in i:
        if row[8]==n:
            mil_list.append(row)
    min_mil=min(mil_list)
    return man_mil
def classline():
    n=int(input("Enter the highway mileage"))
    car_list=[]
    for row in i:
        if row[11]>n:
            carlist.append(row[0:11])
    return car_list
def hmil():
    n=int(input("Enter the highway mileage"))
    for row in i:
        c=c+1
    for row in i:
        if row[11]==n:
            v=v+1
    perc=v/c*100
    return perc
def main(n,i):
    Carline=[]
    Cyl=[]
    HwyFE=[]
    FE=[]
    rows=1
    for row in i:
        rows+=1
        if rows <=1102:  
            Cyl.append(int(row['# Cyl']))
            Carline.append(row['Carline Class Desc'])
            HwyFE.append(row['Hwy FE (Guide) - Conventional Fuel'])
n=int(input("Enter the number of cylinders"))
main(n,i)
avg(n)
max_mil(n)
min_mil(n)
classline()
hmil()
a.close()
    
    
    
  
