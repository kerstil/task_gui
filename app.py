import tkinter as tk
from TaskGui import TaskGui


if __name__ == '__main__':
    window = tk.Tk() # Loo põhiaken
    TaskGui(window) # Loo GUI aga anna aken kaas
    window.mainloop() # Viimane rida koodis

