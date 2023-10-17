
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

# section = doc.find('section')

print(doc.select('.heading-primary')[0].contents[0].strip())

# print(doc.select('.heading-25-extrabold.color-black'))

#Instead of just outputting the results of doc.select, if we assign them to a variable, we can then iterate over that variable using a for loop

courses = doc.select('.heading-25-extrabold.color-black')
for course in courses:
    print(course.contents[0].strip())


courses1 = doc.select('.heading-25-extrabold.color-black')[0]
print(courses1)

#the output is 
#<h3 class="heading-25-extrabold color-black"> Software Engineering  </h3>
 # this is This is an bs4.element.Tag object.
 # 
name = doc.select('.heading-25-extrabold.color-black')[0].name
print(name)
#it should output
# => 'h2'   which is the name of the tag element    

print(doc.select('.heading-25-extrabold.color-black')[0].attrs)                                                         





