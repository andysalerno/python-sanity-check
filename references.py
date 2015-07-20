# This is a quick and simple overview of references in Python.  It is both for my own benefit and for anyone
# who likes a nice reminder about how these things work.

animals = ['cat', 'cow', 'donkey', 'horse']  # we create a list
animals_copy = ['cat', 'cow', 'donkey', 'horse']  # and then create another list with identical values

animals_reference = animals  # make create a reference and assign it to the same object to which animals is assigned
assert animals_reference is animals  # both references point to the same object, and therefore share *identity*
assert animals_reference == animals  # equal identity means equality (an object is equal to itself)

assert animals_copy is not animals  # the other list refers to a different object
assert animals_copy == animals  # but the other object is still equivalent


# Lists can get tricky!  Don't think of it like a contiguous array of objects, think of it just as a list of
# references! Observe...

cat = animals[0]  # cat points to the same object as animals[0].
assert cat is animals[0]  # no copy occurred, still same object

animals[0] = animals[0].capitalize()  # refer animals[0] to the output of animals[0].capitalize()
assert cat is not animals[0]  # animals[0] now refers to another object
assert animals_reference is animals  # underlying list was altered, no copy occurred
assert animals_copy != animals  # animals changed, its list is no longer equal in content to animals_copy

animals_slice = animals[0:]  # make a slice of animals that is the full size of animals
assert animals_slice is not animals  # interesting! slicing for the full length yields a copy
assert animals_slice == animals  # which is obviously still equivalent in content. This is useful.

# let's move on...



# To be continued...
