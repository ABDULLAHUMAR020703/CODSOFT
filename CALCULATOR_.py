import tkinter as tk
def add_digit(digit):
    current_text=entry_num.get()
    entry_num.delete(0,tk.END)
    entry_num.insert(tk.END,current_text+str(digit))
def add_operation(operator):
    current_text=entry_num.get()
    if current_text and current_text[-1].isdigit():
        entry_num.insert(tk.END,operator)
def clear_entry():
    entry_num.delete(0,tk.END)
def calculate():
    try:
        expression=entry_num.get()
        result=eval(expression)
        entry_num.delete(0,tk.END)
        entry_num.insert(tk.END,str(result))
    except Exception as e:
        entry_num.delete(0,tk.END)
        entry_num.insert(tk.END,"Error")

root=tk.Tk()
root.title("Calculator")
root.geometry('250x250')
entry_num=tk.Entry(root,width=20,font=('Arial',14),justify='right')
digits='7894561230'
row_val=1
col_val=0
for digit in digits:
    tk.Button(root,text=digit,command=lambda d=digit:add_digit(d),
              bg='black',fg='white',font=('Arial',12)).grid(row=row_val,column=col_val,padx=5,pady=5)
    col_val+=1
    if col_val>2:
        col_val=0
        row_val+=1

operations='+-*/'
row_val=1
col_val=3
for operator in operations:
    tk.Button(root,text=operator,command=lambda o=operator:add_operation(o),
              bg='black',fg='white',font=('Arial',12)).grid(row=row_val,column=col_val,padx=5,pady=5)
    row_val+=1

tk.Button(root, text="C", command=clear_entry, bg="orange", fg="white", font=('Arial', 12)).grid(row=4, column=1,columnspan=1, padx=5, pady=5)
tk.Button(root, text="=", command=calculate, bg="orange", fg="white", font=('Arial', 12)).grid(row=4, column=2,columnspan=1, padx=5, pady=5)

entry_num.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

root.mainloop()