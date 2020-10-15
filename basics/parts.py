import tkinter as tk
from tkinter import messagebox
from db import Database

db = Database('store.db')


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Part Manager')
        master.geometry('700x350')
        self.create_widgets()
        self.populate_list()

    def create_widgets(self):
        # Part
        self.part_text = tk.StringVar()
        self.part_label = tk.Label(self.master, text="Part Name", font=('bold', 14), pady=20)
        self.part_label.grid(row=0, column=0, sticky=tk.W)
        self.part_entry = tk.Entry(self.master, textvariable=self.part_text)
        self.part_entry.grid(row=0, column=1)

        # Customer
        self.customer_text = tk.StringVar()
        self.customer_label = tk.Label(self.master, text="Customer", font=('bold', 14), pady=20)
        self.customer_label.grid(row=0, column=2, sticky=tk.W)
        self.customer_entry = tk.Entry(self.master, textvariable=self.customer_text)
        self.customer_entry.grid(row=0, column=3)

        # Retailer
        self.retailer_text = tk.StringVar()
        self.retailer_label = tk.Label(self.master, text="Retailer", font=('bold', 14))
        self.retailer_label.grid(row=1, column=0, sticky=tk.W)
        self.retailer_entry = tk.Entry(self.master, textvariable=self.retailer_text)
        self.retailer_entry.grid(row=1, column=1)

        # price

        self.price_text = tk.StringVar()
        self.price_label = tk.Label(self.master, text="Price", font=('bold', 14))
        self.price_label.grid(row=1, column=2, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=3)

        # Buttons
        self.add_btn = tk.Button(self.master, text='Add Part', width=12, command=self.add_item)
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(self.master, text='Remove Part', width=12, command=self.remove_item)
        self.remove_btn.grid(row=2, column=1, pady=20)

        self.update_btn = tk.Button(self.master, text='Update Part', width=12, command=self.update_item)
        self.update_btn.grid(row=2, column=2, pady=20)

        self.exit_btn = tk.Button(self.master, text='Clear Input', width=12, command=self.clear_text)
        self.exit_btn.grid(row=2, column=3, pady=20)

        # Part list (list box)
        self.parts_list = tk.Listbox(self.master, height=8, width=50, border=1)
        self.parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

        # bind a event to the list boc

    def populate_list(self):
        self.parts_list.delete(0, tk.END)

        for row in db.fetch():
            self.parts_list.insert(tk.END, row)

    def add_item(self):
        part = self.part_text.get()
        customer = self.customer_text.get()
        retailer = self.retailer_text.get()
        price = self.price_text.get()

        if part == '' or customer == '' or retailer == '' or price == '':
            messagebox.showerror(title="Required Fileds", message='Please include all fields')
            return

        db.insert(part, customer, retailer, price)
        self.parts_list.delete(0, tk.END)
        self.clear_text()
        self.populate_list()

    def remove_item(self):
        print("removing an item")

    def update_item(self):
        print("updaing an item")

    def clear_text(self):
        self.part_entry.delete(0, tk.END)
        self.retailer_entry.delete(0, tk.END)
        self.customer_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
