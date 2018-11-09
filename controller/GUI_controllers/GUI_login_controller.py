
from tkinter import *
from tkinter import messagebox

# from model.GUI_model.GUI_login_model import login_model
from view import login_UI
from view import main_frame

# from .GUI_option_controller import option_controller

from model import MailParser

class login_controller:

    """
        The login GUI controller.
        It creates the login UI
        Contains functions that the UI's buttons will use.

        gets the login info
    """

    def __init__(self):
        self.UI = login_UI()
        self.UI.get_but.config(command=self._login)
        self.UI.can_but.config(command=lambda: self.exit())
        self.UI.radio_but_new.config(command=lambda:self.UI.var.set(0))
        self.UI.radio_but_all.config(command=lambda:self.UI.var.set(1))

    def _login(self):
        user_email = str(self.UI.account_entry.get())
        user_pass = str(self.UI.pin_entry.get())
        scan_type = str(self.UI.var.get())

        mail = MailParser(user_email, user_pass)
        mail.getMail(int(scan_type))
        print("Good")
        print(scan_type)

    def exit(self):
        self.UI.master.destroy()


if __name__ == "__main__":
    # root = Tk()
    frame = login_UI()
    # ui = login_controller(root, frame)
    mainloop()