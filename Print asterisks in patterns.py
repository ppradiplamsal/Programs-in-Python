#PROBLEM:
#Write a recursive helper function called writeChars that accepts an integer
#parameter n and prints out a string returned by another recursive method
#that is called by writeChars.

#GIVEN:
#writeChars(0) prints out: The string is
#writeChars(1) prints out: The string is *
#writeChars(2) prints out: The string is **
#writeChars(3) prints out: The string is <*>
#writeChars(4) prints out: The string is <**>
#writeChars(5) prints out: The string is <<*>>
#writeChars(6) prints out: The string is <<**>>
#writeChars(7) prints out: The string is <<<*>>>
#writeChars(8) prints out: The string is <<<**>>>
#even number has two asteriks **
#odd number has one asteriks*



#TEST CASES:
#Input: 1
#Output:*

#Input: 3
#Output: <*>

#Input: 5
#Output: <<*>>

#PROGRAM



def starStr(n):
    if n<=0:
        return ""
    elif n==1:
        return "*"
    elif n==2:
        return "**"
    else:
        return ("<" + starStr(n-2) + ">")

def writechar(n):
    print("\nThe string is: ", starStr(n))

def main():
    print("Welcome to the string printing program.\n")
    flag = 1
    while (flag==1):
            try:
                n = int(input("\nEnter an integer for the string size: "))
                flag = 0
            except:
                print("\n", n, "is invalid-Please try again\n")
                flag = 1

            writechar(n)
            flag0 = 1
            while (flag0 == 1):
                inp = input("\nWould you like to enter another number [y or n]: ")
                if inp == 'y':
                    flag0 = 0
                    flag = 1
                elif inp == 'n':
                    flag0 = 0
                    flag = 0
                else:
                    print(inp, "is invalid - please try again\n")
                    flag0 = 1
    print("bye")


main()               
                
    
    


    




            
