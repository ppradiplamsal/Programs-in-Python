#PROBLEM: Write a function to return a randomly generated 6-element integer set
#which represents one lotto ticket.

#GIVEN:
#lottotexas.csv file with the list of winning numbers from the year
#1992 to 2017.
#Each ticket cost $1.
#lottotexas.csv has the winiing numbers from the year 1992 to 2017.
#2 matching numbers- $2
#3 matching numbers - $10
#4 matching numbers - $100
#5 matching numbers - $1000
#6 matching numbers - $10000



#TEST CASES:
#input : randomly generated numbers
#output: Your Lottery Ticket is [ 36, 39, 14, 18, 22]
#output: Your Total Winnings from 1992 to 2017 are: 720 dollars
#output: You would have spent 2605 dollars on Texas lotto tickets from 1992 to 2017

#PROGRAM

import csv
from random import *

total = 0

def rand_num_gen(ticket):
    for l in range(6):
        ticket.append(str(randint(1, 54)))
    return ticket


try:

    ticket = []
    rand_num_gen(ticket)

    fname = "lotto8exas.csv"
    lottotexas = open(fname, "r")
    reader = csv.reader(lottotexas)

    dictionary = {}
    


    c1 = 0


    for i in reader:
        day = ""
        numbers = []
        
        
        day = day + i[1] + "/" + i[2] + "/" + i[3]

        for j in range (4, 10):
            numbers.append(i[j])

        dictionary[day] = numbers



    for m in dictionary.values():
        c1 += 1
        c2 = 0
        for n in ticket:
            if n in m:
                c2 += 1
        if c2 == 2:
            total += 2
        elif c2 == 3:
            total += 10
        elif c2 == 4:
            total += 100
        elif c2 == 5:
            total += 10000
        elif c2 == 6:
            total += 100000

except IOError:
    print ("Cannot open ", fname)

print("Your Lotto ticket is  ", ticket)

print("Your total winning from 1992 to 2017 are " , total, "dollars")

print("You would have spent", c1, " dollars on Texas lotto tickets from 1992 to 2017")




