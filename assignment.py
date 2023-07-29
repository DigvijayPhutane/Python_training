'''# Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
odd_list=[]
for i in range(len(my_list)):
    if i % 2 != 0:
        odd_list.append(my_list[i])
    else:
        pass
print(odd_list)
'''
'''
#Find the sum of the series upto n terms
n = 5
term = 2
series_sum = term
current_term = term
for i in range(1,n):
    current_term = current_term * 10 + term
    series_sum = series_sum + current_term
print(series_sum)
'''
#Python program to count the number of even and odd numbers from a series of numbers.
'''
num_list = [1,3,5,6,99,134,55]
evelist = []
oddlist = []
for i in num_list:
    if i % 2 == 0 :
        evelist.append(i)
    else:
        oddlist.append(i)

print("the count of even numbers is : ",len(evelist))
print('the count of odd numbers is: ',len(oddlist))
'''

'''# Python program that accepts a string and calculates the number of digits and letters.
user_in = input("enter ur statement: ")
digits = 0
letters = 0
for i in user_in:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1

print("the count of digits is : ",digits)
print("the count of letters is : ",letters)


'''
'''#Write a Python program that accepts a sentence from the user and counts the occurrences of each word in the sentence. Display the word and its count in alphabetical order.
sentence = input("enter your sentence : ")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.keys())
for word in sorted_words:
    count = word_count[word]
    print(word, ":", count)'''

"""sentence = input("enter your sentence : ")
words = sentence.split()
print(words)
print("--------------------------------------")
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.keys())
print(sorted_words)
for word in sorted_words:
    count = word_count[word]
    print(word, ":" , count )
"""





'''a = 'seema got 89 77 75 90 65'
number = ''
for char in a:
    if char.isdigit():
        number += char
if number:
    print(number)
else:
    print("nahi he boss")

fetch_numb = [int(number[i:i+2])
              for i in range(0, len(number), 2)]

total_marks = sum(fetch_numb)

percentage = (total_marks / (len(fetch_numb) * 100)) * 100

print("Numbers:", number)
print("Total Marks:", fetch_numb)
print("Percentage:", percentage)
'''

'''n=('amol is in pune you contact him:9877665544')
for i in n:
    if str(i).isnumeric():
        print(i,end="")'''



