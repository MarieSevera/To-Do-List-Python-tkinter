from tkinter import *
import customtkinter
from def_save import save_button

#main window
window = customtkinter.CTk()
window.minsize(269,313)
window.resizable(False, False)
window.title('To Do List')


# font and colors
main_font = 'Arial'
main_color = 'white'
button_color = 'black'
window.config(bg=main_color)

def add_text():
    list_box.insert(END, f'{input_field.get()}\n')
    input_field.delete(0, END)

def remove_item():
    list_box.delete(ANCHOR)
    with open('tasks.txt', 'w') as file:
        tasks = list_box.get(0, END)
        for task in tasks:
            if task.endswith("\n"):
                file.write(f'{task}')
            else:
                file.write(f'{task}\n')

def clear_list():
    list_box.delete(0, END)    
    with open('tasks.txt', 'w') as file:
        file.truncate(0)

def save_list():
    with open('tasks.txt', 'w') as file:
        tasks = list_box.get(0, END)
        for task in tasks:
            if task.endswith("\n"):
                file.write(f'{task}')
            else:
                file.write(f'{task}\n')


def open_list():
    try:
        with open('tasks.txt', 'r') as file:
            for polozka in file:

                list_box.insert(END, polozka)
    except:
        print('No polozla')

# window split
input_frame = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
button_frame = customtkinter.CTkFrame(window)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# input_frame content
input_field = customtkinter.CTkEntry(input_frame, font=(main_font, 14), width=170)
input_button = customtkinter.CTkButton(input_frame, text='Add to list', width=80, font=(main_font, 15), command=add_text)
input_field.grid(row=0, column=0, padx=5, pady=5)
input_button.grid(row=0, column=1, padx=5, pady=5)

# Scrollbar
scroll = customtkinter.CTkScrollbar(text_frame, width=13)
scroll.grid(row=0, column=1, sticky=NS)

# list
list_box = Listbox(text_frame, height=10, width=28, font=(main_font, 14), yscrollcommand=scroll.set)
list_box.grid(row=0, column=0, padx=5, pady=5)



# Scrollbar and  list connection
scroll.configure(command=list_box.yview)

# buttons
button_1 = customtkinter.CTkButton(button_frame, text='Remove item', width=130, font=(main_font, 15), command=remove_item)
button_1.grid(row=0, column=1, padx=2, pady=5)
button_2 = customtkinter.CTkButton(button_frame, text='Clear list', width=130, font=(main_font, 15), command=clear_list)
button_2.grid(row=1, column=0, padx=2, pady=5)
button_3 = customtkinter.CTkButton(button_frame, text='Save list', width=130, font=(main_font, 15), command=save_list)
button_3.grid(row=0, column=0, padx=2, pady=5)
button_4 = customtkinter.CTkButton(button_frame, text='Quit', width=130, font=(main_font, 15), command=save_button)
button_4.grid(row=1, column=1, padx=2, pady=5)

open_list()
window.after(100, lambda: input_field.focus_set())
window.mainloop()