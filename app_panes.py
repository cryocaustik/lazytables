import tkinter as tk
from PIL import Image, ImageTk


FONT_HEADER = ('Consolas')
FONT_SUB_HEADER = ('Segoe UI', 14)
FONT_TEXT = ('Segoe UI', 12)
FONT_BUTTON = ('Segoe UI', 12)

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
        _pane.pack(side=tk.TOP, ipadx=10, fill=tk.X)
        _pane.config(background='#303030')

        txt_serv_name = 'mySqlServ'
        txt_db_name = 'myDb'
        txt_schema_name = 'dev'
        txt_target_dt = ''

        # create objects
        frm_serv = tk.Frame(
            _pane, pady=10, width=30
        )
        frm_database = tk.Frame(
            _pane, pady=10, width=30
        )
        frm_schema = tk.Frame(
            _pane, pady=10, width=30
        )
        frm_target_dt = tk.Frame(
            _pane, pady=10, width=30
        )
        frm_buttons = tk.Frame(
            _pane, width=30
        )

        lbl_hdr = tk.Label(
            _pane, text=" Notfication Process", justify='center', anchor='w'
            , relief='groove', font=FONT_SUB_HEADER, bg='#303030', fg='#0083a8'
        )
        lbl_serv_name = tk.Label(
            _pane, text="SQL Server: ", anchor='e', width=15
            , bg='#303030', fg='#fff', font=FONT_TEXT
        )
        lbl_db_name = tk.Label(
            _pane, text="SQL Database: ", anchor='e', width=15
            , bg='#303030', fg='#fff', font=FONT_TEXT
        )
        lbl_schema_name = tk.Label(
            _pane, text="SQL Schema: ", anchor='e', width=15
            , bg='#303030', fg='#fff', font=FONT_TEXT
        )
        lbl_target_dt = tk.Label(
            _pane, text="Target Drop Date: ", anchor='e', width=15
            , bg='#303030', fg='#fff', font=FONT_TEXT
        )

        entry_serv_name = tk.Entry(
            _pane, font=FONT_TEXT, width=30
        )
        entry_db_name = tk.Entry(
            _pane, font=FONT_TEXT, width=30
        )
        entry_schema_name = tk.Entry(
            _pane, font=FONT_TEXT, width=30
        )
        entry_target_dt = tk.Entry(
            _pane, font=FONT_TEXT, width=30
        )

        bttn_execute = tk.Button(
            _pane, text='Execute', bg='#a82d2d', fg='#fff', relief='groove', font=FONT_BUTTON
            , command=lambda: print('notif execute')
        )

        # style objects
        frm_serv.config(
            bg='#303030'
        )
        frm_database.config(
            bg='#303030'
        )
        frm_schema.config(
            bg='#303030'
        )
        frm_target_dt.config(
            bg='#303030'
        )
        frm_buttons.config(
            bg='#303030'
        )

        # populate objects
        entry_serv_name.insert(1, txt_serv_name)
        entry_db_name.insert(1, txt_db_name)
        entry_schema_name.insert(1, txt_schema_name)
        entry_target_dt.insert(1, txt_target_dt)

        # layout objects
        lbl_hdr.pack(side=tk.TOP, fill=tk.BOTH, ipady=10)
        frm_serv.pack(side=tk.TOP, fill=tk.BOTH)
        frm_database.pack(side=tk.TOP, fill=tk.BOTH)
        frm_schema.pack(side=tk.TOP, fill=tk.BOTH)
        frm_target_dt.pack(side=tk.TOP, fill=tk.BOTH)
        frm_buttons.pack(side=tk.TOP, fill=tk.BOTH)

        lbl_serv_name.pack(side=tk.LEFT, fill=tk.BOTH, in_=frm_serv)
        lbl_db_name.pack(side=tk.LEFT, fill=tk.BOTH, in_=frm_database)
        lbl_schema_name.pack(side=tk.LEFT, fill=tk.BOTH, in_=frm_schema)
        lbl_target_dt.pack(side=tk.LEFT, fill=tk.BOTH, in_=frm_target_dt)

        entry_serv_name.pack(side=tk.LEFT, fill=tk.BOTH, in_=frm_serv)
        entry_db_name.pack(side=tk.LEFT, fill=tk.BOTH, in_=frm_database)
        entry_schema_name.pack(side=tk.LEFT, fill=tk.BOTH, in_=frm_schema)
        entry_target_dt.pack(side=tk.LEFT, fill=tk.BOTH, in_=frm_target_dt)

        bttn_execute.pack(side=tk.BOTTOM, fill=tk.BOTH, ipady=5, pady=(35, 0), in_=frm_buttons)
