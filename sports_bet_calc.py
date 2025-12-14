#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from tkinter import *


def run_calculator():

    player = enter_name.get().lower()
    line_text = enter_line.get()

    try:
        line = float(line_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    # Title: nflverse-data/stats_player_week_2025.csv
    # Author: mrcaseb
   #  Date: 2025
   #  Code version: 2.0
   #  Availability: https://github.com/nflverse/nflverse-data/releases/tag/stats_player.

    infile = pd.read_csv("stats_player_week_2025.csv" , usecols=['player_display_name' , 'receiving_yards'])

    player_stats = infile[infile['player_display_name'].str.lower() == player]

    if player_stats.empty:
        lbl_result.config(text="Player not found.")
        return

    yards = player_stats['receiving_yards']


    over = 0
    under = 0
    tie = 0

    for row in yards:
        if row > line:
            over += 1
        elif row < line:
            under += 1
        else:
            tie += 1

    if over > under:
        lbl_result.config(text="-----OVER-----")
    elif under > over:
        lbl_result.config(text="-----UNDER-----")
    else:
        lbl_result.config(text="-----TIE-----")


root = Tk()

app = Frame(root)
app.grid()

root.title("SPORTS BETTING CALCULATOR")

title = Label(app, text='SPORTS BETTING CALCULATOR')
title.grid(row=0, column=0, columnspan=2, pady=10)

name_label = Label(app, text="Player First & Last Name:")
enter_name = Entry(app)
name_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
enter_name.grid(row=1, column=1, padx=5, pady=5, sticky="w")

number_label = Label(app, text="Enter Receiving Yards Line:")
enter_line = Entry(app)
number_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
enter_line.grid(row=2, column=1, padx=5, pady=5, sticky="w")

calc_bttn = Button(app, text="Calculate", command=run_calculator)
calc_bttn.grid(row=3, column=0, columnspan=2, pady=15)

lbl_result = Label(app, text="")
lbl_result.grid(row=4,column=0,columnspan=2,pady=10)

root.mainloop()




# In[ ]:




