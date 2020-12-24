import os
from art import logo

bidders = {}

next_bidder = True


def bidder_list(name, price):
    bidders[name] = price


while next_bidder:
    os.system('cls')
    print("Welcome To Blind Auction!!!")
    print(logo)
    name = input("Type Your Name:")
    price = int(input("Bid your Price:$"))
    bidder_list(name, price)
    if input('Are there any other Bidders? Type "yes" or "no":').lower() == "no":
        next_bidder = False

name_list = list(bidders.keys())
price_list = list(bidders.values())

winner = max(price_list)

print(f"The Winner is {name_list[price_list.index(winner)]} with a bid of {winner}")
