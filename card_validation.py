# Credit Card Validator - Takes in a credit card number from a common credit card
# vendor (Visa, MasterCard, American Express, Discoverer) and validates it to
# make sure that it is a valid number (look into how credit cards use a checksum).

"""
 Most credit card number can be validated using the Luhn algorithm, which is
 more or a less a glorified Modulo 10 formula!
The Luhn Formula:

1. Drop the last digit from the number. The last digit is what we want to check
    against
2. Reverse the numbers
3. Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to
 all any result higher than 9
4. Add all the numbers together
5. The check digit (the last number of the card) is the amount that you would
need to add to get a multiple of 10 (Modulo 10)

"""
# Drop the last digit from the number. The last digit is what we want to check against
card_number = input("Enter a credit card number to validate: ")
last_digit = card_number[-1]
# print(last_digit)
card_number = card_number[:-1]
# reverse the numbers
card_number = card_number[::-1]
# print(card_number)

#  Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to
# all any result higher than 9
odd_digits = []
even_digits = []
for i, num in enumerate(card_number):
    if i % 2 == 0:
        odd_digits.append(int(num) * 2)
    else:
        even_digits.append(int(num))
# 4. Add all the numbers together
# print(odd_digits)
# print(even_digits)
all_digits = odd_digits + even_digits
print(all_digits)
digits = []
for num in all_digits:
    if num > 9:
        num = num - 9
        digits.append(num)
    else:
        digits.append(num)
# print(digits)

# 5. The check digit (the last number of the card) is the amount that you would
# need to add to get a multiple of 10 (Modulo 10)
sum_digits = sum(digits)
# print(sum_digits)
if sum_digits % 10 == int(last_digit):
    print("The card is valid")
else:
    print("The card is not valid")
