from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bil Management")
root.resizable(False,False)
'''determines whether the window can be resized by the user or no.'''

'''function the reset button will perform'''
def Reset():
    entry_dosa.delete(0,END)
    entry_cookies.delete(0,END)
    entry_tea.delete(0,END)
    entry_coffee.delete(0,END)
    entry_juice.delete(0,END)
    entry_pizza.delete(0,END)
    entry_sandwich.delete(0,END)
    entry_total.delete(0,END)
    '''END specifies the ending index of text to be deleted'''

'''function the total button will perform'''
def Total():
    try:
        a1=int(Dosa.get())
    except:
        a1=0

    try:
        a2=int(Cookies.get())
    except:
        a2=0

    try:
        a3=int(Tea.get())
    except:
        a3=0

    try:
        a4=int(Coffee.get())
    except:
        a4=0

    try:
        a5=int(Juice.get())
    except:
        a5=0

    try:
        a6=int(Pizza.get())
    except:
        a6=0

    try: a7=int(Sandwich.get())
    except: a7=0
    
#define cost
    c1=60*a1
    c2=30*a2
    c3=15*a3
    c4=20*a4
    c5=100*a5
    c6=170*a6
    c7=90*a7
    lbl_total=Label(f2,font=("aria",20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)
    
    entry_total.place(x=20,y=100)
    
    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f'%totalcost)
    Total_bill.set(string_bill)
    
    

Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()
'''The pack() method is used to organize the label within its parent widget (in this case, the root window).'''

#menucard
f = Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa.........Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Cookies......Rs.30/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Tea..........Rs.15/plate",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Coffee.......Rs.20/plate",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Juice........Rs.100/plate",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Pizza........Rs.170/plate",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Sandwich....Rs.90/plate",fg="black",bg="lightgreen").place(x=10,y=260)

#bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)
Bill=Label(f2,text="Bill",font=("calibri",20),bg="lightyellow")
Bill.place(x=120,y=10)

#entry work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Dosa=StringVar()
Cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
Pizza=StringVar()
Sandwich=StringVar()
Total_bill=StringVar()

#Label

lbl_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
lbl_cookies=Label(f1,font=("aria",20,'bold'),text="Cookies",width=12,fg="blue4")
lbl_tea=Label(f1,font=("aria",20,'bold'),text="Tea",width=12,fg="blue4")
lbl_coffee=Label(f1,font=("aria",20,'bold'),text="Coffee",width=12,fg="blue4")
lbl_juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=12,fg="blue4")
lbl_pizza=Label(f1,font=("aria",20,'bold'),text="Pizza",width=12,fg="blue4")
lbl_sandwich=Label(f1,font=("aria",20,'bold'),text="Sandwich",width=12,fg="blue4")

lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_tea.grid(row=3,column=0)
lbl_coffee.grid(row=4,column=0)
lbl_juice.grid(row=5,column=0)
lbl_pizza.grid(row=6,column=0)
lbl_sandwich.grid(row=7,column=0)


#Entry

entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=Dosa,bd=6,width=8,bg="lightpink")
entry_cookies=Entry(f1,font=("aria",20,'bold'),textvariable=Cookies,bd=6,width=8,bg="lightpink")
entry_tea=Entry(f1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg="lightpink")
entry_coffee=Entry(f1,font=("aria",20,'bold'),textvariable=Coffee,bd=6,width=8,bg="lightpink")
entry_juice=Entry(f1,font=("aria",20,'bold'),textvariable=Juice,bd=6,width=8,bg="lightpink")
entry_pizza=Entry(f1,font=("aria",20,'bold'),textvariable=Pizza,bd=6,width=8,bg="lightpink")
entry_sandwich=Entry(f1,font=("aria",20,'bold'),textvariable=Sandwich,bd=6,width=8,bg="lightpink")
entry_total=Entry(f2,font=("aria",20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")

entry_dosa.grid(row=1,column=1)
entry_cookies.grid(row=2,column=1)
entry_tea.grid(row=3,column=1)
entry_coffee.grid(row=4,column=1)
entry_juice.grid(row=5,column=1)
entry_pizza.grid(row=6,column=1)
entry_sandwich.grid(row=7,column=1)

#buttons

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="RESET",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="TOTAL",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()
'''starts the Tkinter event loop, allowing the GUI to interact with the user.'''


