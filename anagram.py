word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if sorted(word1) == sorted(word2):
    print("The words are Anagrams")
else:
    print("The words are not Anagrams")