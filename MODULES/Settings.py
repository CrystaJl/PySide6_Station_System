class System_Station_Main_window_settings:
    def setupSystemStationMainSettings(self):
        #переключение между основным окном(страницей) и основными настройками
        self.go_to_settings_main_page_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(1))
        self.go_to_main_page_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(0))

        #три подключения к кнопкам основной страницы кнопок, и переключение, при нажатии на них, страниц справа
        self.go_to_settings_manager_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(0))
        self.go_to_settings_panel_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.go_to_settings_contacts_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(2))

        #Блок подключений различного мониторинга, включая подключения возврата на предыдущие страницы справа и страницы кнопок
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.return_to_settings_tracking_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(1))

        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.go_to_settings_tracking_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(1))

        self.go_to_tracking_trends_online_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(3))
        self.go_to_tracking_pumps_developments_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(4))

        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(5))
        self.go_to_tracking_trends_history_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(2))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.return_to_settings_main_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))

        #Блок подключений журнала, так же как и выше включая подключения возврата на предыдущие страницы справа и страницы кнопок
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.return_to_settings_journal_buttons_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(3))

        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.go_to_settings_journal_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(3))

        self.go_to_journal_current_events_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(6))
        self.go_to_journal_changes_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(7))

        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(8))
        self.go_to_journal_history_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(4))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.return_to_settings_main_buttons_pushButton_2.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))

        #Так как настройки станции не имеют вложенных страниц с кнопками из за чего есть три блока: 1) сам переход в настройки станции 2) возврат 3) отображение страниц настроек станции
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_settings_station_settings_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(5))

        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.return_to_settings_main_buttons_pushButton_3.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))

        self.go_to_station_settings_engine_parameters_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_station_settings_sensors_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(10))
        self.go_to_station_settings_general_pumps_parameters_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(11))
        self.go_to_station_settings_turn_on_extra_pumps_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(12))
        self.go_to_station_settings_turn_off_extra_pumps_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(13))
        self.go_to_station_settings_options_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(14))
        self.go_to_station_settings_emergency_modes_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(15))

        #последние подключения к вкладке инженерного меню, так же с возвратом к основным кнопкам и странице
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(16))
        self.go_to_settings_engineering_menu_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(6))

        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.return_to_settings_main_buttons_pushButton_4.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(0))

        self.go_to_engineering_pid_registration_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(16))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(17))
        self.go_to_engineering_plc_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(17))

        #дубликат двух существующих подключений (доступ из другого места к тем страницам, к которым уже есть доступ из другого места)
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(9))
        self.go_to_engineering_station_settings_page_pushButton.clicked.connect(lambda: self.settings_buttons_stackedWidget.setCurrentIndex(5))
    
        self.go_to_engineering_backup_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(18))

        #так же два дубликата
        self.go_to_engineering_panel_settings_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(1))
        self.go_to_engineering_contacts_page_pushButton.clicked.connect(lambda: self.settings_pages_stackedWidget.setCurrentIndex(2))

#Выше находится блок кода, отвечающий за подключение всех возможных кнопок, связанных со страницами кнопок и страницами основной работы с обурудованием, для полноценной работы в приложении(wow)
###################################################################################################################################################################################################
###################################################################################################################################################################################################
#Данный блок кода сфокусирован на подключение всех возможных кнопок, связанных с паролями и уровнями доступа, к окну, отвечающее за изменение доступа и за изменение атрибутов(future is comming)

        #Планировщик
        self.manager_morning_1_pushButton.clicked.connect(self.show_password_window)
        self.manager_morning_2_pushButton.clicked.connect(self.show_password_window)
        self.manager_morning_3_pushButton.clicked.connect(self.show_password_window)
        self.manager_morning_4_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_1_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_2_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_3_pushButton.clicked.connect(self.show_password_window)
        self.manager_day_4_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_1_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_2_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_3_pushButton.clicked.connect(self.show_password_window)
        self.manager_evening_4_pushButton.clicked.connect(self.show_password_window)
        self.manager_user_setpoint_pushButton.clicked.connect(self.show_password_window)
        self.manager_monday_pushButton.clicked.connect(self.show_password_window)
        self.manager_tuesday_pushButton.clicked.connect(self.show_password_window)
        self.manager_wednesday_pushButton.clicked.connect(self.show_password_window)
        self.manager_thursday_pushButton.clicked.connect(self.show_password_window)
        self.manager_friday_pushButton.clicked.connect(self.show_password_window)
        self.manager_saturday_pushButton.clicked.connect(self.show_password_window)
        self.manager_sunday_pushButton.clicked.connect(self.show_password_window)

        #Настройки панели
        self.panel_settings_display_disable_time_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_screensaver_activation_time_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_buzzer_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_date_day_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_date_month_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_date_year_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_time_hour_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_time_minutes_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_time_seconds_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_ip_1_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_ip_2_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_ip_3_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_ip_4_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_mask_1_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_mask_2_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_mask_3_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_mask_4_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_gateway_1_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_gateway_2_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_gateway_3_pushButton.clicked.connect(self.show_password_window)
        self.panel_settings_gateway_4_pushButton.clicked.connect(self.show_password_window)

        #Контакты
        self.contacts_number_of_pumps_pushButton.clicked.connect(self.show_password_window)
        self.contacts_current_workings_number_of_pumps_pushButton.clicked.connect(self.show_password_window)

        #Параметры двигателей                  (внутри настроек станции)
        self.station_settings_engine_parameters_voltage_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_amperage_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_frequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_speed_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_power_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_acceleration_time_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_slow_down_time_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_read_settings_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_engine_parameters_write_settings_pushButton.clicked.connect(self.show_password_window)

        #Настройки датчиков                    (внутри настроек станции)
        self.station_settings_sensors_settings_milliamps_at_suction_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_sensors_settings_milliamps_at_discharge_pushButton.clicked.connect(self.show_password_window)

        #Общие параметры насосов               (внутри настроек станции)
        self.station_settings_general_pumps_parameters_minimal_operating_frequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_maximal_operating_frequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_start_using_master_from_0_Hz_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_use_pump_rotation_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_pump_rotation_interval_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_general_pumps_parameters_pump_rotation_time_of_day_pushButton.clicked.connect(self.show_password_window)

        #Включение дополнительных насосов      (внутри настроек станции)
        self.station_settings_turn_on_extra_pumps_master_frequency_on_extra_pump_start_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_acceptable_drawdown_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_delay_for_critical_drawdown_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_critical_drawdown_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_delay_for_acceptable_drawdown_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_delay_for_leaving_to_fixed_frequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_fixed_frequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_on_extra_pumps_operating_time_at_fixed_frequency_pushButton.clicked.connect(self.show_password_window)

        #Выключение дополнительных насосов     (внутри настроек станции)
        self.station_settings_turn_off_extra_pumps_master_frequency_on_extra_pump_shutdown_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_acceptable_jump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_delay_for_critical_jump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_critical_jump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_delay_for_acceptable_jump_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_delay_for_leaving_to_fixed_frequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_fixed_frequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_turn_off_extra_pumps_operating_time_at_fixed_frequency_pushButton.clicked.connect(self.show_password_window)

        #Опции                                 (внутри настроек станции)
        self.station_settings_options_energy_saving_mode_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_start_energy_saving_mode_once_every_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_presure_drawdown_to_turn_off_energy_saving_mode_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_increase_pressure_by_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_swing_integration_time_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_acceptable_pressure_swing_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_options_acceptable_frequency_swing_pushButton.clicked.connect(self.show_password_window)

        #Аварийные режимы                      (внутри настроек станции)
        self.station_settings_emergency_modes_differential_operating_frequency_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_differential_failure_delay_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_differential_maximum_number_of_failures_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_dry_warnings_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_dry_failure_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_dry_failure_delay_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_shutdown_delay_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_critical_pressure_to_shutdown_pushButton.clicked.connect(self.show_password_window)
        self.station_settings_emergency_modes_control_pipeline_rupture_pushButton.clicked.connect(self.show_password_window)

        #Настройки пид-asujdaiu-регистрации                    (внутри инженерного меню)
        self.engineering_menu_pid_registration_settings_proportional_coefficient_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_integral_coefficient_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_differential_coefficient_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_constant_of_integration_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_ustavka_change_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_pid_registration_settings_ustavka_for_change_pushButton.clicked.connect(self.show_password_window)

        #Бекап                                                 (внутри инженерного меню)
        self.engineering_menu_backup_save_90_days_of_journal_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_backup_save_energy_independent_memory_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_backup_save_trends_pushButton.clicked.connect(self.show_password_window)
        self.engineering_menu_backup_factory_all_settings_pushButton.clicked.connect(self.show_password_window)

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