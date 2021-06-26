import csv

sort_method = str(input("Would you like to sort by Rating, Ease of Prep, Type, Prep Time, or Ingredients? "))


if sort_method == "rating":
    stars = int(input("How many stars would you like your dish to be? (0 - 5) "))
    with open('recipes_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                #print(f'\t{row[0]} has a difficulty of {row[1]},{row[2]}.')
                #print({row[4]})
                if str(stars*"⭐")==str({row[1]}):
                    print({row[0]}+" has "+stars+" stars, is "+{row[2]}+" to make. It takes "+{row[4]}+" minutes to make and requires the following ingredients: "+{row[5]})
                line_count += 1