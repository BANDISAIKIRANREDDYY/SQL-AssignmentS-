#!/usr/bin/env python
# coding: utf-8

# In[1]:


age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Your ticket is free")
elif age <= 17:
    print("Your ticket price is Rs. 100")
elif age <= 59:
    print("Your ticket price is Rs. 200")
else:
    print("Your ticket price is Rs. 120")


# In[2]:


units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 8

    print("Total bill: Rs.", bill)


# In[3]:


number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
    


# In[4]:


total = 0
days = 0

while total < 1000:
    savings = float(input("Enter today's savings: "))

    if savings < 0:
        print("Savings cannot be negative. Enter again.")
    else:
        total = total + savings
        days = days + 1

print("Goal reached in", days, "days! Total saved: Rs.", total)


# In[5]:


correct_pin = "4321"
attempts = 0
access_granted = False

while attempts < 3 and access_granted == False:
    pin = input("Enter PIN: ")
    attempts = attempts + 1

    if pin == correct_pin:
        print("Access granted")
        access_granted = True
    else:
        print("Wrong PIN")

if access_granted == False:
    print("Card blocked")


# In[6]:


n = int(input("Enter N: "))

even_count = 0
odd_count = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# In[7]:


secret_number = 27
guesses = 0
correct = False

while correct == False:
    guess = int(input("Guess the number: "))
    guesses = guesses + 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        correct = True

print("Correct! You took", guesses, "guesses.")


# In[16]:


marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")


# In[18]:


96


# In[10]:


marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")


# In[11]:


marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")


# In[12]:


marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")


# In[13]:


marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")


# In[14]:


marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")


# In[15]:


marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Fail")


# In[19]:


bill_number = int(input("Enter bill number: "))

if bill_number < 0:
    print("Invalid bill number")
else:
    digit_sum = 0

    while bill_number > 0:
        digit = bill_number % 10
        digit_sum = digit_sum + digit
        bill_number = bill_number // 10

    print("Sum of digits:", digit_sum)

    if digit_sum > 20:
        print("Congratulations! You win a free gift.")
    else:
        print("Sorry, you do not get a free gift.")


# In[20]:


steps = int(input("Enter number of steps: "))

for row in range(1, steps + 1):
    for column in range(row):
        print("*", end="")
    print()


# In[ ]:




