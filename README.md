# structLib

structLib is essentially a module which contains the _Struct_ class. This class is specifically
aimed at making your life easier when working with JSON-like objects (meaning nested
_dict_ / _list_ objects)

## Installation

To install structLib on your python setup, run the following:
```bash
pip install structLib
```
On linux or mac you will probably need to run this command instead:
```bash
python3 -m pip install structLib
```
Please note that version 3.8 (or higher) of python is required to run this library!

## Usage

Let's have closer look at what we can do with this library and how...
If you take a look at the code or the help module you will notice that the _Struct_ class isn't the only element in there.
There is indeed a bunch of other functions defined. The only reason these functions are not part of the class is because 
they work using recursive algorithms, therefore it was way easier to implement them outside and then simply call them from 
the class methods when needed. Note that you **should not** be using those functions, the _Struct_ class handles all of that for you.

Now let's look at some code shall we? The following code can be found in the examples folder.
```python
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
```

## Requirements

None! That's also what is cool about it! 🙂

## Authors

[EddieBreeg](https://github.com/EddieBreeg)