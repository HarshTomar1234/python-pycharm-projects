from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


# Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.grid(column=0, row=1)
kilometer_result_label = Label(text="0", font=("Arial", 24, "bold"))
kilometer_result_label.grid(column=1, row=1)
kilometer_label = Label(text="Km", font=("Arial", 24, "bold"))
kilometer_label.grid(column=2, row=1)


# Buttons

# calls miles_to_km() when pressed
calculate_button = Button(text="Calculate", command=miles_to_km, width=20, font=("Arial", 10, "bold"))
calculate_button.grid(column=1, row=2)

# Entries
miles_input = Entry(width=20, font=24)
# Add some text to begin with
miles_input.insert(END, string="0")
# Gets text in entry
print(miles_input.get())
miles_input.grid(column=1, row=0)

window.mainloop()
