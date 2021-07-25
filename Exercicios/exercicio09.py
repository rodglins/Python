word = str(input("Tape one word to verify the palindrome: "))
if word == word[::-1]:
	print(f'The word {word} is a palindrome.')
else:
	print(f'The word {word} is not a palindrome.')