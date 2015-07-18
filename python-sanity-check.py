animals = ['cat', 'cow', 'donkey', 'horse']  # we start with a list
animals_copy = ['cat', 'cow', 'donkey', 'horse']  # and then make another list with the same values

animals_reference = animals  # make another reference and assign it to animals
assert animals_reference is animals  # both have same identity (refer to same object)
assert animals_reference == animals  # both refer to same object which is equal to itself

assert animals_copy is not animals  # the other list refers to a different object
assert animals_copy == animals  # but the other object is still equivalent

cat = animals[0]  # refer cat to animals[0]
assert cat is animals[0]  # no copy occurred, still same object

animals[0] = animals[0].capitalize()  # modify first element of animals
assert cat is not animals[0]  # animals[0] now refers to another object
assert animals_reference is animals  # underlying list was altered, no copy occurred
assert animals_copy != animals  # animals changed, its list is no longer equal in content to animals_copy

animals_slice = animals[0:]  # make a slice of animals that is the full size of animals
assert animals_slice is not animals  # interesting! slicing for the full length yields a copy
assert animals_slice == animals  # which is obviously still equivalent in content. This is useful.

# To be continued...
