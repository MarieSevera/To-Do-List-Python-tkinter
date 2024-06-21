from tkinter import *
import customtkinter

#main window
window = customtkinter.CTk()
window.minsize(269,270)
window.resizable(False, False)
window.title('To Do List')
window.overrideredirect(True)

# move window
def start_move(event):
    window.x = event.x
    window.y = event.y

def do_move(event):
    x = (event.x_root - window.x)
    y = (event.y_root - window.y)
    window.geometry(f"+{x}+{y}")

window.bind("<Button-1>", start_move)
window.bind("<B1-Motion>", do_move)

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
    

def clear_list():
    list_box.delete(0, END)    
    
def save_button():
    main_font = 'Arial'
    save_window = customtkinter.CTk()
    save_window.geometry('250x150')
    save_window.resizable(False, False)
    save_window.title('Save')

    def yes():
        # with open('tasks.txt', 'w') as file:
        #     file.truncate(0)
        with open('tasks.txt', 'w') as file:
            tasks = list_box.get(0, END)
            for task in tasks:
                if task.endswith("\n"):
                    file.write(f'{task}')
                else:
                    file.write(f'{task}\n')
        save_window.destroy() 
        window.destroy()

    def no():
        save_window.destroy() 
        window.destroy()

    save_label = customtkinter.CTkLabel(save_window, text='Save To Do List?', font=(main_font, 15))
    save_label.place(x=70, y=30)

    yes_button = customtkinter.CTkButton(save_window, text='Yes', font=(main_font, 15), width=80, command=yes)
    yes_button.place(x=30, y=80)

    no_button = customtkinter.CTkButton(save_window, text='No', font=(main_font, 15), width=80, command=no)
    no_button.place(x=140, y=80)

    save_window.attributes('-topmost', True)
    save_window.after(10, lambda: save_window.attributes('-topmost', False))
    save_window.mainloop()


def open_list():
    try:
        with open('tasks.txt', 'r') as file:
            for polozka in file:

                list_box.insert(END, polozka)
    except:
        print('No polozla')

# window split
name_frame = customtkinter.CTkFrame(window)
input_frame = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
button_frame = customtkinter.CTkFrame(window)
name_frame.pack()
input_frame.pack()
text_frame.pack()
button_frame.pack()

# first label
name = customtkinter.CTkLabel(name_frame, text='TO DO', font=(main_font, 20))
name.grid(row=0, column=0, padx=105)

# input_frame content
input_field = customtkinter.CTkEntry(input_frame, font=(main_font, 14), width=170)
input_button = customtkinter.CTkButton(input_frame, text='Add to list', width=80, font=(main_font, 12), command=add_text)

input_field.grid(row=1, column=0, padx=5, pady=5)
input_button.grid(row=1, column=1, padx=5, pady=5)

# Scrollbar
scroll = customtkinter.CTkScrollbar(text_frame, width=13)
scroll.grid(row=0, column=1, sticky=NS)

# list
list_box = Listbox(text_frame, height=10, width=28, font=(main_font, 14), yscrollcommand=scroll.set)
list_box.grid(row=0, column=0, padx=5, pady=5)



# Scrollbar and  list connection
scroll.configure(command=list_box.yview)

# buttons
button_1 = customtkinter.CTkButton(button_frame, text='Remove item', width=85, font=(main_font, 12), command=remove_item)
button_1.grid(row=0, column=0, padx=2, pady=5)
button_2 = customtkinter.CTkButton(button_frame, text='Clear list', width=85, font=(main_font, 12), command=clear_list)
button_2.grid(row=0, column=1, padx=2, pady=5)
button_4 = customtkinter.CTkButton(button_frame, text='Quit', width=85, font=(main_font, 12), command=save_button)
button_4.grid(row=0, column=2, padx=2, pady=5)

open_list()
window.after(100, lambda: input_field.focus_set())
window.attributes('-topmost', True)
window.after(10, lambda: window.attributes('-topmost', False))
window.mainloop()