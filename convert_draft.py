#Written and created by Paul "Phil" Billingsby. 2018.
def conv():


        #Main converter that is apart of the Converter Program.
        print (" 1: Miles/Km\n 2: F°/C°\n 3: Lbs/Kg")
        options1 = input("Please type 1, 2 or 3 to select conversion: ")
        bad_input = ("Input not recognized. Try again.\n") #Intro input strings

        if not options1 in ["1", "2", "3"]: #If option selected isn't 1, 2 or 3
                print (bad_input)#This piece of code seems to run fine right now.
                conv()
        if options1 == "1": #If options1 = 1: Distance conversion selected
            mile2 = "Type '1' to convert to KM or "
            km2 = "Type '2' to convert to Miles: "
            conv_dist = input(mile2 + km2) #Gets user input
            if not conv_dist in ["1", "2"]: #If input not 1, or 2
                    print (bad_input)
                    conv()
            if conv_dist == "1": #Selects Miles to KM
                m_in = input("Type distance in miles: ")
                if int(m_in.isdigit()) == False: #Prints error string if distance isnt a number.
                    print (bad_input)
                    conv()
                m_out = float(m_in) * 1.609 #Formula
                print ("Your result is: {0:.3f} km".format(m_out) +"\n") #String format results
                conv()
            elif conv_dist == "2": #Selects KM to Miles
                km_in = input("Type distance in kilometers: ")
                if int(km_in.isdigit()) == False: #Prints error string if distance less/equal to 0
                    print (bad_input + "\n")
                    conv()
                else:
                    km_out = float(km_in) / 1.609 #Formula
                    print ("Your result is: {0:.3f} miles".format(km_out) + "\n") #String format
                conv()

        if options1 == "2": #If options1 = 2: Temperature conversion selected.
            cel2 = "Type '1' to convert to F° or "
            fah2 = "'2' to convert to C°: " 
            conv_temp = input(cel2 + fah2) #Concatenated string in input
            if not conv_temp in ["1", "2"]: #If input not 1, or 2
                print (bad_input)
                conv()

            if conv_temp == "1": #Selects C to F
                cel_in = input("Type temperature in Celcius: ")
                if int(cel.isdigit()) == False: #If cel_in isn't a number, print error
                        print (bad_input)
                        conv()
                if int(cel_in) > 10000: #If input exceeds 10000
                        print ("Wow thats incredibly hot.\n")
                        conv()
                else:
                        cel_out = (float(cel_in) * 9/5) + 32 #Formula
                        print ("Your result is: {0:.3f}F°\n".format(cel_out)) #String format results
                        conv()
            elif conv_temp == "2": #Selects F to C
                fah_in = input("Type temperature in Fahrenheit: ")
                if int(fah_in.isdigit()) == False:
                        print (bad_input) 
                        conv()
                if int(fah_in) > 10000:
                    print ("Wow thats incredibly hot.\n")
                    conv()
                else:
                        fah_out = (float(fah_in) - 32) * 5/9 #Formula
                        print ("Your result is: {0:.3f}C°\n".format(fah_out))
                        conv()
        if options1 == "3": #If options1 = 3: Weight conversion selected.
            kg2 = "Type '1' to convert to pounds or "
            lbs2 = "Type '2' to convert to kilograms: "
            conv_weight = input(kg2 + lbs2) #Gets user input
            if not conv_weight in ["1", "2"]:
                print (bad_input)
                conv()
            if conv_weight == "1":
                kg_in = input("Type weight in kg: ")
                if int(kg_in.isdigit()) == False:
                        print (bad_input)
                        conv()
                else:
                        kg_out = int(kg_in) * 2.205 #KG to Lbs formula.
                        print ("Your result is: {0:.2f}".format(kg_out) + "lbs\n")
                        conv()
            elif conv_weight == "2":
                lbs_in = input("Type weight in lbs: ")
                if int(lbs_in.isdigit()) == False:
                        print (bad_input)
                        conv()
                else:
                        lbs_out = int(lbs_in) / 2.205 #Lbs to KG formula
                        print ("Your result is: {:.2f}".format(lbs_out) + "kg\n")
                        conv()
                        

    



        

