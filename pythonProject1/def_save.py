from tkinter import *
import customtkinter


# font and colors


def save_button():
    main_font = 'Arial'
    save_window = customtkinter.CTk()
    save_window.geometry('250x150')
    save_window.resizable(False, False)
    save_window.title('Save')

    def save_list():
        with open('tasks.txt', 'w') as file:
            tasks = list_box.get(0, END)
            for task in tasks:
                if task.endswith("\n"):
                    file.write(f'{task}')
                else:
                    file.write(f'{task}\n')

    save_label = customtkinter.CTkLabel(save_window, text='Save To Do List?', font=(main_font, 15))
    save_label.place(x=70, y=30)

    yes_button = customtkinter.CTkButton(save_window, text='Yes', font=(main_font, 15), width=80, command=save_list)
    yes_button.place(x=30, y=80)

    no_button = customtkinter.CTkButton(save_window, text='No', font=(main_font, 15), width=80, command=save_window.destroy)
    no_button.place(x=140, y=80)

    save_window.mainloop()
save_button()



