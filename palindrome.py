print("Check if the given string is a palindrome or not")
string = input("Enter a string: ")
cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")    