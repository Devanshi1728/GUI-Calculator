from tkinter import *   # GUI Library
import math             # for math function
import parser           
import tkinter.messagebox

root=Tk()   #create screen
root.title("Calculator")            #give Title
tinput=StringVar()                  
operator = ""           
class Calc:                     # create class named "calc"
    def __init__(self,root):                                            
        self.f=Frame(root, height=600, width=600, bg="black")                           #give height and width and background color black
       
        self.f.grid()                           #grid layout for buttons
        
        def buttonClick(numbers):                       # functions for button click
            global operator
            operator = operator + str(numbers)
            tinput.set(operator)

        def buttonEquals():
            global operator
            sumup=str(eval(operator))
            tinput.set(sumup)
            operator=""
            
        def buttonclear():
            global operator
            operator=''
            tinput.set("0")                         #default it print 0

        def standard():                                 #menu function standard
            root.resizable(width=False, height=False)
            root.geometry("410x315+0+0")                    #set height and width

        def scicalc():                                      #scientific menu items function
            root.resizable(width=False, height=False)
            root.geometry("860x315+0+0")                    #set height and width
            
        def cos():                                      #function cos for scientific calculation
            global a
            a=float(tinput.get())                       #create global variable "a" and convert into float datatype 
            tinput.set(math.cos(a))                     #math.cos() math function for cos...   it takes input from tinput

        def sin():
            global a
            a=int(tinput.get())                          #same as cos but here sin()...take input from tinput and convert in int datatype
            tinput.set(math.sin(a))                         #set math function sin()

        def cosh():
            global a
            a=int(tinput.get())
            tinput.set(math.cosh(a))            # same as above but cosh()

        def tan():                          #tan() these all are math function
            global a
            a=int(tinput.get())
            tinput.set(math.tan(a))

        def factorial():
            global a
            a=int(tinput.get())
            tinput.set(math.factorial(a))

        def tanh():
            global a
            a=int(tinput.get())
            tinput.set(math.tanh(a))
            
        def ceil():
            global a
            a=float(tinput.get())
            tinput.set(math.ceil(a))

        def trunc():
            global a
            a=int(tinput.get())
            tinput.set(math.trunc(a))

        def acosh():
            global a
            a=int(tinput.get())
            tinput.set(math.acosh(a))

        def log():
            global a
            a=int(tinput.get())
            tinput.set(math.log(a))

        def log2():
            global a
            a=int(tinput.get())
            tinput.set(math.log2(a))

        def exp():
            global a
            a=int(tinput.get())
            tinput.set(math.exp(a))

        def expm1():
            global a
            a=int(tinput.get())
            tinput.set(math.expm1(a))

        def floor():
            global a
            a=float(tinput.get())
            tinput.set(math.floor(a))

        def radians():
            global a
            a=int(tinput.get())
            tinput.set(math.radians(a))

        def log10():
            global a
            a=int(tinput.get())
            tinput.set(math.log10(a))

        def degrees():
            global a
            a=int(tinput.get())
            tinput.set(math.degrees(a))

        def fabs():
            global a
            a=int(tinput.get())
            tinput.set(math.fabs(a))
            
        def asin():
            global a
            a=float(tinput.get())
            tinput.set(math.asin(a))

        def asinh():
            global a
            a=float(tinput.get())
            tinput.set(math.asinh(a))

        def sqrt():
            global a
            a=int(tinput.get())
            tinput.set(math.sqrt(a))

        def acos():
            global a
            a=float(tinput.get())
            tinput.set(math.acos(a))

        def pow():
            global a
            a=int(tinput.get())         
            b=int(tinput.get())            
            tinput.set(math.pow(a,b))          


        self.menubar=Menu(root)       #create menubar                    
        root.config(menu=self.menubar)               #configure menubar to root  
        
        self.filemenu=Menu(root,tearoff=0)              
        self.filemenu.add_command(label="Standard", command=standard)  #add menuitem called "standard"
        self.filemenu.add_separator()                       #create separator ______verticle line between two menu items
        self.filemenu.add_command(label="Scientific", command=scicalc) #add menu item "scietific" 

        self.menubar.add_cascade(label='File', menu=self.filemenu)     
        
        self.t=Entry(self.f, font=('Rockwell Condensed Bold',20),  textvariable=tinput, justify='right', fg='white', bg='grey', bd=25, width=24)
        self.t.grid(columnspan=4)      #set font, alignment, forground color, background color ..
        self.t.insert(0,"0")         #tinput is our textbox where we type...we give name "tinput" n default insert 0


 ############################################################################################################################
    
        self.ce=Button(self.f, text=chr(67) + chr(69), width=10, height=1, bg='grey', fg='white',  command = buttonclear)
        self.ce.grid(row=1, column=0, padx=5, pady=10)         #buttons, set height width color and command that is name of function    
                                                                #set at 1st row and 0th column
        self.c=Button(self.f, text='√', width=10, height=1, bg='grey', fg='white', command = sqrt)
        self.c.grid(row=1, column=1, padx=5, pady=10)     #row 1 column 1, create button with name color,and function 

        self.sqrt=Button(self.f, text= chr(94), width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick("**"))                                                                                                                     
        self.sqrt.grid(row=1, column=2, padx=5, pady=10)     #all buttons in grid with row and column
        
        self.mod=Button(self.f, text='%', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("%"))
        self.mod.grid(row=1, column=3, padx=5, pady=10)             #lambda function to call our user define function

        self.pi=Button(self.f, text='π', width=10, height=1, bg='grey', fg='white', command=lambda:buttonClick(math.pi))
        self.pi.grid(row=1, column=4, padx=5, pady=10)

        self.cos=Button(self.f, text='cos', width=10, height=1, bg='grey', fg='white', command = cos)
        self.cos.grid(row=1, column=5, padx=5, pady=10)

        self.tan=Button(self.f, text='tan', width=10, height=1, bg='grey', fg='white', command = tan)
        self.tan.grid(row=1, column=6, padx=5, pady=10)

        self.fact=Button(self.f, text='factorial', width=10, height=1, bg='grey', fg='white', command = factorial)
        self.fact.grid(row=1, column=7, padx=5, pady=10)

        self.pow=Button(self.f, text='^n', width=10, height=1, bg='grey', fg='white', command = pow)
        self.pow.grid(row=1, column=8, padx=5, pady=10)

    
#####################################################

        self.b7=Button(self.f, text='7', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(7))
        self.b7.grid(row=2, column=0, padx=5, pady=10)     #here 2nd row as above...

        self.b8=Button(self.f, text='8', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(8))
        self.b8.grid(row=2, column=1, padx=5, pady=10)

        self.b9=Button(self.f, text='9', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(9))
        self.b9.grid(row=2, column=2, padx=5, pady=10)

        self.badd=Button(self.f, text='+', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("+"))
        self.badd.grid(row=2, column=3, padx=5, pady=10)
        
        self.tpi=Button(self.f, text='2π', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(math.pi*2))
        self.tpi.grid(row=2, column=4, padx=5, pady=10)

        self.cosh=Button(self.f, text='cosh', width=10, height=1, bg='grey', fg='white', command = cosh)
        self.cosh.grid(row=2, column=5, padx=5, pady=10)

        self.tanh=Button(self.f, text='tanh', width=10, height=1, bg='grey', fg='white', command = tanh)
        self.tanh.grid(row=2, column=6, padx=5, pady=10)

        self.ceil=Button(self.f, text='ceil', width=10, height=1, bg='grey', fg='white', command = ceil)
        self.ceil.grid(row=2, column=7, padx=5, pady=10)

        self.trunc=Button(self.f, text='trunc', width=10, height=1, bg='grey', fg='white', command = trunc)
        self.trunc.grid(row=2, column=8, padx=5, pady=10)

        
############################################################

        
        self.b4=Button(self.f, text='4', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(4))
        self.b4.grid(row=3, column=0, padx=5, pady=10)    #3rd row

        self.b5=Button(self.f, text='5', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(5))
        self.b5.grid(row=3, column=1, padx=5, pady=10)    #3rd row column 1

        self.b6=Button(self.f, text='6', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(6))
        self.b6.grid(row=3, column=2, padx=5, pady=10)  #3rd row column 2 

        self.sub=Button(self.f, text='-', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("-"))
        self.sub.grid(row=3, column=3, padx=5, pady=10)   #3rd row column 3

        self.log=Button(self.f, text='log', width=10, height=1, bg='grey', fg='white', command = log)
        self.log.grid(row=3, column=4, padx=5, pady=10)

        self.acosh=Button(self.f, text='acosh', width=10, height=1, bg='grey', fg='white', command = acosh)
        self.acosh.grid(row=3, column=5, padx=5, pady=10)

        self.exp=Button(self.f, text='Exp', width=10, height=1, bg='grey', fg='white', command = exp)
        self.exp.grid(row=3, column=6, padx=5, pady=10)

        self.floor=Button(self.f, text='floor', width=10, height=1, bg='grey', fg='white', command = floor)
        self.floor.grid(row=3, column=7, padx=5, pady=10)

        self.radn=Button(self.f, text='radians', width=10, height=1, bg='grey', fg='white', command = radians)
        self.radn.grid(row=3, column=8, padx=5, pady=10)

 ############################################
        self.b1=Button(self.f, text='1', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(1))
        self.b1.grid(row=4, column=0, padx=5, pady=10)          #4th row

        self.b2=Button(self.f, text='2', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(2))
        self.b2.grid(row=4, column=1, padx=5, pady=10)

        self.b3=Button(self.f, text='3', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(3))
        self.b3.grid(row=4, column=2, padx=5, pady=10)

        self.mul=Button(self.f, text='*', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("*"))
        self.mul.grid(row=4, column=3, padx=5, pady=10)
 
        self.lt=Button(self.f, text='log2', width=10, height=1, bg='grey', fg='white', command = log2)
        self.lt.grid(row=4, column=4, padx=5, pady=10)

        self.degree=Button(self.f, text='deg', width=10, height=1, bg='grey', fg='white', command = degrees)
        self.degree.grid(row=4, column=5, padx=5, pady=10)
        
        self.sin=Button(self.f, text='sin', width=10, height=1, bg='grey', fg='white', command = sin)
        self.sin.grid(row=4, column=6, padx=5, pady=10)
        
        self.e=Button(self.f, text='e', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick(math.e))
        self.e.grid(row=4, column=7, padx=5, pady=10)     #here use lambda function  

        self.fbs=Button(self.f, text='fabs', width=10, height=1, bg='grey', fg='white', command = fabs)
        self.fbs.grid(row=4, column=8, padx=5, pady=10)

######################################

        self.dot=Button(self.f, text='.', width=10, height=1, bg='grey', fg='white', command = lambda:buttonClick("."))
        self.dot.grid(row=5, column=0, padx=5, pady=10)      #5th row
        
        self.b0=Button(self.f, text='0', width=10, height=1, bg='grey', fg='white',  command = lambda:buttonClick(0))
        self.b0.grid(row=5, column=1, padx=5, pady=10)

        self.bequ=Button(self.f, text='=', width=10, height=1, bg='grey', fg='white', command = buttonEquals)
        self.bequ.grid(row=5, column=2, padx=5, pady=10)

        self.div=Button(self.f, text=chr(247), width=10, height=1, bg='grey', fg='white',  command =lambda:buttonClick("/"))
        self.div.grid(row=5, column=3, padx=5, pady=10)

        self.lten=Button(self.f, text='log10', width=10, height=1, bg='grey', fg='white', command = log10)
        self.lten.grid(row=5, column=4, padx=5, pady=10)

        self.expm=Button(self.f, text='e**x-1', width=10, height=1, bg='grey', fg='white', command = expm1)
        self.expm.grid(row=5, column=5, padx=5, pady=10)

        self.asin=Button(self.f, text='asin', width=10, height=1, bg='grey', fg='white', command = asin)
        self.asin.grid(row=5, column=6, padx=5, pady=10)

        self.asinh=Button(self.f, text='asinh', width=10, height=1, bg='grey', fg='white', command=asinh)
        self.asinh.grid(row=5, column=7, padx=5, pady=10)

        self.acos=Button(self.f, text='acos', width=10, height=1, bg='grey', fg='white', command=acos)
        self.acos.grid(row=5, column=8, padx=5, pady=10)
       

op=Calc(root)         #create object called "op" of class "calc"
root.mainloop()
