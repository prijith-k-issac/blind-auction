from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

bid_record = {}

def blind_auction_winner(bid_detail):
    highest_bid = 0
    highest_bidder_name = ""    
    for key in bid_detail:
            if bid_detail[key] > highest_bid:
                highest_bid = bid_detail[key]
                highest_bidder_name = key
    
    print(f"\nThe highest bid value is {highest_bid} and it's quoted by {highest_bidder_name}")

    
    
    
to_continue = "yes"
while to_continue == "yes":
    print(logo)
    bidder_name = input("\nYour name :\t")
    bid_value = int(input("\nEnter the bid value $\t"))
    bid_record[bidder_name] = bid_value
    user_entry = "wrong"
    while user_entry == "wrong":
        to_continue = input("\nAre there any other bidders: 'yes' or 'no'\t").lower()
        if to_continue == "yes" or to_continue == "no":
            user_entry = "right"
        else:
            print("Enter the option correctly")
    clear()

blind_auction_winner(bid_record) 
    
