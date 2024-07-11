from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

from UI.Ui_System_Station_Main_window import Ui_System_Station_Main_window
from MODULES.Settings import System_Station_Main_window_settings
from MODULES.JsonParser import Json_parser
from MAIN.PasswordWindow import Password_window

import sys 

class System_Station_Main_window(QWidget, Ui_System_Station_Main_window, System_Station_Main_window_settings, Json_parser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSystemStationMainSettings()
        self.setupSystemStationMainWindowIcons()
        self.setupSystemStationMainWindowSvgIcons()

        self.giveTimer()
        self.timeChanger()
        

        self.update_json('test.json', '01', '0100', '01SuctionPressure', 500)
        print(self.read_json('test.json', '01', '0100', '01SuctionPressure'))


    def show_password_window(self, requiered_level, current_button, min, max, text_to_change=""):
        self.current_button = current_button
        self.text_to_change = text_to_change
        self.password_window = Password_window(self, requiered_level, min, max)
        self.password_window.setWindowModality(Qt.ApplicationModal)
        self.password_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = System_Station_Main_window()
    window.show()
    app.exec() 