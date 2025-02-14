from tkinter import *

root = Tk()
root.title("Simple Calculator")
 

input = Entry(root, width=40 , borderwidth=5)
input.grid(row=0, column=0, columnspan=3) 

def show(number):
    current= input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(number))



def clear():
    input.delete(0, END)



def sum(number):
    current= input.get()
    number = input.get()
    input.delete(0, END)
    input.insert(0, int(current) + int(number))



def equal():
    input.insert(sum())

 



btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: show(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: show(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: show(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: show(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: show(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: show(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: show(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: show(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: show(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: show(0))

btn_clear = Button(root, text="Clear", padx=79, pady=20, command= lambda:clear() )
btn_sum = Button(root, text="+", padx=39, pady=20,command=lambda: sum())
btn_equal = Button(root, text="=", padx=91, pady=20 , command=lambda: equal())




btn1.grid(row=1 ,column=0)
btn2.grid(row=1 ,column=1)
btn3.grid(row=1 ,column=2)

btn4.grid(row=2 ,column=0)
btn5.grid(row=2 ,column=1)
btn6.grid(row=2 ,column=2)

btn7.grid(row=3 ,column=0)
btn8.grid(row=3 ,column=1)
btn9.grid(row=3 ,column=2)

btn0.grid(row=4,column=0)

btn_clear.grid(row=4 ,column=1, columnspan=2)
btn_sum.grid(row=5 ,column=0)
btn_equal.grid(row=5 ,column=1, columnspan=2)










root.mainloop()