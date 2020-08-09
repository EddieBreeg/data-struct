# This code aims to illustrate how we can use structLib
from structLib import Struct

# You will notice I only import the Struct class, the reason in because it's the only thing actually useful for us

with open("actors.json") as f_in:
    data = Struct.load(f_in)  # First we load the data into a Struct object.

print(data, '\n')

"""Let's say I want to see if "Tom Cruise" is present in the data structure
I could use the Struct.isValueIn() method but if I want to know where the value is, there is a better option
"""

path = data.pathToValue("Tom Cruise")  # If the value doesn't exist in the Struct, the result will be None
print(path)

# Now I want to get his age:

age = data["Actors", 0, 'age']
print(age, '\n')

# The value is wrong let's fix that
data["Actors", 0, "age"] = 58

# Let's add Jonny Depp in there
jonny = {
    "name": "Jonny Depp",
    "age": 57,
    "Born At": "Owensboro, Kentucky",
    "Birthdate": "June 9, 1963",
    "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Johnny_Depp_Deauville_2019.jpg/390px"
             "-Johnny_Depp_Deauville_2019.jpg",
}

data['Actors'].append(jonny)

print(data, '\n')

# Let's say I want to print the ages of everyone:
for a in data.getAll("age"):
    print(a)

# Now let's sort them by age
data['Actors'] = Struct(data['Actors']).sorted(path="age").data
# Here I have to do this complicated mess because the list isn't at the top level of the structure but rather under
# the "Actors" key
print(data)

# Finally let's write that back into the file
with open("sorted_actors.json", 'w') as f_out:
    data.dump(f_out, indent=4)
