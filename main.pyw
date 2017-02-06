import tkinter as tk
from tkinter import ttk
from query_db import IdentifyTables
from PIL import Image, ImageTk


FONT_HEADER = ('Consolas')
FONT_SUB_HEADER = ('Segoe UI', 14)
FONT_TEXT = ('Segoe UI', 12)
FONT_BUTTON = ('Segoe UI', 12)


class LazyTables(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.main_container = tk.PanedWindow()
        self.main_container.pack(expand=1)
        self.main_container.config(background='#000')

        Menu.menu_pane(self, self.main_container)
        # self.show_body('home')


    def show_body(self, pane_name):
        _body_dict = {
            'home': Body.home_pane
            , 'notif': Body.notif_pane
        }

        if len(self.main_container.children) > 1:
            for _p in self.main_container.children:
                if _p != '!panedwindow':
                    self.main_container.children[_p].pack_forget()

        _body_dict[pane_name](self, self.main_container)


class Menu:

    def menu_pane(self, main_con):
        _pane = tk.PanedWindow(main_con)
        _pane.pack(side=tk.LEFT, expand=1, anchor='nw')
        _pane.config(background='#000')

        # create objects
        image = Image.open('./images/logo_250.png')
        photo = ImageTk.PhotoImage(image,'10x10')
        lbl_hdr = tk.Label(
            _pane, image=photo, bg='#000', fg='#fff'
        )
        lbl_hdr.image = photo

        bttn_home = tk.Button(
            _pane, text='Instructions', bg='#b7b7b7', relief='groove'
            , command=lambda: self.show_body('home'), font=FONT_BUTTON
        )
        bttn_notif = tk.Button(
            _pane, text='Notification', bg='#b7b7b7', relief='groove'
            , command=lambda: self.show_body('notif'), font=FONT_BUTTON
        )
        bttn_drop = tk.Button(
            _pane, text='Drop Archived', bg='#b7b7b7', relief='groove'
            , command=lambda: self.show_body('drop'), font=FONT_BUTTON
        )

        # layout objects
        lbl_hdr.pack(side=tk.TOP, fill=tk.BOTH, ipady=10, anchor='n')
        bttn_home.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)
        bttn_notif.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)
        bttn_drop.pack(side=tk.TOP, fill=tk.BOTH, ipady=5)


class Body:

    def home_pane(self, main_con):
        # declare variables
        _txt_instruct_notif = """Summary:
        This process will identify tables with last modified date > 2 months from today,
        archive them with a target drop date of today + 5 days, and send an email to
        the HCA team advising the target tables will be dropped in 5 days.

    Process:
        1. Click on the 'Notification' button;
        2. Adjust the SQL server, database, and schema if needed;
        3. Click 'Execute'.
        """
        _txt_instruct_drop = """Summary:
        This process will identify tables in the archive matching the target drop date specified,
        and drop the target tables.

    Process:
        1. Click on 'Drop Archived' button;
        2. Adjust the SQL server, database, and schema if needed;
        3. Click 'Execute'.
        """
        _txt_drop_warn = "*** This process is irreversible; tables dropped using this method will be permanently deleted ***"

        _pane = tk.PanedWindow(main_con)
        _pane.pack(side=tk.LEFT, ipadx=10)
        _pane.config(background='#303030')
        # _pane = main_con

        # create objects
        lbl_instr_hdr = tk.Label(
            _pane, text=' Instructions', justify='center', anchor='w'
            , relief='groove', font=FONT_SUB_HEADER, bg='#303030', fg='#0083a8'
        )
        lbl_notif_hdr = tk.Label(
            _pane, text='Notification', justify='center', relief='flat'
            , font=FONT_SUB_HEADER, bg='#303030', fg='#efa700'
        )
        lbl_instr_notif = tk.Label(
            _pane, text=_txt_instruct_notif, justify='left', relief='sunken'
            , font=FONT_TEXT, bg='#303030', fg='#fff'
        )
        lbl_drop_hdr = tk.Label(
            _pane, text='Drop Archived', justify='center', relief='flat'
            , font=FONT_SUB_HEADER, bg='#303030', fg='#efa700'
        )
        lbl_drop_warn = tk.Label(
            _pane, text=_txt_drop_warn, justify='center', relief='flat'
            , font=FONT_TEXT, bg='#303030', fg='#ef0000'
        )
        lbl_instr_drop = tk.Label(
            _pane, text=_txt_instruct_drop, justify='left', relief='sunken'
            , font=FONT_TEXT, bg='#303030', fg='#fff'
        )


        # layout objects
        lbl_instr_hdr.pack(side=tk.TOP, fill=tk.BOTH, ipady=10)
        lbl_notif_hdr.pack(side=tk.TOP, fill=tk.BOTH)
        lbl_instr_notif.pack(side=tk.TOP, fill=tk.BOTH)
        lbl_drop_hdr.pack(side=tk.TOP, fill=tk.BOTH)
        lbl_drop_warn.pack(side=tk.TOP, fill=tk.BOTH)
        lbl_instr_drop.pack(side=tk.TOP, fill=tk.BOTH)


    def notif_pane(self, main_con):

        # declare variables
        _pane = tk.PanedWindow(main_con)
        _pane.pack(side=tk.LEFT, ipadx=10)
        _pane.config(background='#303030')
        # _pane = main_con

        # create objects
        lbl_hdr = tk.Label(
            _pane, text="Notfication Process", justify='center', anchor='w'
            , relief='groove', font=FONT_SUB_HEADER, bg='#303030', fg='#0083a8'
        )
        lbl_serv_name = tk.Label(
            _pane, text="SQL Server: ", anchor='e'
            , bg='#303030', fg='#fff'
        )
        lbl_db_name = tk.Label(
            _pane, text="SQL Database: "
            , bg='#303030', fg='#fff'
        )
        lbl_schema_name = tk.Label(
            _pane, text="SQL Schema: "
            , bg='#303030', fg='#fff'
        )
        lbl_target_dt = tk.Label(
            _pane, text="Target Drop Date: "
            , bg='#303030', fg='#fff'
        )

        txt_serv_name = tk.Entry(
            _pane
        )
        txt_db_name = tk.Entry(
            _pane
        )
        txt_schema_name = tk.Entry(
            _pane
        )
        txt_target_dt = tk.Entry(
            _pane
        )

        # style objects


        # layout objects
        lbl_hdr.pack(side=tk.TOP, fill=tk.BOTH, ipady=10, anchor='n')
        lbl_serv_name.pack(side=tk.TOP, fill=tk.BOTH)
        lbl_db_name.pack(side=tk.TOP, fill=tk.BOTH)
        lbl_schema_name.pack(side=tk.TOP, fill=tk.BOTH)
        lbl_target_dt.pack(side=tk.TOP, fill=tk.BOTH)



if __name__ == '__main__':
    app = LazyTables()
    app.title('Lazy Tables')
    app.iconbitmap(default='./images/icon.ico')
    app.config(bg='#cecece')

    app.update()
    app.mainloop()



