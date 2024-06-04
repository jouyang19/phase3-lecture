my_dict = {
    'name': 'joe',
    'age': 55
}

# TODO Key Lookups
my_dict['key']
# How to pronounce: my dict sub element

# TODO Nested lists
my_dict['sub'] = {'name': 'anne', 'age' : 66} # define a nested list
my_dict['sub']['name'] #access nested lists 

# TODO Using invalid key
my_dict['badkey'] # raises KeyError

# TODO Add a key/value pair
my_dict['newkey'] = 'new value'

# TODO Update a value
my_dict['name'] = 'sam'

# TODO Test if a key exists
'name' in my_dict # True 
'badkey' in my_dict # False

# TODO use .get()
# my_dict.get('key', 'default value')
my_dict.get('name')
my_dict.get('badkey', 'missing value')

# TODO Delete a key
# my_dict.pop('key')
# del my_dict.pop('key')
my_dict.pop('sub')
del my_dict['phone']

# TODO get the length of a dict
len(my_dict)

# TODO Merge two dicts
# my_dict.update(other_dict)
x = { 'age': 6, 'phone': '555-555-5555'}
my_dict.update(x)

# TODO copy a dict
my_dict.copy()

# TODO loop over a dict
for key in my_dict:
    print(key, my_dict[key])

# Using .items() for dict iteration
for key, value in my_dict.items():
    print(key, value)