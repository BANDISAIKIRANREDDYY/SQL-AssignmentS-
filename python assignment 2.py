#!/usr/bin/env python
# coding: utf-8

# In[1]:


marks = [78, 45, 92, 33, 67, 88, 51, 29]

passed = 0

for mark in marks:
    if mark >= 35:
        passed = passed + 1

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Class average:", sum(marks) / len(marks))
print("Students passed:", passed)


# In[2]:


shopping_list = []

while True:
    item = input("Enter item: ").strip().lower()

    if item == "done":
        break
    elif item == "":
        print("Please enter an item")
    elif item in shopping_list:
        print("Already added")
    else:
        shopping_list.append(item)

for i in range(len(shopping_list)):
    print(str(i + 1) + ". " + shopping_list[i])

print("Total items:", len(shopping_list))


# In[3]:


username = input("Enter username: ")

if len(username) < 5 or len(username) > 12:
    print("Invalid: Username must have 5 to 12 characters")
elif " " in username:
    print("Invalid: Username cannot contain spaces")
elif username[0].isdigit():
    print("Invalid: Username cannot start with a digit")
else:
    print("Valid username")


# In[4]:


username = input("Enter username: ")

if len(username) < 5 or len(username) > 12:
    print("Invalid: Username must have 5 to 12 characters")
elif " " in username:
    print("Invalid: Username cannot contain spaces")
elif username[0].isdigit():
    print("Invalid: Username cannot start with a digit")
else:
    print("Valid username")


# In[5]:


username = input("Enter username: ")

if len(username) < 5 or len(username) > 12:
    print("Invalid: Username must have 5 to 12 characters")
elif " " in username:
    print("Invalid: Username cannot contain spaces")
elif username[0].isdigit():
    print("Invalid: Username cannot start with a digit")
else:
    print("Valid username")


# In[6]:


username = input("Enter username: ")

if len(username) < 5 or len(username) > 12:
    print("Invalid: Username must have 5 to 12 characters")
elif " " in username:
    print("Invalid: Username cannot contain spaces")
elif username[0].isdigit():
    print("Invalid: Username cannot start with a digit")
else:
    print("Valid username")


# In[7]:


sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for character in sentence.lower():
    if character in "aeiou":
        vowels = vowels + 1
    elif character in "bcdfghjklmnpqrstvwxyz":
        consonants = consonants + 1
    elif character == " ":
        spaces = spaces + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)


# In[8]:


sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for character in sentence.lower():
    if character in "aeiou":
        vowels = vowels + 1
    elif character in "bcdfghjklmnpqrstvwxyz":
        consonants = consonants + 1
    elif character == " ":
        spaces = spaces + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)


# In[10]:


sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for character in sentence.lower():
    if character in "aeiou":
        vowels = vowels + 1
    elif character in "bcdfghjklmnpqrstvwxyz":
        consonants = consonants + 1
    elif character == " ":
        spaces = spaces + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)


# In[11]:


sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for character in sentence.lower():
    if character in "aeiou":
        vowels = vowels + 1
    elif character in "bcdfghjklmnpqrstvwxyz":
        consonants = consonants + 1
    elif character == " ":
        spaces = spaces + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)


# In[12]:


sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for character in sentence.lower():
    if character in "aeiou":
        vowels = vowels + 1
    elif character in "bcdfghjklmnpqrstvwxyz":
        consonants = consonants + 1
    elif character == " ":
        spaces = spaces + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)


# In[13]:


name = input("Enter your name: ").strip().lower()

reversed_name = ""

for character in name:
    reversed_name = character + reversed_name

if name == "":
    print("Please enter a name")
elif name == reversed_name:
    print("Bonus! Your name is a palindrome.")
else:
    print("Your name is not a palindrome.")


# In[14]:


name = input("Enter your name: ").strip().lower()

reversed_name = ""

for character in name:
    reversed_name = character + reversed_name

if name == "":
    print("Please enter a name")
elif name == reversed_name:
    print("Bonus! Your name is a palindrome.")
else:
    print("Your name is not a palindrome.")


# In[15]:


name = input("Enter your name: ").strip().lower()

reversed_name = ""

for character in name:
    reversed_name = character + reversed_name

if name == "":
    print("Please enter a name")
elif name == reversed_name:
    print("Bonus! Your name is a palindrome.")
else:
    print("Your name is not a palindrome.")


# In[16]:


temps = [32, 35, 38, 41, 36, 29, 40]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

hottest_index = 0
fahrenheit = []

for i in range(len(temps)):
    if temps[i] > 37:
        print("Heat alert:", days[i])

    if temps[i] > temps[hottest_index]:
        hottest_index = i

    converted = temps[i] * 9 / 5 + 32
    fahrenheit.append(converted)

print("Hottest day:", days[hottest_index])
print("Temperature:", temps[hottest_index], "°C")
print("Temperatures in Fahrenheit:", fahrenheit)


# In[17]:


sentence = input("Enter a sentence: ")
words = sentence.split()

if len(words) == 0:
    print("No words entered")
else:
    longest = words[0]
    shortest = words[0]
    capital_count = 0

    for word in words:
        if len(word) > len(longest):
            longest = word

        if len(word) < len(shortest):
            shortest = word

        if word[0].isupper():
            capital_count = capital_count + 1

    print("Longest word:", longest)
    print("Shortest word:", shortest)
    print("Words starting with capital letter:", capital_count)


# In[18]:


sentence = input("Enter a sentence: ")
words = sentence.split()

if len(words) == 0:
    print("No words entered")
else:
    longest = words[0]
    shortest = words[0]
    capital_count = 0

    for word in words:
        if len(word) > len(longest):
            longest = word

        if len(word) < len(shortest):
            shortest = word

        if word[0].isupper():
            capital_count = capital_count + 1

    print("Longest word:", longest)
    print("Shortest word:", shortest)
    print("Words starting with capital letter:", capital_count)


# In[19]:


sentence = input("Enter a sentence: ")
words = sentence.split()

if len(words) == 0:
    print("No words entered")
else:
    longest = words[0]
    shortest = words[0]
    capital_count = 0

    for word in words:
        if len(word) > len(longest):
            longest = word

        if len(word) < len(shortest):
            shortest = word

        if word[0].isupper():
            capital_count = capital_count + 1

    print("Longest word:", longest)
    print("Shortest word:", shortest)
    print("Words starting with capital letter:", capital_count)


# In[20]:


sentence = input("Enter a sentence: ")
words = sentence.split()

if len(words) == 0:
    print("No words entered")
else:
    longest = words[0]
    shortest = words[0]
    capital_count = 0

    for word in words:
        if len(word) > len(longest):
            longest = word

        if len(word) < len(shortest):
            shortest = word

        if word[0].isupper():
            capital_count = capital_count + 1

    print("Longest word:", longest)
    print("Shortest word:", shortest)
    print("Words starting with capital letter:", capital_count)


# In[21]:


balances = [1500, -200, 3000, -50, 0, 750, -1000]

positive_accounts = []
negative_accounts = []

for balance in balances:
    if balance > 0:
        positive_accounts.append(balance)
    elif balance < 0:
        negative_accounts.append(balance)

total_owed = -sum(negative_accounts)

print("Positive accounts:", positive_accounts)
print("Negative accounts:", negative_accounts)
print("Total amount owed: Rs.", total_owed)


# In[22]:


password = input("Enter a password: ")

has_uppercase = False
has_lowercase = False
has_digit = False

for character in password:
    if character.isupper():
        has_uppercase = True

    if character.islower():
        has_lowercase = True

    if character.isdigit():
        has_digit = True

conditions_met = 0

if has_uppercase:
    conditions_met = conditions_met + 1

if has_lowercase:
    conditions_met = conditions_met + 1

if has_digit:
    conditions_met = conditions_met + 1

if len(password) >= 8:
    conditions_met = conditions_met + 1

if conditions_met == 4:
    print("Strong")
elif conditions_met >= 2:
    print("Medium")
else:
    print("Weak")


# In[23]:


password = input("Enter a password: ")

has_uppercase = False
has_lowercase = False
has_digit = False

for character in password:
    if character.isupper():
        has_uppercase = True

    if character.islower():
        has_lowercase = True

    if character.isdigit():
        has_digit = True

conditions_met = 0

if has_uppercase:
    conditions_met = conditions_met + 1

if has_lowercase:
    conditions_met = conditions_met + 1

if has_digit:
    conditions_met = conditions_met + 1

if len(password) >= 8:
    conditions_met = conditions_met + 1

if conditions_met == 4:
    print("Strong")
elif conditions_met >= 2:
    print("Medium")
else:
    print("Weak")


# In[24]:


password = input("Enter a password: ")

has_uppercase = False
has_lowercase = False
has_digit = False

for character in password:
    if character.isupper():
        has_uppercase = True

    if character.islower():
        has_lowercase = True

    if character.isdigit():
        has_digit = True

conditions_met = 0

if has_uppercase:
    conditions_met = conditions_met + 1

if has_lowercase:
    conditions_met = conditions_met + 1

if has_digit:
    conditions_met = conditions_met + 1

if len(password) >= 8:
    conditions_met = conditions_met + 1

if conditions_met == 4:
    print("Strong")
elif conditions_met >= 2:
    print("Medium")
else:
    print("Weak")


# In[25]:


password = input("Enter a password: ")

has_uppercase = False
has_lowercase = False
has_digit = False

for character in password:
    if character.isupper():
        has_uppercase = True

    if character.islower():
        has_lowercase = True

    if character.isdigit():
        has_digit = True

conditions_met = 0

if has_uppercase:
    conditions_met = conditions_met + 1

if has_lowercase:
    conditions_met = conditions_met + 1

if has_digit:
    conditions_met = conditions_met + 1

if len(password) >= 8:
    conditions_met = conditions_met + 1

if conditions_met == 4:
    print("Strong")
elif conditions_met >= 2:
    print("Medium")
else:
    print("Weak")


# In[26]:


full_name = input("Enter your full name: ")
names = full_name.split()

if len(names) == 0:
    print("Please enter a name")
else:
    initials = ""
    title_name = ""
    short_name = ""

    for i in range(len(names)):
        part = names[i].title()

        initials = initials + part[0] + "."

        if i > 0:
            title_name = title_name + " "

        title_name = title_name + part

        if i < len(names) - 1:
            short_name = short_name + part[0] + ". "
        else:
            short_name = short_name + part

    print("Initials:", initials)
    print("Title case:", title_name)
    print("Surname in full:", short_name)


# In[27]:


full_name = input("Enter your full name: ")
names = full_name.split()

if len(names) == 0:
    print("Please enter a name")
else:
    initials = ""
    title_name = ""
    short_name = ""

    for i in range(len(names)):
        part = names[i].title()

        initials = initials + part[0] + "."

        if i > 0:
            title_name = title_name + " "

        title_name = title_name + part

        if i < len(names) - 1:
            short_name = short_name + part[0] + ". "
        else:
            short_name = short_name + part

    print("Initials:", initials)
    print("Title case:", title_name)
    print("Surname in full:", short_name)


# In[ ]:




