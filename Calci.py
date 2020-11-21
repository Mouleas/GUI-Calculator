from tkinter import *

window=Tk()

window.title('CALCULATOR')

window.geometry('530x455')

window.configure(bg='white')

window.iconbitmap('favicon.ico')

window.resizable(False,False)

expression=''
def press(num):
    global expression

    expression=expression+str(num)

    equation.set(expression)

def clear():
    global expression

    expression=''
    equation.set('0')

def equal():
    global expression

    try:

        total=str(eval(expression))

        equation.set(total)

        expression=''

    except:
        equation.set('error..')
        equation.set('0')        
        
        

button=Frame(window,bg='#00b386')
button.pack()

equation=StringVar()
equation.set('0')
entry=Entry(button,textvariable=equation,justify='right',font=('arial',34,'bold'))
entry.pack()

button_1=Button(button,text='1',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(1))
button_2=Button(button,text='2',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(2))
button_3=Button(button,text='3',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(3))

addition=Button(button,text='+',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press('+'))

button_4=Button(button,text='4',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(4))
button_5=Button(button,text='5',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(5))
button_6=Button(button,text='6',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(6))

subtract=Button(button,text='-',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press('-'))

button_7=Button(button,text='7',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(7))
button_8=Button(button,text='8',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(8))
button_9=Button(button,text='9',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(9))

multiply=Button(button,text='X',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press('*'))

button_0=Button(button,text='0',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press(0))

button_dot=Button(button,text='.',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press('.'))

button_clr=Button(button,text='clear',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=clear)

division=Button(button,text='/',font=('times new roman',12),relief='ridge',borderwidth=1,bg='#00b386',width=13,height=3,command=lambda:press('/'))

button_equal=Button(button,text='=',font=('times new roman',15),relief='ridge',borderwidth=1,bg='#00b386',width=45,height=3,command=equal)


entry.grid(row=0,column=0,columnspan=6,pady=15)


button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
addition.grid(row=1,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
subtract.grid(row=2,column=3)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
multiply.grid(row=3,column=3)
button_0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)
button_clr.grid(row=4,column=2)
division.grid(row=4,column=3)
button_equal.grid(row=5,column=0,columnspan=6)








