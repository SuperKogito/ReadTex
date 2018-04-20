import tkinter as tk
from PIL import ImageTk
from pygame import mixer
from logic import Reader


class Player():
    def __init__(self):
        self.pause_state = 0
    
    def play(self):
        if self.pause_state == 0:
            mixer.init()
            mixer.music.load('text_to_speech_file.mp3')
            mixer.music.play()
        else:
            mixer.music.unpause()
    
    def stop(self):
        mixer.music.stop()
        self.pause_state = 0
    
    def pause(self):
        mixer.music.pause()
        self.pause_state = 1
        
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.player = Player()

        for r in range(6): self.master.rowconfigure(r, weight=1)
        for c in range(2): self.master.columnconfigure(c, weight=1)

        self.Frame1 = self.make_frame(0, 0, 5, 1)
        self.Frame2 = self.make_frame(0, 1, 5, 1)
        self.Frame3 = self.make_frame(5, 0, 1, 2)

        self.make_button(self.Frame1, "icons/play.png", 0)
        self.make_button(self.Frame1, "icons/stop.png", 1)
        self.make_button(self.Frame1, "icons/pause.png", 2)
        
        self.create_input_widget()
        self.create_status_widget()
        
    def create_input_widget(self):
        self.input = tk.LabelFrame(self.Frame2, text=" Input text ")
        self.textvar = tk.StringVar()
        self.textbox = tk.Text(self.input, height=4, width=50, font=("TkDefaultFont", 14), wrap='word', undo=True)
        self.textbox.pack(expand=1, fill="both", padx=5, pady=5)
        self.input.pack(expand=1, fill="both", padx=5, pady=5)

        button2 = tk.Button(self.input, text="Read this", command=lambda: self.read())
        button2.pack(side=tk.LEFT, expand=1, fill="both", padx=5, pady=5)
    
    def create_status_widget(self):
        self.output = tk.LabelFrame(self.Frame3)
        self.status_message = tk.StringVar()
        self.status_message.set('No sample yet')
        self.textwidget = tk.Label(self.output, textvariable=self.status_message, bd=1, anchor="n", height=1, width=20)
        self.textwidget.configure(relief='flat', state="normal")
        self.textwidget.config(bg='black', fg='white', font=("Courier", 10))
        self.textwidget.pack(side=tk.RIGHT, expand=1, fill="both", padx=2, pady=2)
        self.output.pack(expand=1, fill="both", padx=2, pady=2)

    def make_frame(self, r, c, rs, cs):
        frame = tk.Frame()
        frame.grid(row = r, column = c, rowspan = rs, columnspan = cs, sticky = tk.W+tk.E+tk.N+tk.S)
        return frame

    def make_button(self, Frame, img_name, i):
        b = tk.Button(Frame,  fg = "#0080ff", bg = "black")
        image = ImageTk.PhotoImage(file=img_name)
        if i==0: b.config(image=image, command=lambda: self.player.play())
        elif i==1: b.config(image=image, command=lambda: self.player.stop())
        else: b.config(image=image, command=lambda: self.player.pause())
        b.image = image
        b.pack(side="top", fill="both", expand=True, padx=2, pady=3)

    def read(self):
        self.reader = Reader()
        text = self.textbox.get("1.0", tk.END)
        self.reader.process(text)
        self.status_message.set('Mp3 file generated. Press play to listen to it.')