import tkinter as tk
from tkinter import ttk
from query_db import IdentifyTables
from app_panes import Menu as ap_Menu, Body as ap_Body
from PIL import Image, ImageTk


class LazyTables(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.main_container = tk.PanedWindow()
        self.main_container.pack(expand=1)
        self.main_container.config(background='#000')

        ap_Menu.menu_pane(self, self.main_container)
        # self.show_body('home')

    def show_body(self, pane_name):
        _body_dict = {
            'home': ap_Body.home_pane
            , 'notif': ap_Body.notif_pane
        }

        if len(self.main_container.children) > 1:
            for _p in self.main_container.children:
                if _p != '!panedwindow':
                    self.main_container.children[_p].pack_forget()

        _body_dict[pane_name](self, self.main_container)


if __name__ == '__main__':
    app = LazyTables()
    app.title('Lazy Tables')
    app.iconbitmap(default='./images/icon.ico')
    app.config(bg='#cecece')
    app.resizable(0, 0)
    app.update()
    app.mainloop()



