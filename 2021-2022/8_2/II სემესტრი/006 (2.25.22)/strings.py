# სტრიქონები  string

# a = "This is a string"
# print(a)
#
# a = "d"
# print(a, type(a))
#
# a = "14562"
# print(a, type(a))
#
# a = 14.562
# print(a, type(a))


# მრავალსტრიქონიანი სტრიქონები
# intro = "Hello there! \
# My name is Paata Mamporia, \
# I am 49 years old. \
# I love Rygby."
# print(intro)
#
# intro = "Hello there! " \
#         "My name is Paata Mamporia, " \
#         "I am 49 years old. " \
#         "I love Rygby."
# print(intro)
#
# print()

# '\n'  ახალ ხაზზე გადასვლა  New line  End line  ENTER
# intro = "Hello there!\n\
# My name is Paata Mamporia,\n\
# I am 49 years old.\n\
# I love Rygby."
# print(intro, "\n")
#
# intro = """Hello there!
# My name is Paata Mamporia,
# I am 49 years old.
# I love Rygby."""
# print(intro, "\n")
#
# intro = '''Hello there!
# My name is Paata Mamporia,
# I am 49 years old.
# I love Rygby.'''
# print(intro, "\n")
#
# intro = '''Hello there!
#         My name is Paata Mamporia,
#               I am 49 years old.
#                     I love Rygby.'''
# print(intro, "\n")


# ბრჭყალები ბრჭყალებში
# "Hello!", said Susan.
# print(""Hello!", said Susan.")
# print('"Hello!", said Susan.')
# # print("'Hello!', said Susan.")
# # print("""'Hello!', said Susan.""")
# #
# # # "That's is my Teddy", said Pedro.
# # print("\"That's is my Teddy\", said Pedro.")
# # print('"That\'s is my Teddy", said Pedro.')
# # print('''"That's is my Teddy", said Pedro.''')
# #
# # print("c:\\users\\paata\\strings.py")
# # print(r"c:\users\paata\strings.py")
# # print(r"c:\users\paata\strings.py\n")
# # print(r"c:\users\paata\strings.py", "\n")


# ცარიელი სტრიქონი
# a = ''
# a = ""
# print(a, type(a))


# სტრიქონების „შეკრება“ '+' ოპერატორით (კონკატენაცია)
# str1 = "Hello"
# str2 = "there"
# string = str1 + " " +  str2 + "!"
# print(string)

# Susan sais "Hi"!
# a = 'Hi'
# # print('Susan sais "' + a + '"!')
# # print('Daniel sais "' + a + '"!')
# # print('Kety sais "' + a + '"!')


# წვდომა სტრიქონის სიმბოლოებზე
# a = 'Hello there!'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[11], "\n")
#
# print(a[-1])
# print(a[-2])
# print(a[-3])


# ჭრები სტიქონში Slice. სინტაქსი: string[start:stop-1:step=1]
# a = 'Hello there!'
# print(a[0:4:1])
# print(a[0:4])
# print(a[:4])
# print(a[2:7])
# print(a[2:9:3])
# print(a[3:])
# print(a[-4:])
# print(a[-9::3])
# print(a[2::3])
# print(a[::3])



# სტრიქონული მეთოდები

#1. სტრიქონის სიგრძე (სიმბოლოების რაოდენობა)  len()
# a = "Hello world!"
# print(len(a))


#2. .capitalize(), .upper(), .lower(), .title()
# a = 'i am hErE.'
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.title())
# a = a.lower()
# print(a)


#3. .count()
# სინტაქსი: string.count(word)
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
# print(a.count('Susan'))
# print(a.count('Barky'))
# print(a.count('barky'))
# print(a.count('susan'))
# print(a.count('Jeck'))


#4. .strip(), .lstrip(), .rstrip()
# a = '              Hello there!      '
# print(a.strip())
#
# a = '*********Hello there!****'
#
# # a = a.strip('*')
# # print(a)
#
# a = a.rstrip('*')
# print(a)


#5. .replace(), .finf(), .index()
# a = '''Susan is a lovely girl.
# Barky is Susan's best friend.
# Barky plays with Susan...'''
#
# a = a.replace('Susan', 'Ronny', 2)
# print(a)

# a = 'I cyan love coding. I have fun with coding.'
# print(a.find('coding'))
# print(a.find('c'))
# print(a.find('Coding'))
#
# print()
#
# print(a.index('Coding'))
# print(a.index('coding'))
# print(a.index('c'))


#6. .split()
# სინტაქსი: string.split(separator, maxsplit)
a = "I love coding."
print(a.split())   # separatot=' ' or separator='\n' or separator='\t', maxsplit=-1

a = "I love coding.\nI have fun with\t\t\tcoding."
print(a.split())   # separatot=' ' or separator='\n' or separator='\t', maxsplit=-1

a = "I love coding.\nI have fun with\t\t\tcoding."
print(a.split('.'))   # separatot=' ' or separator='\n' or separator='\t', maxsplit=-1

a = "I love coding.\nI have fun with\t\t\tcoding."
print(a.split('.\n'))   # separatot=' ' or separator='\n' or separator='\t', maxsplit=-1

a = "numbers*123*numbers*456*numbers*789"
print(a.split('*'))

a = "numbers*123*numbers*456*numbers*789"
print(a.split('*', 1))

a = "numbers*123*numbers*456*numbers*789"
print(a.split('*',2))
