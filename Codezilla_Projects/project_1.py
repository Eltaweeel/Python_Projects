#In this project we are asking user to enter any word, then we are going to reverse the word. So first letter will be last and son on

first_word = input("Please enter the word: \n")
final_word = first_word[::-1]
print("the reversed word is: {}".format(final_word))
