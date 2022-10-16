#Write a method to remove any givin character from string
sentance = "Hello World"
print(sentance.replace("W", "L"))

#Write a program to find all prime numbers up to a given range of numbers 
less_numbers = int(input ("Please, Enter the Less Range number: "))  
upper_numbers = int(input ("Please, Enter the Upper Range number: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (less_numbers,upper_numbers + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)

#Write a function that count how many the given character repeated in a given string
def TestString(test_my_name):
    test_my_name = "MyNameIsZahraa"
count = 0
  
for i in test_my_name:
    if i == 'a':
        count = count + 1
print ("Count of a in MyNameIsZahraa is : "
                            +  str(count))
TestString()

