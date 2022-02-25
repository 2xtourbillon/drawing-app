import tkinter as tk
import tkinter.ttk as ttk

class FreeHandDrawing(tk.Tk):
    """initialing the main window"""
    def __init_(self):
        super().__init__()
        self.title('Free Hand Drawing Tool')
        self._xold = None #coords
        self._yold = None
        self.canvas = None
        self.color = 'Black'
        self.thickness = 1
        #tag will be assigned to separate drawings on the canvas for undo button
        self.tag = ['tag', '0'] 
        self._create_widgets()



FreeHandDrawing().mainloop()