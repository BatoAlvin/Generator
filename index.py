from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator by Alvin')

root.geometry("500x300")



def new_rand():
    #Clear entry box
    pw_entry.delete(0, END)

    #Get password lenght
    length = 8

    #Create variable to hold our password
    my_password = ''

    #Loop through password length
    for x in range(length):
        my_password += chr(randint(33,126))
    
    #Output password
    pw_entry.insert(0, my_password)


#Labelframe
frame = LabelFrame(root, text='Password Lenght is 8 Characters')
frame.pack(pady=20)

#Password label
my_label = Label(root, text='Password Length is 8 Characters')
my_label.pack()

#Input field for password
pw_entry = Entry(root, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20)

#Create frame for buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#Create buttons
my_button = Button(my_frame, text='Generate Strong Password', command=new_rand)
my_button.grid(row=0, column=0, padx=10)



root.mainloop()