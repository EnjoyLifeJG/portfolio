'''
By Jean-G. De Souza
Essex University Online
PG Cert in Computer Science - Module OOP: Unit 9 - Activity 4

    Activity instructions:
  " Extend the following program to test accuracy of operations using the assert statement:
            # Python String Operations
            str1 = 'Hello'
            str2 ='World!'
            # using +
            print('str1 + str2 = ', str1 + str2)
            # using *
            print('str1 * 3 =', str1 * 3)         "
'''

# --------------------------


# Python String Operations
str1 = 'Hello'
str2 = 'World!'

# using +
concatenated = str1 + str2
print('str1 + str2 = ', concatenated)
# Test for concat.
assert concatenated == 'HelloWorld!', f"Unexpected result. Expecting 'HelloWorld!' instead of '{concatenated}'."

# using *
multiplied = str1 * 3
print('str1 * 3 =', multiplied)
# Test for multiply
assert multiplied == 'HelloHelloHello', f"Unexpected result. Expecting 'HelloHelloHello' instead of '{multiplied}'. "

print("All tests passed!")
