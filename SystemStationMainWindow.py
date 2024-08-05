from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

from UI.Ui_System_Station_Main_window import Ui_System_Station_Main_window
from MODULES.Settings import System_Station_Main_window_settings
from MODULES.JsonParser import Json_parser
from MAIN.PasswordWindow import Password_window
from MAIN.UpdateAttributeWindow import Update_Attribute_window
import sys

class System_Station_Main_window(QWidget, Ui_System_Station_Main_window, System_Station_Main_window_settings, Json_parser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSystemStationMainSettings()
        self.setupSystemStationMainWindowSvgIcons()
        self.giveTimer()
        self.timeChanger()
        
        from MODULES.Settings import GraphsViewer
        self.graph_viewer = GraphsViewer(self.main_graphicsView)
        self.graph_viewer.main()

    def choose_attribute_or_password_window(self, requiered_level, json_key, min_value, max_value):
        if self.current_level >= requiered_level:
            self.update_attribute_window = Update_Attribute_window(self, json_key, min_value, max_value)
            self.update_attribute_window.setWindowModality(Qt.ApplicationModal)
            self.update_attribute_window.show()
        else:
            self.password_window = Password_window(self)
            self.password_window.setWindowModality(Qt.ApplicationModal)
            self.password_window.show()

    def show_password_window(self):
        self.password_window = Password_window(self)
        self.password_window.setWindowModality(Qt.ApplicationModal)
        self.password_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = System_Station_Main_window()
    window.show()
    app.exec() 