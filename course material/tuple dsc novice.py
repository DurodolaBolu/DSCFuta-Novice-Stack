# Python Tuples

'''Python provides another type that is an ordered collection of objects, called a tuple

Tuples are identical to lists in all respects, except for the following properties:

1. Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([])
2. Tuples are immutable.

Here is a short example showing a tuple definition, indexing, and slicing'''

empty_tuple = ()
my_tuple = ('this', 'is', 'my', 'tuple','data', 'type')

my_tuple[0]

my_tuple[1:5]

'''Do not fret, Our favorite string and list reversal mechanism works for tuples as well:'''

my_tuple[::-1]

'''Note: Even though tuples are defined using parentheses, you still index
and slice tuples using square brackets, just as for strings and lists'''

'''Everything you’ve learned about lists—they are ordered, they can contain arbitrary
objects, they can be indexed and sliced, they can be nested—is true of tuples as well.
But they can’t be modified:
'''
food = ('semo', 'fried rice', 'yam',)

my_tuple[0] = 'Spaghetti'



