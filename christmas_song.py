# On the first day of Christmas
# My true love gave to me:
# A partridge in a pear tree.
#
# On the second day of Christmas
# My true love gave to me:
# Two turtle doves and
# A partridge in a pear tree.
#
# On the third day of Christmas
# My true love gave to me:
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the forth day of Christmas
# My true love gave to me:
# Four calling birds
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the fifth day of Christmas
# My true love gave to me:
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the sixth day of Christmas,
# My true love gave to me:
# Six geese a-laying
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the seventh day of Christmas,
# My true love gave to me:
# Seven swans a-swimming
# Six geese a-laying
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the eight day of Christmas,
# My true love gave to me:
# Eight maids a-milking
# Seven swans a-swimming
# Six geese a-laying
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the ninth day of Christmas,
# My true love gave to me:
# Nine ladies dancing
# Eight maids a-milking
# Seven swans a-swimming
# Six geese a-laying
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the tenth day of Christmas,
# My true love gave to me:
# Ten lords a-leaping
# Nine ladies dancing
# Eight maids a-milking
# Seven swans a-swimming
# Six geese a-laying
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the eleventh day of Christmas,
# My true love gave to me:
# Eleven pipers piping
# Ten lords a-leaping
# Nine ladies dancing
# Eight maids a-milking
# Seven swans a-swimming
# Six geese a-laying
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves and
# A partridge in a pear tree.
#
# On the Twelfth day of Christmas,
# My true love gave to me:
# Twelve drummers drumming
# Eleven pipers piping
# Ten lords a-leaping
# Nine ladies dancing
# Eight maids a-milking
# Seven swans a-swimming
# Six geese a-laying
# Five golden rings
# Four calling birds
# Three french hens
# Two turtle doves
# And a partridge in a pear tree.

days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth',
        'ninth', 'tenth', 'eleventh', 'Twelfth']
gifts = [
    'A partridge in a pear tree.',
    'Two turtle doves and',
    'Three french hens',
    'Four calling birds',
    'Five golden rings',
    'Six geese a-laying',
    'Seven swans a-swimming',
    'Eight maids a-milking',
    'Nine ladies dancing',
    'Ten lords a-leaping',
    'Eleven pipers piping',
    'Twelve drummers drumming'
]
for i in range(0, len(days)):

    print("""
    On the {} day of Christmas
    My true love gave to me:
    """.format(days[i]))
    elements =  gifts[:i+1][::-1]
    for elem in elements:
        print('\t',elem)
