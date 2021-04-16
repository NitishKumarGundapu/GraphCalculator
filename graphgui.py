import numpy as np
from numpy import *
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from tkinter import messagebox as msg

def parser(eq,a,b):
    try : 
        x = np.linspace(a,b,1000)
        if type(eval(eq)) == np.ndarray :
            return True 
        else :
            return False
    except Exception as e:
        return False

def get_graph():
    eq = eq_var.get()
    a,b = lb_var.get(),ub_var.get()
    gv = var1.get()
    if parser(eq,a,b) and a<b:
        try : 
            x = np.linspace(a,b,1000)
            y = eval(eq)
            plt.plot(x,y,color = "green",label=eq)
            plt.legend()
            plt.axhline(y=0,color='red')
            plt.axvline(x=0,color='red')
            plt.xlabel("X-Values")
            plt.ylabel("Y-Values")
            if gv == 1:
                plt.grid(True)
            plt.show()
    
        except Exception as e: 
            return 
    else :
        msg.showerror("Error","Enter the Correct Details")

root = Tk()
root.title("Graph Calculator")
root.geometry("500x450")
root.resizable(False,False)

#Graph Calculator
Title_label = Label(root,text="Graph Calculator",width=30,font=("Consolas",18)).place(x=53,y=35)

#Equation
eq_label = Label(root,text="Equation",width=15,font=("Consolas",10)).place(x=55,y=135)
eq_var = StringVar()
eq_entry = ttk.Entry(root,width=25,textvariable=eq_var).place(x=265,y=135)

#Lower Bound
lb_label = Label(root,text="Lower Bound",width=15,font=("Consolas",10)).place(x=55,y=185)
lb_var = IntVar()
lb_entry = ttk.Entry(root,width=15,textvariable=lb_var).place(x=298,y=185)

#Upper Bound
ub_label = Label(root,text="upper Bound",width=15,font=("Consolas",10)).place(x=55,y=235)
ub_var = IntVar()
ub_entry = ttk.Entry(root,width=15,textvariable=ub_var).place(x=298,y=235)

#Grid
grid_label = Label(root,text="Grid",width=20,font=("Consolas", 10)).place(x=35,y=285)
var1 = IntVar()
R_yes = ttk.Radiobutton(root,text="Yes",variable=var1,value=1).place(x=285,y=285)
R_no = ttk.Radiobutton(root,text="No",variable=var1,value=0).place(x=351,y=285)

#Submit
submit_button = ttk.Button(root, text='Get Graph',width=20,command=get_graph).place(x=180,y=375)

root.mainloop()