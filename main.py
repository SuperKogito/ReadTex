import tkinter as tk
from gui import Application

def callback():
    print("called the callback!")

def create_menu(root):
    menu = tk.Menu(root)
    root.config(menu=menu)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=callback)
    filemenu.add_command(label="Open...", command=callback)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=callback)
    helpmenu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=callback)
    
def main():
    root = tk.Tk()
    app = Application(master=root)
    # Set title and bg
    root.title("ReadTex")
    root.configure(background='black')
    # Create a menu
    create_menu(root)
    app.mainloop()


if __name__ == "__main__":
    main()
