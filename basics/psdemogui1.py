"""a sample gui app"""

from tkinter import Tk, Label

root = Tk()  # window
root.title('a sample GUI app')
root.geometry('350x200')
lbl = Label(root, text='Greetings', underline=1, font=['Courier', 50])
lbl.pack()
root.mainloop()