from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtCore import Qt, QTimer, QTime, QDateTime
from PySide6.QtSvg import QSvgRenderer
import json
import os


class System_Station_Main_window_settings:
    def setupSystemStationMainSettings(self):
        #ключевые атрибуты взаимодействия с приложением, включая как интерфейс, так и логику
        self.current_level = 0
        self.security_levels = [0, 1, 2, 3, 4, 5, 6]
        self.test_json = 'test.json'

        #атрибуты для работы с видом
        self.svg_icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SVGICONS")
        self.current_theme = 'black'

###################################################################################################################################################################################################################################################################################################################################################
#Блок кода, отвечающий за подключение всех возможных кнопок, связанных со страницами кнопок и страницами основной работы с оборудованием
        #переключение между основным окном(страницей) и основными настройками, дополнительно, переключение между страницами в основном окне
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(1))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_main_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_settings_main_page_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(0))
        self.go_to_settings_main_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_graphic_page_pushButton, 'go_to_main_graphic_page_pushButton_white.svg', 1))
        self.go_to_settings_main_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_statistics_page_pushButton, 'go_to_main_statistics_page_pushButton_grey.svg', 1))
        self.go_to_settings_main_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_switch_page_pushButton, 'go_to_main_switch_page_pushButton_grey.svg', 1))

        self.go_to_main_graphic_page_pushButton.clicked.connect(lambda: self.main_main_pages_stackedWidget.setCurrentIndex(0))
        self.go_to_main_graphic_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_graphic_page_pushButton, 'go_to_main_graphic_page_pushButton_white.svg', 1))
        self.go_to_main_graphic_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_statistics_page_pushButton, 'go_to_main_statistics_page_pushButton_grey.svg', 1))
        self.go_to_main_graphic_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_switch_page_pushButton, 'go_to_main_switch_page_pushButton_grey.svg', 1))

        self.go_to_main_statistics_page_pushButton.clicked.connect(lambda: self.main_main_pages_stackedWidget.setCurrentIndex(1))
        self.go_to_main_statistics_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_statistics_page_pushButton, 'go_to_main_statistics_page_pushButton_white.svg', 1))
        self.go_to_main_statistics_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_graphic_page_pushButton, 'go_to_main_graphic_page_pushButton_grey.svg', 1))
        self.go_to_main_statistics_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_switch_page_pushButton, 'go_to_main_switch_page_pushButton_grey.svg', 1))

        self.go_to_main_switch_page_pushButton.clicked.connect(lambda: self.main_main_pages_stackedWidget.setCurrentIndex(2))
        self.go_to_main_switch_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_switch_page_pushButton, 'go_to_main_switch_page_pushButton_white.svg', 1))
        self.go_to_main_switch_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_graphic_page_pushButton, 'go_to_main_graphic_page_pushButton_grey.svg', 1))
        self.go_to_main_switch_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_main_statistics_page_pushButton, 'go_to_main_statistics_page_pushButton_grey.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #три подключения к кнопкам основной страницы кнопок, и переключение, при нажатии на них, страниц справа
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))
        
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(2))
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #Блок подключений различного мониторинга, включая подключения возврата на предыдущие страницы справа и страницы кнопок

        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))
        
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.settings_time_label.setVisible(True))

        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_tracking_trends_online_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_tracking_pumps_developments_page_icon_label_2, 'empty.svg', 1))

        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_tracking_trends_online_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_tracking_pumps_developments_page_icon_label_2, 'empty.svg', 1))

        self.go_to_tracking_pumps_developments_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(4))
        self.go_to_tracking_pumps_developments_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_tracking_pumps_developments_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_tracking_pumps_developments_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_tracking_trends_online_page_icon_label_2, 'empty.svg', 1))

        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(5))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(2))


        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.settings_time_label.setVisible(False))


        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_tracking_trends_online_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_tracking_pumps_developments_page_icon_label_2, 'empty.svg', 1))
 
###################################################################################################################################################################################################################################################################################################################################################
        #Блок подключений журнала, так же как и выше включая подключения возврата на предыдущие страницы справа и страницы кнопок
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(3))

        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(3))
        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_journal_current_events_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_journal_changes_page_icon_label_2, 'empty.svg', 1))

        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_journal_current_events_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.go_to_journal_current_events_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_journal_current_events_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_journal_current_events_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_journal_changes_page_icon_label_2, 'empty.svg', 1))

        self.go_to_journal_changes_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(7))
        self.go_to_journal_changes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_journal_changes_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_journal_changes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_journal_current_events_page_icon_label_2, 'empty.svg', 1))

        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(8))
        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(4))


        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(3))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_journal_current_events_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_journal_changes_page_icon_label_2, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #Так как настройки станции не имеют вложенных страниц с кнопками из за чего есть три блока: 1) сам переход в настройки станции 2) возврат 3) отображение страниц настроек станции
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(5))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))

        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(10))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(11))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(12))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(13))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(14))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(15))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #последние подключения к вкладке инженерного меню, так же с возвратом к основным кнопкам и странице
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(16))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(6))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_plc_page_icon_label_2, 'empty.svg', 1))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_backup_page_icon_label_2, 'empty.svg', 1))

        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_2, 'указатель влево.svg', 1))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_2, 'empty.svg', 1))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_2, 'empty.svg', 1))

        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(16))
        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_plc_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_backup_page_icon_label_2, 'empty.svg', 1))

        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(17))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(17))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_plc_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_backup_page_icon_label_2, 'empty.svg', 1))


        #дубликат существующего подключения с переходом на соответствующую страницу кнопок(доступ из другого места к тем страницам, к которым уже есть доступ из другого места)
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(5))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_2, 'empty.svg', 1))
        #############################################################################################################################

        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(18))
        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_backup_page_icon_label_2, 'указатель влево.svg', 1))
        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_plc_page_icon_label_2, 'empty.svg', 1))

        #дубликат двух существующих подключений (доступ из другого места к тем страницам, к которым уже есть доступ из другого места)
        self.go_to_engineering_panel_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.go_to_engineering_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_backup_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_panel_settings_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_plc_page_icon_label_2, 'empty.svg', 1))

        self.go_to_engineering_contacts_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(2))
        self.go_to_engineering_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_backup_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_2, 'empty.svg', 1))
        self.go_to_engineering_contacts_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.go_to_engineering_plc_page_icon_label_2, 'empty.svg', 1))
        #############################################################################################################################

###################################################################################################################################################################################################################################################################################################################################################
#блок кода контроля и отслеживания СТРАНИЦ ДЛЯ НАСТРОЙКИ И КОНТРОЛЯ ОБОРУДОВАНИЯ, отвечает за визуальное подтверждения действий путем изменения svg иконок кнопок, лейблов и т.д. исходя из нажатой кнопки навигации по приложению, включая будущие навигации по графикам и в лейблах отображения json значений
        #Подключение изменения иконок кнопок страниц работы с оборудованием через кнопки в страницах кнопки(сделаны подключения здесь, так как они относится к изменению иконок в странице оборудования, хоть подключения идут из кнопок, находящихся в страницах кнопок)
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'указатель верх.svg', 1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))

        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'указатель верх.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))

        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'указатель верх.svg', 1))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))

        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_12_hours_icon_label, 'указатель верх.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #Подключение кнопок в странице трендов
        self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_30_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_1_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_3_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_online_set_10_minutes_icon_label, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #Подключение кнопок в странице онлайн трендов, находящейся в странице трендов(формально, по структуре доступ выглядит именно так)
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_1_hour_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_1_hour_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_3_hours_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_3_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_6_hours_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_12_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_6_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_12_hours_icon_label, 'указатель верх.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_10_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_30_minutes_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_1_hour_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_3_hours_icon_label, 'empty.svg', 1))
        self.tracking_trends_history_set_12_hours_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.tracking_trends_history_set_6_hours_icon_label, 'empty.svg', 1))

###################################################################################################################################################################################################################################################################################################################################################
        #Подключение кнопок в вложенной странице истории журнала, находящейся в странице журнала(формально, по структуре доступ выглядит именно так)
        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_all_60NumberDisplayAlarm_icon_label, 'указатель верх.svg', 1))
        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_emergencies_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_warnings_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_messages_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_user_events_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_all_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_all_60NumberDisplayAlarm_icon_label, 'указатель верх.svg', 1))
        self.journal_history_set_all_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_emergencies_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_all_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_warnings_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_all_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_messages_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_all_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_user_events_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_emergencies_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_emergencies_60NumberDisplayAlarm_icon_label, 'указатель верх.svg', 1))
        self.journal_history_set_emergencies_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_all_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_emergencies_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_warnings_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_emergencies_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_messages_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_emergencies_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_user_events_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_warnings_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_warnings_60NumberDisplayAlarm_icon_label, 'указатель верх.svg', 1))
        self.journal_history_set_warnings_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_all_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_warnings_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_emergencies_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_warnings_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_messages_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_warnings_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_user_events_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_messages_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_messages_60NumberDisplayAlarm_icon_label, 'указатель верх.svg', 1))
        self.journal_history_set_messages_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_all_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_messages_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_emergencies_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_messages_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_warnings_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_messages_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_user_events_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_user_events_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_user_events_60NumberDisplayAlarm_icon_label, 'указатель верх.svg', 1))
        self.journal_history_set_user_events_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_all_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_user_events_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_emergencies_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_user_events_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_warnings_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))
        self.journal_history_set_user_events_60NumberDisplayAlarm_pushButton.clicked.connect(lambda: self.changeCurrentPageWidgetIcon(self.journal_history_set_messages_60NumberDisplayAlarm_icon_label, 'empty.svg', 1))



###################################################################################################################################################################################################################################################################################################################################################
#Данный блок кода сфокусирован на подключение всех возможных кнопок, связанных с паролями и уровнями доступа, к окну, отвечающему за изменение доступа и за изменение атрибутов
        #Планировщик
        self.manager_user_setpoint_10SetpointUser_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointUser', 0.00, 99.99))

        self.manager_monday_10TypeOfDayMonday_pushButton.clicked.connect(lambda: self.SettingsManagerPageInstantlyUpdateJson(self.security_levels[3], '10TypeOfDayMonday'))
        self.manager_tuesday_10TypeOfDayTuesday_pushButton.clicked.connect(lambda: self.SettingsManagerPageInstantlyUpdateJson(self.security_levels[3], '10TypeOfDayTuesday'))
        self.manager_wednesday_10TypeOfDayWednesday_pushButton.clicked.connect(lambda: self.SettingsManagerPageInstantlyUpdateJson(self.security_levels[3], '10TypeOfDayWednesday'))
        self.manager_thursday_10TypeOfDayThursday_pushButton.clicked.connect(lambda: self.SettingsManagerPageInstantlyUpdateJson(self.security_levels[3], '10TypeOfDayThursday'))
        self.manager_friday_10TypeOfDayFriday_pushButton.clicked.connect(lambda: self.SettingsManagerPageInstantlyUpdateJson(self.security_levels[3], '10TypeOfDayFriday'))
        self.manager_saturday_10TypeOfDaySaturday_pushButton.clicked.connect(lambda: self.SettingsManagerPageInstantlyUpdateJson(self.security_levels[3], '10TypeOfDaySaturday'))
        self.manager_sunday_10TypeOfDaySunday_pushButton.clicked.connect(lambda: self.SettingsManagerPageInstantlyUpdateJson(self.security_levels[3], '10TypeOfDaySunday'))

        self.manager_morning_1_1_10WeekdayMorningHour_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekdayMorningHour', 0, 23))
        self.manager_morning_1_2_10WeekdayMorningMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekdayMorningMinutes', 0, 59))
        self.manager_morning_2_1_10WeekendMorningHour_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekendMorningHour', 0, 23))
        self.manager_morning_2_2_10WeekendMorningMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekendMorningMinutes', 0, 59))
        self.manager_morning_3_10SetpointWeekdaysMorning_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointWeekdaysMorning', 0.00, 99.99))
        self.manager_morning_4_10SetpointWeekendsMorning_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointWeekendsMorning', 0.00, 99.99))

        self.manager_day_1_1_10WeekdayDayHour_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekdayDayHour', 0, 23))
        self.manager_day_1_2_10WeekdayDayMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekdayDayMinutes', 0, 59))
        self.manager_day_2_1_10DayOffMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10DayOffMinutes', 0, 23))
        self.manager_day_2_2_10DayOffMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10DayOffMinutes', 0, 59))
        self.manager_day_3_10SetpointWeekdaysDay_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointWeekdaysDay', 0.00, 99.99))
        self.manager_day_4_10SetpointWeekendsDay_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointWeekendsDay', 0.00, 99.99))

        self.manager_evening_1_1_10WeekdayEveningHour_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekdayEveningHour', 0, 23))
        self.manager_evening_1_2_10WeekdayEveningMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekdayEveningMinutes', 0, 59))
        self.manager_evening_2_1_10WeekendEveningHour_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekendEveningHour', 0, 23))
        self.manager_evening_2_2_10WeekendEveningMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekendEveningMinutes', 0, 59))
        self.manager_evening_3_10SetpointWeekdaysEvening_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointWeekdaysEvening', 0.00, 99.99))
        self.manager_evening_4_10SetpointWeekendsEvening_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointWeekendsEvening', 0.00, 99.99))

        self.manager_night_1_1_10WeekdayNightHour_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekdayNightHour', 0, 23))
        self.manager_night_1_2_10WeekdayNightMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekdayNightMinutes', 0, 59))
        self.manager_night_2_1_10WeekendNightHour_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekendNightHour', 0, 23))
        self.manager_night_2_2_10WeekendNightMinutes_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10WeekendNightMinutes', 0, 59))
        self.manager_night_3_10SetpointWeekdaysNights_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointWeekdaysNights', 0.00, 99.99))
        self.manager_night_4_10SetpointWeekendsNights_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '10SetpointWeekendsNights', 0.00, 99.99))

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
        self.contacts_number_of_pumps_19QuantityPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[0], '19QuantityPump', 100000, 10000000))
        self.contacts_current_workings_number_of_pumps_19WorkingQuantityPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[0], '19WorkingQuantityPump', 100000, 10000000))

###################################################################################################################################################################################################################################################################################################################################################
        #Параметры двигателей                  (внутри настроек станции)
        self.station_settings_engine_parameters_voltage_18MotorVoltage_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_engine_parameters_amperage_18MotorCurrent_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_engine_parameters_frequency_18MotorFrequency_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_engine_parameters_speed_18MotorSpeed_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_engine_parameters_power_18MotorPower_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_engine_parameters_acceleration_time_18AccelerationTime_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_engine_parameters_slow_down_time_18DecelerationTime_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

        self.station_settings_engine_parameters_read_settings_pushButton.clicked.connect(self.show_password_window)                        #переименовать атрибут
        self.station_settings_engine_parameters_write_settings_pushButton.clicked.connect(self.show_password_window)                       #переименовать атрибут

###################################################################################################################################################################################################################################################################################################################################################
        #Настройки датчиков                    (внутри настроек станции)
        self.station_settings_sensors_settings_milliamps_at_suction_16RangeSuctionSensor_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_sensors_settings_milliamps_at_discharge_16RangeDischargeSensor_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

###################################################################################################################################################################################################################################################################################################################################################
        #Общие параметры насосов               (внутри настроек станции)
        self.station_settings_general_pumps_parameters_minimal_operating_frequency_11MinimumFrequency_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_general_pumps_parameters_maximal_operating_frequency_11MaximumFrequency_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.station_settings_general_pumps_parameters_start_using_master_from_0_Hz_11ZeroStartMaster_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000)) бит проблема
        # self.station_settings_general_pumps_parameters_use_pump_rotation_11ChangeEnable_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000)) бит проблема
        self.station_settings_general_pumps_parameters_pump_rotation_interval_11WizardChangeInterval_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_general_pumps_parameters_pump_rotation_time_of_day_11ChangeHour_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

###################################################################################################################################################################################################################################################################################################################################################
        #Включение дополнительных насосов      (внутри настроек станции)
        self.station_settings_turn_on_extra_pumps_master_frequency_on_extra_pump_start_12FrequencyToTurnOnTheAuxiliaryPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_on_extra_pumps_acceptable_drawdown_12PermissiblePressureDrop_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_on_extra_pumps_delay_for_critical_drawdown_12DelayWithAllowablePressureDrop_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_on_extra_pumps_critical_drawdown_12CriticalPressureDrop_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_on_extra_pumps_delay_for_acceptable_drawdown_12DelayCriticalPressureDrop_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_on_extra_pumps_delay_for_leaving_to_fixed_frequency_12DelayFixedFrequencyStartPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_on_extra_pumps_fixed_frequency_12FixedFrequencyStartingPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_on_extra_pumps_operating_time_at_fixed_frequency_12FixedFrequencyTimeStartPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

###################################################################################################################################################################################################################################################################################################################################################
        #Выключение дополнительных насосов     (внутри настроек станции)
        self.station_settings_turn_off_extra_pumps_master_frequency_on_extra_pump_shutdown_13FrequencyToTurnOffTheAuxiliaryPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_off_extra_pumps_acceptable_jump_13PermissibleOverpressure_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_off_extra_pumps_delay_for_critical_jump_13DelayPermissibleOverpressure_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_off_extra_pumps_critical_jump_13CriticalOverpressure_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_off_extra_pumps_delay_for_acceptable_jump_13DelayCriticalOverpressure_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_off_extra_pumps_delay_for_leaving_to_fixed_frequency_13DelayFixedFrequencyStopPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_off_extra_pumps_fixed_frequency_13FixedFrequencyPumpStop_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_turn_off_extra_pumps_operating_time_at_fixed_frequency_13FixedFrequencyTimeStopPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

###################################################################################################################################################################################################################################################################################################################################################
        #Опции                                 (внутри настроек станции)
        self.station_settings_options_energy_saving_mode_15PowerSavingModeOn_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_options_start_energy_saving_mode_once_every_15PowerSavingModeTime_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_options_presure_drawdown_to_turn_off_energy_saving_mode_15PowerSavingModeExitPresure_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_options_increase_pressure_by_15PowerSavingModePressureIncrease_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_options_swing_integration_time_15PowerSavingModeIntegrationTime_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_options_acceptable_pressure_swing_15PowerSavingAllowablePressureSwing_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_options_acceptable_frequency_swing_15PowerSavingPermissibleFrequencySpan_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

###################################################################################################################################################################################################################################################################################################################################################
        #Аварийные режимы                      (внутри настроек станции)
        self.station_settings_emergency_modes_differential_operating_frequency_14PumpStartConfirmationFrequency_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_emergency_modes_differential_failure_delay_14PumpStartConfirmationAlarmDelay_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_emergency_modes_differential_maximum_number_of_failures_14MaxAlarmConfirmationStartPump_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_emergency_modes_dry_warnings_pushButton.clicked.connect(self.show_password_window)                                                            #переименовать атрибут
        self.station_settings_emergency_modes_dry_failure_pushButton.clicked.connect(self.show_password_window)                                                             #переименовать атрибут
        self.station_settings_emergency_modes_dry_failure_delay_pushButton.clicked.connect(self.show_password_window)                                                       #переименовать атрибут
        self.station_settings_emergency_modes_shutdown_delay_pushButton.clicked.connect(self.show_password_window)                                                          #переименовать атрибут
        self.station_settings_emergency_modes_critical_pressure_to_shutdown_14CriticalPressureAlarmThreshold_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.station_settings_emergency_modes_control_pipeline_rupture_pushButton.clicked.connect(self.show_password_window)                                                #переименовать атрибут

###################################################################################################################################################################################################################################################################################################################################################
        #Настройки пид-регистрации                             (внутри инженерного меню)
        self.engineering_menu_pid_registration_settings_proportional_coefficient_17ProportionalCoefficient_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.engineering_menu_pid_registration_settings_integral_coefficient_17IntegralCoefficient_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.engineering_menu_pid_registration_settings_differential_coefficient_17DifferentialCoefficient_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        self.engineering_menu_pid_registration_settings_constant_of_integration_17IntegrationTime_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_pid_registration_settings_ustavka_change_10SetpointModePid_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000)) бит проблема
        self.engineering_menu_pid_registration_settings_ustavka_for_change_17SetpointPID_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

###################################################################################################################################################################################################################################################################################################################################################
        #PLC                                                   (внутри инженерного меню)
        # self.engineering_menu_plc_02DigitalInput16Bit0_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit1_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit2_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit3_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit4_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit5_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit6_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit7_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit8_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit9_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit10_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalInput16Bit11_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_09AlarmModbusPLC_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

        # self.engineering_menu_plc_02DigitalOutput16Bit0_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit1_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit2_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit3_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit4_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit5_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit6_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit7_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit8_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit9_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit10_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))
        # self.engineering_menu_plc_02DigitalOutput16Bit11_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000))

        # self.engineering_menu_plc_pushButton_26.clicked.connect(self.show_password_window)                     #переименовать атрибут
        # self.engineering_menu_plc_pushButton_27.clicked.connect(self.show_password_window)                     #переименовать атрибут
        # self.engineering_menu_plc_pushButton_28.clicked.connect(self.show_password_window)                     #переименовать атрибут
        # self.engineering_menu_plc_pushButton_29.clicked.connect(self.show_password_window)                     #переименовать атрибут
        # self.engineering_menu_plc_pushButton_30.clicked.connect(self.show_password_window)                     #переименовать атрибут

###################################################################################################################################################################################################################################################################################################################################################
        #Бекап                                                 (внутри инженерного меню)
        # self.engineering_menu_backup_save_90_days_of_journal_80LogBackup_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000)) бит проблема
        # self.engineering_menu_backup_save_energy_independent_memory_80RWBackup_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000)) бит проблема
        # self.engineering_menu_backup_save_trends_80TrendsBackup_pushButton.clicked.connect(lambda: self.choose_attribute_or_password_window(self.security_levels[3], '', 100000, 10000000)) бит проблема

        self.engineering_menu_backup_factory_all_settings_pushButton.clicked.connect(self.show_password_window) #переименовать атрибут


###################################################################################################################################################################################################################################################################################################################################################
#Методы работы с json записью значений

    def SettingsManagerPageInstantlyUpdateJson(self, requiered_level, json_key):
        if self.current_level < requiered_level:
            self.show_password_window()
        else:
            json_value = self.readJson(self.test_json, json_key)
            if json_value == 0 or json_value == 1:
                self.updateJson(self.test_json, json_key, json_value + 1)
            else:
                self.updateJson(self.test_json, json_key, 0)
            self.updateCurrentJsonStatistics()


###################################################################################################################################################################################################################################################################################################################################################
#Методы работы с json загрузкой значений, работающих по отслеживанию текущей страницы и загрузки значений только для текущей страницы пользователя, чтобы не нагружать систему лишними загрузками, которые пользователь не будет отслеживать
#Основной метод проверки текущей страницы и перенаправление на метод загрузки json значений во все необходимые виждеты страницы

    def updateCurrentJsonStatistics(self):
        main_stackedWidget = self.main_stackedWidget.currentIndex()

        if main_stackedWidget == 0:
            self.MainPageLoadJson()

            main_main_pages_stackedWidget_currentIndex = self.main_main_pages_stackedWidget.currentIndex()

            if main_main_pages_stackedWidget_currentIndex == 0: self.MainGraficPageLoadJson()
            elif main_main_pages_stackedWidget_currentIndex == 1: self.MainStatisticsPageLoadJson()
            elif main_main_pages_stackedWidget_currentIndex == 2: pass#self.MainSwitchPageLoadJson()

        elif main_stackedWidget == 1:
            settings_pages_stackedWidget_currentIndex = self.settings_pages_stackedWidget.currentIndex()

            if settings_pages_stackedWidget_currentIndex == 0:         self.SettingsManagerPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 1:       pass#self.SettingsPanelSettingsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 2:       self.SettingsContactsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 3:       self.SettingsTrackingTrendsOnlinePageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 4:       self.SettingsTrackingPumpsDevelopmentsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 5:       self.SettingsTrackingTrendsHistoryPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 6:       pass#self.SettingsJournalCurrentEventsPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 7:       pass#self.SettingsJournalChangesPageLoadJson()
            elif settings_pages_stackedWidget_currentIndex == 8:       pass#self.SettingsJournalHistoryPageLoadJson()
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
#Первый блок кода для главной страницы приложения. Включает в себя метод для главного окна приложения и три метода для загрузки json значений в три страницы главого приложения
    #загрузка значений и иконок для основного окна
    def MainPageLoadJson(self):
        self.MainPageUpdateSvgIcon(self.main_01Mode_pushButton, self.readJson(self.test_json, '01Mode'), '01Mode')

        self.MainPageUpdateSvgIcon(self.main_exit_statistic_60Pump1_icon_label, self.readJson(self.test_json, '60Pump1'), '60Pump1')
        self.MainPageUpdateSvgIcon(self.main_enter_statistic_60Pump1_icon_label, self.readJson(self.test_json, '60Pump1'), '60Pump1')

        self.main_exit_statistic_01DischargePressure_label.setText(                 f"{self.readJson(self.test_json, '01DischargePressure')}")
        self.main_task_statistic_01Setpoint_label.setText(                          f"{self.readJson(self.test_json, '01Setpoint')}")
        self.main_some_triangle_statistic_01DifferencePressure_label.setText(       f"{self.readJson(self.test_json, '01DifferencePressure')}")
        self.main_frequency_statistic_01FrequencySetpoint_label.setText(            f"{self.readJson(self.test_json, '01FrequencySetpoint')}")
        self.main_enter_statistic_01SuctionPressure_label.setText(                  f"{self.readJson(self.test_json, '01SuctionPressure')}")

        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection1_label_1_1, self.readJson(self.test_json, '60StartPumpDetection1'), '60StartPumpDetection1')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection2_label_2_1, self.readJson(self.test_json, '60StartPumpDetection2'), '60StartPumpDetection2')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection3_label_3_1, self.readJson(self.test_json, '60StartPumpDetection3'), '60StartPumpDetection3')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection4_label_4_1, self.readJson(self.test_json, '60StartPumpDetection4'), '60StartPumpDetection4')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection5_label_5_1, self.readJson(self.test_json, '60StartPumpDetection5'), '60StartPumpDetection5')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60StartPumpDetection6_label_6_1, self.readJson(self.test_json, '60StartPumpDetection6'), '60StartPumpDetection6')

        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon1_label_1_2, self.readJson(self.test_json, '60FCIcon1'), '60FCIcon1')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon2_label_2_2, self.readJson(self.test_json, '60FCIcon2'), '60FCIcon2')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon3_label_3_2, self.readJson(self.test_json, '60FCIcon3'), '60FCIcon3')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon4_label_4_2, self.readJson(self.test_json, '60FCIcon4'), '60FCIcon4')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon5_label_5_2, self.readJson(self.test_json, '60FCIcon5'), '60FCIcon5')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60FCIcon6_label_6_2, self.readJson(self.test_json, '60FCIcon6'), '60FCIcon6')

        self.MainPageUpdateSvgIcon(self.main_pipe_up_icon_60UpperPipeline_label, self.readJson(self.test_json, '60UpperPipeline'), '60UpperPipeline')
        self.MainPageUpdateSvgIcon(self.main_pipe_down_icon_60LowerPipeline_label, self.readJson(self.test_json, '60LowerPipeline'), '60LowerPipeline')

        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump1_label_1, self.readJson(self.test_json, '60Pump1'), '60Pump1')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump2_label_2, self.readJson(self.test_json, '60Pump2'), '60Pump2')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump3_label_3, self.readJson(self.test_json, '60Pump3'), '60Pump3')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump4_label_4, self.readJson(self.test_json, '60Pump4'), '60Pump4')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump5_label_5, self.readJson(self.test_json, '60Pump5'), '60Pump5')
        self.MainPageUpdateSvgIcon(self.main_pump_icon_60Pump6_label_6, self.readJson(self.test_json, '60Pump6'), '60Pump6')

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

###################################################################################################################################################################################################################################################################################################################################################
    #первая страница stackedWidget-а основного окна
    def MainGraficPageLoadJson(self):
        self.main_graphic_70Scale1_label.setText(                                   f"{self.readJson(self.test_json, '70Scale1')}")
        self.main_graphic_70Scale2_label.setText(                                   f"{self.readJson(self.test_json, '70Scale2')}")
        self.main_graphic_70Scale3_label.setText(                                   f"{self.readJson(self.test_json, '70Scale3')}")
        self.main_graphic_70Scale4_label.setText(                                   f"{self.readJson(self.test_json, '70Scale4')}")
        self.main_graphic_70Scale5_label.setText(                                   f"{self.readJson(self.test_json, '70Scale5')}")
        self.main_graphic_70Scale6_label.setText(                                   f"{self.readJson(self.test_json, '70Scale6')}")

    def MainGraficPageUpdateSvgIcon(self, widget, json_value, json_value_name):
        pass

###################################################################################################################################################################################################################################################################################################################################################
    #вторая страница stackedWidget-а основного окна
    def MainStatisticsPageLoadJson(self):
        self.main_statistics_03Frequency_label_1.setText(                           f"{self.readJson(self.test_json, '03Frequency')}")
        self.main_statistics_03Frequency_label_2.setText(                           f"{self.readJson(self.test_json, '03Frequency')}")
        self.main_statistics_03Frequency_label_3.setText(                           f"{self.readJson(self.test_json, '03Frequency')}")
        self.main_statistics_03Frequency_label_4.setText(                           f"{self.readJson(self.test_json, '03Frequency')}")
        self.main_statistics_03Frequency_label_5.setText(                           f"{self.readJson(self.test_json, '03Frequency')}")
        self.main_statistics_03Frequency_label_6.setText(                           f"{self.readJson(self.test_json, '03Frequency')}")

        self.main_statistics_03Speed_label_1.setText(                               f"{self.readJson(self.test_json, '03Speed')}")
        self.main_statistics_03Speed_label_2.setText(                               f"{self.readJson(self.test_json, '03Speed')}")
        self.main_statistics_03Speed_label_3.setText(                               f"{self.readJson(self.test_json, '03Speed')}")
        self.main_statistics_03Speed_label_4.setText(                               f"{self.readJson(self.test_json, '03Speed')}")
        self.main_statistics_03Speed_label_5.setText(                               f"{self.readJson(self.test_json, '03Speed')}")
        self.main_statistics_03Speed_label_6.setText(                               f"{self.readJson(self.test_json, '03Speed')}")

        self.main_statistics_03Current_label_1.setText(                             f"{self.readJson(self.test_json, '03Current')}")
        self.main_statistics_03Current_label_2.setText(                             f"{self.readJson(self.test_json, '03Current')}")
        self.main_statistics_03Current_label_3.setText(                             f"{self.readJson(self.test_json, '03Current')}")
        self.main_statistics_03Current_label_4.setText(                             f"{self.readJson(self.test_json, '03Current')}")
        self.main_statistics_03Current_label_5.setText(                             f"{self.readJson(self.test_json, '03Current')}")
        self.main_statistics_03Current_label_6.setText(                             f"{self.readJson(self.test_json, '03Current')}")

        self.main_statistics_03Torque_label_1.setText(                              f"{self.readJson(self.test_json, '03Torque')}")
        self.main_statistics_03Torque_label_2.setText(                              f"{self.readJson(self.test_json, '03Torque')}")
        self.main_statistics_03Torque_label_3.setText(                              f"{self.readJson(self.test_json, '03Torque')}")
        self.main_statistics_03Torque_label_4.setText(                              f"{self.readJson(self.test_json, '03Torque')}")
        self.main_statistics_03Torque_label_5.setText(                              f"{self.readJson(self.test_json, '03Torque')}")
        self.main_statistics_03Torque_label_6.setText(                              f"{self.readJson(self.test_json, '03Torque')}")

        self.main_statistics_03Power_label_1.setText(                               f"{self.readJson(self.test_json, '03Power')}")
        self.main_statistics_03Power_label_2.setText(                               f"{self.readJson(self.test_json, '03Power')}")
        self.main_statistics_03Power_label_3.setText(                               f"{self.readJson(self.test_json, '03Power')}")
        self.main_statistics_03Power_label_4.setText(                               f"{self.readJson(self.test_json, '03Power')}")
        self.main_statistics_03Power_label_5.setText(                               f"{self.readJson(self.test_json, '03Power')}")
        self.main_statistics_03Power_label_6.setText(                               f"{self.readJson(self.test_json, '03Power')}")

        self.main_statistics_03PowerBusVoltage_label_1.setText(                     f"{self.readJson(self.test_json, '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_2.setText(                     f"{self.readJson(self.test_json, '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_3.setText(                     f"{self.readJson(self.test_json, '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_4.setText(                     f"{self.readJson(self.test_json, '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_5.setText(                     f"{self.readJson(self.test_json, '03PowerBusVoltage')}")
        self.main_statistics_03PowerBusVoltage_label_6.setText(                     f"{self.readJson(self.test_json, '03PowerBusVoltage')}")

        self.main_statistics_03Temperature_label_1.setText(                         f"{self.readJson(self.test_json, '03Temperature')}")
        self.main_statistics_03Temperature_label_2.setText(                         f"{self.readJson(self.test_json, '03Temperature')}")
        self.main_statistics_03Temperature_label_3.setText(                         f"{self.readJson(self.test_json, '03Temperature')}")
        self.main_statistics_03Temperature_label_4.setText(                         f"{self.readJson(self.test_json, '03Temperature')}")
        self.main_statistics_03Temperature_label_5.setText(                         f"{self.readJson(self.test_json, '03Temperature')}")
        self.main_statistics_03Temperature_label_6.setText(                         f"{self.readJson(self.test_json, '03Temperature')}")

        self.main_statistics_03ElectricEnergyMeter_label_1.setText(                 f"{self.readJson(self.test_json, '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_2.setText(                 f"{self.readJson(self.test_json, '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_3.setText(                 f"{self.readJson(self.test_json, '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_4.setText(                 f"{self.readJson(self.test_json, '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_5.setText(                 f"{self.readJson(self.test_json, '03ElectricEnergyMeter')}")
        self.main_statistics_03ElectricEnergyMeter_label_6.setText(                 f"{self.readJson(self.test_json, '03ElectricEnergyMeter')}")

    # def MainStatisticsPageUpdateSvgIcon(self, widget, json_value, json_value_name): 
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #третья страница stackedWidget-а основного окна
    # def MainSwitchPageLoadJson(self):
    #     pass
    # def MainSwitchPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
#Второй блок кода для страницы настроек всего приложения. Включает в себя 19 методов для загрузки json значений в 20 страниц главного приложения
    #1 страница настроек
    def SettingsManagerPageLoadJson(self):

        self.SettingsManagerPageUpdateShieldSvgIcon(self.shield_1_label)
        self.manager_user_setpoint_10SetpointUser_pushButton.setText(               f"{self.readJson(self.test_json, '10SetpointUser')}")

        self.SettingsManagerPageUpdateShieldSvgIcon(self.shield_2_label)
        self.SettingsManagerPageUpdateStyles(self.manager_monday_10TypeOfDayMonday_pushButton,       self.readJson(self.test_json, '10TypeOfDayMonday'))
        self.SettingsManagerPageUpdateStyles(self.manager_tuesday_10TypeOfDayTuesday_pushButton,     self.readJson(self.test_json, '10TypeOfDayTuesday'))
        self.SettingsManagerPageUpdateStyles(self.manager_wednesday_10TypeOfDayWednesday_pushButton, self.readJson(self.test_json, '10TypeOfDayWednesday'))
        self.SettingsManagerPageUpdateStyles(self.manager_thursday_10TypeOfDayThursday_pushButton,   self.readJson(self.test_json, '10TypeOfDayThursday'))
        self.SettingsManagerPageUpdateStyles(self.manager_friday_10TypeOfDayFriday_pushButton,       self.readJson(self.test_json, '10TypeOfDayFriday'))
        self.SettingsManagerPageUpdateStyles(self.manager_saturday_10TypeOfDaySaturday_pushButton,   self.readJson(self.test_json, '10TypeOfDaySaturday'))
        self.SettingsManagerPageUpdateStyles(self.manager_sunday_10TypeOfDaySunday_pushButton,       self.readJson(self.test_json, '10TypeOfDaySunday'))

        self.SettingsManagerPageUpdateShieldSvgIcon(self.shield_3_label)
        self.manager_morning_1_1_10WeekdayMorningHour_pushButton.setText(           f"{self.readJson(self.test_json, '10WeekdayMorningHour')}")
        self.manager_morning_1_2_10WeekdayMorningMinutes_pushButton.setText(        f"{self.readJson(self.test_json, '10WeekdayMorningMinutes')}")
        self.manager_morning_2_1_10WeekendMorningHour_pushButton.setText(           f"{self.readJson(self.test_json, '10WeekendMorningHour')}")
        self.manager_morning_2_2_10WeekendMorningMinutes_pushButton.setText(        f"{self.readJson(self.test_json, '10WeekendMorningMinutes')}")
        self.manager_morning_3_10SetpointWeekdaysMorning_pushButton.setText(        f"{self.readJson(self.test_json, '10SetpointWeekdaysMorning')}")
        self.manager_morning_4_10SetpointWeekendsMorning_pushButton.setText(        f"{self.readJson(self.test_json, '10SetpointWeekendsMorning')}")

        self.SettingsManagerPageUpdateShieldSvgIcon(self.shield_4_label)
        self.manager_day_1_1_10WeekdayDayHour_pushButton.setText(                   f"{self.readJson(self.test_json, '10WeekdayDayHour')}")
        self.manager_day_1_2_10WeekdayDayMinutes_pushButton.setText(                f"{self.readJson(self.test_json, '10WeekdayDayMinutes')}")
        self.manager_day_2_1_10DayOffMinutes_pushButton.setText(                    f"{self.readJson(self.test_json, '10DayOffMinutes')}")
        self.manager_day_2_2_10DayOffMinutes_pushButton.setText(                    f"{self.readJson(self.test_json, '10DayOffMinutes')}")
        self.manager_day_3_10SetpointWeekdaysDay_pushButton.setText(                f"{self.readJson(self.test_json, '10SetpointWeekdaysDay')}")
        self.manager_day_4_10SetpointWeekendsDay_pushButton.setText(                f"{self.readJson(self.test_json, '10SetpointWeekendsDay')}")

        self.SettingsManagerPageUpdateShieldSvgIcon(self.shield_5_label)
        self.manager_evening_1_1_10WeekdayEveningHour_pushButton.setText(           f"{self.readJson(self.test_json, '10WeekdayEveningHour')}")
        self.manager_evening_1_2_10WeekdayEveningMinutes_pushButton.setText(        f"{self.readJson(self.test_json, '10WeekdayEveningMinutes')}")
        self.manager_evening_2_1_10WeekendEveningHour_pushButton.setText(           f"{self.readJson(self.test_json, '10WeekendEveningHour')}")
        self.manager_evening_2_2_10WeekendEveningMinutes_pushButton.setText(        f"{self.readJson(self.test_json, '10WeekendEveningMinutes')}")
        self.manager_evening_3_10SetpointWeekdaysEvening_pushButton.setText(        f"{self.readJson(self.test_json, '10SetpointWeekdaysEvening')}")
        self.manager_evening_4_10SetpointWeekendsEvening_pushButton.setText(        f"{self.readJson(self.test_json, '10SetpointWeekendsEvening')}")

        self.SettingsManagerPageUpdateShieldSvgIcon(self.shield_6_label)
        self.manager_night_1_1_10WeekdayNightHour_pushButton.setText(               f"{self.readJson(self.test_json, '10WeekdayNightHour')}")
        self.manager_night_1_2_10WeekdayNightMinutes_pushButton.setText(            f"{self.readJson(self.test_json, '10WeekdayNightMinutes')}")
        self.manager_night_2_1_10WeekendNightHour_pushButton.setText(               f"{self.readJson(self.test_json, '10WeekendNightHour')}")
        self.manager_night_2_2_10WeekendNightMinutes_pushButton.setText(            f"{self.readJson(self.test_json, '10WeekendNightMinutes')}")
        self.manager_night_3_10SetpointWeekdaysNights_pushButton.setText(           f"{self.readJson(self.test_json, '10SetpointWeekdaysNights')}")
        self.manager_night_4_10SetpointWeekendsNights_pushButton.setText(           f"{self.readJson(self.test_json, '10SetpointWeekendsNights')}")

        self.manager_current_day_of_the_week_01DayOfTheWeek_label.setText(          f"{self.readJson(self.test_json, '01DayOfTheWeek')}")
        self.manager_day_type_01DayType_label.setText(                              f"{self.readJson(self.test_json, '01DayType')}")

        self.manager_01SetpointType_label.setText(                                  f"{self.readJson(self.test_json, '01SetpointType')}")
        self.manager_01Setpoint_label.setText(                                      f"{self.readJson(self.test_json, '01Setpoint')}")


    def SettingsManagerPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)


    def SettingsManagerPageUpdateStyles(self, widget, json_value):
        if json_value == 0:
            widget.setStyleSheet('border: none; border-radius: none; background-color: rgb(144,144,144);')
        elif json_value == 1:
            widget.setStyleSheet('border: none; border-radius: none; background-color: rgb(0,160,227);')
        elif json_value == 2:
            widget.setStyleSheet('border: none; border-radius: none; background-color: rgb(175,37,34);')

###################################################################################################################################################################################################################################################################################################################################################
    #2 страница настроек
    # def SettingsPanelSettingsPageLoadJson(self):
    #     pass
    # def SettingsPanelSettingsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #3 страница настроек
    def SettingsContactsPageLoadJson(self):
        self.contacts_number_of_pumps_19QuantityPump_pushButton.setText(                                   f"{self.readJson(self.test_json, '19QuantityPump')}")
        self.contacts_current_workings_number_of_pumps_19WorkingQuantityPump_pushButton.setText(           f"{self.readJson(self.test_json, '19WorkingQuantityPump')}")

    # def SettingsContactsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #4 страница настроек
    def SettingsTrackingTrendsOnlinePageLoadJson(self):
        ################################################################################################################################################################################################################################
        # self.tracking_trends_online_set_1_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70OnlineTrendsDynamicRangeTime', 60))
        # self.tracking_trends_online_set_3_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70OnlineTrendsDynamicRangeTime', 180))
        # self.tracking_trends_online_set_10_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70OnlineTrendsDynamicRangeTime', 600))           перенести в 
        # self.tracking_trends_online_set_30_minutes_70OnlineTrendsDynamicRangeTime_pushButton.clicked.connect(lambda: self.updateJson(self.test_json, '70OnlineTrendsDynamicRangeTime', 1800))          setup, как
        #                                                                                                                                                                                                               инициализацию 
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility4_pushButton.clicked.connect(lambda: SettingsTrackingTrendsOnlinePageToogleJsonValue(self.readJson(self.test_json, '70OnlineTrendsObservationLine4'), '70OnlineTrendsObservationLine4'))                      подключений
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility1_pushButton.clicked.connect(lambda: SettingsTrackingTrendsOnlinePageToogleJsonValue(self.readJson(self.test_json, '70OnlineTrendsObservationLine1'), '70OnlineTrendsObservationLine1'))
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility2_pushButton.clicked.connect(lambda: SettingsTrackingTrendsOnlinePageToogleJsonValue(self.readJson(self.test_json, '70OnlineTrendsObservationLine2'), '70OnlineTrendsObservationLine2'))
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility3_pushButton.clicked.connect(lambda: SettingsTrackingTrendsOnlinePageToogleJsonValue(self.readJson(self.test_json, '70OnlineTrendsObservationLine3'), '70OnlineTrendsObservationLine3'))
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility5_pushButton.clicked.connect(lambda: SettingsTrackingTrendsOnlinePageToogleJsonValue(self.readJson(self.test_json, '70OnlineTrendsObservationLine5'), '70OnlineTrendsObservationLine5'))
        # self.tracking_trends_online_70OnlineTrendsChannelVisibility6_pushButton.clicked.connect(lambda: SettingsTrackingTrendsOnlinePageToogleJsonValue(self.readJson(self.test_json, '70OnlineTrendsObservationLine6'), '70OnlineTrendsObservationLine6'))
        ################################################################################################################################################################################################################################
    # def SettingsTrackingTrendsOnlinePageToogleJsonValue(self, json_value, json_key):
    #     if json_value == 0:
    #         self.updateJson(self.test_json, json_key, 1)
    #     else:
    #         self.updateJson(self.test_json, json_key, 0)
        self.tracking_trends_online_70Scale6_label.setText(                                   f"{self.readJson(self.test_json, '70Scale6')}")
        self.tracking_trends_online_70Scale5_label.setText(                                   f"{self.readJson(self.test_json, '70Scale5')}")
        self.tracking_trends_online_70Scale4_label.setText(                                   f"{self.readJson(self.test_json, '70Scale4')}")
        self.tracking_trends_online_70Scale3_label.setText(                                   f"{self.readJson(self.test_json, '70Scale3')}")
        self.tracking_trends_online_70Scale2_label.setText(                                   f"{self.readJson(self.test_json, '70Scale2')}")
        self.tracking_trends_online_70Scale1_label.setText(                                   f"{self.readJson(self.test_json, '70Scale1')}")

        self.tracking_trends_online_70OnlineTrendsObservationLine4_label.setText(             f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine4')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine1_label.setText(             f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine1')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine2_label.setText(             f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine2')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine3_label.setText(             f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine3')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine5_label.setText(             f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine5')}")
        self.tracking_trends_online_70OnlineTrendsObservationLine6_label.setText(             f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine6')}")

    # def SettingsTrackingTrendsOnlinePageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #5 страница настроек
    def SettingsTrackingPumpsDevelopmentsPageLoadJson(self):
        ################################################################################################################################################################################################################################
        # self.tracking_pumps_development_150PumpRunHours1_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpRunHours2_pushButton.clicked.connect(lambda: self.show_password_window)
        # self.tracking_pumps_development_150PumpRunHours3_pushButton.clicked.connect(lambda: self.show_password_window)                        перенести в
        # self.tracking_pumps_development_150PumpRunHours4_pushButton.clicked.connect(lambda: self.show_password_window)                        setup, как
        # self.tracking_pumps_development_150PumpRunHours5_pushButton.clicked.connect(lambda: self.show_password_window)                        инициализацию
        # self.tracking_pumps_development_150PumpRunHours6_pushButton.clicked.connect(lambda: self.show_password_window)                        подключений

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
        
        self.tracking_pumps_development_150PumpRunHours1_label.setText(                  f"{self.readJson(self.test_json, '150PumpRunHours1')}")
        self.tracking_pumps_development_150PumpRunHours2_label.setText(                  f"{self.readJson(self.test_json, '150PumpRunHours2')}")
        self.tracking_pumps_development_150PumpRunHours3_label.setText(                  f"{self.readJson(self.test_json, '150PumpRunHours3')}")
        self.tracking_pumps_development_150PumpRunHours4_label.setText(                  f"{self.readJson(self.test_json, '150PumpRunHours4')}")
        self.tracking_pumps_development_150PumpRunHours5_label.setText(                  f"{self.readJson(self.test_json, '150PumpRunHours5')}")
        self.tracking_pumps_development_150PumpRunHours6_label.setText(                  f"{self.readJson(self.test_json, '150PumpRunHours6')}")

        self.tracking_pumps_development_150PumpRunHours1_pushButton.setText(             f"{self.readJson(self.test_json, '150PumpRunHours1')}")
        self.tracking_pumps_development_150PumpRunHours2_pushButton.setText(             f"{self.readJson(self.test_json, '150PumpRunHours2')}")
        self.tracking_pumps_development_150PumpRunHours3_pushButton.setText(             f"{self.readJson(self.test_json, '150PumpRunHours3')}")
        self.tracking_pumps_development_150PumpRunHours4_pushButton.setText(             f"{self.readJson(self.test_json, '150PumpRunHours4')}")
        self.tracking_pumps_development_150PumpRunHours5_pushButton.setText(             f"{self.readJson(self.test_json, '150PumpRunHours5')}")
        self.tracking_pumps_development_150PumpRunHours6_pushButton.setText(             f"{self.readJson(self.test_json, '150PumpRunHours6')}")

        self.tracking_pumps_development_150PumpNumberOfStarts1_pushButton.setText(       f"{self.readJson(self.test_json, '150PumpNumberOfStarts1')}")
        self.tracking_pumps_development_150PumpNumberOfStarts2_pushButton.setText(       f"{self.readJson(self.test_json, '150PumpNumberOfStarts2')}")
        self.tracking_pumps_development_150PumpNumberOfStarts3_pushButton.setText(       f"{self.readJson(self.test_json, '150PumpNumberOfStarts3')}")
        self.tracking_pumps_development_150PumpNumberOfStarts4_pushButton.setText(       f"{self.readJson(self.test_json, '150PumpNumberOfStarts4')}")
        self.tracking_pumps_development_150PumpNumberOfStarts5_pushButton.setText(       f"{self.readJson(self.test_json, '150PumpNumberOfStarts5')}")
        self.tracking_pumps_development_150PumpNumberOfStarts6_pushButton.setText(       f"{self.readJson(self.test_json, '150PumpNumberOfStarts6')}")

        self.tracking_pumps_development_150NumberOfStartsPerHour1_pushButton.setText(    f"{self.readJson(self.test_json, '150NumberOfStartsPerHour1')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour2_label.setText(         f"{self.readJson(self.test_json, '150NumberOfStartsPerHour2')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour3_label.setText(         f"{self.readJson(self.test_json, '150NumberOfStartsPerHour3')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour4_label.setText(         f"{self.readJson(self.test_json, '150NumberOfStartsPerHour4')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour5_label.setText(         f"{self.readJson(self.test_json, '150NumberOfStartsPerHour5')}")
        self.tracking_pumps_development_150NumberOfStartsPerHour6_label.setText(         f"{self.readJson(self.test_json, '150NumberOfStartsPerHour6')}")

        self.tracking_pumps_development_150HoursSinceLastStopPump1_pushButton.setText(   f"{self.readJson(self.test_json, '150HoursSinceLastStopPump1')}")
        self.tracking_pumps_development_150HoursSinceLastStopPump2_pushButton.setText(   f"{self.readJson(self.test_json, '150HoursSinceLastStopPump2')}")
        self.tracking_pumps_development_150HoursSinceLastStopPump3_pushButton.setText(   f"{self.readJson(self.test_json, '150HoursSinceLastStopPump3')}")
        self.tracking_pumps_development_150HoursSinceLastStopPump4_pushButton.setText(   f"{self.readJson(self.test_json, '150HoursSinceLastStopPump4')}")
        self.tracking_pumps_development_150HoursSinceLastStopPump5_pushButton.setText(   f"{self.readJson(self.test_json, '150HoursSinceLastStopPump5')}")
        self.tracking_pumps_development_150HoursSinceLastStopPump6_pushButton.setText(   f"{self.readJson(self.test_json, '150HoursSinceLastStopPump6')}")

    # def SettingsTrackingPumpsDevelopmentsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #6 страница настроек
    def SettingsTrackingTrendsHistoryPageLoadJson(self):
        self.tracking_trends_history_70OnlineTrendsObservationLine4_label.setText( f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine4')}")
        self.tracking_trends_history_70OnlineTrendsObservationLine1_label.setText( f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine1')}")
        self.tracking_trends_history_70OnlineTrendsObservationLine2_label.setText( f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine2')}")
        self.tracking_trends_history_70OnlineTrendsObservationLine3_label.setText( f"{self.readJson(self.test_json, '70OnlineTrendsObservationLine3')}")

        self.tracking_trends_history_70Scale6_label.setText(                       f"{self.readJson(self.test_json, '70Scale6')}")
        self.tracking_trends_history_70Scale5_label.setText(                       f"{self.readJson(self.test_json, '70Scale5')}")
        self.tracking_trends_history_70Scale4_label.setText(                       f"{self.readJson(self.test_json, '70Scale4')}")
        self.tracking_trends_history_70Scale3_label.setText(                       f"{self.readJson(self.test_json, '70Scale3')}")
        self.tracking_trends_history_70Scale2_label.setText(                       f"{self.readJson(self.test_json, '70Scale2')}")
        self.tracking_trends_history_70Scale1_label.setText(                       f"{self.readJson(self.test_json, '70Scale1')}")

    # def SettingsTrackingTrendsHistoryPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #7 страница настроек
    # def SettingsJournalCurrentEventsPageLoadJson(self):
    #     pass
    # def SettingsJournalCurrentEventsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #8 страница настроек
    # def SettingsJournalChangesPageLoadJson(self):
    #     pass
    # def SettingsJournalChangesPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #9 страница настроек
    # def SettingsJournalHistoryPageLoadJson(self):
    #     pass
    # def SettingsJournalHistoryPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #10 страница настроек
    def SettingsStationSettingsEngineParametersPageLoadJson(self):

        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_15_label)
        self.station_settings_engine_parameters_voltage_18MotorVoltage_pushButton.setText(                f"{self.readJson(self.test_json, '18MotorVoltage')}")

        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_16_label)
        self.station_settings_engine_parameters_amperage_18MotorCurrent_pushButton.setText(               f"{self.readJson(self.test_json, '18MotorCurrent')}")

        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_17_label)
        self.station_settings_engine_parameters_frequency_18MotorFrequency_pushButton.setText(            f"{self.readJson(self.test_json, '18MotorFrequency')}")

        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_18_label)
        self.station_settings_engine_parameters_speed_18MotorSpeed_pushButton.setText(                    f"{self.readJson(self.test_json, '18MotorSpeed')}")

        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_19_label)
        self.station_settings_engine_parameters_power_18MotorPower_pushButton.setText(                    f"{self.readJson(self.test_json, '18MotorPower')}")

        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_20_label)
        self.station_settings_engine_parameters_acceleration_time_18AccelerationTime_pushButton.setText(  f"{self.readJson(self.test_json, '18AccelerationTime')}")

        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_21_label)
        self.station_settings_engine_parameters_slow_down_time_18DecelerationTime_pushButton.setText(     f"{self.readJson(self.test_json, '18DecelerationTime')}")

        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_22_label)
        self.SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self.shield_23_label)


    def SettingsStationSettingsEngineParametersPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)

    # def SettingsStationSettingsEngineParametersPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #11 страница настроек
    def SettingsStationSettingsSensorsSettingsPageLoadJson(self):

        self.SettingsStationSettingsSensorsSettingsPageUpdateShieldSvgIcon(self.shield_24_label)
        self.station_settings_sensors_settings_milliamps_at_suction_16RangeSuctionSensor_pushButton.setText(      f"{self.readJson(self.test_json, '16RangeSuctionSensor')}")

        self.SettingsStationSettingsSensorsSettingsPageUpdateShieldSvgIcon(self.shield_25_label)
        self.station_settings_sensors_settings_milliamps_at_discharge_16RangeDischargeSensor_pushButton.setText(  f"{self.readJson(self.test_json, '16RangeDischargeSensor')}")

        self.station_settings_sensors_settings_suction_sensor_rating_01SuctionPressure_label.setText(             f"{self.readJson(self.test_json, '01SuctionPressure')}")
        self.station_settings_sensors_settings_discharge_sensor_rating_01DischargePressure_label.setText(         f"{self.readJson(self.test_json, '01DischargePressure')}")
        self.station_settings_sensors_settings_milliamps_at_suction_01SuctionSensorMaValue_label.setText(         f"{self.readJson(self.test_json, '01SuctionSensorMaValue')}")
        self.station_settings_sensors_settings_milliamps_at_discharge_01DischargeSensorMaValue_label.setText(     f"{self.readJson(self.test_json, '01DischargeSensorMaValue')}")

    def SettingsStationSettingsSensorsSettingsPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)

    # def SettingsStationSettingsSensorsSettingsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #12 страница настроек
    def SettingsStationSettingsGeneralPumpsParametersPageLoadJson(self):
        self.SettingsStationSettingsGeneralPumpsParametersPageUpdateShieldSvgIcon(self.shield_26_label)
        self.station_settings_general_pumps_parameters_minimal_operating_frequency_11MinimumFrequency_pushButton.setText( f"{self.readJson(self.test_json, '11MinimumFrequency')}")

        self.SettingsStationSettingsGeneralPumpsParametersPageUpdateShieldSvgIcon(self.shield_27_label)
        self.station_settings_general_pumps_parameters_maximal_operating_frequency_11MaximumFrequency_pushButton.setText( f"{self.readJson(self.test_json, '11MaximumFrequency')}")

        self.SettingsStationSettingsGeneralPumpsParametersPageUpdateShieldSvgIcon(self.shield_28_label)
        self.station_settings_general_pumps_parameters_start_using_master_from_0_Hz_11ZeroStartMaster_pushButton.setText( f"{self.readJson(self.test_json, '11PumpOptions')}")  #бит 11ZeroStartMaster

        self.SettingsStationSettingsGeneralPumpsParametersPageUpdateShieldSvgIcon(self.shield_29_label)
        self.station_settings_general_pumps_parameters_use_pump_rotation_11ChangeEnable_pushButton.setText(               f"{self.readJson(self.test_json, '11PumpOptions')}") #бит 11ChangeEnable

        self.SettingsStationSettingsGeneralPumpsParametersPageUpdateShieldSvgIcon(self.shield_30_label)
        self.station_settings_general_pumps_parameters_pump_rotation_interval_11WizardChangeInterval_pushButton.setText(  f"{self.readJson(self.test_json, '11WizardChangeInterval')}")

        self.SettingsStationSettingsGeneralPumpsParametersPageUpdateShieldSvgIcon(self.shield_31_label)
        self.station_settings_general_pumps_parameters_pump_rotation_time_of_day_11ChangeHour_pushButton.setText(         f"{self.readJson(self.test_json, '11ChangeHour')}")

    def SettingsStationSettingsGeneralPumpsParametersPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)

    # def SettingsStationSettingsGeneralPumpsParametersPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #13 страница настроек
    def SettingsStationSettingsTurnOnExtraPumpsPageLoadJson(self):

        self.SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self.shield_32_label)
        self.station_settings_turn_on_extra_pumps_master_frequency_on_extra_pump_start_12FrequencyToTurnOnTheAuxiliaryPump_pushButton.setText( f"{self.readJson(self.test_json, '12FrequencyToTurnOnTheAuxiliaryPump')}")

        self.SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self.shield_33_label)
        self.station_settings_turn_on_extra_pumps_acceptable_drawdown_12PermissiblePressureDrop_pushButton.setText(                            f"{self.readJson(self.test_json, '12PermissiblePressureDrop')}")

        self.SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self.shield_34_label)                                                                                
        self.station_settings_turn_on_extra_pumps_delay_for_critical_drawdown_12DelayWithAllowablePressureDrop_pushButton.setText(             f"{self.readJson(self.test_json, '12DelayWithAllowablePressureDrop')}")

        self.SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self.shield_35_label)
        self.station_settings_turn_on_extra_pumps_critical_drawdown_12CriticalPressureDrop_pushButton.setText(                                 f"{self.readJson(self.test_json, '12CriticalPressureDrop')}")

        self.SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self.shield_36_label)
        self.station_settings_turn_on_extra_pumps_delay_for_acceptable_drawdown_12DelayCriticalPressureDrop_pushButton.setText(                f"{self.readJson(self.test_json, '12DelayCriticalPressureDrop')}")

        self.SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self.shield_37_label)
        self.station_settings_turn_on_extra_pumps_delay_for_leaving_to_fixed_frequency_12DelayFixedFrequencyStartPump_pushButton.setText(      f"{self.readJson(self.test_json, '12DelayFixedFrequencyStartPump')}")

        self.SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self.shield_38_label)
        self.station_settings_turn_on_extra_pumps_fixed_frequency_12FixedFrequencyStartingPump_pushButton.setText(                             f"{self.readJson(self.test_json, '12FixedFrequencyStartingPump')}")

        self.SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self.shield_39_label)
        self.station_settings_turn_on_extra_pumps_operating_time_at_fixed_frequency_12FixedFrequencyTimeStartPump_pushButton.setText(          f"{self.readJson(self.test_json, '12FixedFrequencyTimeStartPump')}")

    def SettingsStationSettingsTurnOnExtraPumpsPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)
    
    # def SettingsStationSettingsTurnOnExtraPumpsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #14 страница настроек
    def SettingsStationSettingsTurnOffExtraPumpsPageLoadJson(self):

        self.SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self.shield_40_label)
        self.station_settings_turn_off_extra_pumps_master_frequency_on_extra_pump_shutdown_13FrequencyToTurnOffTheAuxiliaryPump_pushButton.setText( f"{self.readJson(self.test_json, '13FrequencyToTurnOffTheAuxiliaryPump')}")

        self.SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self.shield_41_label)
        self.station_settings_turn_off_extra_pumps_acceptable_jump_13PermissibleOverpressure_pushButton.setText(                                    f"{self.readJson(self.test_json, '13PermissibleOverpressure')}")

        self.SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self.shield_42_label)
        self.station_settings_turn_off_extra_pumps_delay_for_critical_jump_13DelayPermissibleOverpressure_pushButton.setText(                       f"{self.readJson(self.test_json, '13DelayPermissibleOverpressure')}")

        self.SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self.shield_43_label)
        self.station_settings_turn_off_extra_pumps_critical_jump_13CriticalOverpressure_pushButton.setText(                                         f"{self.readJson(self.test_json, '13CriticalOverpressure')}")

        self.SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self.shield_44_label)
        self.station_settings_turn_off_extra_pumps_delay_for_acceptable_jump_13DelayCriticalOverpressure_pushButton.setText(                        f"{self.readJson(self.test_json, '13DelayCriticalOverpressure')}")

        self.SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self.shield_45_label)
        self.station_settings_turn_off_extra_pumps_delay_for_leaving_to_fixed_frequency_13DelayFixedFrequencyStopPump_pushButton.setText(           f"{self.readJson(self.test_json, '13DelayFixedFrequencyStopPump')}")

        self.SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self.shield_46_label)
        self.station_settings_turn_off_extra_pumps_fixed_frequency_13FixedFrequencyPumpStop_pushButton.setText(                                     f"{self.readJson(self.test_json, '13FixedFrequencyPumpStop')}")

        self.SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self.shield_47_label)
        self.station_settings_turn_off_extra_pumps_operating_time_at_fixed_frequency_13FixedFrequencyTimeStopPump_pushButton.setText(               f"{self.readJson(self.test_json, '13FixedFrequencyTimeStopPump')}")

    def SettingsStationSettingsTurnOffExtraPumpsPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)

    # def SettingsStationSettingsTurnOffExtraPumpsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #15 страница настроек
    def SettingsStationSettingsOptionsPageLoadJson(self):
        self.SettingsStationSettingsOptionsPageUpdateShieldSvgIcon(self.shield_48_label)
        self.station_settings_options_energy_saving_mode_15PowerSavingModeOn_pushButton.setText(                                       f"{self.readJson(self.test_json, '15PowerSavingModeOn')}")

        self.SettingsStationSettingsOptionsPageUpdateShieldSvgIcon(self.shield_49_label)
        self.station_settings_options_start_energy_saving_mode_once_every_15PowerSavingModeTime_pushButton.setText(                    f"{self.readJson(self.test_json, '15PowerSavingModeTime')}")

        self.SettingsStationSettingsOptionsPageUpdateShieldSvgIcon(self.shield_50_label)
        self.station_settings_options_presure_drawdown_to_turn_off_energy_saving_mode_15PowerSavingModeExitPresure_pushButton.setText( f"{self.readJson(self.test_json, '15PowerSavingModeExitPresure')}")

        self.SettingsStationSettingsOptionsPageUpdateShieldSvgIcon(self.shield_51_label)
        self.station_settings_options_increase_pressure_by_15PowerSavingModePressureIncrease_pushButton.setText(                       f"{self.readJson(self.test_json, '15PowerSavingModePressureIncrease')}")

        self.SettingsStationSettingsOptionsPageUpdateShieldSvgIcon(self.shield_52_label)
        self.station_settings_options_swing_integration_time_15PowerSavingModeIntegrationTime_pushButton.setText(                      f"{self.readJson(self.test_json, '15PowerSavingModeIntegrationTime')}")

        self.SettingsStationSettingsOptionsPageUpdateShieldSvgIcon(self.shield_53_label)
        self.station_settings_options_acceptable_pressure_swing_15PowerSavingAllowablePressureSwing_pushButton.setText(                f"{self.readJson(self.test_json, '15PowerSavingAllowablePressureSwing')}")

        self.SettingsStationSettingsOptionsPageUpdateShieldSvgIcon(self.shield_54_label)
        self.station_settings_options_acceptable_frequency_swing_15PowerSavingPermissibleFrequencySpan_pushButton.setText(             f"{self.readJson(self.test_json, '15PowerSavingPermissibleFrequencySpan')}")

        self.station_settings_options_80PowerSavingPeakToPeakPressure_label.setText(                                                   f"{self.readJson(self.test_json, '80PowerSavingPeakToPeakPressure')}")
        self.station_settings_options_80PowerSavingPeakToPeakFrequency_label.setText(                                                  f"{self.readJson(self.test_json, '80PowerSavingPeakToPeakFrequency')}")
        self.station_settings_options_80PowerSavingModeOutput_label.setText(                                                           f"{self.readJson(self.test_json, '80PowerSavingModeOutput')}")

    def SettingsStationSettingsOptionsPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)

    # def SettingsStationSettingsOptionsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #16 страница настроек
    def SettingsStationSettingsEmergencyModesPageLoadJson(self):
        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_55_label)
        self.station_settings_emergency_modes_differential_operating_frequency_14PumpStartConfirmationFrequency_pushButton.setText(       f"{self.readJson(self.test_json, '14PumpStartConfirmationFrequency')}")

        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_56_label)
        self.station_settings_emergency_modes_differential_failure_delay_14PumpStartConfirmationAlarmDelay_pushButton.setText(            f"{self.readJson(self.test_json, '14PumpStartConfirmationAlarmDelay')}")

        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_57_label)
        self.station_settings_emergency_modes_differential_maximum_number_of_failures_14MaxAlarmConfirmationStartPump_pushButton.setText( f"{self.readJson(self.test_json, '14MaxAlarmConfirmationStartPump')}")

        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_58_label)
        # self.station_settings_emergency_modes_dry_warnings_pushButton.setText(                                                            f"{self.readJson(self.test_json, '')}")

        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_59_label)
        # self.station_settings_emergency_modes_dry_failure_pushButton.setText(                                                             f"{self.readJson(self.test_json, '')}")

        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_60_label)
        # self.station_settings_emergency_modes_dry_failure_delay_pushButton.setText(                                                       f"{self.readJson(self.test_json, '')}")

        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_61_label)
        # self.station_settings_emergency_modes_shutdown_delay_pushButton.setText(                                                          f"{self.readJson(self.test_json, '')}")

        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_62_label)
        self.station_settings_emergency_modes_critical_pressure_to_shutdown_14CriticalPressureAlarmThreshold_pushButton.setText(          f"{self.readJson(self.test_json, '14CriticalPressureAlarmThreshold')}")

        self.SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self.shield_63_label)

    def SettingsStationSettingsEmergencyModesPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)

    # def SettingsStationSettingsEmergencyModesPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #17 страница настроек
    def SettingsEngineeringMenuPIDRegistrationSettingsPageLoadJson(self):
        self.SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateShieldSvgIcon(self.shield_64_label)
        self.engineering_menu_pid_registration_settings_proportional_coefficient_17ProportionalCoefficient_pushButton.setText( f"{self.readJson(self.test_json, '17ProportionalCoefficient')}")

        self.SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateShieldSvgIcon(self.shield_65_label)
        self.engineering_menu_pid_registration_settings_integral_coefficient_17IntegralCoefficient_pushButton.setText(         f"{self.readJson(self.test_json, '17IntegralCoefficient')}")

        self.SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateShieldSvgIcon(self.shield_66_label)
        self.engineering_menu_pid_registration_settings_differential_coefficient_17DifferentialCoefficient_pushButton.setText( f"{self.readJson(self.test_json, '17DifferentialCoefficient')}")

        self.SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateShieldSvgIcon(self.shield_67_label)
        self.engineering_menu_pid_registration_settings_constant_of_integration_17IntegrationTime_pushButton.setText(          f"{self.readJson(self.test_json, '17IntegrationTime')}")

        self.SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateShieldSvgIcon(self.shield_68_label)
        self.engineering_menu_pid_registration_settings_ustavka_change_10SetpointModePid_pushButton.setText(                   f"{self.readJson(self.test_json, '10SetpointMode')}") #бит 10SetpointModePid

        self.SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateShieldSvgIcon(self.shield_69_label)
        self.engineering_menu_pid_registration_settings_ustavka_for_change_17SetpointPID_pushButton.setText(                   f"{self.readJson(self.test_json, '17SetpointPID')}")

        self.engineering_meny_pid_registration_settings_01DischargePressure_label.setText(                                     f"{self.readJson(self.test_json, '01DischargePressure')}")
        self.engineering_meny_pid_registration_settings_01Setpoint_pushButton.setText(                                         f"{self.readJson(self.test_json, '01Setpoint')}")
        self.engineering_meny_pid_registration_settings_01PIDError_label.setText(                                              f"{self.readJson(self.test_json, '01PIDError')}")
        self.engineering_meny_pid_registration_settings_01PIDProportional_label.setText(                                       f"{self.readJson(self.test_json, '01PIDProportional')}")
        self.engineering_meny_pid_registration_settings_01PIDIntegral_label.setText(                                           f"{self.readJson(self.test_json, '01PIDIntegral')}")
        self.engineering_meny_pid_registration_settings_01PIDDerivative_pushButton.setText(                                    f"{self.readJson(self.test_json, '01PIDDerivative')}")
        self.engineering_meny_pid_registration_settings_01PIDOutput_label.setText(                                             f"{self.readJson(self.test_json, '01PIDOutput')}")
        self.engineering_meny_pid_registration_settings_01FrequencySetpoint_label.setText(                                     f"{self.readJson(self.test_json, '01FrequencySetpoint')}")

    def SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateShieldSvgIcon(self, widget):
        if self.current_level > 0:
            self.changeCurrentPageWidgetIcon(widget, 'empty.svg', 1)
        else:
            self.changeCurrentPageWidgetIcon(widget, 'shield.svg', 1)

    # def SettingsEngineeringMenuPIDRegistrationSettingsPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #18 страница настроек
    def SettingsEngineeringMenuPLCPageLoadJson(self):
        self.engineering_menu_plc_02ADC1_label.setText(                                     f"{self.readJson(self.test_json, '02ADC1')}")
        self.engineering_menu_plc_02ADC2_label.setText(                                     f"{self.readJson(self.test_json, '02ADC2')}")
        self.engineering_menu_plc_02ADC3_label.setText(                                     f"{self.readJson(self.test_json, '02ADC3')}")
        self.engineering_menu_plc_02ADC4_label.setText(                                     f"{self.readJson(self.test_json, '02ADC4')}")
        self.engineering_menu_plc_02ADC5_label.setText(                                     f"{self.readJson(self.test_json, '02ADC5')}")
        self.engineering_menu_plc_02DAC1_label.setText(                                     f"{self.readJson(self.test_json, '02DAC1')}")

    # def SettingsEngineeringMenuPLCPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #19 страница настроек
    def SettingsEngineeringMenuBackupPageLoadJson(self):
        self.engineering_menu_backup_save_90_days_of_journal_80LogBackup_pushButton.setText(       f"{self.readJson(self.test_json, '80LogBackup')}")
        self.engineering_menu_backup_save_energy_independent_memory_80RWBackup_pushButton.setText( f"{self.readJson(self.test_json, '80LogBackup')}") #бит 80RWBackup
        self.engineering_menu_backup_save_trends_80TrendsBackup_pushButton.setText(                f"{self.readJson(self.test_json, '80LogBackup')}") #бит 80TrendsBackup

    # def SettingsEngineeringMenuBackupPageUpdateSvgIcon(self, widget, json_value, json_value_name):
    #     pass

###################################################################################################################################################################################################################################################################################################################################################
    #инициализация постоянных svg иконок для всего приложения
    def setupSystemStationMainWindowSvgIcons(self):
        if self.current_theme == 'white':
            pass
        else:
            pass
###################################################################################################################################################################################################################################################################################################################################################
        #подключение иконок для страниц кнопок навигации по приложению
        self.changeCurrentPageWidgetIcon(self.go_to_main_graphic_page_pushButton, 'go_to_main_graphic_page_pushButton_white.svg', 1)#
        self.changeCurrentPageWidgetIcon(self.go_to_main_statistics_page_pushButton, 'go_to_main_statistics_page_pushButton_grey.svg', 1)#
        self.changeCurrentPageWidgetIcon(self.go_to_main_switch_page_pushButton, 'go_to_main_switch_page_pushButton_grey.svg', 1)
        self.changeCurrentPageWidgetIcon(self.main_01Mode_pushButton, 'Stop_orange.svg', 1)
        

        self.changeCurrentPageWidgetIcon(self.go_to_settings_main_page_icon_label, 'main.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_manager_page_icon_label_1, 'календарь.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_tracking_page_icon_label_1, 'monitoring.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_tracking_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_journal_page_icon_label_1, 'journal.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_journal_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_station_settings_page_icon_label_1, 'одна_настройка.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_station_settings_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_engineering_menu_page_icon_label_1, 'гаечный_ключ.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_engineering_menu_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_panel_settings_page_icon_label_1, 'настройки панели.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_settings_contacts_page_icon_label_1, 'поддержка.svg', 1)


        self.changeCurrentPageWidgetIcon(self.return_to_settings_main_buttons_icon_label, 'стрелка_влево.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_tracking_trends_online_page_icon_label_1, 'monitoring.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_tracking_trends_history_page_icon_label_1, 'monitoring.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_tracking_trends_history_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_tracking_pumps_developments_page_icon_label_1, 'таймер.svg', 1)


        self.changeCurrentPageWidgetIcon(self.return_to_settings_tracking_buttons_icon_label, 'стрелка_влево.svg', 1)


        self.changeCurrentPageWidgetIcon(self.return_to_settings_main_buttons_icon_label_2, 'стрелка_влево.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_journal_current_events_page_icon_label_1, 'monitoring.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_journal_history_page_icon_label_1, 'monitoring.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_journal_history_page_icon_label_2, 'стрелка_вправо.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_journal_changes_page_icon_label_1, 'таймер.svg', 1)


        self.changeCurrentPageWidgetIcon(self.return_to_settings_journal_buttons_icon_label, 'стрелка_влево.svg', 1)


        self.changeCurrentPageWidgetIcon(self.return_to_settings_main_buttons_icon_label_3, 'стрелка_влево.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_station_settings_engine_parameters_page_icon_label_1, 'параметры_двигателей.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_station_settings_sensors_settings_page_icon_label_1, '360.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_station_settings_general_pumps_parameters_page_icon_label_1, '360.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_on_extra_pumps_page_icon_label_1, 'extra+1.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_station_settings_turn_off_extra_pumps_page_icon_label_1, 'extra-1.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_station_settings_options_page_icon_label_1, 'опции.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_station_settings_emergency_modes_page_icon_label_1, 'Warning.svg', 1)


        self.changeCurrentPageWidgetIcon(self.return_to_settings_main_buttons_icon_label_4, 'стрелка_влево.svg', 1)
        self.changeCurrentPageWidgetIcon(self.go_to_engineering_pid_registration_settings_page_icon_label_1, 'settings.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################
        #подключение иконок для страниц оборудования

#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE
        #временные подключения для того, чтобы увидеть как будут размещены иконки
        # self.changeCurrentPageWidgetIcon(self.main_exit_statistic_60Pump1_icon_label, 'main_exit_enter_statistic_icon_label_blue.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_enter_statistic_60Pump1_icon_label, 'main_exit_enter_statistic_icon_label_blue.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pipe_up_icon_60UpperPipeline_label, 'main_pipe_up_icon_label_2_4.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pipe_down_icon_60LowerPipeline_label, 'main_pipe_down_icon_label_2_4.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60Pump1_label_1, 'main_pump_icon_label_blue_1.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60Pump2_label_2, 'main_pump_icon_label_blue_2.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60Pump3_label_3, 'main_pump_icon_label_blue_3.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60Pump4_label_4, 'main_pump_icon_label_blue_4.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60Pump5_label_5, 'main_pump_icon_label_grey.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60Pump6_label_6, 'main_pump_icon_label_grey.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60StartPumpDetection1_label_1_1, 'empty.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60StartPumpDetection2_label_2_1, 'main_pump_up_icon_label_1.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60StartPumpDetection3_label_3_1, 'empty.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60StartPumpDetection4_label_4_1, 'main_pump_up_icon_label_4.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60StartPumpDetection5_label_5_1, 'empty.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60StartPumpDetection6_label_6_1, 'empty.svg', 0)


        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60FCIcon1_label_1_2, 'main_pump_down_icon_label_line.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60FCIcon2_label_2_2, 'main_pump_down_icon_label_off.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60FCIcon3_label_3_2, 'main_pump_down_icon_label_line.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60FCIcon4_label_4_2, 'main_pump_down_icon_label_on.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60FCIcon5_label_5_2, 'empty.svg', 0)
        # self.changeCurrentPageWidgetIcon(self.main_pump_icon_60FCIcon6_label_6_2, 'empty.svg', 0)
    

        # self.changeCurrentPageWidgetIcon(self.main_graphic_70ScaleNumber_pushButton, 'main_graphic_70ScaleNumber_pushButton_red.svg', 1)
#DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE_DELETE

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.manager_icon_label_1, 'Источник.svg', 1)
        self.changeCurrentPageWidgetIcon(self.manager_icon_label_2, 'Пользователь.svg', 1)
        self.changeCurrentPageWidgetIcon(self.manager_icon_label_3, 'календарь.svg', 1)
        self.changeCurrentPageWidgetIcon(self.manager_icon_label_4_1, 'Календарь событие.svg', 1)
        self.changeCurrentPageWidgetIcon(self.manager_icon_label_4_2, 'Календарь событие.svg', 1)
        self.changeCurrentPageWidgetIcon(self.manager_icon_label_4_3, 'Календарь событие.svg', 1)
        self.changeCurrentPageWidgetIcon(self.manager_icon_label_4_4, 'Календарь событие.svg', 1)
        self.changeCurrentPageWidgetIcon(self.manager_icon_label_5_1, 'глаз.svg', 1)
        self.changeCurrentPageWidgetIcon(self.manager_icon_label_5_2, 'глаз.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.panel_settings_icon_label_1, 'Яркость.svg', 1)
        self.changeCurrentPageWidgetIcon(self.panel_settings_icon_label_2, 'main.svg', 1)
        self.changeCurrentPageWidgetIcon(self.panel_settings_icon_label_3, 'Audio.svg', 1)
        self.changeCurrentPageWidgetIcon(self.panel_settings_icon_label_4, 'Календарь.svg', 1)
        self.changeCurrentPageWidgetIcon(self.panel_settings_icon_label_5, 'часы.svg', 1)
        self.changeCurrentPageWidgetIcon(self.panel_settings_icon_label_6, 'ip.svg', 1)
        self.changeCurrentPageWidgetIcon(self.panel_settings_icon_label_7, 'Маска.svg', 1)
        self.changeCurrentPageWidgetIcon(self.panel_settings_icon_label_8, 'шлюз.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.contacts_icon_label_1_1, 'help.svg', 1)
        self.changeCurrentPageWidgetIcon(self.contacts_icon_label_1_2, 'help.svg', 1)
        self.changeCurrentPageWidgetIcon(self.contacts_icon_label_2, 'календарь.svg', 1)
        self.changeCurrentPageWidgetIcon(self.contacts_icon_label_3, 'Ключ.svg', 1)
        self.changeCurrentPageWidgetIcon(self.contacts_icon_label_4, 'Насос.svg', 1)
        self.changeCurrentPageWidgetIcon(self.contacts_icon_label_5, 'Email.svg', 1)
        self.changeCurrentPageWidgetIcon(self.contacts_icon_label_6, 'Web.svg', 1)
        self.changeCurrentPageWidgetIcon(self.contacts_icon_label_7, 'Телефон.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_1, 'Напряжение.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_2, 'ток.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_3, 'частота.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_4, 'скорость.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_5, 'мощность.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_6, 'время_ускорения.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_7, 'Время тормажения.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_8, 'Стрелка в лево.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_engine_parameters_icon_label_9, 'Стрелка в право.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.station_settings_sensors_settings_icon_label_1, 'всасывание.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_sensors_settings_icon_label_2, 'нагнетание.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_sensors_settings_icon_label_3_1, 'глаз.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_sensors_settings_icon_label_3_2, 'глаз.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_sensors_settings_icon_label_3_3, 'глаз.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_sensors_settings_icon_label_3_4, 'глаз.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.station_settings_general_pumps_parameters_icon_label_1_1, 'частота.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_general_pumps_parameters_icon_label_1_2, 'частота.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_general_pumps_parameters_icon_label_2, 'ноль.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_general_pumps_parameters_icon_label_3, 'ротация.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_general_pumps_parameters_icon_label_4, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_general_pumps_parameters_icon_label_5, 'часы.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.station_settings_turn_on_extra_pumps_icon_label_1_1, 'частота.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_on_extra_pumps_icon_label_2, 'галочка.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_on_extra_pumps_icon_label_3_1, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_on_extra_pumps_icon_label_4, 'Warning.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_on_extra_pumps_icon_label_3_2, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_on_extra_pumps_icon_label_3_3, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_on_extra_pumps_icon_label_1_2, 'частота.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_on_extra_pumps_icon_label_5, 'часы.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.station_settings_turn_off_extra_pumps_icon_label_1_1, 'частота.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_off_extra_pumps_icon_label_2, 'галочка.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_off_extra_pumps_icon_label_3_1, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_off_extra_pumps_icon_label_4, 'Warning.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_off_extra_pumps_icon_label_3_2, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_off_extra_pumps_icon_label_3_3, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_off_extra_pumps_icon_label_1_2, 'частота.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_turn_off_extra_pumps_icon_label_5, 'часы.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_1, 'энергосбережение.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_2, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_3, 'просадка_давления_для_выключения_энерго_сбер.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_4, 'повышать_давление_на.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_5, 'Период.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_6_1, 'Размах.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_6_2, 'Размах.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_7_1, 'глаз.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_7_2, 'глаз.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_options_icon_label_7_3, 'глаз.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_1, 'частотсрабатывания.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_2, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_3, 'максимальное_аварии.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_4, 'Warning.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_5, 'go_to_main_switch_page_pushButton_white.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_6, 'интервал.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_7, 'Stop.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_8, 'стоп_при_крит_давл.svg', 1)
        self.changeCurrentPageWidgetIcon(self.station_settings_emergency_modes_icon_label_9, 'контроль_разрыва.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.engineering_menu_pid_registration_settings_icon_label_1, 'пропорциональный_кеф.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_pid_registration_settings_icon_label_2, 'интегральный_кеф.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_pid_registration_settings_icon_label_3, 'диффиерец_кеф.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_pid_registration_settings_icon_label_4, 'Интегрирование.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_pid_registration_settings_icon_label_5, 'Источник.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_pid_registration_settings_icon_label_6, 'Напряжение.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_pid_registration_settings_icon_label_7, 'глаз.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_pid_registration_settings_icon_label_8, 'empty.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################

        self.changeCurrentPageWidgetIcon(self.engineering_menu_plc_up_plc_icon_label, 'plc_up.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_plc_down_plc_icon_label, 'plc_down.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################
        
        self.changeCurrentPageWidgetIcon(self.engineering_menu_backup_icon_label_1, 'journal.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_backup_icon_label_2, 'Чип.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_backup_icon_label_3, 'monitoring.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_backup_icon_label_4, 'сброс.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_backup_icon_label_5, 'песочные_часы.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_backup_icon_label_6, 'песочные_часы.svg', 1)
        self.changeCurrentPageWidgetIcon(self.engineering_menu_backup_icon_label_7, 'песочные_часы.svg', 1)

###################################################################################################################################################################################################################################################################################################################################################
#Блок кода основной логики программы. Включает различные укомплектованные методы работы приложения. Методы являются системными(формально) и составляют основу работы приложения.

    def changeCurrentPageWidgetIcon(self, widget, svg_filename, set_widget_size):
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
#

class Global_Keypad_settings:
    def delete_text(self):
        self.text_to_aply_label.setText(self.text_to_aply_label.text()[:-1])

    def setupGlobalKeypadSettings(self):
        self.number_0_pushButton.clicked.connect(lambda: self.append_text('0'))
        self.number_1_pushButton.clicked.connect(lambda: self.append_text('1'))
        self.number_2_pushButton.clicked.connect(lambda: self.append_text('2'))
        self.number_3_pushButton.clicked.connect(lambda: self.append_text('3'))
        self.number_4_pushButton.clicked.connect(lambda: self.append_text('4'))
        self.number_5_pushButton.clicked.connect(lambda: self.append_text('5'))
        self.number_6_pushButton.clicked.connect(lambda: self.append_text('6'))
        self.number_7_pushButton.clicked.connect(lambda: self.append_text('7'))
        self.number_8_pushButton.clicked.connect(lambda: self.append_text('8'))
        self.number_9_pushButton.clicked.connect(lambda: self.append_text('9'))
        self.delete_previous_pushButton.clicked.connect(lambda: self.delete_text())
        self.clear_all_pushButton.clicked.connect(lambda: self.text_to_aply_label.setText(''))
        self.accept_pushButton.clicked.connect(lambda: self.set_changes())

###################################################################################################################################################################################################################################################################################################################################################
#

class Password_Window_settings(Global_Keypad_settings):
    def setupPasswordWindowSettings(self, parent):
        self.setupGlobalKeypadSettings()

        self.parent = parent

    def set_changes(self):
        current_text = self.text_to_aply_label.text()

        with open('users.json', 'r') as f:
            users = json.load(f)

        for user, details in users.items():
            if details["password"] == current_text:
                self.parent.current_level = int(details["level"])
                print(self.parent.current_level)
                self.close()
        self.close()
            

    def append_text(self, text):
        current_text = self.text_to_aply_label.text()

        if len(current_text) == 6:
            return

        self.text_to_aply_label.setText(current_text + text)

###################################################################################################################################################################################################################################################################################################################################################
#

class Update_Attribute_Window_settings(Global_Keypad_settings):
    def setupUpdateAttributeWindowSettings(self, parent, json_key, min_value, max_value):
        self.setupGlobalKeypadSettings()

        if isinstance(min_value, float) and isinstance(max_value, float):
            self.is_float = 1
            self.set_comma_pushButton.clicked.connect(lambda: self.append_text('.'))
        else:
            self.is_float = 0
            self.set_comma_pushButton.setEnabled(False)

        self.parent = parent
        self.json_key = json_key
        self.min_value = min_value
        self.max_value = max_value

        self.title_text_label.setText(f"min: {self.min_value}   max: {self.max_value}")

    def set_changes(self):
        if self.text_to_aply_label.text() == '':
            self.text_to_aply_label.setText('0')
        if self.is_float:
            current_text = float(self.text_to_aply_label.text())
        else:
            current_text = int(self.text_to_aply_label.text())

        self.close()
        self.parent.updateJson(self.parent.test_json, self.json_key, current_text)
        self.parent.updateCurrentJsonStatistics()

    def append_text(self, text):
        current_text = self.text_to_aply_label.text()
        
        # ограничения на количество цифр до и после запятой
        max_value_str = str(self.max_value)
        if '.' in max_value_str:
            max_digits_before_decimal, max_digits_after_decimal = map(len, max_value_str.split('.'))
        else:
            max_digits_before_decimal = len(max_value_str)
            max_digits_after_decimal = 0

        # если текст - десятичная точка
        if text == '.' and ('.' in current_text or current_text == ''):
            return
        
        new_text = current_text + text

        # проверка количества цифр до и после запятой
        if '.' in new_text:
            before_decimal, after_decimal = new_text.split('.')
            if len(before_decimal) > max_digits_before_decimal or len(after_decimal) > max_digits_after_decimal:
                return
        else:
            if len(new_text) > max_digits_before_decimal:
                return

        # проверка, что новое значение - допустимое число
        try:
            new_value = float(new_text)
        except ValueError:
            return

        # проверка, что новое значение в диапазоне
        if new_value < self.min_value or new_value > self.max_value:
            return

        # обновляем текст, если все проверки пройдены
        self.text_to_aply_label.setText(new_text)