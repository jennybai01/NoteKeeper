from tkinter import *
import os

#storing registration details in an external file
def register_user(): #button
    username_info = username.get()
    password_info = password.get()
    
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text = "").pack()
    Label(screen1, text = "Registration Success!", fg = "green", font = ("Times New Roman", 11)).pack()

#registration page
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()
    
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    
    Label(screen2, text = "Username").pack()
    global username_entry1
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password").pack()
    global password_entry1
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "")
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def saved():
    screen10 = Toplevel(screen)
    screen10.title("Info")
    screen10.geometry("300x250")
    Label(screen10, text = "Saved!").pack()
    
def save():
    filename = raw_file_name.get()
    notes = raw_note.get()

    data = open(filename, "w")
    data.write(notes)
    data.close()

    saved()
    
def create_note():
    screen9 = Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("300x250")

    global raw_file_name
    raw_file_name = StringVar()
    global raw_note
    raw_note = StringVar()

    Label(screen9, text = "Please enter a filename for the note below: ").pack()
    raw_file_name_entry = Entry(screen9, textvariable = raw_file_name)
    raw_file_name_entry.pack()

    Label(screen9, text = "Please enter the notes for the file below: ").pack()
    raw_note_entry = Entry(screen9, textvariable = raw_note)
    raw_note_entry.pack()

    Label(screen9, text = "").pack()
    Button(screen9, text = "Save", command = save).pack()

def view_notes1():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()

    screen12 = Toplevel(screen)
    screen12.title("View")
    screen12.geometry("400x400")
    Label(screen12, text = data1).pack()
    
def view_notes():
    screen11 = Toplevel(screen)
    screen11.title("Info")
    screen11.geometry("250x250")
    all_files = os.listdir()
    Label(screen11, text = "Please use one of the file names below: ").pack()
    Label(screen11, text = all_files).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    enter_filename1 = Entry(screen11, textvariable = raw_filename1)
    enter_filename1.pack()
    Button(screen11, text = "OK", command = view_notes1).pack()
    
def delete_notes1():
    filename3 = raw_filename3.get()
    os.remove(filename3)

    screen14 = Toplevel(screen)
    screen14.title("View")
    screen14.geometry("400x400")
    Label(screen14, text = filename3 + " removed!").pack()

def delete_notes():
    screen13 = Toplevel(screen)
    screen13.title("Info")
    screen13.geometry("250x250")
    all_files = os.listdir()
    Label(screen13, text = "Please use one of the file names below: ").pack()
    Label(screen13, text = all_files).pack()
    global raw_filename3
    raw_filename3 = StringVar()
    enter_filename3 = Entry(screen13, textvariable = raw_filename3)
    enter_filename3.pack()
    Button(screen13, text = "OK", command = delete_notes1).pack()
    
def session():
    screen8 = Toplevel(screen)
    screen8.title("Dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome to the dashboard.").pack()
    Label(screen8, text = "").pack()
    Button(screen8, text = "Create New Note", command = create_note).pack()
    Label(screen8, text = "").pack()
    Button(screen8, text = "View Notes", command = view_notes).pack()
    Label(screen8, text = "").pack()
    Button(screen8, text = "Delete Notes", command = delete_notes).pack()

def delete_screen4():
    screen4.destroy()
    
def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Error")
    screen4.geometry("150x100")
    Label(screen4, text = "Password not recognized :(").pack()
    Button(screen4, text = "OK", command = delete_screen4).pack()

def delete_screen5():
    screen5.destroy()
    
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Password Error")
    screen5.geometry("150x100")
    Label(screen5, text = "User not found :(").pack()
    Button(screen5, text = "OK", command = delete_screen5).pack()
    
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            session()
        else:
            password_not_recognized()
    else:
        user_not_found()
        
def leave():
    exit()
    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Times New Roman", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text="").pack()
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    Label(text = "").pack()
    Button(text = "Exit", height = "2", width = "30", command = leave).pack()

    screen.mainloop()


main_screen()
