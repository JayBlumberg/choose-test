from tkinter import *

master = Tk()
v=IntVar()
msg = ""


Label(master, text="Welcome to the Chooze toolbox", font = "helvetica 16 bold", fg = "dark green", height = 2).grid(row=0, column=5)

Label(master, text="Sales Extracts",font = "helvetica 16 bold", fg = "dark green").grid(row=25, column=3)
Label(master, text="Scripts",font = "helvetica 16 bold", fg = "dark green").grid(row=25, column = 8)

Label(master, text="Inventory",font = "helvetica 16 bold", fg = "dark green").grid(row=80, column=3)
Label(master, text="Best Practices",font = "helvetica 16 bold", fg = "dark green").grid(row=80, column = 8)


Radiobutton(master, text="Amazon Sales", variable=v,value=1).grid(row=40, column=3, sticky = W)
Radiobutton(master, text="Zappos Sales", variable=v,value=2).grid(row=50, column=3, sticky = W)
Radiobutton(master, text="Other Sales", variable=v,value=3).grid(row=60, column=3, sticky = W)

Radiobutton(master, text="Deploy Script to Server", variable=v,value=4).grid(row=40, column=8, sticky = W)
Radiobutton(master, text="Publish Webpage", variable=v,value=5).grid(row=50, column=8, sticky = W)
Radiobutton(master, text="Create Excel or PDF", variable=v,value=6).grid(row=60, column=8, sticky = W)
Radiobutton(master, text="Deploy Shopify to Marketplace", variable=v,value=7).grid(row=70, column=8, sticky = W)


Radiobutton(master, text="Show All", variable=v,value=8).grid(row=100, column=3, sticky = W)
Radiobutton(master, text="Show by Producct", variable=v,value=9).grid(row=110, column=3, sticky = W)
Radiobutton(master, text="Other", variable=v,value=10).grid(row=120, column=3, sticky = W)


Radiobutton(master, text="Publish Best Practice", variable=v,value=11).grid(row=110, column=8, sticky = W)
Radiobutton(master, text="Create Best Practice Document", variable=v,value=12).grid(row=100, column=8, sticky = W)


def mystart_process():
    x = v.get()
    msg = ""
    print ("start process = ", x)
    if x == 1:
        import SQL_test
        msg = "Amazon Sales Retrieved"
        Label(master, text="Message=" + msg, fg = "red").grid(row=130, column = 3)


Button(master, text='Quit', command = master.quit).grid(row=150, column=7)
Button(master, text='Start', command = mystart_process).grid(row=150, column=5)
                                 
mainloop( )
