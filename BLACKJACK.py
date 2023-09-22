print("BLACKJACK!")
print("Blackjack payout is 3:2\n")

starting_money = float(input("Starting Money:  "))
bet_amount = float(input("Bet Amount:      "))

print("\nENDING MONEY FOR A...")
blackjack = (starting_money)+(bet_amount*1.5)
win = starting_money + bet_amount
push = starting_money
lose = starting_money - bet_amount
print("Blackjack:\t\t{}".format(blackjack))
print("Win:\t\t\t{}".format(win))
print("Push:\t\t\t{}".format(push))
print("Lose:\t\t\t{}".format(lose))
print("\nBye!")
