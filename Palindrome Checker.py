def is_palindrome(word):
    word = word.lower().replace(" ", "")  # optional: remove spaces
    return word == word[::-1]

# Example usage
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
