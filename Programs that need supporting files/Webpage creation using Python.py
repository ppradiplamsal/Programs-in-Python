#PROBLEM:
# To write a program to enable a user to create a web page
# where he user will be prompted for the name of the web page file and its title.

#GIVEN:
# the string variable can be called “body”
# and can be initialized with
#body = '<html>\n<head>\n<title>'
# prompted for the web page title and the title can be concatenated to body
# thusly
#webpagetitle = inpu(‘Please enter the web page title: ‘) body += webpagetitle


#TEST CASES
#Input: file name, webpage name
#Output: web page with image

#Input: file name, webpage name
#output: webpage with image.




print("Welcome to the webpage creator")


def file_present(path):
    try:
        f = open(path)
        f.close()
    except IOError as err:
        return False
 
    return True

while True:
    file_name = input("Please enter a file name for webpage: ")
    file_name = file_name + ".html"
    file_path1 = file_name #location of the file in the drive
    filepresent1 = file_present(file_path1)
    if filepresent1 == True:
        print(file_name + " exists - please enter another file")
    else:
        break

title = input("Please enter a webpage title: ")

body = "<html>\n<head>\n<title>" + title + "</title>\n</head>\n<body>\n"

flag = 1

while flag ==1: 
    print("\nWebpage additional menu choices")
    print ("[t]ext line")
    print ("[i]mage")
    print ("[b]old text line")
    print ("[c]olor text line")
    print ("[e]xit")


    choice = input("Enter menu choice [t,i,b,c,e]: ")

    if choice == 't':
        text1 = input("Please enter a line of text for your webpage: ")
        body = body + "<p>\n" + text1 + "<br/>\n"

    elif choice == 'i':
        while True:
            img1 = input("Please enter a image filename: ")
            file_path2 = "/Users/gauravthapa/Desktop/python lab5/" + img1 + ".jpg" #location of the image in the drive
            filepresent2 = file_present(file_path2)
            if filepresent2 == False:
                print(img1 + ".jpg" + " does not exist - please enter another file")
            else:
                break
        body = body + "<img src=" + '"' + img1 + ".jpg" + '"' + "><br/>\n"

    elif choice == 'b':
        bold1 = input("Please enter a line of text to be bolded for your webpage: ")
        body = body + "<b>" + bold1 + "</b><br/>\n"
    
        
    elif choice == 'c':
        color1 = input("Please enter a font color: ")
        color_text = input("Please enter a line of text for the new font color: ")
        body = body + "<font color=" + '"' + color1 + '"' + ">" + color_text + "</font><br/>\n"
        flag = 1
        
    elif choice == 'e':
        body = body + "</p>\n</body>\n</html>"
        print("Preparing the web page")
        print("The web page is now in" + file_name)
        print("Enjoy your new web page")
        break

    else:
        print("Invalid menu choice - please try again")


f = open(file_name,'w')
f.write(body)
f.close()

    


    
                 
