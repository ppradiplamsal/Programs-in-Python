
#PROBLEM:
#Write a function to take a 70- character string of Myers Briggs response
#and return a list of percentage of B. The list [30,45,10,10]
#Write another function to take list of percentages and return Myers Brigs
# 4 dimension as a single letters.

#GIVEN:
#The 70 character string in the problem background the list should be
#retruned as [30,45,10,10]


#TEST CASES:

#Test 1 :  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#result 1 :  [0.0, 0.0, 0.0, 0.0]
#test 2:  BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#result 2 :  [100.0, 100.0, 100.0, 100.0]
#test 3 :  AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
#result 3 :  [50.0, 50.0, 50.0, 50.0]
#test 4 :  ABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABABAB
#result 4 :  [50.0, 50.0, 50.0, 50.0]
#test 5 :  BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA
#result 5:  [30.0, 45.0, 10.0, 10.0]
#test 6 :  BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA
#result 6 :  [60.0, 30.0, 10.0, 20.0]
#test 7 :  AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB
#result 7 :  [0.0, 0.0, 0.0, 0.0]
#Test 1:  [0.0, 0.0, 0.0, 0.0]
#Result 1:   I S I J
#Test 2:  [100.0, 100.0, 100.0, 100.0]
#Result 2:   EIFP
#Test 3:  [50.0, 50.0, 50.0, 50.0]
#Result 3:   EIFP
#Test 4:  [50.0, 50.0, 50.0, 50.0]
#Result 4:   EIFP
#Test 5:  [30.0, 45.0, 10.0, 10.0]
#Result 5:   I S I J
#Test 6:  [60.0, 30.0, 10.0, 20.0]
#Result 6:   E S I J
#Test 7:  [0.0, 0.0, 0.0, 0.0]
#Result 7:   I S I J



#PROGRAM:

test1 = "A" * 70
test2 = "B" * 70
test3 = "A"* 35 + "B" * 35
test4 = "AB"*35
test5 = "BABAAAABAAAAAAAABAAAABBAAAAAABAAAABABAABAAABABABAABAAAAAABAAAAAABAAAAA"
test6 = "BABAAAABAAAAAAABAAAABBAAAAAABAAAABABAABAAABABAABAAABABABAABAAAAAABAAAA"
test7 = "AABBAABBBBBABABAAABAABABBAABBAAAABBBAAABAABAABABAAAABAABBBBAAABBAABABB"

def percentageCounter(name):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0

    list1 = [ ]
    i = 0

    while i <= 63:
        if name[i] == "B": num1 += 1

        if name[i + 1] == "B": num2 += 1

        if name[i+2] == "B": num2 += 1

        if name[i+3] == "B": num3 += 1

        if name [i+4] == "B": num3 += 1

        if name [i+5] == "B": num4 += 1

        if name [i+6] == "B": num4 += 1


        i = i + 7
    list1.append(float(num1 *10))
    list1.append(float(num2*5))
    list1.append(float(num3*5))
    list1.append(float(num4*5))

    return list1


def nature(given_list):
    nature = " "

    if given_list[0] < 50.0:
       nature = nature + "I"
    else:
        nature = nature + "E"

    if given_list [1] < 50.0:
        nature = nature + " S"

    else:
        nature = nature + "I"

    if given_list [1] < 50.0:
        nature = nature + " I"

    else:
        nature = nature + "F"

    if given_list [1] < 50.0:
        nature = nature + " J"

    else:
        nature = nature + "P"

    return nature



print("Test 1 : ", test1)
result_list1 = percentageCounter(test1)
print("result 1 : ", result_list1)


print("test 2: ", test2)
result_list2 = percentageCounter(test2)
print("result 2 : ", result_list2)

print("test 3 : ", test3)
result_list3 = percentageCounter(test3)
print("result 3 : ", result_list3)

print("test 4 : ", test4)
result_list4 = percentageCounter(test4)
print("result 4 : ", result_list4)

print("test 5 : ", test5)
result_list5 = percentageCounter(test5)
print("result 5: ", result_list5)

print("test 6 : ", test6)
result_list6 = percentageCounter(test6)
print("result 6 : ", result_list6)

print("test 7 : ", test7)
result_list7 = percentageCounter(test1)
print("result 7 : ", result_list7)




print("Test 1: ", result_list1)
print("Result 1: ", nature(result_list1))

print("Test 2: ", result_list2)
print("Result 2: ", nature(result_list2))

print("Test 3: ", result_list3)
print("Result 3: ", nature(result_list3))

print("Test 4: ", result_list4)
print("Result 4: ", nature(result_list4))

print("Test 5: ", result_list5)
print("Result 5: ", nature(result_list5))

print("Test 6: ", result_list6)
print("Result 6: ", nature(result_list6))

print("Test 7: ", result_list7)
print("Result 7: ", nature(result_list7))




    

    


    

        
 













            
    
    
