import matplotlib.pyplot as plt

year=[]
country=[]
abreviation = []
death_rate= []
h_l_finder =[]

with open("life-expectancy.csv") as life_expectancy_file:
    
    #seperates data into seperate list
    for lines in life_expectancy_file:
        data = lines.split(",")
        country.append(data[0])
        abreviation.append(data[1])
        year.append(data[2])
        death_rate.append(data[3].strip())
        h_l_finder.append(data[3].strip())
         

    #largest/smallest death rate finder
    h_l_finder.sort()
    h_l_finder.remove(h_l_finder[-1])
    largest_index = death_rate.index(h_l_finder[-1])
    lowest_index = death_rate.index(h_l_finder[0])
    print(f"largest {death_rate[largest_index]}, {country[largest_index]} in {year[largest_index]}")
    print(f"lowest {death_rate[lowest_index]}, {country[lowest_index]} in {year[lowest_index]}")

    #year indexer for personal imput
    what_year = input("\nwhat year would you like to see? ")
    indexes_year = []
    total = 0
    for years in range(len(year)):
        if year[years] == what_year: 
            indexes_year.append(years)
            total = total+float(death_rate[years]) 
    average = total / len(indexes_year)
    print(f"\nThe average life expectancy during this year was {average:.2f}")

    #highest in year
    highest_value = 0
    for value in indexes_year:
        if float(death_rate[value]) > highest_value:
            highest_value = float(death_rate[value])
            position = value 
    print(f"the highest value is {highest_value}, {country[position]} in {year[position]}")
    
    
    #lowest in year 
    lowest_value = highest_value
    for value in indexes_year:
        if float(death_rate[value]) < lowest_value:
            lowest_value = float(death_rate[value])
            position = value
    print(f"The lowest value is {lowest_value}, {country[position]} in {year[position]}")

    #Country indexer 
    x_axis = [] #year 
    y_axis = [] #Life expectancy 
    what_country = input("\nWhat country would you like to look up?")
    for nation in range(len(country)):
        indexed_nation = str(country[nation])
        if indexed_nation.lower() == what_country.lower():
            
            x_int = int(year[nation])
            y_int = float(death_rate[nation])
            x_axis.append(x_int)
            y_axis.append(y_int)
            print(f"{country[nation]} in {year[nation]} was {death_rate[nation]}")
    plt.plot (x_axis,y_axis)
    plt.xlabel ("Year")
    plt.ylabel ("Life Expectancy (in years)")
    plt.title (f"Life Expectancy over time in {what_country.capitalize()}")
    plt.show()