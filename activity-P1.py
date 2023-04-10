"""
Problem 1:

Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on the item because it's black Friday sales.

Write a function that takes as input the amount of the asset that you are buying and a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.
"""

def calc_final_price(item_p, prime_member):
    black_friday_discount = item_p *0.92

    if prime_member:
        discount = black_friday_discount*0.85
    else:
        discount= black_friday_discount
    
    return discount
item_p = 98
prime_member = True
final_price = calc_final_price(item_p, prime_member)
print(final_price)