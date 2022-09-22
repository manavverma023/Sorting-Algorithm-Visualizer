from asyncio import selector_events
from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root=Tk()
root.title('Sorting Algorithm Visualizer')
root.geometry('900x600+200+80')
root.config(bg='#b4ccc0')
data=[]

def drawData(data,colorArray):
    canvas.delete("all")
    canvas_height=450
    canvas_width=870
    x_width=canvas_width/(len(data)+1)
    offset=10
    spacing_bet_rect=10
    normalized_data=[i/max(data) for i in data]
    
    for i,height in enumerate(normalized_data):
        x0=i*x_width + offset + spacing_bet_rect
        y0=canvas_height-height*400   #multiplied by 400 to normalize the vlaues with one and data dont go out of canvas
        x1=(i+1)*x_width
        y1=canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=("Average Sans",15,"bold"),fill="orange")
    
    root.update_idletasks()
def StartAlgorithm():
    global data 
    if not data:
        return
    if (algo_menu.get()=="Quick Sort"):
        quick_sort(data,0,len(data)-1,drawData,speedscale.get())
        
    elif algo_menu.get()=="Bubble Sort":
        bubble_sort(data,drawData,speedscale.get())
    
    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, drawData, speedscale.get())
    drawData(data,['green' for x in range(len(data))])

def Generate():
    global data
    print("Selected Algorithm: "+ selected_algorithm.get())
    minivalue=int(minvalue.get())
    maxivalue=int(maxvalue.get())
    sizeevalue=int(sizevalue.get()) 
    data=[]
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue,maxivalue+1))
    drawData(data,['#f58142' for x in range(len(data))])
    
selected_algorithm=StringVar()

#label,buttons and speek
mainlabel=Label(root, text="Algorithm: ",font=("Average Sans",16,"bold"),bg="#69cf9e",width=10,relief=GROOVE,fg="black",bd=5)
mainlabel.place(x=0,y=0)

algo_menu=ttk.Combobox(root,width=15,font=("Average Sans",17,"bold"),textvariable=selected_algorithm,
                       values=["Bubble Sort","Merge Sort","Quick Sort"])
algo_menu.place(x=145,y=0)
algo_menu.current(0)

random_generate=Button(root,text="GENERATE",bg="#e86b79",font=("Average Sans",12,"bold"),relief=SUNKEN,activebackground="#eef06e",
                       activeforeground="white",bd=5,width=10,command=Generate)
random_generate.place(x=750,y=60)

sizevaluelabel=Label(root, text="Size: ",font=("Average Sans",12,"bold"),bg="#69cf9e",width=10,relief=GROOVE,fg="black",bd=5)
sizevaluelabel.place(x=0,y=60)
sizevalue=Scale(root,from_=3,to=30,resolution=1,orient=HORIZONTAL,font=("Average Sans",14,"bold"),relief=GROOVE,bd=2,width=8)
sizevalue.place(x=120,y=60)

minvaluelabel=Label(root, text="Min Value: ",font=("Average Sans",12,"bold"),bg="#69cf9e",width=10,relief=GROOVE,fg="black",bd=5)
minvaluelabel.place(x=250,y=60)
minvalue=Scale(root,from_=0,to=10,resolution=1,orient=HORIZONTAL,font=("Average Sans",14,"bold"),relief=GROOVE,bd=2,width=8)
minvalue.place(x=370,y=60)

maxvaluelabel=Label(root, text="Max Value: ",font=("Average Sans",12,"bold"),bg="#69cf9e",width=10,relief=GROOVE,fg="black",bd=5)
maxvaluelabel.place(x=500,y=60)
maxvalue=Scale(root,from_=0,to=100,resolution=1,orient=HORIZONTAL,font=("Average Sans",14,"bold"),relief=GROOVE,bd=2,width=8)
maxvalue.place(x=620,y=60)

start=Button(root,text="START",bg="#e86b79",font=("Average Sans",12,"bold"),relief=SUNKEN,activebackground="#eef06e",
             activeforeground="white",bd=5,width=10,command=StartAlgorithm)
start.place(x=750,y=0)

speedlabel=Label(root, text="Speed: ",font=("Average Sans",12,"bold"),bg="#69cf9e",width=10,relief=GROOVE,fg="black",bd=5)
speedlabel.place(x=400,y=0)
speedscale=Scale(root,from_=0.1,to=3.0,resolution=0.2,length=200,digits=2,orient=HORIZONTAL,font=("Average Sans",14,"bold"),relief=GROOVE,bd=2,width=8)
speedscale.place(x=520,y=0)

canvas=Canvas(root,width=870,height=450,bg="black")
canvas.place(x=10,y=150)


root.mainloop()