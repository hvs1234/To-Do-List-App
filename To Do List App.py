#Libraries
from tkinter import *
from tkinter import messagebox,filedialog,colorchooser

#Application Setup
root = Tk()
root.title("To Do List App")
root.configure(bg="light blue")
root.resizable(False,False)
root.geometry("400x650+580+80")

#Functions
task_list = []

def addtask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("Tasklist.txt") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        list1.insert( END,task)

def opentask():
    try:
        global task_list
        with open("TaskList.txt","r") as taskfile :
            tasks = taskfile.readlines()
            for t in tasks:
                if t!='\n':
                    task_list.append(t)
                    list1.insert(END,t)
    except:
        file = open("Tasklist.txt","w")

#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\task.png")
img2 = PhotoImage(file="E:\\pyImages\\topbar.png")
img3 = PhotoImage(file="E:\\pyImages\\dock.png")
img4 = PhotoImage(file="E:\\pyImages\\task.png")
img5 = PhotoImage(file="E:\\pyImages\\delete.png")


root.iconphoto(False,img1)
l1 = Label(root,image=img2,bg="light blue"); l1.pack()
l2 = Label(root,image=img3,bg="#32405b"); l2.place(x=30,y=25)
l3 = Label(root,image=img4,bg="#32405b"); l3.place(x=340,y=25)
h1 = Label(root,text="ALL TASK",font="Algerian 20 bold",bg="#32405b",fg="white")
h1.place(x=130,y=20)
f1 = Frame(root,width=400,height=50,bg="light blue"); f1.place(x=0,y=180)
task = StringVar()
task_entry = Entry(f1,width=18,bd=4,
font="Arial 20 bold",fg="indigo",bg="light grey")
task_entry.place(x=10,y=7) ; task_entry.focus()

btn1 = Button(f1,text="ADD",font="Arial 20 bold",
width=6,bg="#5a95ff",fg="white",
activebackground="#5a95ff",activeforeground="white",command=addtask);
btn1.place(x=290,y=0)

f2 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
f2.pack(pady=(160,0))

list1 = Listbox(f2,font="arial 12 bold",width=40,height=16,bg="#32405b",
cursor="hand2",fg="white",selectbackground="#5a95ff")
list1.pack(side=LEFT,fill=BOTH,padx=2)
sc1 = Scrollbar(f2,bg="#32405b") ; sc1.pack(side=RIGHT,fill=BOTH)

list1.config(yscrollcommand=sc1.set)
sc1.config(command=list1.yview)

btn2 = Button(root,image=img5,bd=0,bg="light blue",activebackground="light blue")
btn2.pack(side=BOTTOM,pady=13)

opentask()
root.mainloop()