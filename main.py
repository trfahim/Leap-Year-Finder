##(1)
from tkinter import *
import tkinter.messagebox
import tkinter as tk


##(2)
def check():

  global year
  year = entry_1.get()

  try:
    YEAR = int(year)
  except ValueError:

    tkinter.messagebox.askokcancel(title="Invalid input",
                                   message="You can only use numbers.")

  if YEAR % 4 == 0:

    result_1 = tk.Label(window,
                        text=f"\n**{YEAR} is a leap year.**",
                        font=("Times 15", 15, "bold"),
                        bg=("#1ABC9C"),
                        fg=("black"))
    result_1.grid(
      row=4,
      column=1,
      pady=5,
      padx=5,
    )

  else:
    result_2 = tk.Label(window,
                        text=f"\n{YEAR} is not a leap year.",
                        font=("Times 15", 15, "bold"),
                        bg=("#1ABC9C"),
                        fg=("black"))
    result_2.grid(
      row=4,
      column=1,
      pady=5,
      padx=5,
    )


##(3)
window = tk.Tk()
window.title("Leap Year Finder-[TR Fahim]")
window.config(background=("#1ABC9C"))
window.geometry("500x280")

##(4)
label_1 = tk.Label(window,
                   text="Leap Year Finder",
                   padx=10,
                   pady=10,
                   font="Georgiav 15",
                   bg=("#1ABC9C"),
                   fg="blue")
label_1.grid(row=1, column=1, pady=10, padx=5)

label_0 = tk.Label(window,
                   text="ENTER YEAR",
                   padx=10,
                   pady=5,
                   font="bold",
                   bg=("#e4c2f5"),
                   fg="black")

label_0.grid(row=2, column=0, pady=10, padx=5)

entry_1 = tk.Entry(window, text="YYYY", width=10, font="Arial 20")

entry_1.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

year = 0

button_1 = tk.Button(window,
                     text="Check",
                     command=check,
                     width=5,
                     bg="thistle1",
                     pady=5,
                     padx=5,
                     relief=GROOVE,
                     font="Georgia 15")

button_1.place(x=180, y=200)

window.mainloop()

### end ###
