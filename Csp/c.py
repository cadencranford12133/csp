import tkinter as tk

root = tk.Tk()
root.title('Calculator')
root.geometry('300x300')


clear__bttn = tk.Button(root, text='Clear')
clear__bttn.grid(row=0,column=2)

message_var = tk.StringVar(root)
message_label2=tk.Entry(
   root,
   textvariable= message_var
)
message_label2.grid(row=0,column=0)

first__bttn = tk.Button(root, text='1')
first__bttn.grid(row=1,column=0,sticky=(tk.W,tk.E))

second__bttn = tk.Button(root, text='2')
second__bttn.grid(row=1,column=1,sticky=(tk.W,tk.E))

third__bttn = tk.Button(root, text='3')
third__bttn.grid(row=1,column=2,sticky=(tk.W,tk.E))

fourth_bttn=tk.Button(root, text='4')
fourth_bttn.grid(row=2,column=0,sticky=(tk.W,tk.E))

fifth_bttn=tk.Button(root, text='5')
fifth_bttn.grid(row=2,column=1,sticky=(tk.W,tk.E))


sixth_bttn=tk.Button(root, text='6')
sixth_bttn.grid(row=2,column=2,sticky=(tk.W,tk.E))

seventh_bttn=tk.Button(root, text='7')
seventh_bttn.grid(row=3,column=0,sticky=(tk.W,tk.E))

eighth_bttn=tk.Button(root, text='8')
eighth_bttn.grid(row=3,column=1,sticky=(tk.W,tk.E))

nineth_bttn=tk.Button(root, text='9')
nineth_bttn.grid(row=3,column=2,sticky=(tk.W,tk.E))

zero_bttn=tk.Button(root, text='0')
zero_bttn.grid(row=5,column=0,sticky=(tk.W,tk.E))

divide_bttn =tk.Button (root, text='/')
divide_bttn.grid(row=1,column=4,sticky=(tk.W,tk.E))

multi_bttn =tk.Button (root, text='*')
multi_bttn.grid(row=2,column=4,sticky=(tk.W,tk.E))

add_bttn =tk.Button (root, text='+')
add_bttn.grid(row=3,column=4,sticky=(tk.W,tk.E))

subtract_bttn =tk.Button (root, text='-')
subtract_bttn.grid(row=4,column=4,sticky=(tk.W,tk.E))



root.mainloop()