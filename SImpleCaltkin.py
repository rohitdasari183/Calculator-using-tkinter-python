from tkinter import *
cal=Tk()
cal.title("Simple Calculator")
text_input=StringVar()
text_disp=Entry(cal,font=("Arial",20,"bold"),textvariable=text_input,bd=30,fg="black",insertwidth=5,bg="orange",justify="right").grid(columnspan=4)
operator=""
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")
def btnEquals():
    global operator
    result=str(eval(operator))
    text_input.set(result)
    operator=""
    
    

btn7=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="+",command=lambda:btnClick("+")).grid(row=1,column=3)

btn6=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="6",command=lambda:btnClick(6)).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn4=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="4",command=lambda:btnClick(4)).grid(row=2,column=2)
Substraction=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="-",command=lambda:btnClick("-")).grid(row=2,column=3)

btn3=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="3",command=lambda:btnClick(3)).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn1=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="1",command=lambda:btnClick(1)).grid(row=3,column=2)
Multiplication=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="+",command=lambda:btnClick("*")).grid(row=3,column=3)

btn0=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="0",command=lambda:btnClick(0)).grid(row=4,column=0)
btnC=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="C",command=btnClearDisplay).grid(row=4,column=1)
btnEq=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="=",command=btnEquals).grid(row=4,column=2)
Division=Button(cal,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),bg="orange",text="/",command=lambda:btnClick("/")).grid(row=4,column=3)

cal.mainloop()

 

 
