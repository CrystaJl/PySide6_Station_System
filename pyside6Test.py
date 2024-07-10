from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

from UI.Ui_System_Station_Main_window import Ui_System_Station_Main_window
from MODULES.Settings import System_Station_Main_window_settings
from MAIN.PasswordWindow import Password_window

import sys 

class System_Station_Main_window(QWidget, Ui_System_Station_Main_window, System_Station_Main_window_settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSystemStationMainSettings()
        self.setupSystemStationMainWindowIcons()
        self.setupSystemStationMainWindowSvgIcons()

    def show_password_window(self, requiered_level):
        self.password_window = Password_window(self, requiered_level)
        self.password_window.setWindowModality(Qt.ApplicationModal)
        self.password_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = System_Station_Main_window()
    window.show()
    app.exec() 