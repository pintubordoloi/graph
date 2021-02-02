from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

root = Tk()

root.geometry("1200x700")
root.title("Graph")

data_size = 0


def open_file():

    if graph_frame.winfo_children():
        for widget in graph_frame.winfo_children():
            widget.destroy()

    file = askopenfilename()
    graph_data = pd.read_csv(file)
    print(len(graph_data))
    global data_size
    data_size = len(graph_data)
    fig = Figure(figsize=(5,5), dpi=100)
    plot1 = fig.add_subplot(111)
    graph_data.plot(kind='bar', legend=True, ax=plot1)
    canvas = FigureCanvasTkAgg(fig, graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, graph_frame)
    toolbar.update()
    canvas.get_tk_widget().pack()


def enter_data():
    print('Inside Enter Data')
    print(data_size)


def display_data():
    print('Inside Display data')
    print(data_size)
    for i in range(data_size):
        entries = Entry(data_frame, fg='blue', font=('Arial', 16, 'bold'))
        for j in 1:
            entries.grid(row=i, column=j)




##graph frame to hold graph
graph_frame = Frame(root, bd=4, relief=RIDGE)
graph_frame.place(x=0, y=0, width=600, height=650)


##info frame to hold info about the graph
info_frame = Frame(root, bd=4, relief=RIDGE)
info_frame.place(x=600, y=0, width=600, height=650)

##data frame to get the data from the user
data_frame = Frame(info_frame, bd=4, relief=RIDGE)
data_frame.place(x=0, y=50, width=599, height=600)

entry1 = Entry(data_frame, fg='blue', font=('Arial', 16, 'bold'))
entry1.grid(row=0, column=0)

entry2 = Entry(data_frame, fg='blue', font=('Arial', 16, 'bold'))
entry2.grid(row=0, column=1)


button1 = Button(info_frame, text='Open', command=open_file)
button1.grid(row=0, column=0)

button2 = Button(info_frame, text='Enter Data', command=enter_data)
button2.grid(row=0, column=1)


root.mainloop()