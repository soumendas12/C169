from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.geometry("900x600")
root.title("Classes")

class CreateElement:
    def __init__(self):
        print("This is CreateElements class")
        self.numList = ["1", "2", "3", "4"]

        
    def createLabel(self):
        label = Label(root,text = "A new label is been created using class", fg="red")
        label.pack()
        
    def createButton(self):    
        btn = Button(root, text = "Button ", command = self.message)
        btn.pack(padx=20, pady = 10)
        
    def createDropdown(self):
        self.numVal = StringVar()
        dropdown = ttk.Combobox(root, values=self.numList, textvariable=self.numVal, state="readonly")
        dropdown.pack(pady=10)
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")
        
        
    def choose(self):
        element = comboboxVal.get()
        if(element == "Label"):
            self.createLabel()
        elif(element == "Button"):
            self.createButton()
        elif(element == "Dropdown"):
            self.createDropdown()

comboboxText = ["Label", "Button", "Dropdown"]
comboboxVal = StringVar()
combobox = ttk.Combobox(root, state="readonly", values=comboboxText, textvariable=comboboxVal)
combobox.pack(pady=10)

instance_of_create_element = CreateElement()
button = Button(root, text="Create Element", command=instance_of_create_element.choose)
button.pack(pady=10)

root.mainloop()