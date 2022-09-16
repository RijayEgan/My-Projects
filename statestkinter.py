import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('States and Capitals Quiz')
    self.geometry('500x500')

    # label
    self.label = ttk.Label(self, text='Hello, Tkinter!')
    self.label.pack()

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
  app = App()
  app.mainloop()