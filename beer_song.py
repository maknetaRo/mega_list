# Display the complete lyrics for the song:     99 Bottles of Beer on the Wall.
#
# The beer song
#
# The lyrics follow this form:
#
#     99 bottles of beer on the wall
#     99 bottles of beer
#     Take one down, pass it around
#     98 bottles of beer on the wall
#
#     98 bottles of beer on the wall
#     98 bottles of beer
#     Take one down, pass it around
#     97 bottles of beer on the wall
#
# ... and so on, until reaching 0.
#
# Grammatical support for "1 bottle of beer" is optional.
#
# As with any puzzle, try to do it in as creative/concise/comical a way as
# possible (simple, obvious solutions allowed, too).

for i in range(99, 0, -1):
    print("""
    {} bottles of beer on the wall
    {} bottles of beer
    Take on down pass it around
    {} bottles of beer on the wall
    """.format(i, i, i-1))
