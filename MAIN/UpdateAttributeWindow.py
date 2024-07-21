from PySide6.QtWidgets import QWidget

from UI.Ui_Keypad_window import Ui_Keypad_window
from MODULES.Settings import Update_Attribute_Window_settings

class Update_Attribute_window(QWidget, Ui_Keypad_window, Update_Attribute_Window_settings):
    def __init__(self, parent, requiered_level, min, max):
        super().__init__()
        self.setupUi(self)
        self.setupUpdateAttributeWindowSettings(parent, requiered_level, min, max)