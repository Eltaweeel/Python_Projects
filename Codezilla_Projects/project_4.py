#In this project we are asking taking text from file then change all strings to lowercase and output it to file
#then using the text in output file to check how many vowels in this text and how many times any vowel has repitated

infile = open('input.txt','r')
outfile = open('output.txt','w')
with open('input.txt','r') as infile:

    text = infile.read()
    text = text.lower()
with open('output.txt','w')as outfile:
    outfile.write(text)

infile.close()

file = open('output.txt','r')


count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
NumOfWords = 0

with open('output.txt','r') as file:
    for line in file:
        for word in line.split():
            NumOfWords +=1

            for i in word:

                if i == "a":
                    count_a += 1
                elif i == "e":
                    count_e += 1
                elif i == "i":
                    count_i += 1
                elif i == "o":
                    count_o += 1
                elif i == "u":
                    count_u += 1

print(f"A is repeated {count_a} times")
print(f"E is repeated {count_e} times")
print(f"I is repeated {count_i} times")
print(f"O is repeated {count_o} times")
print(f"U is repeated {count_u} times")

print(f"Number of vowels are: {count_a + count_e + count_i + count_o + count_u}")

print(f"Number of words are: {NumOfWords}")
