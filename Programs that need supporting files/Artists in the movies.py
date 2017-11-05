#A program to determine which artist is in which movies


def union(dictt,tup1,tup2):
    
    try:
            
        for items in dictt:
            if items==tup1:
                a=set(dictt[items])
            if items==tup2:
                b=set(dictt[items])
        return a|b
   
    except UnboundLocalError:
        print("You did not type in the exact format. Do it again.")
def intersection(dictt,tup1,tup2):
    for items in dictt:
        if items==tup1:
            a=set(dictt[items])
        if items==tup2:
            b=set(dictt[items])
    return a&b
def symdifference(dictt,tup1,tup2):
    for items in dictt:
        if items==tup1:
            a=set(dictt[items])
        if items==tup2:
            b=set(dictt[items])
    return a^b
def all_other(dictt,name):
    l=[]
    for elements in dictt.values():
        if name in elements:
            for i in list(set(elements).difference(set([name]))):
                l.append(i)
    return l
def main():
    main_list=[]
    dictt={}
    listt=[]
    with open ("imdb_update.csv", "r") as file:
        for elements in file:
            main_list.append(elements.strip().split(","))
        for rows in main_list:
            for p in range (1,len(rows)):
                listt=[rows[0]]
                rows[p]=(rows[p][:-7],rows[p][-5:-1])
                if rows[p] not in dictt:
                    dictt[rows[p]]=listt
                else:
                    dictt[rows[p]].append(rows[0])
        x1,y1=input("Enter the name of the first movie in the format:Movie Name"),input("Enter the year of release of the first movie in the format:2090")
        x2,y2=input("Enter the name of the second movie in the format:Movie Name"),input("Enter the year of release of the second movie in the format:2090")
         
        tup1=(x1,y1)
        tup2=(x2,y2)
        print("")
        print("")
        print("")
        print ("All the actors in the two movies are:")
        for i in union(dictt,tup1,tup2): print (i)
        print("")
        print("")
        print ("The common actors in the two movies are:")
        for i in intersection(dictt,tup1,tup2): print (i)
        print("")
        print("")
        print ("The actors in only one of the two movies are:")
        for i in symdifference(dictt,tup1,tup2): print (i)
        print("")
        print("")
        name=input("Enter the name of the artist you want to lookup in the format:Artist Name")
        print("")
        print (name, "has acted with the following artists:")
        for i in all_other(dictt,name): print (i)
main()
 
                                      
                                    


