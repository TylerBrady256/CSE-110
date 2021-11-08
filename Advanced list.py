people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 100
for less in people:

    less = less.split()
    age = int(less[1])
    name = less[0]
    
    if age < youngest:
        youngest = age
        name_youngest = name

print (f"the youngest person is {name_youngest} who is {youngest} years old")