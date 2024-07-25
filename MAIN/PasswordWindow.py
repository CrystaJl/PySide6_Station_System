from PySide6.QtWidgets import QWidget

from UI.Ui_Keypad_window import Ui_Keypad_window
from MODULES.Settings import Password_Window_settings

class Password_window(QWidget, Ui_Keypad_window, Password_Window_settings):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.setupPasswordWindowSettings(parent)