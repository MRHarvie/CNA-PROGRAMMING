print(50*'=')

print("\t\t\tBaseball Team Manager")
print("MENU OPTIONS")
print("1 - Calculate betting average")
print("2 - Exit program")

print(50*"=")

program_running = True
while program_running:
    menu = int(input("Menu Option: "))
    if menu == 1:

        number_of_bats = float(input("Official number of at bats: "))
        hits = float(input("Number of hits: "))
        batting_a = (hits / number_of_bats)
        print("Batting average is: {:.3f}\n".format(batting_a))

    elif menu == 2:
        program_running = False
    else:
            print("\nThis is not a valid option.")
print("\nBye!")