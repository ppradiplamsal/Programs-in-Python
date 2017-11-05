# A program to find the artist name, genre, popular songs


import csv
def songsar(file,name):
    la=[]
    for rows in file:
        if rows["Artist"]==name:
            la.append(rows["Title"])
            return la
def songsal(file,album):
    lb=[]
    for rows in file:
        if rows["Album"]==album:
            lb.append(rows["Title"])
            return lb
def gen(file,genre):
    lc=[]
    for rows in file:
        if rows["Genre"]==genre:
            lc.append(rows["Title"])
            return lc
def add():
    with open('Playlist.csv', 'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        n=int(input("How many songs do you want to add"))
        print("Enter the Tile, Artist, Album, Genre, Duration of the song in correct format")
        for i in range(n):
            writer.writerow({'Title': input(), 'Artist': input(), 'Album': input(), 'Genre': input(), 'Duration': input()})
        return
def dell(file):
    delll=input("Enter the song you want to delete in the correct format")
    with open ('Playlist.csv',"r") as inp, open ('Playlist_edited.csv',"w") as out:
        writer=csv.writer(out)
        for elements in csv.reader(inp):
            if delll!=elements["Title"]:
                writer.writerow(elements)
    return
def popular(LIST):
    c=1
    b=0
    dictt={}
    for rows in LIST:
        b=b+1
    for rows in range (b-1):
        if LIST[rows]["Artist"]==LIST[rows+1]["Artist"]:
            c+=1
        else:
            dictt[LIST[rows]["Artist"]]=c
            
            if rows==b-2:
                dictt[LIST[b-1]["Artist"]]=1
    li=[]
    for elems in dictt:
        li.append(dictt[elems])
    l=[]
    for i in dictt:
        if dictt[i]==max(li):
            l.append(i)
    return l
def longest(file):
    dic={}
    for oi in file:
        dic[oi["Title"]]=(int(oi["Duration"][0])*60+int(oi["Duration"][-2:]))
        l=[]
        li=[]
        for j in dic:
            l.append(dic[j])
        for i in dic:
            if dic[i]==max(l):
                li.append(i)
    return i
def main():
    with open ("Playlist.csv","r") as f:
        file=csv.DictReader(f)
        LIST=list(file)
        name=input("Enter the name of the Artist you want to know all the songs of in correct format")
        print("")
        print("All the songs of",name,"are:")
        for i in songsar(file,name):
            print(i)
        print("")
        print("")
        album=input("Enter the name of the Album you want to know all the songs of in correct format")
        print("")
        print("All the songs of",album,"are:")
        for i in songsal(file,album):
            print(i)
        print("")
        print("")
        genre=input("Enter the genre you want to know all the songs of in correct format")
        print("")
        print("All the", genre, "songs are:")
        for i in gen(file,genre):
            print(i)
        print("")
        print("")
        add()
        print("")
        dell(file)
        print("")
        print("")
        print("The most popular song is/are:")
        for i in popular(file):
            print(i)
        print("")
        print("")
        print("The longest song is/are:")
        for i in longest(file):
            print(i)
main()

