#In this project we are asking the user to enter any word so we can check if is palindrome or not

word = input("Please enter a word to check palindromic or not: \n")
word = word.lower()
if word == word[::-1]:
    print("This word is palindromic.")
else:
    print("This is not palindromic word!!")
