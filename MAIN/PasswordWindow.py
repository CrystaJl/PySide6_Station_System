from PySide6.QtWidgets import QWidget

from UI.Ui_Password_window import Ui_Password_window
from MODULES.Settings import Password_window_settings

class Password_window(QWidget, Ui_Password_window, Password_window_settings):
    def __init__(self, is_password, user_level):
        super().__init__()
        self.setupUi(self)
        self.setupPasswordWindowSettings(is_password, user_level)