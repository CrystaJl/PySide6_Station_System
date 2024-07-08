import json
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
        self.text_to_aply_label.setText('') #ФУ КОСТЫЛЕМ ВАНЯЕТ
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
        self.clear_all_pushButton.clicked.connect(lambda: self.delete_all_text())
        self.delete_previous_pushButton.clicked.connect(lambda: self.delete_text())
        self.accept_password_window_pushButton.clicked.connect(lambda: self.set_changes())
        self.is_password = is_password
        self.user_level = user_level


        
    def append_text(self, text):
        current_text = str(self.text_to_aply_label.text())
        if text == ',':
            if current_text == '' or "," in current_text:
                text = ''

        new_text = str(current_text + str(text))
        self.text_to_aply_label.setText(new_text)

    def delete_text(self):
        current_text = str(self.text_to_aply_label.text())
        new_text = str(current_text[:-1])
        self.text_to_aply_label.setText(new_text)

    def delete_all_text(self):
        self.text_to_aply_label.setText('')


    def give_them_text(self, role, level):
        self.password_text_label.setText(f"min: {role}   max: {level}")

    def set_changes(self):
        current_text = str(self.text_to_aply_label.text())

        with open('users.json', 'r') as f:
            passwords = json.load(f)
        
            
        for user, details in passwords.items():
            if details["password"] == current_text:
                role = details["role"]
                level = details["level"]
                print(f"Role for password '{current_text}' found: {role}, {level}")
                self.user_level = role
                print(self.user_level)
                self.give_them_text(role, level)



        
