def batting_avg():
    def sep_line():
        '''
        

        Creates a Seperator
        
        Parameters
        -------
        character : string
            seperator character.
            
        Returns
        -------
        String
            A ling with seperators.

        '''
        print(50*'=')

    sep_line()
    def title():    
        print("\t\t\tBaseball Team Manager")
    
    def menuz():
            print("MENU OPTIONS")
            print("1 - Calculate batting average")
            print("2 - Exit program")
    title()
    menuz()

    sep_line()

    program_running = True
    while program_running:
        menu = int(input("Menu Option: "))
        if menu == 1:

            number_of_bats = float(input("Official number of at bats: "))
            hits = float(input("Number of hits: "))
            def batting_a(hits, number_of_bats):
                b_a = number_of_bats / hits
                return b_a
            calculated_ba = batting_a(number_of_bats,hits)
            print("Batting average is: {:.3f}\n".format(calculated_ba))

        elif menu == 2:
            program_running = False
        else:
            print("\nThis is not a valid option.")
            print("\nMENU OPTIONS\n1 - Calculate Batting Average\n2 - Exit Program")
batting_avg()
print("\nBye!")