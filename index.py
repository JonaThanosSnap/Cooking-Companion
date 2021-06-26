#imported Libraries

import csv

import tkinter as tk

#creating tkinter window

window = tk.Tk()

window.geometry("800x500")

window.configure(bg = "")

#function for getting the inputted ingredients

def search():

    global ingredients

    ingredients = text_box.get("1.0",tk.END).splitlines()

    window.destroy()

#tkinter widgets

label = tk.Label(text="What ingredients do you own?")

text_box = tk.Text()

button = tk.Button(text="Enter",command = search)

label.pack()

text_box.pack()

button.pack()

window.mainloop()

makeable_food = []

#reads the CSV file

with open('recipes_data.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0

    #we don't want to inclue the first row which are the headers

    for row in csv_reader:

        if line_count == 0:

            line_count += 1

        #splits the ingredients and puts them into an array

        else:

            ingredient_list = (row[5].split(","))

            matches = 0

            for i in ingredients:

                matches += ingredient_list.count(i)

            #if over 80% of the ingredients needed for the dish are owned, it is considered makeable

            if (matches/len(ingredient_list)) >= 0.8:

                makeable_food.append(row[0]+" is rated "+row[1]+", has a difficulty rating of "+row[2]+", is a "+row[3]+", and takes "+row[4]+"m to make. The ingredients needed are: "+row[5]+"." )

#more tkinter windows for displaying final results

text_box2 = tk.Text(width = 200)

text_box2.tag_configure("center",justify = "center")

if len(makeable_food) > 0:

    text_box2.insert("1.0","You can make the following dishes with your ingredients:" + "\n" + "\n")

    for x in makeable_food:

        text_box2.insert(tk.END, x + "\n" + "\n")

#if none of your ingredients match, you cannot make anything :(

else:

    text_box2.insert("5.0","Unfortunately, nothing can be made with your ingredients")

text_box2.tag_add("center","1.0","end")

text_box2.pack()

window.mainloop()
