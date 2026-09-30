#!/usr/bin/env python
# coding: utf-8

# In[1]:


contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()

        if name in contacts:
            print("Contact already exists")
        else:
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print("Contact added")

    elif choice == "2":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts saved")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "4":
        break

    else:
        print("Invalid choice")


# In[2]:


contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()

        if name in contacts:
            print("Contact already exists")
        else:
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print("Contact added")

    elif choice == "2":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts saved")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "4":
        break

    else:
        print("Invalid choice")


# In[3]:


contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()

        if name in contacts:
            print("Contact already exists")
        else:
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print("Contact added")

    elif choice == "2":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts saved")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "4":
        break

    else:
        print("Invalid choice")


# In[4]:


visits = [101, 205, 101, 330, 205, 412, 101, 330, 509]

unique_visitors = set(visits)

print("Total visits:", len(visits))
print("Unique visitors:", len(unique_visitors))
print("Unique visitor IDs:", sorted(unique_visitors))


# In[5]:


marks = {
    "Aman": 82,
    "Priya": 91,
    "Rahul": 45,
    "Sneha": 67,
    "Kiran": 30
}

passed_students = {}
topper = ""
highest_marks = -1

for name, mark in marks.items():
    if mark >= 40:
        print(name, ": Pass")
        passed_students[name] = mark
    else:
        print(name, ": Fail")

    if mark > highest_marks:
        highest_marks = mark
        topper = name

print("Topper:", topper)
print("Topper's marks:", highest_marks)
print("Passed students:", passed_students)


# In[6]:


text = input("Enter text: ")
counts = {}

for character in text:
    if character != " ":
        counts[character] = counts.get(character, 0) + 1

print(counts)

if len(counts) == 0:
    print("No characters to count")
else:
    most_frequent = ""
    highest_count = 0

    for character, count in counts.items():
        if count > highest_count:
            highest_count = count
            most_frequent = character

    print(
        "Most frequent character:",
        most_frequent,
        "(" + str(highest_count) + " times)"
    )


# In[7]:


text = input("Enter text: ")
counts = {}

for character in text:
    if character != " ":
        counts[character] = counts.get(character, 0) + 1

print(counts)

if len(counts) == 0:
    print("No characters to count")
else:
    most_frequent = ""
    highest_count = 0

    for character, count in counts.items():
        if count > highest_count:
            highest_count = count
            most_frequent = character

    print(
        "Most frequent character:",
        most_frequent,
        "(" + str(highest_count) + " times)"
    )


# In[8]:


text = input("Enter text: ")
counts = {}

for character in text:
    if character != " ":
        counts[character] = counts.get(character, 0) + 1

print(counts)

if len(counts) == 0:
    print("No characters to count")
else:
    most_frequent = ""
    highest_count = 0

    for character, count in counts.items():
        if count > highest_count:
            highest_count = count
            most_frequent = character

    print(
        "Most frequent character:",
        most_frequent,
        "(" + str(highest_count) + " times)"
    )


# In[9]:


menu = {
    "dosa": 60,
    "idli": 40,
    "vada": 30,
    "coffee": 25,
    "tea": 15
}

total = 0

while True:
    item = input("Enter item or 'bill' to finish: ").strip().lower()

    if item == "bill":
        break
    elif item in menu:
        total = total + menu[item]
        print("Item added")
    else:
        print("Item not available")

print("Subtotal: Rs.", total)

if total > 200:
    discount = total * 0.10
    total = total - discount
    print("Discount: Rs.", discount)

print("Total bill: Rs.", total)


# In[10]:


cities = [
    ("Hyderabad", 17.38, 78.48),
    ("Mumbai", 19.07, 72.87),
    ("Chennai", 13.08, 80.27),
    ("Delhi", 28.61, 77.20)
]

northern_city = cities[0][0]
highest_latitude = cities[0][1]

for name, latitude, longitude in cities:
    print(name, "- Latitude:", latitude, "Longitude:", longitude)

    if latitude > highest_latitude:
        highest_latitude = latitude
        northern_city = name

print("Farthest north:", northern_city)
print("Highest latitude:", highest_latitude)

]


# In[11]:


books = {
    "Python Basics": 3,
    "Data Science 101": 0,
    "Machine Learning": 2,
    "SQL Guide": 1
}

book_name = input("Enter book name: ").strip()

if book_name not in books:
    print("Book not found")
elif books[book_name] == 0:
    print("Currently unavailable")
else:
    books[book_name] = books[book_name] - 1
    print("Book issued successfully")

print("Updated dictionary:", books)


# In[12]:


books = {
    "Python Basics": 3,
    "Data Science 101": 0,
    "Machine Learning": 2,
    "SQL Guide": 1
}

book_name = input("Enter book name: ").strip()

if book_name not in books:
    print("Book not found")
elif books[book_name] == 0:
    print("Currently unavailable")
else:
    books[book_name] = books[book_name] - 1
    print("Book issued successfully")

print("Updated dictionary:", books)


# In[13]:


employees = [
    ("Ravi", "IT"),
    ("Anjali", "HR"),
    ("Suresh", "IT"),
    ("Meena", "Finance"),
    ("Arun", "HR"),
    ("Divya", "IT")
]

departments = {}

for name, department in employees:
    if department not in departments:
        departments[department] = []

    departments[department].append(name)

print(departments)

for department, names in departments.items():
    print(department, ":", len(names), "employees")


# In[14]:


answer_key = ("B", "C", "A", "D", "B")

wrong_questions = set()
score = 0

for i in range(len(answer_key)):
    answer = input(
        "Enter answer for question " + str(i + 1) + ": "
    ).strip().upper()

    if answer == answer_key[i]:
        print("Question", i + 1, ": Correct")
        score = score + 1
    else:
        print("Question", i + 1, ": Wrong")
        wrong_questions.add(i + 1)

print("Wrong question numbers:", wrong_questions)
print("Final score:", score, "out of 5")

if score == 5:
    print("Excellent")
elif score >= 3:
    print("Good")
else:
    print("Needs improvement")


# In[15]:


answer_key = ("B", "C", "A", "D", "B")

wrong_questions = set()
score = 0

for i in range(len(answer_key)):
    answer = input(
        "Enter answer for question " + str(i + 1) + ": "
    ).strip().upper()

    if answer == answer_key[i]:
        print("Question", i + 1, ": Correct")
        score = score + 1
    else:
        print("Question", i + 1, ": Wrong")
        wrong_questions.add(i + 1)

print("Wrong question numbers:", wrong_questions)
print("Final score:", score, "out of 5")

if score == 5:
    print("Excellent")
elif score >= 3:
    print("Good")
else:
    print("Needs improvement")


# In[16]:


answer_key = ("B", "C", "A", "D", "B")

wrong_questions = set()
score = 0

for i in range(len(answer_key)):
    answer = input(
        "Enter answer for question " + str(i + 1) + ": "
    ).strip().upper()

    if answer == answer_key[i]:
        print("Question", i + 1, ": Correct")
        score = score + 1
    else:
        print("Question", i + 1, ": Wrong")
        wrong_questions.add(i + 1)

print("Wrong question numbers:", wrong_questions)
print("Final score:", score, "out of 5")

if score == 5:
    print("Excellent")
elif score >= 3:
    print("Good")
else:
    print("Needs improvement")


# In[17]:


answer_key = ("B", "C", "A", "D", "B")

wrong_questions = set()
score = 0

for i in range(len(answer_key)):
   answer = input(
       "Enter answer for question " + str(i + 1) + ": "
   ).strip().upper()

   if answer == answer_key[i]:
       print("Question", i + 1, ": Correct")
       score = score + 1
   else:
       print("Question", i + 1, ": Wrong")
       wrong_questions.add(i + 1)

print("Wrong question numbers:", wrong_questions)
print("Final score:", score, "out of 5")

if score == 5:
   print("Excellent")
elif score >= 3:
   print("Good")
else:
   print("Needs improvement")


# In[18]:


answer_key = ("B", "C", "A", "D", "B")

wrong_questions = set()
score = 0

for i in range(len(answer_key)):
    answer = input(
        "Enter answer for question " + str(i + 1) + ": "
    ).strip().upper()

    if answer == answer_key[i]:
        print("Question", i + 1, ": Correct")
        score = score + 1
    else:
        print("Question", i + 1, ": Wrong")
        wrong_questions.add(i + 1)

print("Wrong question numbers:", wrong_questions)
print("Final score:", score, "out of 5")

if score == 5:
    print("Excellent")
elif score >= 3:
    print("Good")
else:
    print("Needs improvement")


# In[ ]:




