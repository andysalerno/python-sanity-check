

# Let's start with loops...
for x in range(10):
    y = 'what scope is y in?'  # declare y in what appears to be an "inner scope," in this case a loop...

assert y == 'what scope is y in?'  # ...and it remains visible!
assert x == 9  # ...x also 'leaks' out. (My IDE actually interprets this wrongly, warning x and  y haven't been declared yet)

# repeat after me: for loops do not create a new scope!  Now let's talk about functions.

global_list = ['kitty']
def append_to_list():
    global_list.append('puppy')  # modifying an object from an upper scope is okay; the object will be modified...

append_to_list()
assert global_list == ['kitty', 'puppy']  # ...as you can see here.

def change_list_ref_broken():
    global_list = ['cat', 'dog']  # however, trying to change the reference will create a new reference for that scope
    assert global_list == ['cat', 'dog']
    inner_scope = 'I fall out of scope when the function ends!'

assert global_list == ['kitty', 'puppy']  # global_list didn't change outside the function scope
try:
    print(inner_scope)  # Can't access this -- will throw a NameError exception.
except NameError:
    pass

# classes have a keyword 'global' which lets them access the reference from its global scope. Observe:
class Seiko_Watch:
    global global_list
    global_list = ['diver watch', 'field watch', 'pilot watch']

assert global_list == ['diver watch', 'field watch', 'pilot watch']  # the reference itself changed at the global scope

# Note how we never even instantiated an object of Seiko_Watch.  Its member fields are processed anyway!