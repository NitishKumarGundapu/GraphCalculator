import numpy as np
from numpy import *
import warnings
import matplotlib.pyplot as plt
from matplotlib import style

warnings.filterwarnings("ignore")

print("h for Help and e for Exit")

print("Remember the Independent Variable is x use in it in your Equations")

def parser(eq):
    try : 
        if type(eval(s[0])) == np.ndarray :
            return True 
        else :
            print("Error Occured ! Enter the Correct Equation")
            return False

    except Exception as e:
        print("Error Occured ! Enter the Correct Equation")
        return False


while True :
    x = np.array([x for x in range(100)])
    s = list(input(">> ").split())
    
    if s[0].lower() == 'h' :
        print("Type the Equation inorder to get the graph !!")
        continue

    elif s[0].lower() == 'e' :
        print("Thank you for using the Calculator !!")
        break

    elif parser(s[0]):
        try : 
            a,b = -10,10
            x = np.linspace(a,b,1000)
            y = eval(s[0])
            plt.plot(x,y,color = "green",label=s[0])
            plt.legend()
            plt.axhline(y=0,color='red')
            plt.axvline(x=0,color='red')
            plt.xlabel("X-Values")
            plt.ylabel("Y-Values")
            plt.grid(True)
            plt.show()
    
        except Exception as e: 
            print("The Error Occured is : ",e)
            break
        continue