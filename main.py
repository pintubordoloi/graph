from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from csv import reader

root = Tk()

root.geometry("1200x700")
root.title("Graph")

data_size = 0
data_row =0


def open_file():

    if graph_frame.winfo_children():
        for widget in graph_frame.winfo_children():
            widget.destroy()

    file = fd.askopenfilename()
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
    print(file)
    #printing the table when a csv file is open
    display_data(table_frame,file)
    


def enter_data():
    print('Inside Enter Data')
    

#function to display data in table format
def display_data(frame,name):
    with open(name,'r') as read_obj:
        #reading as ab object
    	csv_reader = reader(read_obj)
    	tot_row=0
        #reading each row of the csv file
    	for row in (csv_reader):
            #so that row can be set to 0,1,2,3...and not 1,2,3,4,5
            #since adding row+1 at the end of the second for loop 
            #getting indentation error 
    		tot_row=tot_row+1
    		tot_col=0
            #taking one value of each row at a time     		
    		for data in row:
    			e = Entry(frame, width=8,fg='blue',font=('Ariel',11,'italic'))
    			e.grid(row=(tot_row-1),column=tot_col)
    			e.insert(END,data)
    			tot_col=tot_col+1
           




##graph frame to hold graph
graph_frame = Frame(root, bd=4, relief=RIDGE)
graph_frame.place(x=0, y=0, width=600, height=650)


##info frame to hold info about the graph
info_frame = Frame(root, bd=4, relief=RIDGE)
info_frame.place(x=600, y=0, width=600, height=650)

##data frame to get the data from the user
data_frame = Frame(info_frame, bd=4, relief=RIDGE)
data_frame.place(x=0, y=50, width=599, height=600)

#Frame to hold table data of the given csv file 
table_frame= Frame(root, bd=4, relief=RIDGE)
table_frame.place(x=601, y=51, width=600, height=598) 

#entry1 = Entry(data_frame, fg='blue', font=('Arial', 16, 'bold'))
#entry1.grid(row=0, column=0)

#entry2 = Entry(data_frame, fg='blue', font=('Arial', 16, 'bold'))
#entry2.grid(row=0, column=1)


button1 = Button(info_frame, text='Open', command=open_file)
button1.grid(row=0, column=0)

button2 = Button(info_frame, text='Enter Data', command=enter_data)
button2.grid(row=0, column=1)

#t= display_data(table_frame)


root.mainloop()
