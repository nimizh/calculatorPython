import tkinter
from tkinter import *
from tkinter import messagebox

val = ''
A = 0
operator = ''

#---------------BUTTONS CLICKED----------------
def button1clicked():
    global val
    val = val + '1'
    data.set(val)

def button2clicked():
    global val
    val = val + '2'
    data.set(val)


def button3clicked():
    global val
    val = val + '3'
    data.set(val)


def button4clicked():
    global val
    val = val + '4'
    data.set(val)


def button5clicked():
    global val
    val = val + '5'
    data.set(val)


def button6clicked():
    global val
    val = val + '6'
    data.set(val)


def button7clicked():
    global val
    val = val + '7'
    data.set(val)


def button8clicked():
    global val
    val = val + '8'
    data.set(val)

def button9clicked():
    global val
    val = val + '9'
    data.set(val)

def button0clicked():
    global val
    val = val + '0'
    data.set(val)
# ------------OPERATIONS----------

def btnPclicked():

    global A
    global operator
    global val

    A = int(val)
    operator = '+'
    val = val + '+'
    data.set(val)

def btnMclicked():

    global A
    global operator
    global val

    A = int(val)
    operator = '-'
    val = val + '-'
    data.set(val)

def btnAclicked():

    global A
    global operator
    global val

    A = int(val)
    operator = '*'
    val = val + '*'
    data.set(val)

def btnDclicked():

    global A
    global operator
    global val

    A = int(val)
    operator = '/'
    val = val + '/'
    data.set(val)


def btnCclicked():
    global A
    global operator
    global val
    val = ""
    A= 0
    operator = ""
    data.set(val)


def result():
    global A
    global operator
    global val

    val2 =val

    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val = str(C)

    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)

    elif operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)

    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error, divisible is not possible by 0")
            A =''
            val = ''
        else:
            C = A/x
            data.set(C)
            val = str(C)





root = Tk()
root.geometry('350x450+600+200')
root.title("Calcultor")
root.resizable(0,0)
root.wm_iconbitmap('favicon.ico')

data = StringVar()


lbl = Label(root,text = 'Label',anchor = SE, font = 'Verdana 20 bold',bg='white',fg = 'black',textvariable = data ,padx = 10)
lbl.pack(expand = True, fill ='both')
frame1 = Frame(root)
frame1.pack(expand = True , fill = 'both')

frame2 = Frame(root)
frame2.pack(expand = True , fill = 'both')

frame3 = Frame(root)
frame3.pack(expand = True , fill = 'both')

frame4 = Frame(root)
frame4.pack(expand = True , fill = 'both')



btn7 = Button(
    frame1,
    text ="7",
font = 'Verdana 20 ',
    relief = GROOVE,
    border =0,
command = button7clicked
)
btn7.pack(side = LEFT, expand = True, fill = 'both')

btn8 = Button(
    frame1,
    text ="8",
font = 'Verdana 20 ',
    relief=GROOVE,
    border=0,
command = button8clicked
)
btn8.pack(side = LEFT, expand = True, fill = 'both')

btn9 = Button(
    frame1,
    text ="9",
font = 'Verdana 20',
    relief=GROOVE,
    border=0,
command = button9clicked
)
btn9.pack(side = LEFT, expand = True, fill = 'both')

btnP = Button(
    frame1,
    text ="+",
font = 'Verdana 20 bold',
    relief=GROOVE,
    border=0,
    command =btnPclicked
)
btnP.pack(side = LEFT, expand = True, fill = 'both')

btn4 = Button(
    frame2,
    text ="4",
font = 'Verdana 20',
    relief=GROOVE,
    border=0,
command = button4clicked
)
btn4.pack(side = LEFT, expand = True, fill = 'both')


btn5 = Button(
    frame2,
    text ="5",
font = 'Verdana 20',
    relief=GROOVE,
    border=0,
command = button5clicked
)
btn5.pack(side = LEFT, expand = True, fill = 'both')

btn6 = Button(
    frame2,
    text ="6",
font = 'Verdana 20',
    relief = GROOVE,
    border =0,
command = button6clicked

)
btn6.pack(side = LEFT, expand = True, fill = 'both')


btnM = Button(
    frame2,
    text ="-",
font = 'Verdana 20 bold',
    relief=GROOVE,
    border=0,
    command =btnMclicked
)
btnM.pack(side = LEFT, expand = True, fill = 'both')

btn1 = Button(
    frame3,
    text ="1",
font = 'Verdana 20',
    relief=GROOVE,
    border=0,
    command = button1clicked
)
btn1.pack(side = LEFT, expand = True, fill = 'both')


btn2 = Button(
    frame3,
    text ="2",
font = 'Verdana 20',
    relief=GROOVE,
    border=0,
command = button2clicked
)
btn2.pack(side = LEFT, expand = True, fill = 'both')

btn3 = Button(
    frame3,
    text ="3",
font = 'Verdana 20',
    relief = GROOVE,
    border =0,
command = button3clicked
)
btn3.pack(side = LEFT, expand = True, fill = 'both')

btnA = Button(
    frame3,
    text ="*",
font = 'Verdana 20 bold',
    relief=GROOVE,
    border=0,
    command =btnAclicked
)
btnA.pack(side = LEFT, expand = True, fill = 'both')

btnC = Button(
    frame4,
    text ="C",
font = 'Verdana 20 bold',
    relief = GROOVE,
    border =0,
    command = btnCclicked
)
btnC.pack(side = LEFT, expand = True, fill = 'both')

btnZ = Button(
    frame4,
    text ="0",
font = 'Verdana 20',
    relief=GROOVE,
    border=0,
    command=  button0clicked
)
btnZ.pack(side = LEFT, expand = True, fill = 'both')

btnE = Button(
    frame4,
    text ="=",
font = 'Verdana 20 bold',
    relief=GROOVE,
    border=0,
    command = result,
)
btnE.pack(side = LEFT, expand = True, fill = 'both')

btnD = Button(
    frame4,
    text ="/",
font = 'Verdana 20 bold',
    relief=GROOVE,
    border=0,
    command =btnDclicked
)
btnD.pack(side = LEFT, expand = True, fill = 'both')

root.mainloop()
