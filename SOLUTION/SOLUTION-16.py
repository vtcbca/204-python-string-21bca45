#Enter any string and check it is Palindrome or not
x=input("Enter Number:")
print(x)
y=x[::-1]
print("palindrome String" if x==y else "Not a Palindrome String")
