# Change Return Program - The user enters a cost and then the amount of money
# given. The program will figure out the change and the number of quarters,
#  dimes, nickels, pennies needed for the change.

print("""
In Poland we've got:
1gr, 2gr, 5gr, 10gr, 20gr, 50gr, 1zl, 2zl, 5zl, 10zl, 20zl, 50zl, 100zl, 200zl
 """)

cost = float(input("Enter cost of an item: "))
money = float(input("Enter amoutn of money given: "))

difference = round(money - cost, 2)
print(difference)
difference = str(difference).split('.')
print(difference)

grosze = int(difference[1])
zlotych = int(difference[0])

two_hundred = zlotych // 200
zlotych %= 200
one_hundred = zlotych // 100
zlotych %= 100
fifty_zloty = zlotych // 50
zlotych %= 50
twenty_zloty = zlotych // 20
zlotych %= 20
ten_zloty = zlotych // 10
zlotych %= 10
five_zloty = zlotych // 5
zlotych %= 5
two_zloty = zlotych // 2
zlotych %= 2
one_zloty = zlotych // 1
print("""
{} notes - 200zl,
{} notes - 100zl,
{} notes - 50zl,
{} notes - 20zl,
{} notes - 10zl,
{} coin - 5zl,
{} coin - 2zl,
{} coin - 1zl""".format(two_hundred, one_hundred, fifty_zloty, twenty_zloty,
 ten_zloty, five_zloty, two_zloty, one_zloty))

fifties = grosze // 50
grosze %= 50
twenties = grosze // 20
grosze %= 20
tens = grosze // 10
grosze %= 10
fives = grosze // 5
grosze %= 5
twoes = grosze // 2
grosze %= 2
ones = grosze // 1


print("""
{} - 50 groszy,
{} - 20 groszy,
{} - 10 groszy,
{} - 5 groszy,
{} - 2 groszy,
{} - 1 gorszy.""".format(fifties, twenties, tens, fives, twoes, ones))
