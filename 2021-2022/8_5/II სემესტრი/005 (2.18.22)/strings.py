# სტრიქონები  string

# a = "This is a string"
# print(a)
#
# a = 'This is a string'
# print(a)
#
# a = "d"
# print(a, type(a))
#
# a = '12345'
# print(a, type(a))
#
# a = 123.45
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata mamporia, \
# I am 19 years old. \
# I love Rugby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata mamporia, " \
#         "I am 19 years old. " \
#         "I love Rugby."
# print(intro)
#
# print()

# '\n'  ახალ ხაზზე გადასვლა  New line  End line  ENTER
# intro = "Hello there!\n\
# My name is Paata mamporia,\n\
# I am 19 years old.\n\
# I love Rugby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata mamporia,
# I am 19 years old.
# I love Rugby."""
# print(intro, "\n")
#
# intro = '''Hello there!
# My name is Paata mamporia,
# I am 19 years old.
# I love Rugby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#                 My name is Paata mamporia,
#                             I am 19 years old.
#         I love Rugby.'''
# print(intro, "\n")


# ბრწყალები ბრჭყალებში
# "Hello", said Susan.
# print(""Hello", said Susan.")
# print('"Hello", said Susan.')
# print("'Hello', said Susan.")
#
# # "That's is my Teddy", said Pedro.
# print("\"That's is my Teddy\", said Pedro.")
# print('"That\'s is my Teddy", said Pedro.')
# print(""""That's is my Teddy", said Pedro.""")
# print('''"That's is my Teddy", said Pedro.''')
#
# print("c:\\users\\paata\\strings.py")
# print(r"c:\users\paata\strings.py")
# print(r"c:\users\paata\strings.py\n")


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a, type(a))


# ევდომა სტრიქონის სიმბოლოებზე
# a = "Hello there!"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტრიქონში slice. სინტაქსი: string[start:stop-1:step=1]
# a = "Hello there!"
# print(a[0:4:1])         # პირველი ოთხი სიმბოლო
# print(a[0:4])           # პირველი ოთხი სიმბოლო
# print(a[:4])            # პირველი ოთხი სიმბოლო
# print(a[2:7])           # სიმბოლოები მითითებული დიაპაზონით
# print(a[2:9:3])         # სიმბოლოები მითითებული დიაპაზონით
# print(a[-4:])           # ბოლო ოთხი სიმბოლო
# print(a[3:])

a = "Hello there!"
print(a, id(a))
# print(a[:-1] + " friends!")

a = 'P' + a[1:]
print(a, id(a))

a = 'H' + a[1:]
print(a, id(a))