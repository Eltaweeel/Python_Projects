"""In this project we are asking user to enter any text
and we will check how many vowels in this text and how many times any vowel has repitated"""

string = input ("Please enter any text: ")
text = string.lower()

count_a = 0
count_e = 0
count_i= 0
count_o = 0
count_u=0

for i in text:
    if i == "a":
        count_a +=1
    elif i == "e":
        count_e +=1
    elif i == "i":
        count_i +=1
    elif i == "o":
        count_o +=1
    elif i == "u":
        count_u +=1
print (f"A is repeated {count_a} times")
print (f"E is repeated {count_e} times")
print (f"I is repeated {count_i} times")
print (f"O is repeated {count_o} times")
print (f"U is repeated {count_u} times")

print (f"Number of vowels are: {count_a + count_e + count_i + count_o + count_u}")