print(50*"=")
print("\t\t\t\tBaseball Team Manager")
print("""\nThis porgram calculates the batting average for a player based 
on the player's official nmber at bats and hits.""")
print(50*"=")
name = input("What is the batter's name? ") 
batting_number = int(input("What is the amount of times at bat? ")) 
hits = int(input("How many hits at bat? "))


average = hits / batting_number
print("{}'s Batting Average is:  {:.3f}".format(name,average))
