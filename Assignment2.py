#!/usr/bin/env python
# coding: utf-8

# ## Question 1
# 
# Consider the following Python module:
# What value is displayed when the last expression (a) is evaluated? Explain your
# answer by indicating what happens in every executed statement.
# 

# In[149]:


a = 0
def b():
    global a
    a = c(a)
def c(a):
    return a + 2

b()
b()
b()
print(a)


# Answer 1 :
# 
# The answer displayed is 6
# We are making the local variable 'a' as a global variable as it can be used within the fuction c().
# First a=o, then it is declared global and passed to c, where it gets added as 2 and returned .Again this process repeats twice, a gets added up and becomes 6.

# 
# ## Question 2.
# Function fileLength(), given to you, takes the name of a file as input and returns the length of the file:
# 
# fileLength('midterm.py')
# 284
# fileLength('idterm.py')
# Traceback (most recent call last):
# File "<pyshell#34>", line 1, in <module>
#  fileLength('idterm.py')
# File "/Users/me/midterm.py", line 3, in fileLength
#  infile = open(filename)
# FileNotFoundError: [Errno 2] No such file or directory:
# 'idterm.py'
# As shown above, if the file cannot be found by the interpreter or if it cannot be read
# as a text file, an exception will be raised. Modify function fileLength() so that a
# friendly message is printed instead:
# fileLength('midterm.py')
# 358
# fileLength('idterm.py')
# File idterm.py not found.

# In[10]:


def file_length(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        file.close()
        print(len(contents))
    except FileNotFoundError:
        print(file_name+" not found")

file_length('currencies.txt')
file_length('wrongfile.py')


# ## Question 3
# Write a class named Marsupial that can be used as shown below:
# m = Marsupial()
# m.put_in_pouch('doll')
# m.put_in_pouch('firetruck')
# m.put_in_pouch('kitten')
# m.pouch_contents()
# ['doll', 'firetruck', 'kitten']
# Now write a class named Kangaroo as a subclass of Marsupial that inherits all the
# attributes of Marsupial and also:
# 
# a. extends the Marsupial __init__ constructor to take, as input, the
# coordinates x and y of the Kangaroo object,
# b. supports method jump that takes number values dx and dy as input and
# moves the kangaroo by dx units along the x-axis and by dy units along the yaxis, and
# c. overloads the __str__ operator so it behaves as shown below.
#  k = Kangaroo(0,0)
# print(k)
# I am a Kangaroo located at coordinates (0,0)
# k.put_in_pouch('doll')
#  k.put_in_pouch('firetruck')
#  k.put_in_pouch('kitten')
#  k.pouch_contents()
# ['doll', 'firetruck', 'kitten']
#  k.jump(1,0)
#  k.jump(1,0)
#  k.jump(1,0)
#  print(k)
# I am a Kangaroo located at coordinates (3,0)

# In[33]:


class Marsupial:
    
    def __init__(self):
        self.pouch=[]
    def put_in_pouch(self,item):
        self.pouch.append(item)
    def pouch_contents(self):
        print(self.pouch)
        
class Kangaroo(Marsupial):
    def __init__(self,x1,y1):
        self.x = x1
        self.y = y1
        Marsupial.__init__(self)
    
    def jump(self,x1,y1):
        self.x = self.x + x1
        self.y = self.y + y1
        
    def __str__(self):
        return 'print(k) I am a Kangaroo located at coordinates ({}, {})'.format(self.x, self.y)

m=Marsupial()
m.put_in_pouch("doll")
m.put_in_pouch("firetruck")
m.put_in_pouch("kitten")
m.pouch_contents()

k=Kangaroo(0,0)
print(k)
k.put_in_pouch("doll")
k.put_in_pouch("firetruck")
k.put_in_pouch("kitten")
k.pouch_contents()

k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# ## Question 4
# Write function collatz() that takes a positive integer x as input and prints the
# Collatz sequence starting at x. A Collatz sequence is obtained by repeatedly applying
# this rule to the previous number x in the sequence:
# x = {
# 𝑥/2 𝑖𝑓 𝑥 𝑖𝑠 𝑒𝑣𝑒𝑛
# 3𝑥 + 1 𝑖𝑓 𝑥 𝑖𝑠 𝑜𝑑𝑑
# Your function should stop when the sequence gets to number 1. Your
# implementation must be recursive, without any loops

# In[39]:


def collatz(x):
    print(int(x))
    if x > 1:
        if x%2==0:
            collatz(int(x)/2)
        else:
            collatz((int(x) * 3) + 1)
collatz(10)


# ## Question 5
# Write a recursive method binary() that takes a non-negative
# integer n and prints the binary representation of integer n.

# In[72]:


def binary(n):
       if n == 0 :
           return 0
       else:
           return (n % 2 + 10 * binary(int(n // 2)))         
binary(9)


# 
# ## Question 6
# Implement a class named HeadingParser that can be used to parse an HTML document, and retrieve and print all the headings in the document. You should implement your class as a subclass of HTMLParser, defined in Standard Library module html.parser. When fed a string containing HTML code, your class should print the headings, one per line and in the order in which they appear in the document. Each heading should be indented as follows: an h1 heading should have indentation 0, and h2 heading should have indentation 1, etc. Test your implementation using w3c.html.
# 
# infile = open('w3c.html') content = infile.read() infile.close() hp = HeadingParser() hp.feed(content) W3C Mission Principles
# 
# 

# In[95]:


class HeadingParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        self.tag = tag 
    def handle_data(self, data):
        if self.tag in ['h1','h2','h3','h4','h5','h6']:
            n=int(self.tag[1])       
            print (n*' '+data, end = '')
  
infile = open('w3c.html')
content = infile.read()
infile.close()
parser = HeadingParser()
parser.feed(content)
            


# ## Question 7
# Implement recursive function webdir() that takes as input: a URL (as a string) and non-negative integers depth and indent. Your function should visit every web page reachable from the starting URL web page in depth clicks or less, and print each web page's URL. As shown below, indentation, specified by indent, should be used to indicate the depth of a URL.
# 
# webdir('http://reed.cs.depaul.edu/lperkovic/test1.html', 2, 0)
# 
# http://reed.cs.depaul.edu/lperkovic/test1.html
# 
# http://reed.cs.depaul.edu/lperkovic/test2.html
# 
#     http://reed.cs.depaul.edu/lperkovic/test4.html
# 
# http://reed.cs.depaul.edu/lperkovic/test3.html
# 
#     http://reed.cs.depaul.edu/lperkovic/test4.html

# In[ ]:


Not Completed


# ## Question 8
# Write SQL queries on the below database table that return:
# 
# a) All the temperature data.
# 
# b) All the cities, but without repetition.
# 
# c) All the records for India.
# 
# d) All the Fall records.
# 
# e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters.
# 
# f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.
# 
# g) The total annual rainfall for Cairo.
# 
# h) The total rainfall for each season.

# In[134]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[135]:


get_ipython().run_line_magic('sql', 'sqlite://')


# In[136]:


get_ipython().run_cell_magic('sql', '', 'CREATE TABLE Weather (City varchar(50), Country varchar(50), Season varchar(50), Temperature float, Rainfall float)')


# In[137]:


get_ipython().run_cell_magic('sql', '', "INSERT INTO Weather VALUES ('Mumbai','India','Winter',24.8,5.9);\nINSERT INTO Weather VALUES ('Mumbai','India','Spring',28.4,16.2);\nINSERT INTO Weather VALUES ('Mumbai','India','Summer',27.9,1549.4);\nINSERT INTO Weather VALUES ('Mumbai','India','Fall',27.6,346.0);\nINSERT INTO Weather VALUES ('London','United Kingdom','Winter',4.2,207.7);\nINSERT INTO Weather VALUES ('London','United Kingdom','Spring',8.3,169.6);\nINSERT INTO Weather VALUES ('London','United Kingdom','Summer',15.7,157.0);\nINSERT INTO Weather VALUES ('London','United Kingdom','Fall',10.4,218.5);\nINSERT INTO Weather VALUES ('Cairo','Egypt','Winter',13.6,16.5);\nINSERT INTO Weather VALUES ('Cairo','Egypt','Spring',20.7,6.5);\nINSERT INTO Weather VALUES ('Cairo','Egypt','Summer',27.7,0.1);\nINSERT INTO Weather VALUES ('Cairo','Egypt','Fall',22.2,4.5);")


# In[138]:


get_ipython().run_line_magic('sql', 'SELECT * FROM Weather;')


# In[139]:


get_ipython().run_cell_magic('sql', '', 'SELECT Temperature FROM Weather')


# In[140]:


get_ipython().run_cell_magic('sql', '', 'SELECT DISTINCT City FROM Weather')


# In[141]:


get_ipython().run_cell_magic('sql', '', "SELECT * FROM Weather WHERE Country = 'India'")


# In[142]:


get_ipython().run_cell_magic('sql', '', "SELECT * FROM Weather WHERE Season = 'Fall'")


# In[143]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM Weather WHERE Rainfall >= 200 AND Rainfall <= 400')


# In[144]:



get_ipython().run_cell_magic('sql', '', 'SELECT City, Country FROM Weather WHERE Temperature > 20.0 ORDER BY Temperature ASC')


# In[145]:


get_ipython().run_cell_magic('sql', '', "SELECT SUM(Rainfall) FROM Weather Where City = 'Cairo'")


# In[147]:


get_ipython().run_cell_magic('sql', '', 'SELECt SUM(Rainfall) FROM Weather GROUP BY Season')


# 
# ## question 9
# Suppose list words is defined as follows:
# 
# words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# 
# Write list comprehension expressions that use list words and generate the following lists:
# 
# a) in Upper case letters
# 
# b) in lower case letters
# 
# c) the list of lengths of words in list words
# 
# d) the list containing a list for every word of list words, where each list contains the word in uppercase and lowercase and the length of the word
# 
# e) the list of words in list words containing 4 or more characters

# In[148]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print([word.upper() for word in words])
print([word.lower() for word in words])
print([len(word) for word in words])
print([[word.upper(), word.lower(), len(word)] for word in words])
print([word for word in words if len(word) > 3])


# In[ ]:




