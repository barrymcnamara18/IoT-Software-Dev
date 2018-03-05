####################
## EXAMPLE: for loops over strings
####################
s = "idemou loops"
for index in range(len(s)):
   if s[index] == 'i' or s[index] == 'u':
       print("There is an i or u")

print "Here we do again ..."
for char in s:
   if char == 'i' or char == 'u':
       print("There is an i or u")
       break


####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))
#
# i = 0
# while i < len(word):
#    char = word[i]
#    if char in an_letters:
#        print("Give me an " + char + "! " + char)
#    else:
#        print("Give me a  " + char + "! " + char)
#    i += 1
# print("What does that spell?")
# for i in range(times):
#    print(word, "!!!")
