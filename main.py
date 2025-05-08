from tkinter import *

def calculate():
    miles = float(user.get())
    result = int(miles * 1.609)
    output.config(text=result)

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

Mile = Label(text="Miles", font=("Arial", 24))
Mile.grid(column=2, row=0)

is_equal_to = Label(text="is equal to",font=("Arial", 24))
is_equal_to.grid(column=0, row=1)

output = Label(text="0",font=("Arial", 24))
output.grid(column=1, row=1)

Km = Label(text="Km", font=("Arial", 24))
Km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

user = Entry(width=7)
user.insert(END, string = "0")
user.grid(column=1, row=0)



window.mainloop()
