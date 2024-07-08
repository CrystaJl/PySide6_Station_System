class System_Station_Main_window_settings:
    def setupSystemStationMainSettings(self):
        self.go_to_main_settings_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(1))
        self.go_to_main_page_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(0))
        self.morning_1_pushButton.clicked.connect(self.show_password_window)
        self.morning_2_pushButton.clicked.connect(self.show_password_window)
        self.morning_3_pushButton.clicked.connect(self.show_password_window)
        self.morning_4_pushButton.clicked.connect(self.show_password_window)
        self.day_1_pushButton.clicked.connect(self.show_password_window)
        self.day_2_pushButton.clicked.connect(self.show_password_window)
        self.day_3_pushButton.clicked.connect(self.show_password_window)
        self.day_4_pushButton.clicked.connect(self.show_password_window)
        self.evening_1_pushButton.clicked.connect(self.show_password_window)
        self.evening_2_pushButton.clicked.connect(self.show_password_window)
        self.evening_3_pushButton.clicked.connect(self.show_password_window)
        self.evening_4_pushButton.clicked.connect(self.show_password_window)
        self.user_setpoint_pushButton.clicked.connect(self.show_password_window)
        self.monday_pushButton.clicked.connect(self.show_password_window)
        self.tuesday_pushButton.clicked.connect(self.show_password_window)
        self.wednesday_pushButton.clicked.connect(self.show_password_window)
        self.thursday_pushButton.clicked.connect(self.show_password_window)
        self.friday_pushButton.clicked.connect(self.show_password_window)
        self.saturday_pushButton.clicked.connect(self.show_password_window)
        self.sunday_pushButton.clicked.connect(self.show_password_window)

        self.is_password = 1
        self.user_level = 0 #5

class Password_window_settings:
    def setupPasswordWindowSettings(self, is_password, user_level):
        self.number_0_pushButton.clicked.connect(lambda: self.append_text(0))
        self.number_1_pushButton.clicked.connect(lambda: self.append_text(1))
        self.number_2_pushButton.clicked.connect(lambda: self.append_text(2))
        self.number_3_pushButton.clicked.connect(lambda: self.append_text(3))
        self.number_4_pushButton.clicked.connect(lambda: self.append_text(4))
        self.number_5_pushButton.clicked.connect(lambda: self.append_text(5))
        self.number_6_pushButton.clicked.connect(lambda: self.append_text(6))
        self.number_7_pushButton.clicked.connect(lambda: self.append_text(7))
        self.number_8_pushButton.clicked.connect(lambda: self.append_text(8))
        self.number_9_pushButton.clicked.connect(lambda: self.append_text(9))
        self.set_comma_pushButton.clicked.connect(lambda: self.append_text(','))
        self.clear_all_pushButton.clicked.connect(lambda: self.append_text('clear'))
        self.delete_previous_pushButton.clicked.connect(lambda: self.append_text('del_prev'))
        self.accept_password_window_pushButton.clicked.connect(lambda: self.set_changes)
        self.is_password = is_password
        self.user_level = user_level

    def append_text(self, text):
        print(text)

    def set_changes(self):
        pass