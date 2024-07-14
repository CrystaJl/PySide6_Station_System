from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtCore import Qt, QTimer, QTime, QDateTime
from PySide6.QtSvg import QSvgRenderer
import json
import os


class System_Station_Main_window_settings:
    def setupSystemStationMainSettings(self):

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
#Блок кода, отвечающий за подключение всех возможных кнопок, связанных со страницами кнопок и страницами основной работы с оборудованием

###################################################################################################################################################################################################################################################################################################################################################
        #переключение между основным окном(страницей) и основными настройками, дополнительно, переключение между страницами в основном окне
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(1))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_settings_main_page_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(0))

        self.go_to_main_graphic_page_pushButton.clicked.connect(lambda: self.main_main_pages_stackedWidget.setCurrentIndex(0))
        self.go_to_main_statistics_page_pushButton.clicked.connect(lambda: self.main_main_pages_stackedWidget.setCurrentIndex(1))
        self.go_to_main_switch_page_pushButton.clicked.connect(lambda: self.main_main_pages_stackedWidget.setCurrentIndex(2))

###################################################################################################################################################################################################################################################################################################################################################
        #три подключения к кнопкам основной страницы кнопок, и переключение, при нажатии на них, страниц справа
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_manager_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))
        
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(2))
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_contacts_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_manager_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #Блок подключений различного мониторинга, включая подключения возврата на предыдущие страницы справа и страницы кнопок
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_tracking_trends_online_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_tracking_pumps_developments_page_icon_label_2, 'empty.svg', 1))

        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_tracking_trends_online_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_tracking_pumps_developments_page_icon_label_2, 'empty.svg', 1))

        self.go_to_tracking_pumps_developments_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(4))
        self.go_to_tracking_pumps_developments_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_tracking_pumps_developments_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_tracking_pumps_developments_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_tracking_trends_online_page_icon_label_2, 'empty.svg', 1))

        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(5))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(2))

        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_tracking_trends_online_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_tracking_pumps_developments_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'указатель верх.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #Блок подключений журнала, так же как и выше включая подключения возврата на предыдущие страницы справа и страницы кнопок
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(3))

        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(3))
        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_journal_current_events_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_journal_changes_page_icon_label_2, 'empty.svg', 1))

        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_journal_current_events_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.go_to_journal_current_events_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_journal_current_events_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_journal_current_events_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_journal_changes_page_icon_label_2, 'empty.svg', 1))

        self.go_to_journal_changes_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(7))
        self.go_to_journal_changes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_journal_changes_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_journal_changes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_journal_current_events_page_icon_label_2, 'empty.svg', 1))

        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(8))
        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(4))

        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(3))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_journal_current_events_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_journal_changes_page_icon_label_2, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #Так как настройки станции не имеют вложенных страниц с кнопками из за чего есть три блока: 1) сам переход в настройки станции 2) возврат 3) отображение страниц настроек станции
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(5))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))

        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(10))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(11))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(12))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(13))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(14))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_options_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(15))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #последние подключения к вкладке инженерного меню, так же с возвратом к основным кнопкам и странице
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(16))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(6))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_plc_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_backup_page_icon_label_2, 'empty.svg', 1))

        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(16))
        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_plc_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_backup_page_icon_label_2, 'empty.svg', 1))

        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(17))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(17))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_plc_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_backup_page_icon_label_2, 'empty.svg', 1))


        #дубликат существующего подключения с переходом на соответствующую страницу кнопок(доступ из другого места к тем страницам, к которым уже есть доступ из другого места)
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(5))
        #############################################################################################################################

        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(18))
        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_backup_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.go_to_engineering_plc_page_icon_label_2, 'empty.svg', 1))

        #дубликат двух существующих подключений (доступ из другого места к тем страницам, к которым уже есть доступ из другого места)
        self.go_to_engineering_panel_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.go_to_engineering_contacts_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(2))
        #############################################################################################################################


###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
#Данный блок кода сфокусирован на подключение всех возможных кнопок, связанных с паролями и уровнями доступа, к окну, отвечающему за изменение доступа и за изменение атрибутов

###################################################################################################################################################################################################################################################################################################################################################
        #Планировщик
        self.manager_user_setpoint_10SetpointUser_pushButton.clicked.connect(self.show_password_window)

        self.manager_monday_10TypeOfDayMonday_pushButton.clicked.connect(self.show_password_window)
        self.manager_tuesday_10TypeOfDayTuesday_pushButton.clicked.connect(self.show_password_window)
        self.manager_wednesday_10TypeOfDayWednesday_pushButton.clicked.connect(self.show_password_window)
        self.manager_thursday_10TypeOfDayThursday_pushButton.clicked.connect(self.show_password_window)
        self.manager_friday_10TypeOfDayFriday_pushButton.clicked.connect(self.show_password_window)
        self.manager_saturday_10TypeOfDaySaturday_pushButton.clicked.connect(self.show_password_window)
        self.manager_sunday_10TypeOfDaySunday_pushButton.clicked.connect(self.show_password_window)

        self.manager_morning_1_1_10WeekdayMorningHour_pushButton.clicked.connect(lambda: self.show_password_window(3, self.manager_morning_1_1_10WeekdayMorningHour_pushButton, 0, 50))
        self.manager_morning_1_2_10WeekdayMorningMinutes_pushButton.clicked.connect(lambda: self.show_password_window(3, self.manager_morning_1_2_10WeekdayMorningMinutes_pushButton, 0, 50))
        self.manager_morning_2_1_10WeekendMorningHour_pushButton.clicked.connect(lambda: self.show_password_window(4, self.manager_morning_2_1_10WeekendMorningHour_pushButton, 0, 60))
        self.manager_morning_2_2_10WeekendMorningMinutes_pushButton.clicked.connect(lambda: self.show_password_window(4, self.manager_morning_2_2_10WeekendMorningMinutes_pushButton, 0, 60))
        self.manager_morning_3_10SetpointWeekdaysMorning_pushButton.clicked.connect(self.show_password_window)
        self.manager_morning_4_10SetpointWeekendsMorning_pushButton.clicked.connect(self.show_password_window)

        self.manager_day_1_1_10WeekdayDayHour_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_1_2_10WeekdayDayMinutes_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_2_1_10DayOffMinutes_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_2_2_10DayOffMinutes_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_3_10SetpointWeekdaysDay_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_4_10SetpointWeekendsDay_pushButton.clicked.connect(self.show_password_window)

        self.manager_evening_1_1_10WeekdayEveningHour_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_1_2_10WeekdayEveningMinutes_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_2_1_10WeekendEveningHour_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_2_2_10WeekendEveningMinutes_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_3_10SetpointWeekdaysEvening_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_4_10SetpointWeekendsEvening_pushButton.clicked.connect(self.show_password_window)

        self.manager_night_1_1_10WeekdayNightHour_pushButton.clicked.connect(self.show_password_window)
        self.manager_night_1_2_10WeekdayNightMinutes_pushButton.clicked.connect(self.show_password_window)
        self.manager_night_2_1_10WeekendNightHour_pushButton.clicked.connect(self.show_password_window)
        self.manager_night_2_2_10WeekendNightMinutes_pushButton.clicked.connect(self.show_password_window)
        self.manager_night_3_10SetpointWeekdaysNights_pushButton.clicked.connect(self.show_password_window)
        self.manager_night_4_10SetpointWeekendsNights_pushButton.clicked.connect(self.show_password_window)

###################################################################################################################################################################################################################################################################################################################################################
        #Настройки панели
        self.panel_settings_display_disable_time_pushButton.clicked.connect(self.show_password_window)               #переименовать атрибут
        self.panel_settings_screensaver_activation_time_pushButton.clicked.connect(self.show_password_window)        #переименовать атрибут
        self.panel_settings_buzzer_pushButton.clicked.connect(self.show_password_window)                             #переименовать атрибут
        self.panel_settings_date_day_pushButton.clicked.connect(self.show_password_window)                           #переименовать атрибут
        self.panel_settings_date_month_pushButton.clicked.connect(self.show_password_window)                         #переименовать атрибут
        self.panel_settings_date_year_pushButton.clicked.connect(self.show_password_window)                          #переименовать атрибут
        self.panel_settings_time_hour_pushButton.clicked.connect(self.show_password_window)                          #переименовать атрибут
        self.panel_settings_time_minutes_pushButton.clicked.connect(self.show_password_window)                       #переименовать атрибут
        self.panel_settings_time_seconds_pushButton.clicked.connect(self.show_password_window)                       #переименовать атрибут
        self.panel_settings_ip_1_pushButton.clicked.connect(self.show_password_window)                               #переименовать атрибут
        self.panel_settings_ip_2_pushButton.clicked.connect(self.show_password_window)                               #переименовать атрибут
        self.panel_settings_ip_3_pushButton.clicked.connect(self.show_password_window)                               #переименовать атрибут
        self.panel_settings_ip_4_pushButton.clicked.connect(self.show_password_window)                               #переименовать атрибут
        self.panel_settings_mask_1_pushButton.clicked.connect(self.show_password_window)                             #переименовать атрибут
        self.panel_settings_mask_2_pushButton.clicked.connect(self.show_password_window)                             #переименовать атрибут
        self.panel_settings_mask_3_pushButton.clicked.connect(self.show_password_window)                             #переименовать атрибут
        self.panel_settings_mask_4_pushButton.clicked.connect(self.show_password_window)                             #переименовать атрибут
        self.panel_settings_gateway_1_pushButton.clicked.connect(self.show_password_window)                          #переименовать атрибут
        self.panel_settings_gateway_2_pushButton.clicked.connect(self.show_password_window)                          #переименовать атрибут
        self.panel_settings_gateway_3_pushButton.clicked.connect(self.show_password_window)                          #переименовать атрибут
        self.panel_settings_gateway_4_pushButton.clicked.connect(self.show_password_window)                          #переименовать атрибут

###################################################################################################################################################################################################################################################################################################################################################
        #Контакты
        self.contacts_number_of_pumps_19QuantityPump_pushButton.clicked.connect(lambda: self.show_password_window(0, self.contacts_number_of_pumps_19QuantityPump_pushButton, 0, 6, "Колличество насосов:            "))
        self.contacts_current_workings_number_of_pumps_19WorkingQuantityPump_pushButton.clicked.connect(self.show_password_window)

###################################################################################################################################################################################################################################################################################################################################################
        #Параметры двигателей                  (внутри настроек станции)
        self.station_settings_engine_parameters_voltage_18MotorVoltage_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_amperage_18MotorCurrent_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_frequency_18MotorFrequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_speed_18MotorSpeed_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_power_18MotorPower_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_acceleration_time_18AccelerationTime_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_slow_down_time_18DecelerationTime_pushButton.clicked.connect(self.show_password_window)

        self.station_settings_engine_parameters_read_settings_pushButton.clicked.connect(self.show_password_window)                        #переименовать атрибут
        self.station_settings_engine_parameters_write_settings_pushButton.clicked.connect(self.show_password_window)                       #переименовать атрибут

###################################################################################################################################################################################################################################################################################################################################################
        #Настройки датчиков                    (внутри настроек станции)
        self.station_settings_sensors_settings_milliamps_at_suction_16RangeSuctionSensor_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_sensors_settings_milliamps_at_discharge_16RangeDischargeSensor_pushButton.clicked.connect(self.show_password_window)

###################################################################################################################################################################################################################################################################################################################################################
        #Общие параметры насосов               (внутри настроек станции)
        self.station_settings_general_pumps_parameters_minimal_operating_frequency_11MinimumFrequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_maximal_operating_frequency_11MaximumFrequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_start_using_master_from_0_Hz_11ZeroStartMaster_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_use_pump_rotation_11ChangeEnable_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_pump_rotation_interval_11WizardChangeInterval_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_pump_rotation_time_of_day_11ChangeHour_pushButton.clicked.connect(self.show_password_window)

###################################################################################################################################################################################################################################################################################################################################################
        #Включение дополнительных насосов      (внутри настроек станции)
        self.station_settings_turn_on_extra_pumps_master_frequency_on_extra_pump_start_12FrequencyToTurnOnTheAuxiliaryPump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_acceptable_drawdown_12PermissiblePressureDrop_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_delay_for_critical_drawdown_12DelayWithAllowablePressureDrop_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_critical_drawdown_12CriticalPressureDrop_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_delay_for_acceptable_drawdown_12DelayCriticalPressureDrop_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_delay_for_leaving_to_fixed_frequency_12DelayFixedFrequencyStartPump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_fixed_frequency_12FixedFrequencyStartingPump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_operating_time_at_fixed_frequency_12FixedFrequencyTimeStartPump_pushButton.clicked.connect(self.show_password_window)

###################################################################################################################################################################################################################################################################################################################################################
        #Выключение дополнительных насосов     (внутри настроек станции)
        self.station_settings_turn_off_extra_pumps_master_frequency_on_extra_pump_shutdown_13FrequencyToTurnOffTheAuxiliaryPump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_acceptable_jump_13PermissibleOverpressure_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_delay_for_critical_jump_13DelayPermissibleOverpressure_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_critical_jump_13CriticalOverpressure_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_delay_for_acceptable_jump_13DelayCriticalOverpressure_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_delay_for_leaving_to_fixed_frequency_13DelayFixedFrequencyStopPump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_fixed_frequency_13FixedFrequencyPumpStop_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_operating_time_at_fixed_frequency_13FixedFrequencyTimeStopPump_pushButton.clicked.connect(self.show_password_window)

###################################################################################################################################################################################################################################################################################################################################################
        #Опции                                 (внутри настроек станции)
        self.station_settings_options_energy_saving_mode_15PowerSavingModeOn_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_start_energy_saving_mode_once_every_15PowerSavingModeTime_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_presure_drawdown_to_turn_off_energy_saving_mode_15PowerSavingModeExitPresure_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_increase_pressure_by_15PowerSavingModePressureIncrease_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_swing_integration_time_15PowerSavingModeIntegrationTime_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_acceptable_pressure_swing_15PowerSavingAllowablePressureSwing_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_acceptable_frequency_swing_15PowerSavingPermissibleFrequencySpan_pushButton.clicked.connect(self.show_password_window)

###################################################################################################################################################################################################################################################################################################################################################
        #Аварийные режимы                      (внутри настроек станции)
        self.station_settings_emergency_modes_differential_operating_frequency_14PumpStartConfirmationFrequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_differential_failure_delay_14PumpStartConfirmationAlarmDelay_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_differential_maximum_number_of_failures_14MaxAlarmConfirmationStartPump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_dry_warnings_pushButton.clicked.connect(self.show_password_window)                                                            #переименовать атрибут
        self.station_settings_emergency_modes_dry_failure_pushButton.clicked.connect(self.show_password_window)                                                             #переименовать атрибут
        self.station_settings_emergency_modes_dry_failure_delay_pushButton.clicked.connect(self.show_password_window)                                                       #переименовать атрибут
        self.station_settings_emergency_modes_shutdown_delay_pushButton.clicked.connect(self.show_password_window)                                                          #переименовать атрибут
        self.station_settings_emergency_modes_critical_pressure_to_shutdown_14CriticalPressureAlarmThreshold_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_control_pipeline_rupture_pushButton.clicked.connect(self.show_password_window)                                                #переименовать атрибут

###################################################################################################################################################################################################################################################################################################################################################
        #Настройки пид-регистрации                             (внутри инженерного меню)
        self.engineering_menu_pid_registration_settings_proportional_coefficient_17ProportionalCoefficient_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_integral_coefficient_17IntegralCoefficient_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_differential_coefficient_17DifferentialCoefficient_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_constant_of_integration_17IntegrationTime_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_ustavka_change_10SetpointModePid_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_ustavka_for_change_17SetpointPID_pushButton.clicked.connect(self.show_password_window)

###################################################################################################################################################################################################################################################################################################################################################
        #PLC                                                   (внутри инженерного меню)
        self.engineering_menu_plc_02DigitalInput16Bit0_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit1_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit2_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit3_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit4_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit5_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit6_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit7_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit8_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit9_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit10_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalInput16Bit11_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_09AlarmModbusPLC_pushButton.clicked.connect(self.show_password_window)

        self.engineering_menu_plc_02DigitalOutput16Bit0_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit1_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit2_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit3_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit4_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit5_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit6_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit7_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit8_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit9_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit10_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_plc_02DigitalOutput16Bit11_pushButton.clicked.connect(self.show_password_window)

        self.engineering_menu_plc_pushButton_26.clicked.connect(self.show_password_window)                     #переименовать атрибут
        self.engineering_menu_plc_pushButton_27.clicked.connect(self.show_password_window)                     #переименовать атрибут
        self.engineering_menu_plc_pushButton_28.clicked.connect(self.show_password_window)                     #переименовать атрибут
        self.engineering_menu_plc_pushButton_29.clicked.connect(self.show_password_window)                     #переименовать атрибут
        self.engineering_menu_plc_pushButton_30.clicked.connect(self.show_password_window)                     #переименовать атрибут

###################################################################################################################################################################################################################################################################################################################################################
        #Бекап                                                 (внутри инженерного меню)
        self.engineering_menu_backup_save_90_days_of_journal_80LogBackup_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_backup_save_energy_independent_memory_80RWBackup_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_backup_save_trends_80TrendsBackup_pushButton.clicked.connect(self.show_password_window)

        self.engineering_menu_backup_factory_all_settings_pushButton.clicked.connect(self.show_password_window) #переименовать атрибут

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
#блок кода контроля и отслеживания СТРАНИЦ ДЛЯ НАСТРОЙКИ И КОНТРОЛЯ ОБОРУДОВАНИЯ, отвечает за визуальное подтверждения действий путем изменения svg иконок кнопок, лейблов и т.д. исходя из нажатой кнопки навигации по приложению, включая будущие навигации по графикам и в лейблах отображения json значений

        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'указатель верх.svg', 1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))

        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'указатель верх.svg', 1))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))

        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_12_hours_icon_label, 'указатель верх.svg', 1))

        self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))

        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_1_hour_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_3_hours_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_6_hours_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_12_hours_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageButtonIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))




###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
#ключевые атрибуты взаимодействия с приложением, включая как интерфейс, так и логику

        self.is_password = 1

    
        self.current_button = None
        self.text_to_change = ""

        self.user_level = 0
        self.current_page = 0
        self.test_json = 'test.json'

        #атрибуты для работы с видом
        self.icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ICONS")
        self.svg_icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SVGICONS")
        self.current_theme = 'black'






###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
#Методы работы с json загрузкой значений, работающих по отслеживанию текущей страницы и загрузки значений только для текущей страницы пользователя, чтобы не нагружать систему лишними загрузками, которые пользователь не будет отслеживать

###################################################################################################################################################################################################################################################################################################################################################
#Основной метод проверки текущей страницы и перенаправление на метод загрузки json значений во все необходимые виждеты страницы

    def updateCurrentJsonStatistics(self):
        main_stackedWidget = self.main_stackedWidget.currentIndex()

        if main_stackedWidget == 0:
            self.MainPageLoadJson()

            main_main_pages_stackedWidget_currentIndex = self.main_main_pages_stackedWidget.currentIndex()

            if main_main_pages_stackedWidget_currentIndex == 0: self.MainGraficPageLoadJson()
            elif main_main_pages_stackedWidget_currentIndex == 1: self.MainStatisticsPageLoadJson()
            elif main_main_pages_stackedWidget_currentIndex == 2: self.MainSwitchPageLoadJson()

        elif main_stackedWidget == 1:
            settings_pages_stackedWidget_currentIndex = self.settings_pages_stackedWidget.currentIndex()

            if settings_pages_stackedWidget_currentIndex == 0:         self.SettingsManagerPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 1:       self.SettingsPanelSettingsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 2:       self.SettingsContactsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 3:       self.SettingsTrackingTrendsOnlinePageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 4:       self.SettingsTrackingPumpsDevelopmentsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 5:       self.SettingsTrackingTrendsHistoryPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 6:       self.SettingsJournalCurrentEventsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 7:       self.SettingsJournalChangesPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 8:       self.SettingsJournalHistoryPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 9:       self.SettingsStationSettingsEngineParametersPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 10:      self.SettingsStationSettingsSensorsSettingsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 11:      self.SettingsStationSettingsGeneralPumpsParametersPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 12:      self.SettingsStationSettingsTurnOnExtraPumpsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 13:      self.SettingsStationSettingsTurnOffExtraPumpsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 14:      self.SettingsStationSettingsOptionsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 15:      self.SettingsStationSettingsEmergencyModesPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 16:      self.SettingsEngineeringMenuPIDRegistrationSettingsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 17:      self.SettingsEngineeringMenuPLCPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 18:      self.SettingsEngineeringMenuBackupPageLoadJson()

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
#Первый блок кода для главной страницы приложения. Включает в себя метод для главного окна приложения и три метода для загрузки json значений в три страницы главого приложения

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #загрузка значений и иконок для основного окна
    def MainPageLoadJson(self):
        self.MainPageUpdateSvgIcon(self.main_01Mode_pushButton, self.readJson(self.test_json, '01', '0107', '01Mode'), '01Mode')

        self.MainPageUpdateSvgIcon(self.main_exit_statistic_60Pump1_icon_label, self.readJson(self.test_json, '60', '06002', '60Pump1'), '60Pump1')
        self.MainPageUpdateSvgIcon(self.main_enter_statistic_60Pump1_icon_label, self.readJson(self.test_json, '60', '06002', '60Pump1'), '60Pump1')

        self.main_exit_statistic_01DischargePressure_label.setText(                 f"{self.readJson(self.test_json, '01', '0101', '01DischargePressure')}")
        self.main_task_statistic_01Setpoint_label.setText(                          f"{self.readJson(self.test_json, '01', '0104', '01Setpoint')}")
        self.main_some_triangle_statistic_01DifferencePressure_label.setText(       f"{self.readJson(self.test_json, '01', '0102', '01DifferencePressure')}")
        self.main_frequency_statistic_01FrequencySetpoint_label.setText(            f"{self.readJson(self.test_json, '01', '0105', '01FrequencySetpoint')}")
        self.main_enter_statistic_01SuctionPressure_label.setText(                  f"{self.readJson(self.test_json, '01', '0100', '01SuctionPressure')}")

        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection1_label_1_1, self.readJson(self.test_json, '60', '06008', '60StartPumpDetection1'), '60StartPumpDetection1')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection2_label_2_1, self.readJson(self.test_json, '60', '06009', '60StartPumpDetection2'), '60StartPumpDetection2')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection3_label_3_1, self.readJson(self.test_json, '60', '06010', '60StartPumpDetection3'), '60StartPumpDetection3')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection4_label_4_1, self.readJson(self.test_json, '60', '06011', '60StartPumpDetection4'), '60StartPumpDetection4')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection5_label_5_1, self.readJson(self.test_json, '60', '06012', '60StartPumpDetection5'), '60StartPumpDetection5')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection6_label_6_1, self.readJson(self.test_json, '60', '06013', '60StartPumpDetection6'), '60StartPumpDetection6')

        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon1_label_1_2, self.readJson(self.test_json, '60', '06026', '60FCIcon1'), '60FCIcon1')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon2_label_2_2, self.readJson(self.test_json, '60', '06027', '60FCIcon2'), '60FCIcon2')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon3_label_3_2, self.readJson(self.test_json, '60', '06028', '60FCIcon3'), '60FCIcon3')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon4_label_4_2, self.readJson(self.test_json, '60', '06029', '60FCIcon4'), '60FCIcon4')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon5_label_5_2, self.readJson(self.test_json, '60', '06030', '60FCIcon5'), '60FCIcon5')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon6_label_6_2, self.readJson(self.test_json, '60', '06031', '60FCIcon6'), '60FCIcon6')

        self.MainPageUpdateSvgIcon(self.main_pipe_up_icon_60UpperPipeline_label, self.readJson(self.test_json, '60', '06001', '60UpperPipeline'), '60UpperPipeline')
        self.MainPageUpdateSvgIcon(self.main_pipe_down_icon_60LowerPipeline_label, self.readJson(self.test_json, '60', '06000', '60LowerPipeline'), '60LowerPipeline')

        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump1_label_1, self.readJson(self.test_json, '60', '06002', '60Pump1'), '60Pump1')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump2_label_2, self.readJson(self.test_json, '60', '06003', '60Pump2'), '60Pump2')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump3_label_3, self.readJson(self.test_json, '60', '06004', '60Pump3'), '60Pump3')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump4_label_4, self.readJson(self.test_json, '60', '06005', '60Pump4'), '60Pump4')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump5_label_5, self.readJson(self.test_json, '60', '06006', '60Pump5'), '60Pump5')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump6_label_6, self.readJson(self.test_json, '60', '06007', '60Pump6'), '60Pump6')

    def MainPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        if widget == self.main_01Mode_pushButton:pass
        if widget == self.main_exit_statistic_60Pump1_icon_label:pass
        if widget == self.main_enter_statistic_60Pump1_icon_label:pass

        if widget == self.main_pump_icon_60StartPumpDetection1_label_1_1:pass
        if widget == self.main_pump_icon_60StartPumpDetection2_label_2_1:pass
        if widget == self.main_pump_icon_60StartPumpDetection3_label_3_1:pass
        if widget == self.main_pump_icon_60StartPumpDetection4_label_4_1:pass
        if widget == self.main_pump_icon_60StartPumpDetection5_label_5_1:pass
        if widget == self.main_pump_icon_60StartPumpDetection6_label_6_1:pass

        if widget == self.main_pump_icon_60FCIcon1_label_1_2:pass
        if widget == self.main_pump_icon_60FCIcon2_label_2_2:pass
        if widget == self.main_pump_icon_60FCIcon3_label_3_2:pass
        if widget == self.main_pump_icon_60FCIcon4_label_4_2:pass
        if widget == self.main_pump_icon_60FCIcon5_label_5_2:pass
        if widget == self.main_pump_icon_60FCIcon6_label_6_2:pass

        if widget == self.main_pipe_up_icon_60UpperPipeline_label:pass
        if widget == self.main_pipe_down_icon_60LowerPipeline_label:pass

        if widget == self.main_pump_icon_60Pump1_label_1:pass
        if widget == self.main_pump_icon_60Pump2_label_2:pass
        if widget == self.main_pump_icon_60Pump3_label_3:pass
        if widget == self.main_pump_icon_60Pump4_label_4:pass
        if widget == self.main_pump_icon_60Pump5_label_5:pass
        if widget == self.main_pump_icon_60Pump6_label_6:pass
        if widget == self.main_pump_icon_60FCIcon6_label_6_2:pass
        if widget == self.main_pump_icon_60FCIcon6_label_6_2:pass
        if widget == self.main_pump_icon_60FCIcon6_label_6_2:pass
        if widget == self.main_pump_icon_60FCIcon6_label_6_2:pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #первая страница stackedWidget-а основного окна
    def MainGraficPageLoadJson(self):
        self.main_graphic_70Scale1_label.setText(                                   f"{self.readJson(self.test_json, '70', '07064', '70Scale1')}")
        self.main_graphic_70Scale2_label.setText(                                   f"{self.readJson(self.test_json, '70', '07065', '70Scale2')}")
        self.main_graphic_70Scale3_label.setText(                                   f"{self.readJson(self.test_json, '70', '07066', '70Scale3')}")
        self.main_graphic_70Scale4_label.setText(                                   f"{self.readJson(self.test_json, '70', '07067', '70Scale4')}")
        self.main_graphic_70Scale5_label.setText(                                   f"{self.readJson(self.test_json, '70', '07068', '70Scale5')}")
        self.main_graphic_70Scale6_label.setText(                                   f"{self.readJson(self.test_json, '70', '07069', '70Scale6')}")

    def MainGraficPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass
        # if widget == self.main_graphic_70Scale1_label:pass
        # if widget == self.main_graphic_70Scale2_label:pass
        # if widget == self.main_graphic_70Scale3_label:pass
        # if widget == self.main_graphic_70Scale4_label:pass
        # if widget == self.main_graphic_70Scale5_label:pass
        # if widget == self.main_graphic_70Scale6_label:pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #вторая страница stackedWidget-а основного окна
    def MainStatisticsPageLoadJson(self):
        self.main_statistics_03Frequency_label_1.setText(                           f"{self.readJson(self.test_json, '03', '0300', '03Frequency')}")
        self.main_statistics_03Frequency_label_2.setText(                           f"{self.readJson(self.test_json, '03', '0300', '03Frequency')}")
        self.main_statistics_03Frequency_label_3.setText(                           f"{self.readJson(self.test_json, '03', '0300', '03Frequency')}")
        self.main_statistics_03Frequency_label_4.setText(                           f"{self.readJson(self.test_json, '03', '0300', '03Frequency')}")
        self.main_statistics_03Frequency_label_5.setText(                           f"{self.readJson(self.test_json, '03', '0300', '03Frequency')}")
        self.main_statistics_03Frequency_label_6.setText(                           f"{self.readJson(self.test_json, '03', '0300', '03Frequency')}")

        self.main_statistics_03Speed_label_1.setText(                               f"{self.readJson(self.test_json, '03', '0301', '03Speed')}")
        self.main_statistics_03Speed_label_2.setText(                               f"{self.readJson(self.test_json, '03', '0301', '03Speed')}")
        self.main_statistics_03Speed_label_3.setText(                               f"{self.readJson(self.test_json, '03', '0301', '03Speed')}")
        self.main_statistics_03Speed_label_4.setText(                               f"{self.readJson(self.test_json, '03', '0301', '03Speed')}")
        self.main_statistics_03Speed_label_5.setText(                               f"{self.readJson(self.test_json, '03', '0301', '03Speed')}")
        self.main_statistics_03Speed_label_6.setText(                               f"{self.readJson(self.test_json, '03', '0301', '03Speed')}")

        self.main_statistics_03Current_label_1.setText(                             f"{self.readJson(self.test_json, '03', '0302', '03Current')}")
        self.main_statistics_03Current_label_2.setText(                             f"{self.readJson(self.test_json, '03', '0302', '03Current')}")
        self.main_statistics_03Current_label_3.setText(                             f"{self.readJson(self.test_json, '03', '0302', '03Current')}")
        self.main_statistics_03Current_label_4.setText(                             f"{self.readJson(self.test_json, '03', '0302', '03Current')}")
        self.main_statistics_03Current_label_5.setText(                             f"{self.readJson(self.test_json, '03', '0302', '03Current')}")
        self.main_statistics_03Current_label_6.setText(                             f"{self.readJson(self.test_json, '03', '0302', '03Current')}")

        self.main_statistics_03Torque_label_1.setText(                              f"{self.readJson(self.test_json, '03', '0303', '03Torque')}")
        self.main_statistics_03Torque_label_2.setText(                              f"{self.readJson(self.test_json, '03', '0303', '03Torque')}")
        self.main_statistics_03Torque_label_3.setText(                              f"{self.readJson(self.test_json, '03', '0303', '03Torque')}")
        self.main_statistics_03Torque_label_4.setText(                              f"{self.readJson(self.test_json, '03', '0303', '03Torque')}")
        self.main_statistics_03Torque_label_5.setText(                              f"{self.readJson(self.test_json, '03', '0303', '03Torque')}")
        self.main_statistics_03Torque_label_6.setText(                              f"{self.readJson(self.test_json, '03', '0303', '03Torque')}")

        self.main_statistics_03Power_label_1.setText(                               f"{self.readJson(self.test_json, '03', '0304', '03Power')}")
        self.main_statistics_03Power_label_2.setText(                               f"{self.readJson(self.test_json, '03', '0304', '03Power')}")
        self.main_statistics_03Power_label_3.setText(                               f"{self.readJson(self.test_json, '03', '0304', '03Power')}")
        self.main_statistics_03Power_label_4.setText(                               f"{self.readJson(self.test_json, '03', '0304', '03Power')}")
        self.main_statistics_03Power_label_5.setText(                               f"{self.readJson(self.test_json, '03', '0304', '03Power')}")
        self.main_statistics_03Power_label_6.setText(                               f"{self.readJson(self.test_json, '03', '0304', '03Power')}")

        self.main_statistics_03PowerBusVoltage_label_1.setText(                     f"{self.readJson(self.test_json, '03', '0305', '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_2.setText(                     f"{self.readJson(self.test_json, '03', '0305', '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_3.setText(                     f"{self.readJson(self.test_json, '03', '0305', '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_4.setText(                     f"{self.readJson(self.test_json, '03', '0305', '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_5.setText(                     f"{self.readJson(self.test_json, '03', '0305', '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_6.setText(                     f"{self.readJson(self.test_json, '03', '0305', '03PowerBusVoltage')}")

        self.main_statistics_03Temperature_label_1.setText(                         f"{self.readJson(self.test_json, '03', '0306', '03Temperature')}")
        self.main_statistics_03Temperature_label_2.setText(                         f"{self.readJson(self.test_json, '03', '0306', '03Temperature')}")
        self.main_statistics_03Temperature_label_3.setText(                         f"{self.readJson(self.test_json, '03', '0306', '03Temperature')}")
        self.main_statistics_03Temperature_label_4.setText(                         f"{self.readJson(self.test_json, '03', '0306', '03Temperature')}")
        self.main_statistics_03Temperature_label_5.setText(                         f"{self.readJson(self.test_json, '03', '0306', '03Temperature')}")
        self.main_statistics_03Temperature_label_6.setText(                         f"{self.readJson(self.test_json, '03', '0306', '03Temperature')}")

        self.main_statistics_03ElectricEnergyMeter_label_1.setText(                 f"{self.readJson(self.test_json, '03', '0308', '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_2.setText(                 f"{self.readJson(self.test_json, '03', '0308', '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_3.setText(                 f"{self.readJson(self.test_json, '03', '0308', '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_4.setText(                 f"{self.readJson(self.test_json, '03', '0308', '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_5.setText(                 f"{self.readJson(self.test_json, '03', '0308', '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_6.setText(                 f"{self.readJson(self.test_json, '03', '0308', '03ElectricEnergyMeter')}")

    def MainStatisticsPageUpdateSvgIcon(self, widget, json_value, json_value_name): 
        pass
        # if widget == self.main_statistics_03Frequency_label_1:pass
        # if widget == self.main_statistics_03Frequency_label_2:pass
        # if widget == self.main_statistics_03Frequency_label_3:pass
        # if widget == self.main_statistics_03Frequency_label_4:pass
        # if widget == self.main_statistics_03Frequency_label_5:pass
        # if widget == self.main_statistics_03Frequency_label_6:pass
            
        # if widget == self.main_statistics_03Speed_label_1:pass
        # if widget == self.main_statistics_03Speed_label_2:pass
        # if widget == self.main_statistics_03Speed_label_3:pass
        # if widget == self.main_statistics_03Speed_label_4:pass
        # if widget == self.main_statistics_03Speed_label_5:pass
        # if widget == self.main_statistics_03Speed_label_6:pass
            
        # if widget == self.main_statistics_03Current_label_1:pass
        # if widget == self.main_statistics_03Current_label_2:pass
        # if widget == self.main_statistics_03Current_label_3:pass
        # if widget == self.main_statistics_03Current_label_4:pass
        # if widget == self.main_statistics_03Current_label_5:pass
        # if widget == self.main_statistics_03Current_label_6:pass
            
        # if widget == self.main_statistics_03Torque_label_1:pass
        # if widget == self.main_statistics_03Torque_label_2:pass
        # if widget == self.main_statistics_03Torque_label_3:pass
        # if widget == self.main_statistics_03Torque_label_4:pass
        # if widget == self.main_statistics_03Torque_label_5:pass
        # if widget == self.main_statistics_03Torque_label_6:pass
            
        # if widget == self.main_statistics_03Power_label_1:pass
        # if widget == self.main_statistics_03Power_label_2:pass
        # if widget == self.main_statistics_03Power_label_3:pass
        # if widget == self.main_statistics_03Power_label_4:pass
        # if widget == self.main_statistics_03Power_label_5:pass
        # if widget == self.main_statistics_03Power_label_6:pass
            
        # if widget == self.main_statistics_03PowerBusVoltage_label_1:pass
        # if widget == self.main_statistics_03PowerBusVoltage_label_2:pass
        # if widget == self.main_statistics_03PowerBusVoltage_label_3:pass
        # if widget == self.main_statistics_03PowerBusVoltage_label_4:pass
        # if widget == self.main_statistics_03PowerBusVoltage_label_5:pass
        # if widget == self.main_statistics_03PowerBusVoltage_label_6:pass
            
        # if widget == self.main_statistics_03Temperature_label_1:pass
        # if widget == self.main_statistics_03Temperature_label_2:pass
        # if widget == self.main_statistics_03Temperature_label_3:pass
        # if widget == self.main_statistics_03Temperature_label_4:pass
        # if widget == self.main_statistics_03Temperature_label_5:pass
        # if widget == self.main_statistics_03Temperature_label_6:pass

        # if widget == self.main_statistics_03ElectricEnergyMeter_label_1:pass
        # if widget == self.main_statistics_03ElectricEnergyMeter_label_2:pass
        # if widget == self.main_statistics_03ElectricEnergyMeter_label_3:pass
        # if widget == self.main_statistics_03ElectricEnergyMeter_label_4:pass
        # if widget == self.main_statistics_03ElectricEnergyMeter_label_5:pass
        # if widget == self.main_statistics_03ElectricEnergyMeter_label_6:pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #третья страница stackedWidget-а основного окна
    def MainSwitchPageLoadJson(self):
        pass
    def MainSwitchPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass


###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
#Второй блок кода для страницы настроек всего приложения. Включает в себя двадцать методов для загрузки json значений в 20 страниц главого приложения

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #1 страница настроек
    def SettingsManagerPageLoadJson(self):
        pass
    def SettingsManagerPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #2 страница настроек
    def SettingsPanelSettingsPageLoadJson(self):
        pass
    def SettingsPanelSettingsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #3 страница настроек
    def SettingsContactsPageLoadJson(self):
        ################################################################################################################################################################################################################################
        #self.contacts_number_of_pumps_19QuantityPump_pushButton.clicked.connect(lambda: self.show_password_window)
        #self.contacts_current_workings_number_of_pumps_19WorkingQuantityPump_pushButton.clicked.connect(lambda: self.show_password_window)
        ################################################################################################################################################################################################################################
        self.contacts_number_of_pumps_19QuantityPump_pushButton.setText(                                   f"{self.readJson(self.test_json, '19', '01900', '19QuantityPump')}")
        self.contacts_current_workings_number_of_pumps_19WorkingQuantityPump_pushButton.setText(           f"{self.readJson(self.test_json, '19', '01901', '19WorkingQuantityPump')}")

    def SettingsContactsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #4 страница настроек
    def SettingsTrackingTrendsOnlinePageLoadJson(self):
        ################################################################################################################################################################################################################################
        # self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '07017', '70OnlineTrendsDynamicRangeTime', 60))
        # self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '07017', '70OnlineTrendsDynamicRangeTime', 180))
        # self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '07017', '70OnlineTrendsDynamicRangeTime', 600))           перенести в 
        # self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '07017', '70OnlineTrendsDynamicRangeTime', 1800))          setup, как
        #                                                                                                                                                                                                               инициализацию 
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility4_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '0701603', '70OnlineTrendsChannelVisibility4', 1))                      подключений
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility1_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '0701600', '70OnlineTrendsChannelVisibility1', 1))
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility2_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '0701601', '70OnlineTrendsChannelVisibility2', 1))
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility3_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '0701602', '70OnlineTrendsChannelVisibility3', 1))
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility5_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '0701604', '70OnlineTrendsChannelVisibility5', 1))
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility6_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70', '0701605', '70OnlineTrendsChannelVisibility6', 1))
        ################################################################################################################################################################################################################################
        self.tracking_trends_online_70Scale6_label.setText(                                   f"{self.readJson(self.test_json, '70', '07069', '70Scale6')}")
        self.tracking_trends_online_70Scale5_label.setText(                                   f"{self.readJson(self.test_json, '70', '07068', '70Scale5')}")
        self.tracking_trends_online_70Scale4_label.setText(                                   f"{self.readJson(self.test_json, '70', '07067', '70Scale4')}")
        self.tracking_trends_online_70Scale3_label.setText(                                   f"{self.readJson(self.test_json, '70', '07066', '70Scale3')}")
        self.tracking_trends_online_70Scale2_label.setText(                                   f"{self.readJson(self.test_json, '70', '07065', '70Scale2')}")
        self.tracking_trends_online_70Scale1_label.setText(                                   f"{self.readJson(self.test_json, '70', '07064', '70Scale1')}")

        self.tracking_trends_online_70OnlineTrendsObservationLine4_label.setText(             f"{self.readJson(self.test_json, '70', '07021', '70OnlineTrendsObservationLine4')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine1_label.setText(             f"{self.readJson(self.test_json, '70', '07018', '70OnlineTrendsObservationLine1')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine2_label.setText(             f"{self.readJson(self.test_json, '70', '07019', '70OnlineTrendsObservationLine2')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine3_label.setText(             f"{self.readJson(self.test_json, '70', '07020', '70OnlineTrendsObservationLine3')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine5_label.setText(             f"{self.readJson(self.test_json, '70', '07022', '70OnlineTrendsObservationLine5')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine6_label.setText(             f"{self.readJson(self.test_json, '70', '07023', '70OnlineTrendsObservationLine6')}")

    def SettingsTrackingTrendsOnlinePageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #5 страница настроек
    def SettingsTrackingPumpsDevelopmentsPageLoadJson(self):
        ################################################################################################################################################################################################################################
        # self.tracking_pumps_development_150PumpRunHours1_label.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpRunHours2_label.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpRunHours3_label.clicked.connect(lambda: self.show_password_window)                        перенести в
        # self.tracking_pumps_development_150PumpRunHours4_label.clicked.connect(lambda: self.show_password_window)                        setup, как
        # self.tracking_pumps_development_150PumpRunHours5_label.clicked.connect(lambda: self.show_password_window)                        инициализацию
        # self.tracking_pumps_development_150PumpRunHours6_label.clicked.connect(lambda: self.show_password_window)                        подключений

        # self.tracking_pumps_development_150PumpNumberOfStarts1_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpNumberOfStarts2_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpNumberOfStarts3_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpNumberOfStarts4_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpNumberOfStarts5_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpNumberOfStarts6_pushButton.clicked.connect(lambda: self.show_password_window)

        # self.tracking_pumps_development_150NumberOfStartsPerHour1_pushButton.clicked.connect(lambda: self.show_password_window)

        # self.tracking_pumps_development_150HoursSinceLastStopPump1_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150HoursSinceLastStopPump2_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150HoursSinceLastStopPump3_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150HoursSinceLastStopPump4_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150HoursSinceLastStopPump5_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150HoursSinceLastStopPump6_pushButton.clicked.connect(lambda: self.show_password_window)
        ################################################################################################################################################################################################################################
        self.tracking_pumps_development_150PumpRunHours1_label.setText(             f"{self.readJson(self.test_json, '150', '015006', '150PumpRunHours1')}")
        self.tracking_pumps_development_150PumpRunHours2_label.setText(             f"{self.readJson(self.test_json, '150', '015007', '150PumpRunHours2')}")
        self.tracking_pumps_development_150PumpRunHours3_label.setText(             f"{self.readJson(self.test_json, '150', '015008', '150PumpRunHours3')}")
        self.tracking_pumps_development_150PumpRunHours4_label.setText(             f"{self.readJson(self.test_json, '150', '015009', '150PumpRunHours4')}")
        self.tracking_pumps_development_150PumpRunHours5_label.setText(             f"{self.readJson(self.test_json, '150', '015010', '150PumpRunHours5')}")
        self.tracking_pumps_development_150PumpRunHours6_label.setText(             f"{self.readJson(self.test_json, '150', '015011', '150PumpRunHours6')}")

        self.tracking_pumps_development_150NumberOfStartsPerHour2_label.setText(             f"{self.readJson(self.test_json, '150', '015013', '150NumberOfStartsPerHour2')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour3_label.setText(             f"{self.readJson(self.test_json, '150', '015014', '150NumberOfStartsPerHour3')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour4_label.setText(             f"{self.readJson(self.test_json, '150', '015015', '150NumberOfStartsPerHour4')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour5_label.setText(             f"{self.readJson(self.test_json, '150', '015016', '150NumberOfStartsPerHour5')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour6_label.setText(             f"{self.readJson(self.test_json, '150', '015017', '150NumberOfStartsPerHour6')}")

    def SettingsTrackingPumpsDevelopmentsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass





###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #6 страница настроек
    def SettingsTrackingTrendsHistoryPageLoadJson(self):
        pass
    def SettingsTrackingTrendsHistoryPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #7 страница настроек
    def SettingsJournalCurrentEventsPageLoadJson(self):
        pass
    def SettingsJournalCurrentEventsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #8 страница настроек
    def SettingsJournalChangesPageLoadJson(self):
        pass
    def SettingsJournalChangesPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #9 страница настроек
    def SettingsJournalHistoryPageLoadJson(self):
        pass
    def SettingsJournalHistoryPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #10 страница настроек
    def SettingsStationSettingsEngineParametersPageLoadJson(self):
        pass
    def SettingsStationSettingsEngineParametersPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #11 страница настроек
    def SettingsStationSettingsSensorsSettingsPageLoadJson(self):
        pass
    def SettingsStationSettingsSensorsSettingsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #12 страница настроек
    def SettingsStationSettingsGeneralPumpsParametersPageLoadJson(self):
        pass
    def SettingsStationSettingsGeneralPumpsParametersPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #13 страница настроек
    def SettingsStationSettingsTurnOnExtraPumpsPageLoadJson(self):
        pass
    def SettingsStationSettingsTurnOnExtraPumpsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #14 страница настроек
    def SettingsStationSettingsTurnOffExtraPumpsPageLoadJson(self):
        pass
    def SettingsStationSettingsTurnOffExtraPumpsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #15 страница настроек
    def SettingsStationSettingsOptionsPageLoadJson(self):
        pass
    def SettingsStationSettingsOptionsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #16 страница настроек
    def SettingsStationSettingsEmergencyModesPageLoadJson(self):
        pass
    def SettingsStationSettingsEmergencyModesPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #17 страница настроек
    def SettingsEngineeringMenuPIDRegistrationSettingsPageLoadJson(self):
        pass
    def SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #18 страница настроек
    def SettingsEngineeringMenuPLCPageLoadJson(self):
        pass
    def SettingsEngineeringMenuPLCPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
    #19 страница настроек
    def SettingsEngineeringMenuBackupPageLoadJson(self):
        pass
    def SettingsEngineeringMenuBackupPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass


        #self.setSvgIcon(widget, json_value, json_value_name)





    # def setupSystemStationMainWindowIcons(self):
    #     if self.current_theme == 'white':
    #         pass
    #     else:
    #         pass

        
#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE
#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE
#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELET
#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE
#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE
#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE
#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE
#Данный setup svg иконок будет не актуален после реализации чтения значений с json файла и включение функции изменения svg иконок для текущей страницы, исходя из переданного json значения(то есть проверки на соответствие из списка возможных значений конкретного json значения, для определения нужной для отображения svg иконки).

    def setupSystemStationMainWindowSvgIcons(self):
        if self.current_theme == 'white':
            pass
        else:
            pass

        self.setSvgIcon(self.main_pump_icon_60StartPumpDetection1_label_1_1, 'main_pump_up_icon_label_1.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60FCIcon1_label_1_2, 'main_pump_down_icon_label_off.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60StartPumpDetection2_label_2_1, 'main_pump_up_icon_label_1.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60FCIcon2_label_2_2, 'main_pump_down_icon_label_off.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60StartPumpDetection3_label_3_1, 'main_pump_up_icon_label_1.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60FCIcon3_label_3_2, 'main_pump_down_icon_label_off.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60StartPumpDetection4_label_4_1, 'main_pump_up_icon_label_1.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60FCIcon4_label_4_2, 'main_pump_down_icon_label_off.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60StartPumpDetection5_label_5_1, 'main_pump_up_icon_label_none.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60FCIcon5_label_5_2, 'main_pump_down_icon_label_none.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60StartPumpDetection6_label_6_1, 'main_pump_up_icon_label_none.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60FCIcon6_label_6_2, 'main_pump_down_icon_label_none.svg', 0)

        self.setSvgIcon(self.main_pump_icon_60Pump1_label_1, 'main_pump_icon_label_red.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60Pump2_label_2, 'main_pump_icon_label_red.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60Pump3_label_3, 'main_pump_icon_label_red.svg', 0)
        self.setSvgIcon(self.main_pump_icon_60Pump4_label_4, 'main_pump_icon_label_red.svg', 0)
        #self.setSvgIcon(self.main_pump_icon_60Pump5_label_5, 'main_pump_icon_label_black.svg', 0)
        #self.setSvgIcon(self.main_pump_icon_60Pump6_label_6, 'main_pump_icon_label_black.svg', 0)


        self.setSvgIcon(self.main_exit_statistic_60Pump1_icon_label, 'main_exit_enter_statistic_icon_label_blue.svg', 0)
        self.setSvgIcon(self.main_enter_statistic_60Pump1_icon_label, 'main_exit_enter_statistic_icon_label_blue.svg', 0)




        self.setSvgIcon(self.main_pipe_up_icon_60UpperPipeline_label, 'main_pipe_up_icon_label_4_4.svg', 0)
        self.setSvgIcon(self.main_pipe_down_icon_60LowerPipeline_label, 'main_pipe_down_icon_label_4_4.svg', 0)


        self.setSvgIcon(self.main_graphic_70ScaleNumber_pushButton, 'main_graphic_70ScaleNumber_pushButton_blue.svg', 1)

        #self.setSvgIcon(self.main_pipe_up_icon_label, 'main_pipe_up_icon_label_1_1.svg', 0)
        #self.setSvgIcon(self.main_pipe_down_icon_label, 'main_pipe_down_icon_label_1_1.svg', 0)
        self.setSvgIcon(self.main_01Mode_pushButton, 'Stop_orange.svg', 1)
        self.setSvgIcon(self.go_to_main_graphic_page_pushButton, '2_grey.svg', 1)#
        self.setSvgIcon(self.go_to_main_statistics_page_pushButton, '1.svg', 1)#
        self.setSvgIcon(self.go_to_main_switch_page_pushButton, 'Alarm_grey.svg', 1)
        self.setSvgIcon(self.go_to_settings_main_page_icon_label, 'main.svg', 1)
        self.setSvgIcon(self.go_to_settings_manager_page_icon_label_1, 'календарь.svg', 1)
        self.setSvgIcon(self.go_to_settings_tracking_page_icon_label_1, 'monitoring.svg', 1)
        self.setSvgIcon(self.go_to_settings_journal_page_icon_label_1, 'journal.svg', 1)
        self.setSvgIcon(self.go_to_settings_station_settings_page_icon_label_1, 'одна_настройка.svg', 1)
        self.setSvgIcon(self.go_to_settings_engineering_menu_page_icon_label_1, 'гаечный_ключ.svg', 1)
        self.setSvgIcon(self.go_to_settings_panel_settings_page_icon_label_1, 'настройки панели.svg', 1)
        self.setSvgIcon(self.go_to_settings_contacts_page_icon_label_1, 'поддержка.svg', 1)


        self.setSvgIcon(self.manager_icon_label_1, 'Источник.svg', 1)
        self.setSvgIcon(self.manager_icon_label_2, 'Пользователь.svg', 1)
        self.setSvgIcon(self.manager_icon_label_3, 'календарь.svg', 1)
        self.setSvgIcon(self.manager_icon_label_4_1, 'Календарь событие.svg', 1)
        self.setSvgIcon(self.manager_icon_label_4_2, 'Календарь событие.svg', 1)
        self.setSvgIcon(self.manager_icon_label_4_3, 'Календарь событие.svg', 1)
        self.setSvgIcon(self.manager_icon_label_4_4, 'Календарь событие.svg', 1)
        self.setSvgIcon(self.manager_icon_label_5_1, 'глаз.svg', 1)
        self.setSvgIcon(self.manager_icon_label_5_2, 'глаз.svg', 1)


        self.setSvgIcon(self.go_to_settings_tracking_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.setSvgIcon(self.return_to_settings_main_buttons_icon_label, 'стрелка_влево.svg', 1)
        self.setSvgIcon(self.go_to_tracking_trends_online_page_icon_label_1, 'monitoring.svg', 1)
        self.setSvgIcon(self.go_to_tracking_trends_history_page_icon_label_1, 'monitoring.svg', 1)
        self.setSvgIcon(self.go_to_tracking_pumps_developments_page_icon_label_1, 'таймер.svg', 1)
        self.setSvgIcon(self.go_to_tracking_trends_history_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.setSvgIcon(self.return_to_settings_tracking_buttons_icon_label, 'стрелка_влево.svg', 1)


        self.setSvgIcon(self.go_to_settings_journal_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.setSvgIcon(self.return_to_settings_main_buttons_icon_label_2, 'стрелка_влево.svg', 1)
        self.setSvgIcon(self.go_to_journal_current_events_page_icon_label_1, 'monitoring.svg', 1)
        self.setSvgIcon(self.go_to_journal_history_page_icon_label_1, 'monitoring.svg', 1)
        self.setSvgIcon(self.go_to_journal_changes_page_icon_label_1, 'таймер.svg', 1)
        self.setSvgIcon(self.go_to_journal_history_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.setSvgIcon(self.return_to_settings_journal_buttons_icon_label, 'стрелка_влево.svg', 1)


        self.setSvgIcon(self.go_to_settings_station_settings_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.setSvgIcon(self.return_to_settings_main_buttons_icon_label_3, 'стрелка_влево.svg', 1)
        self.setSvgIcon(self.go_to_station_settings_engine_parameters_page_icon_label_1, 'параметры_двигателей.svg', 1)
        self.setSvgIcon(self.go_to_station_settings_sensors_settings_page_icon_label_1, '360.svg', 1)
        self.setSvgIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_1, '360.svg', 1)
        self.setSvgIcon(self.go_to_station_settings_options_page_icon_label_1, 'опции.svg', 1)
        self.setSvgIcon(self.go_to_station_settings_emergency_modes_page_icon_label_1, 'Warning.svg', 1)

        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_1, 'Напряжение.svg', 1)
        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_2, 'ток.svg', 1)
        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_3, 'частота.svg', 1)
        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_4, 'скорость.svg', 1)
        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_5, 'мощность.svg', 1)
        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_6, 'время_ускорения.svg', 1)
        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_7, 'Время тормажения.svg', 1)
        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_8, 'Стрелка в лево.svg', 1)
        self.setSvgIcon(self.station_settings_engine_parameters_icon_label_9, 'Стрелка в право.svg', 1)

        self.setSvgIcon(self.station_settings_sensors_settings_icon_label_1, 'всасывание.svg', 1)
        self.setSvgIcon(self.station_settings_sensors_settings_icon_label_2, 'нагнетание.svg', 1)
        self.setSvgIcon(self.station_settings_sensors_settings_icon_label_3_1, 'глаз.svg', 1)
        self.setSvgIcon(self.station_settings_sensors_settings_icon_label_3_2, 'глаз.svg', 1)
        self.setSvgIcon(self.station_settings_sensors_settings_icon_label_3_3, 'глаз.svg', 1)
        self.setSvgIcon(self.station_settings_sensors_settings_icon_label_3_4, 'глаз.svg', 1)

        #параметры насосов общ #параметры насосов общ #параметры насосов общ #параметры насосов общ #параметры насосов общ 
        self.setSvgIcon(self.station_settings_general_pumps_parameters_icon_label_1_1, 'частота.svg', 1)
        self.setSvgIcon(self.station_settings_general_pumps_parameters_icon_label_1_2, 'частота.svg', 1)
        self.setSvgIcon(self.station_settings_general_pumps_parameters_icon_label_2, 'ноль.svg', 1)
        self.setSvgIcon(self.station_settings_general_pumps_parameters_icon_label_3, 'ротация.svg', 1)
        self.setSvgIcon(self.station_settings_general_pumps_parameters_icon_label_4, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_general_pumps_parameters_icon_label_5, 'часы.svg', 1)

        self.setSvgIcon(self.station_settings_turn_on_extra_pumps_icon_label_1_1, 'частота.svg', 1)
        self.setSvgIcon(self.station_settings_turn_on_extra_pumps_icon_label_2, 'галочка.svg', 1)
        self.setSvgIcon(self.station_settings_turn_on_extra_pumps_icon_label_3_1, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_turn_on_extra_pumps_icon_label_4, 'Warning.svg', 1)
        self.setSvgIcon(self.station_settings_turn_on_extra_pumps_icon_label_3_2, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_turn_on_extra_pumps_icon_label_3_3, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_turn_on_extra_pumps_icon_label_1_2, 'частота.svg', 1)
        self.setSvgIcon(self.station_settings_turn_on_extra_pumps_icon_label_5, 'часы.svg', 1)

        self.setSvgIcon(self.station_settings_turn_off_extra_pumps_icon_label_1_1, 'частота.svg', 1)
        self.setSvgIcon(self.station_settings_turn_off_extra_pumps_icon_label_2, 'галочка.svg', 1)
        self.setSvgIcon(self.station_settings_turn_off_extra_pumps_icon_label_3_1, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_turn_off_extra_pumps_icon_label_4, 'Warning.svg', 1)
        self.setSvgIcon(self.station_settings_turn_off_extra_pumps_icon_label_3_2, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_turn_off_extra_pumps_icon_label_3_3, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_turn_off_extra_pumps_icon_label_1_2, 'частота.svg', 1)
        self.setSvgIcon(self.station_settings_turn_off_extra_pumps_icon_label_5, 'часы.svg', 1)

        self.setSvgIcon(self.station_settings_options_icon_label_1, 'энергосбережение.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_2, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_3, 'просадка_давления_для_выключения_энерго_сбер.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_4, 'повышать_давление_на.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_5, 'Период.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_6_1, 'Размах.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_6_2, 'Размах.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_7_1, 'глаз.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_7_2, 'глаз.svg', 1)
        self.setSvgIcon(self.station_settings_options_icon_label_7_3, 'глаз.svg', 1)

        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_1, 'частотсрабатывания.svg', 1)
        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_2, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_3, 'максимальное_аварии.svg', 1)
        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_4, 'Warning.svg', 1)
        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_5, 'Alarm.svg', 1)
        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_6, 'интервал.svg', 1)
        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_7, 'Stop.svg', 1)
        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_8, 'стоп_при_крит_давл.svg', 1)
        self.setSvgIcon(self.station_settings_emergency_modes_icon_label_9, 'контроль_разрыва.svg', 1)


        self.setSvgIcon(self.go_to_settings_station_settings_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.setSvgIcon(self.return_to_settings_main_buttons_icon_label_4, 'стрелка_влево.svg', 1)
        self.setSvgIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_1, 'settings.svg', 1)

        self.setSvgIcon(self.engineering_menu_pid_registration_settings_icon_label_1, 'пропорциональный_кеф.svg', 1)
        self.setSvgIcon(self.engineering_menu_pid_registration_settings_icon_label_2, 'интегральный_кеф.svg', 1)
        self.setSvgIcon(self.engineering_menu_pid_registration_settings_icon_label_3, 'диффиерец_кеф.svg', 1)
        self.setSvgIcon(self.engineering_menu_pid_registration_settings_icon_label_4, 'Интегрирование.svg', 1)
        self.setSvgIcon(self.engineering_menu_pid_registration_settings_icon_label_5, 'Источник.svg', 1)
        self.setSvgIcon(self.engineering_menu_pid_registration_settings_icon_label_6, 'Напряжение.svg', 1)
        self.setSvgIcon(self.engineering_menu_pid_registration_settings_icon_label_7, 'глаз.svg', 1)

        #self.setSvgIcon(self.engineering_menu_pid_registration_settings_icon_label_8, '1.svg', 1) плюсик с палками сюды
        self.setSvgIcon(self.engineering_menu_plc_up_plc_icon_label, 'plc_up.svg', 1)
        self.setSvgIcon(self.engineering_menu_plc_down_plc_icon_label, 'plc_down.svg', 1)


        self.setSvgIcon(self.engineering_menu_backup_icon_label_1, 'journal.svg', 1)
        self.setSvgIcon(self.engineering_menu_backup_icon_label_2, 'Чип.svg', 1)
        self.setSvgIcon(self.engineering_menu_backup_icon_label_3, 'monitoring.svg', 1)
        self.setSvgIcon(self.engineering_menu_backup_icon_label_4, 'сброс.svg', 1)


        self.setSvgIcon(self.go_to_settings_engineering_menu_page_icon_label_2, 'стрелка_вправо.svg', 1)

        self.setSvgIcon(self.panel_settings_icon_label_1, 'Яркость.svg', 1)
        self.setSvgIcon(self.panel_settings_icon_label_2, 'main.svg', 1)
        self.setSvgIcon(self.panel_settings_icon_label_3, 'Audio.svg', 1)
        self.setSvgIcon(self.panel_settings_icon_label_4, 'Календарь.svg', 1)
        self.setSvgIcon(self.panel_settings_icon_label_5, 'часы.svg', 1)
        self.setSvgIcon(self.panel_settings_icon_label_6, 'ip.svg', 1)
        self.setSvgIcon(self.panel_settings_icon_label_7, 'Маска.svg', 1)
        self.setSvgIcon(self.panel_settings_icon_label_8, 'шлюз.svg', 1)


        self.setSvgIcon(self.contacts_icon_label_1_1, 'help.svg', 1)
        self.setSvgIcon(self.contacts_icon_label_1_2, 'help.svg', 1)
        self.setSvgIcon(self.contacts_icon_label_2, 'календарь.svg', 1)
        self.setSvgIcon(self.contacts_icon_label_3, 'Ключ.svg', 1)
        self.setSvgIcon(self.contacts_icon_label_4, 'Насос.svg', 1)
        self.setSvgIcon(self.contacts_icon_label_5, 'Email.svg', 1)
        self.setSvgIcon(self.contacts_icon_label_6, 'Web.svg', 1)
        self.setSvgIcon(self.contacts_icon_label_7, 'Телефон.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
#Блок кода основной логики программы. Включает различные укомплектованные методы работы приложения. Методы являются системными(формально) и составляют основу работы приложения.



    def changeCurrentPageButtonIcon(self, button, svg_name, homelander):
        self.setSvgIcon(button, svg_name, homelander)

    def setSvgIcon(self, widget, svg_filename, set_widget_size):
        svg_path = os.path.join(self.svg_icons_dir, svg_filename)

        svg_renderer = QSvgRenderer(svg_path)
        
        # Получаем размер оригинального SVG
        original_size = svg_renderer.defaultSize()

        # Создаем QPixmap и отрисовываем SVG на нем
        if set_widget_size:
            svg_image = QPixmap(widget.width(), widget.height())
        else:
            svg_image = QPixmap(original_size.width(), original_size.height())

        svg_image.fill(Qt.transparent)

        painter = QPainter(svg_image)
        svg_renderer.render(painter)
        painter.end()

        if isinstance(widget, QPushButton):
            widget.setIcon(QIcon(svg_image))
            widget.setIconSize(svg_image.size())
        elif isinstance(widget, QLabel):
            widget.setPixmap(svg_image)
        #widget.setText('')

    def giveTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeChanger)
        self.timer.timeout.connect(self.updateCurrentJsonStatistics)
        self.timer.start(1000)

    def timeChanger(self):
        current_time = QDateTime.currentDateTime().toString('dd/MM/yy hh:mm')
        self.main_time_label.setText(current_time)
        self.settings_time_label.setText(current_time)

###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################################################################################################################################

class Password_window_settings:
    def setupPasswordWindowSettings(self, parent, requiered_level, min, max):
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
        self.set_comma_pushButton.clicked.connect(lambda: self.append_text('.'))
        self.clear_all_pushButton.clicked.connect(lambda: self.text_to_aply_label.setText(''))
        self.delete_previous_pushButton.clicked.connect(lambda: self.delete_text())
        self.accept_password_window_pushButton.clicked.connect(lambda: self.set_changes())
        self.parent = parent
        self.requiered_level = requiered_level
        self.min = min
        self.max = max
        
        self.give_them_text()
        print(self.parent.user_level, self.requiered_level)


    def change_button_text(self):
        self.parent.is_password = 0
        current_text = str(self.text_to_aply_label.text())
        if float(current_text) >= float(self.min) and float(current_text) <= float(self.max):
            self.parent.current_button.setText(f"{self.parent.text_to_change}{current_text}")
            self.close()



    def give_them_text(self):
        if not self.parent.is_password and self.parent.user_level >= self.requiered_level:
            self.text_to_aply_label.setText('')
            self.password_text_label.setText(f"min: {self.min}   max: {self.max}")
        else:
            self.password_text_label.setText("Введите пароль")

    def set_changes(self):
        current_text = str(self.text_to_aply_label.text())
        if self.parent.is_password:
            with open('users.json', 'r') as f:
                passwords = json.load(f)
                
            for user, details in passwords.items():
                if details["password"] == current_text:
                    role = details["role"]
                    level = int(details["level"])
                    print(f"Role for password '{current_text}' found: {role}, {level}")
                    if int(level) >= self.requiered_level:
                        self.parent.is_password = 0
                        self.parent.user_level = level
                    print(self.parent.user_level, self.requiered_level)
            self.give_them_text()

        else:
            self.parent.is_password = 1
            self.change_button_text()
            



    def append_text(self, text):
        current_text = str(self.text_to_aply_label.text())
        if text == '.':
            if current_text == '' or "." in current_text:
                text = ''

        new_text = str(current_text + str(text))
        if self.parent.is_password == 0:
            if float(new_text) >= self.min and float(new_text) <= self.max:
                self.text_to_aply_label.setText(new_text)
            else: 
                new_text[:-1]
        else:
            self.text_to_aply_label.setText(new_text)
    
    
    def delete_text(self):
        current_text = str(self.text_to_aply_label.text())
        new_text = str(current_text[:-1])
        self.text_to_aply_label.setText(new_text)