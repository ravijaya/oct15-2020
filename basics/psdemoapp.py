from csv import reader
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

fig = fig = Figure(figsize=(5, 4), dpi=100)
root = tk.Tk()

style = ttk.Style(root)
style.theme_use("clam")


def c_open_file_old():
    global fig
    rep = filedialog.askopenfilenames(parent=root,
                                      initialdir='C:',
                                      # initialfile='tmp',
                                      filetypes=[("CSV", "*.csv"),
                                                 ("PNG", "*.png"),
                                                 ("JPEG", "*.jpg"),
                                                 ("All files", "*")])

    # for row in reader(open(rep[0])):
    #     list_box.insert(tk.END, row)
    sales = pd.read_csv(rep[0], parse_dates=['date'])
    customers = sales[['name', 'ext price', 'date']]
    customers_group = customers.groupby('name')
    sales_total = customers_group.sum()
    sorted_sales_total = sales_total.sort_values(by='ext price', ascending=False)
    bar_plot = sorted_sales_total.plot(kind='bar', title='Total Sales by Customer')
    bar_plot.set_xlabel('Customers')
    bar_plot.set_ylabel('Sales ($)')
    fig = bar_plot.get_figure()
    fig.savefig('cust.png')

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

    # pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().grid(row=0, column=1, columnspan=3, rowspan=6, pady=20, padx=20)


ttk.Label(root, text='Default dialogs').grid(row=0, column=0,
                                             padx=4, pady=4,
                                             sticky='ew')
ttk.Button(root, text="Open files", command=c_open_file_old).grid(row=1, column=0,
                                                                  padx=4, pady=4,
                                                                  sticky='ew')

# list_box = tk.Listbox(root, height=8, width=50, border=1)

root.mainloop()
