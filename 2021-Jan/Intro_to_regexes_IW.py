#!/usr/bin/env python
# coding: utf-8

# # An introduction to Regular Expressions in Python

# Ian Watt - Aberdeen Python User Group, 13 January 2021
# 
# Licence: [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/)

# ## Finding strings 
# Finding strings inside longer strings in Python is quite  easy __if__ you know what you are looking for. 

# In[1]:


#find where the string 'name' occurs
str = 'Hello. My name is Ian'
print(str.find('name')) # prints the start position 


# Q. Why was that not 11? 

# ### But ...
# if we want to find something which we don't know the value of (eg. any name that falls after "my name is") or more general patterns (eg. any date, a four digit year, or a Postcode) where we don't know what the exact value is, we need a better way to do that. Imagine a file containing the following:
# 
# __Date Number of sales__ 
# 
# 01 Jan 2019, 47
# 
# 4 Jun 2019 -  91
# 
# 15 Dec 2019 -  66
# 
# 28 Feb 2020, 81
# 
# 1 March 2021, 100
# 
# 29 Jul 21: 43
# 
# etc.
# 
# How would we gather all the datesEnter __Regular Expressions__ (often referred to as _Regexes_ )

# ## Using Regexes for  the first time

# Let's start by importing the Regular Expressions library 

# In[2]:


import re


# Now set up a string in which to search:

# In[3]:


str = "Today's date is 13 Jan 2021."


# Then create a _match object_
# 
# We give it the _re_ search method, some pattern to match, and our target text string. 
# 
# We know that a digit is represented as '\d' so we'll work with that.
# 
# We'll come back to the syntax of the pattern - in this case we say four digits.

# In[4]:


mo = re.search(r'\d\d\d\d', str)


# The match object is a Python object with properties of its own which we can request and use. 

# In[6]:


print(mo)


# In[8]:


print(mo.group()) #the matching group of characters found


# In[10]:


print(f"Start: {mo.start()}, End: {mo.end()}") #start and end positions of the matching group


# In[12]:


print (mo.string) #the string we are searching in


# In[14]:


print (mo.span()) #same as start / end


# ### Pattern syntax
# 
# In our match object  above we ask for '\d\d\d\d'
# 
# '\d' means 'any digit' - so this means any four  consecutive digits. 
# 
# You'll note that the '13' of the date _didn't_ match our pattern as it has two digits followed by  a whitespace character. Only the four consective digits  of 2021 matched. 
# 
# There is a more elegant way to specify four digits: \d{4}
# 
# Try it:

# In[16]:


mo = re.search(r'\d{4}', str)
print(mo.group())


# In[18]:


mo = re.search(r'\d{2,4}', str) #minimum of 2 times, max of 4 times
print(mo.group())


# And we can specify a minimum and maximum number by using 
# '{2,4}' to ask for a minimum of 2 and a maximum of 4 items. 

# ### Extending our search pattern

# How can we find  the first two digits of the date (representing the day)?

# In[20]:


mo = re.search(r'\d{2}', str)
print(mo.group())


# #### Adding the month
# 
# We can create a pattern for alphabetic characters thus
# 
# '[A-Za-z]'
# 
# The 'A-Z' asks for capital letters, and 'a-z' for lower case letters. 

# In[22]:


mo = re.search(r'[A-Za-z]', str)
print(mo.group())


# That gets the first single alphabetic character of our string ('T'). 
# 
# As our query asks for the first instance of an alphabetic character in our _set_ enclosed in square brackets: [ ].
# 
# What would happen if, instead of '[A-Za-z]' we just said '[a-z]'?
# 
# Applying what we know about groups of characters we can extend that:

# In[24]:


mo = re.search(r'[A-Za-z]{3}', str)
print(mo.group())


# That returns the  first three alphabetic characters of the string. 

# So - putting these together how can we get the full date? 
# 
# First we need to know how Regexes handle whitespace. 
# 
# We can specify a whitespace as '\s'

# In[26]:


mo = re.search(r'\s', str)
print(mo.span())


# Can you see how that matches the first occurring space after "Today's" in our string?
# 
# Let's put that all together. 
# 
# We need
# - 2 digits
# - a space
# - 3 letters 
# - a space
# - 4 digits
# 
# Can you write it?  Give it a go before scrollling down

# In[49]:


#add your code here















# In[29]:


#this should work
mo = re.search(r'\d{2}\s[A-Za-z]{3}\s\d{4}', str)
print(mo.group())


# ### Improving our pattern
# 
# How can we improve what we have? What if someone accidentally slips two spaces in, instead of one? Try the following. 

# In[42]:


str2 = "Today's date is 13 Jan  2021."
mo = re.search(r'\d{2}\s[A-Za-z]{3}\s\d{4}', str2)
print (mo.group())

'''
# The example above fails as the mo has not been created as the search fails. 
# we can fix this by checking first

str2 = "Today's date is 13 Jan  2021."
mo = re.search(r'\d{2}\s[A-Za-z]{3}\s\d{4}', str2)

if mo:
    print(mo.group())
else: 
    print("Match Object does not exist as the pattern was not found")
'''


# We can improve our search patterns to guard against that by saying look for one or more whitespace characters. 
# 
# The syntax for that is:
# 
# - '\s+'

# In[44]:


#this should work now (note the plus sign after each 's' character)
mo = re.search(r'\d{2}\s+[A-Za-z]{3}\s+\d{4}', str2)
print(mo.group())
print ("       ^ Note the double space after 'Jan'")


# ## Some useful things to know. 
# Special sequences (as we've seen with '\d' and '\s\'
# 
# ### Special Sequences 
# - \A	Returns a match if the specified characters are at the beginning of the string	"\AWh"
# - \b	Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\band"
# - \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bone"
# - \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# - \D	Returns a match where the string DOES NOT contain digits	"\D"
# - \s	Returns a match where the string contains a white space character	"\s"
# - \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# - \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# - \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# - \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
# 
# And metacharacters.
# 
# ### Metacharacters
# * "[ ]"	A set of characters	"[p-z]"
# * "\"	used before a special sequence (or to escape special characters)	"\d"
# * "."	ANY character (except newline character)	"ba..n"
# * "^"	Starts with	"^Today"
# * "$"	Ends with "erdeen$"
# * "*"	Zero or more occurrences	"fix*"
# * "+"	One or more occurrences	"fix+"
# * "{}"	Exactly the specified number of occurrences	"iss{2}"
# * "|"	Either or	"cats|dogs"
# * "()"	Capture group
# 
# [more examples](https://www.w3schools.com/python/python_regex.asp)

# ### Looking for other things
# 
# We can look for other characters in a similar way
# 

# In[43]:


str3 = "Today's date is 13-Jan-21."
mo = re.search(r'\d{2}-[A-Za-z]{3}-\d{2}', str3) #search for date containing"-" character a
print(mo.group())

str4 = "Today's date is 13/Jan/21."
mo = re.search(r'\d{2}/[A-Za-z]{3}/\d{2}', str4) #search for date containing"/" character a
print(mo.group())


# ## Capture Groups
# We can tell RE to give us back only a part of the match - a capture group. This is useful if you want to make sure that you match a full postcode, for example, but only the area part before the space, or match a full date but only return the year. 
# 
# Capture Groups are denoted by ()

# In[45]:


sc = "Jim's Phone Number: 01224 999999"

mo = re.search(r'Number: ([\d\s]+)', sc) #Match "Number: " and a sequence of numbers and spaces but just capture the numbers and space
print(mo.group(1))


# In[47]:


# A named capture group
mo = re.search(r'Number: (?P<number>.+)', sc) #here the capture group is named by the <number> 
print(mo.group('number'))


# Those named goups can then be referenced again. See the additional resources below. 

# 
# ### Assertions
# 
# Sometimes we want to find something only if it is followed bye somethis else. So Python needs to _look ahead_. 
# 
# For example, what if we want to find "Aberdeen," only if it is followed by "Scotland"? 
# 
# We use'?=' to specify what the query must look ahead to. 

# In[50]:


sa = 'Aberdeen, Scotland is a city of 221,091 people.'

mo = re.search(r'Aberdeen(?=, Scotland)', sa)
print(mo.group())


# In[52]:


sb = 'Aberdeen, Washington is a city of 16,896 people.'

mo = re.search(r'Aberdeen(?=, Scotland)', sb)
print(mo.group()) # this will fail when ', Scotland' is not found


# ### Negative assertions
# 
# We can search for a term only if it is NOT followed by a certain term using '?!'

# In[54]:


sc = 'Aberdeen, Scotland is a city of 16,896 people.'

mo = re.search(r'Aberdeen(?!, Washington)', sc) #find 
#print(mo.group()) # ', Washington' is not found, so the search succeeds


# ## Finding all instances of a set of characters
# 
# We can use the re.findall() function

# In[56]:


phrase = 'Welcome to Episode 3. In Chapter 2, on page 5, at line 17 you will find what you are looking for'
print(re.findall(r'\d+', phrase))
#try changing the '+' to an asterisk "*" What happens? Why? 


# In[58]:


phrase = 'Welcome to Episode 3. In Chapter 2, on page 5, at line 17 you will find what you are looking for.'
print(re.findall(r'[A-Z][a-z]+', phrase)) #find a Capital letter followed by one or more alphabetic character


# ## Compiling regexes
# We can create and save a pattern, and reuse it, for example in a loop. This is much more efficicent than putting the pattern to be used in the loop itself. 

# In[61]:


myRegex = re.compile(r'\d+') 
# This reads the file line-by-line
for line in open("TestFile.txt", 'r'):
    print(myRegex.findall(line))


# ## More resources
# 
# * An introduction to Python Regular Expressions https://www.pythoncentral.io/introduction-to-python-regular-expressions/ (four parts)
# * Python Regex at W£ Schools https://www.w3schools.com/python/python_regex.asp 
# * Regex101 - test your patterns: https://regex101.com 

# In[ ]:




