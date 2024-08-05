unsigned int SysMs=0
unsigned short FrequencySetpoint=0
unsigned short Setpoint=0
// Временные переменные
int TempInt=0
unsigned int TempUInt=0
unsigned short TempUshort=0
short TempShort=0
Bool TempBool=0
float TempFloat=0
unsigned short y=0, i=1
// наработка насосов
unsigned short HoursSinceLastStartPump[6]={0,0,0,0,0,0}, HoursSinceLastStopPump[6]={0,0,0,0,0,0},NumberOfStartsPerHour[6]={0,0,0,0,0,0}, PumpRunHours[6]={0,0,0,0,0,0}, PumpNumberOfStarts[6]={0,0,0,0,0,0}
// Для Pid
unsigned short SetpointPID=0, SoftFillingOut=0, SoftFillingOutControl=0
unsigned int SoftFillingOutTime=0, PIDIterationTime=0
float IntegrationTime=0, ProportionalCoefficient=0, IntegralCoefficient=0, DifferentialCoefficient=0
float PIDError=0, PIDErrorSum=0, PIDErrorDiff=0, PIDProportional=0, PIDIntegral=0, PIDDerivative=0, ErrorPrev=0, PIDOutput=0
// Включение/Выключение дополнительных насосов
unsigned short FrequencyToTurnOnTheAuxiliaryPump=0, PermissiblePressureDrop=0, DelayWithAllowablePressureDrop=0, CriticalPressureDrop=0, DelayCriticalPressureDrop=0, FixedFrequencyStartingPump=0, DelayFixedFrequencyStartPump=0, FixedFrequencyTimeStartPump=0
unsigned short FrequencyToTurnOffTheAuxiliaryPump=0, PermissibleOverpressure=0, DelayPermissibleOverpressure=0, CriticalOverpressure=0, DelayCriticalOverpressure=0, FixedFrequencyPumpStop=0, DelayFixedFrequencyStopPump=0, FixedFrequencyTimeStopPump=0
unsigned int AdditionalPumpsStartKritTime=0, AdditionalPumpsStartTime=0, AdditionalPumpsStopKritTime=0, AdditionalPumpsStopTime=0
unsigned short AdditionalPumpsStartsStop=0, MaximumFrequency=0, MinimumFrequency=0, PumpOptions=0
// Переменные контроллера
unsigned short DigitalInput16=0, DigitalOutput16=0
// Переменные частотников
unsigned short DigitalInputStatus1[6]={0,0,0,0,0,0}, FrequencyFC[6]={0,0,0,0,0,0}, SumFrequencyFC=0, FCRunStatus=0   	// Состояние входов ПЧ
// РПД
unsigned short PumpStarted=0, PumpStartConfirmationFrequency=0, PumpStartConfirmationAlarmDelay=0, MaxAlarmConfirmationStartPump=0
unsigned short StartPumpDetectionTrig=0, SumStartPumpDetectionAlarm[6]={0,0,0,0,0,0}
unsigned int StartPumpDetectionTimePump[6]={0,0,0,0,0,0}
unsigned short AlarmNotStartPump=0, CycleAlarmNotStartPump=0
// Датчики
unsigned short SuctionSensorMaValue=0, DischargeSensorMaValue=0
unsigned short SuctionPressure=0, DischargePressure=0
unsigned short RangeSuctionSensor=0, RangeDischargeSensor=0
unsigned short SensorsAlarm=0
short DifferencePressure=0
// Регистры modbus
unsigned short ModbusRegs[60]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0} // Временный буфер принятых данных
// Маски дискретных входов
unsigned short AutoMode = 0x1 	// DI1 Автоматический режим
unsigned short ManualMode = 0x2 	// DI2 Ручной режим
// Работающие насосы
unsigned short FConverterPoweredPumps=0, MainsPoweredPumps=0, FConverterPoweredPumpsPrev=0
// Аварии
unsigned short AlarmNasos=0
unsigned short StatusWord1=0

unsigned short Mode=0, WorkingQuantityPump=0, NumberOfRunningPumps=0, NumberOfRunningPumpsFC=0

unsigned short PowerSavingMode=0, PowerSavingModeTime=0, PowerSavingModeBit=0, PowerSavingModeSignalMaxPressure=0, PowerSavingModeSignalMinPressure=0, PowerSavingModeSignalMaxFrequency=0, PowerSavingModeSignalMinFrequency=0, PowerSavingPeakToPeakPressure=0, PowerSavingPeakToPeakFrequency=0
unsigned short PowerSavingModeIntegrationTime=0, PowerSavingAllowablePressureSwing=0, PowerSavingPermissibleFrequencySpan=0, PowerSavingModeOutput=0, PowerSavingModeExitPresure=0, PowerSavingModePressureIncrease=0
unsigned int PowerSavingModeAmplitudeTime=0, PowerSavingModeTimeShtamp=0

// крит
unsigned short ModeOfCriticalPressure=0, CriticalPressureAlarmThreshold=0, DelayCriticalPressureAlarm=0, MaxNumberOfAlarmCritPressure=0, CriticalPressure=0, CounterCyclicAlarmCriticalPressure=0
unsigned int CriticalPressureTime=0

// сухой ход
unsigned short DryRunningWarningPressure=0, DryRunningEmergencyPressure=0, MaxNumberEmergencyDryRunning=0, AlarmDryRunningDelay=0, DryRunning=0, CounterCyclicAlarmDryRunning=0, WarningWord1=0, AlarmWord1=0, DryPressureTracking=0
unsigned int DryRunningTime=0

	// Сортировка насосов
unsigned short PumpMaintenance=0


unsigned int UnixTime=0


Sub GetPLC()
	unsigned short ErrorModbusSum=0, AlarmModbus=0
	short Bufer[10]={0,0,0,0,0,0,0,0,0,0}
	bool ErrorModbus=0
    GetDataEx(AlarmModbus, "Local HMI", "09AlarmModbus", 1)             // Получаем слово аварий MODBUS
    GetDataEx(ErrorModbusSum, "Local HMI", "02ModbusErrorSum", 1)       // Получаем сумму ошибок
    GetDataEx(Bufer[0], "ABB_PCH", 4x, 1#0, 2) 				            // Получаем все регистры нашего контроллера
	GetError(ErrorModbus)
	if not ErrorModbus then									            // если ошибок modbus нет
        SetDataEx(Bufer[0], "Local HMI", "02DigitalInput16", 1)			// Сохраняем состояние входов
        SetDataEx(Bufer[1], "Local HMI", "02DigitalOutput16", 1)		// Сохраняем состояние выходов
        AlarmModbus = AlarmModbus & ~0x1                                // Убираем ошибуку связи с PLC
        If ErrorModbusSum >= 10 then
            ErrorModbusSum = 0
        end if
    else
        ErrorModbusSum = ErrorModbusSum + 1
		if ErrorModbusSum >= 20 then 								    // Если количество ошибок достигло 10 то окончательный отвал связи
            AlarmModbus = AlarmModbus | 0x1                             // Выставляем ошибку связи с PLC
		end if
	end if
    GetDataEx(AlarmModbus, "Local HMI", "09AlarmModbus", 1)             // Сохраняем слово аварий MODBUS
    SetDataEx(ErrorModbusSum, "Local HMI", "02ModbusErrorSum", 1)       // Сохраняем сумму ошибок
end sub

Sub GetFC()																		// Считывание регистров частотников
	unsigned short ErrorModbusSum[6]={0,0,0,0,0,0}, FCModel=0, NumberReadFC=0
	short Bufer[20]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
	bool ErrorModbusFc[10]={0,0,0,0,0,0,0,0,0,0}
	// Считываем указатель текущего чтения
	GetDataEx(FCModel, "Local HMI", "150FCModel", 1)							// Модель частотников
	FCModel = 5
	//	0 = Неизвестный ПЧ;
	//  1 = ABB ACS310;
	//  2 = ABB ACS580;
	//  3 = Danfoss FC-051;
	//  4 = ABB ACQ580;
	//  5 = Inovert ISD
	If FCModel == 1 then														// ABB ACS310
		If NumberReadFC == 0 then 												// Опрашиваем первый ПЧ
			GetDataEx(ErrorModbusSum[0], "Local HMI", "03ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
			GetDataEx(Bufer[0], "ABB_PCH", 4x, 2#4, 8) 							// получаем основную группу регистров
			GetError(ErrorModbusFc[0])											// получаем аварию
			GetDataEx(Bufer[8], "ABB_PCH", 4x, 2#32, 1)							// Считываем слово состояния ПЧ
			GetError(ErrorModbusFc[1])											// получаем аварию
		else if NumberReadFC == 1 then 											// Опрашиваем второй ПЧ
			GetDataEx(ErrorModbusSum[1], "Local HMI", "04ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 2 then 											// Опрашиваем третий частотний
			GetDataEx(ErrorModbusSum[2], "Local HMI", "05ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 3 then											// Опрашиваем четвертый частотник
			GetDataEx(ErrorModbusSum[3], "Local HMI", "06ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 4 then											// Опрашиваем пятый частотник
			GetDataEx(ErrorModbusSum[4], "Local HMI", "07ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 5 then 											// Опрашиваем шестой частотник
			GetDataEx(ErrorModbusSum[5], "Local HMI", "08ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		end if
	else if FCModel == 3 then 													//  Danfoss FC-051
		If NumberReadFC == 0 then 												// Опрашиваем первый ПЧ
			GetDataEx(ErrorModbusSum[0], "Local HMI", "03ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 1 then 											// Опрашиваем второй ПЧ
			GetDataEx(ErrorModbusSum[1], "Local HMI", "04ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 2 then 											// Опрашиваем третий частотний
			GetDataEx(ErrorModbusSum[2], "Local HMI", "05ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 3 then											// Опрашиваем четвертый частотник
			GetDataEx(ErrorModbusSum[3], "Local HMI", "06ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 4 then											// Опрашиваем пятый частотник
			GetDataEx(ErrorModbusSum[4], "Local HMI", "07ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 5 then 											// Опрашиваем шестой частотник
			GetDataEx(ErrorModbusSum[5], "Local HMI", "08ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		end if
	else if FCModel == 5 then 													// inovert ISD
		If NumberReadFC == 0 then 												// Опрашиваем первый ПЧ
			GetDataEx(ErrorModbusSum[0], "Local HMI", "03ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
			GetDataEx(Bufer[0], "ABB_PCH", 4x, 2#2, 1) 							// получаем частоту
			Bufer[1] = 0 														// АВХ1 Отсутствует
			GetError(ErrorModbusFc[0])											// получаем аварию
			GetDataEx(Bufer[2], "ABB_PCH", 4x, 2#23, 1)							// Считываем АВХ2
			Bufer[2] = Bufer[2] / 10
			GetError(ErrorModbusFc[1])											// получаем аварию
			GetDataEx(Bufer[2], "ABB_PCH", 4x, 2#21, 1)							// Считываем состояние ЦВХ
			GetError(ErrorModbusFc[2])											// получаем аварию
		else if NumberReadFC == 1 then 											// Опрашиваем второй ПЧ
			GetDataEx(ErrorModbusSum[1], "Local HMI", "04ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 2 then 											// Опрашиваем третий частотний
			GetDataEx(ErrorModbusSum[2], "Local HMI", "05ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 3 then											// Опрашиваем четвертый частотник
			GetDataEx(ErrorModbusSum[3], "Local HMI", "06ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 4 then											// Опрашиваем пятый частотник
			GetDataEx(ErrorModbusSum[4], "Local HMI", "07ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		else if NumberReadFC == 5 then 											// Опрашиваем шестой частотник
			GetDataEx(ErrorModbusSum[5], "Local HMI", "08ModbusErrorSum", 1)	// Получаем сумму ошибок MODBUS ПЧ1
		end if
	end if
	if ErrorModbusFc[0] or ErrorModbusFc[1] or ErrorModbusFc[2] then			// при налиичии аварии считывания
		//if ErrorModbusSum[NumberReadFC] >= 10 Then 							// Если количество ошибок связи больше  максимума
																				// Выставляем окончательная потеря связи
		//	FILL(Bufer[0], 0, 20) 												// Обнуляем буфер
		//End if
		ErrorModbusSum[NumberReadFC] = ErrorModbusSum[NumberReadFC] + 1
	else																		// Если аварий связи нет
		//ErrorModbusSum[NumberReadFC] = 0 										// Обнуляем счетчик аварий
	end if
	If NumberReadFC == 0 then 													// Опрашиваем первый ПЧ
		SetDataEx(ErrorModbusSum[0], "Local HMI", "03ModbusErrorSum", 1)		// Записываем сумму ошибок MODBUS ПЧ1
	else if NumberReadFC == 1 then 												// Опрашиваем второй ПЧ
		SetDataEx(ErrorModbusSum[1], "Local HMI", "04ModbusErrorSum", 1)		// Записываем сумму ошибок MODBUS ПЧ1
	else if NumberReadFC == 2 then 												// Опрашиваем третий частотний
		SetDataEx(ErrorModbusSum[2], "Local HMI", "05ModbusErrorSum", 1)		// Записываем сумму ошибок MODBUS ПЧ1
	else if NumberReadFC == 3 then												// Опрашиваем четвертый частотник
		SetDataEx(ErrorModbusSum[3], "Local HMI", "06ModbusErrorSum", 1)		// Записываем сумму ошибок MODBUS ПЧ1
	else if NumberReadFC == 4 then												// Опрашиваем пятый частотник
		SetDataEx(ErrorModbusSum[4], "Local HMI", "07ModbusErrorSum", 1)		// Записываем сумму ошибок MODBUS ПЧ1
	else if NumberReadFC == 5 then 												// Опрашиваем шестой частотник
		SetDataEx(ErrorModbusSum[5], "Local HMI", "08ModbusErrorSum", 1)		// Записываем сумму ошибок MODBUS ПЧ1
	end if
	// Если есть ошибка и счетчик максимальный то записываем нуливые значения (обнулили буфер выше)
	// если ошибки нет записываем считанные значения.
	if not (ErrorModbusFc[0] or ErrorModbusFc[1] or ErrorModbusFc[2]) or ErrorModbusSum[NumberReadFC] >= 10 then
		If FCModel == 1 then													// ABB ACS310
			GetDataEx(FCRunStatus, "Local HMI", "80FCRunStatus", 1)				// Текущие запущеные ПЧ
			If NumberReadFC == 0 then 											// Опрашиваем первый ПЧ
				SetDataEx(Bufer[0], "Local HMI", "03Frequency", 1)				// Запись частоту в HMI
				SetDataEx(Bufer[1], "Local HMI", "03AnalogInput1", 1)			// Записываем АВХ1 В HMI
				SetDataEx(Bufer[2], "Local HMI", "03AnalogInput2", 1)			// Записываем АВХ2 В HMI
				SetDataEx(Bufer[3], "Local HMI", "03DigitalInputStatus1", 1)	// Записываем ЦВХ В HMI
				SetDataEx(Bufer[8], "Local HMI", "03StatusWord1", 1)			// Записываем слово остояния в HMI
				if Bufer[8] & 0x8 then
				FCRunStatus = FCRunStatus | 0x1
				else
				FCRunStatus = FCRunStatus & ~0x1
				end if
			else if NumberReadFC == 0x1 then 									// Опрашиваем второй ПЧ
				SetDataEx(Bufer[0], "Local HMI", "04Frequency", 1)				// Запись частоту в HMI
				SetDataEx(Bufer[1], "Local HMI", "04AnalogInput1", 1)			// Записываем АВХ1 В HMI
				SetDataEx(Bufer[2], "Local HMI", "04AnalogInput2", 1)			// Записываем АВХ2 В HMI
				SetDataEx(Bufer[3], "Local HMI", "04DigitalInputStatus1", 1)	// Записываем ЦВХ В HMI
				SetDataEx(Bufer[8], "Local HMI", "04StatusWord1", 1)			// Записываем слово остояния в HMI
			else if NumberReadFC == 0x2 then 									// Опрашиваем третий частотний
				SetDataEx(Bufer[0], "Local HMI", "05Frequency", 1)				// Запись частоту в HMI
				SetDataEx(Bufer[1], "Local HMI", "05AnalogInput1", 1)			// Записываем АВХ1 В HMI
				SetDataEx(Bufer[2], "Local HMI", "05AnalogInput2", 1)			// Записываем АВХ2 В HMI
				SetDataEx(Bufer[3], "Local HMI", "05DigitalInputStatus1", 1)	// Записываем ЦВХ В HMI
				SetDataEx(Bufer[8], "Local HMI", "05StatusWord1", 1)			// Записываем слово остояния в HMI
			else if NumberReadFC == 0x4 then									// Опрашиваем четвертый частотник
				SetDataEx(Bufer[0], "Local HMI", "06Frequency", 1)				// Запись частоту в HMI
				SetDataEx(Bufer[1], "Local HMI", "06AnalogInput1", 1)			// Записываем АВХ1 В HMI
				SetDataEx(Bufer[2], "Local HMI", "06AnalogInput2", 1)			// Записываем АВХ2 В HMI
				SetDataEx(Bufer[3], "Local HMI", "06DigitalInputStatus1", 1)	// Записываем ЦВХ В HMI
				SetDataEx(Bufer[8], "Local HMI", "06StatusWord1", 1)			// Записываем слово остояния в HMI
			else if NumberReadFC == 0x8 then									// Опрашиваем пятый частотник
				SetDataEx(Bufer[0], "Local HMI", "07Frequency", 1)				// Запись частоту в HMI
				SetDataEx(Bufer[1], "Local HMI", "07AnalogInput1", 1)			// Записываем АВХ1 В HMI
				SetDataEx(Bufer[2], "Local HMI", "07AnalogInput2", 1)			// Записываем АВХ2 В HMI
				SetDataEx(Bufer[3], "Local HMI", "07DigitalInputStatus1", 1)	// Записываем ЦВХ В HMI
				SetDataEx(Bufer[8], "Local HMI", "07StatusWord1", 1)			// Записываем слово остояния в HMI
			else if NumberReadFC == 0x10 then 									// Опрашиваем шестой частотник
				SetDataEx(Bufer[0], "Local HMI", "08Frequency", 1)				// Запись частоту в HMI
				SetDataEx(Bufer[1], "Local HMI", "08AnalogInput1", 1)			// Записываем АВХ1 В HMI
				SetDataEx(Bufer[2], "Local HMI", "08AnalogInput2", 1)			// Записываем АВХ2 В HMI
				SetDataEx(Bufer[3], "Local HMI", "08DigitalInputStatus1", 1)	// Записываем ЦВХ В HMI
				SetDataEx(Bufer[8], "Local HMI", "08StatusWord1", 1)			// Записываем слово остояния в HMI
			end if
			SetDataEx(FCRunStatus, "Local HMI", "80FCRunStatus", 1)				// Текущие запущеные ПЧ
		else if FCModel == 3 then 												//  Danfoss FC-051
		else if FCModel == 5 then 												//  inovert ISD
		end if
	end if
end sub

// Управление частотными преобразователями
//	разрешение работы, сброс аварии, выход ПИД, Номер ПЧ (0 для всех)
sub SetControlFC(unsigned short EnableFC, unsigned short ResetErrorFC, float PIDOutput, unsigned short NumberFC)
	unsigned short SetpointFC=0, StatusWord[6]={0,0,0,0,0,0},  ControlWord=0, FCModel=0, y=0, i=1
	GetDataEx(FCModel, "Local HMI", "150FCModel", 1)			// Модель частотников
	GetDataEx(StatusWord[0], "Local HMI", "03StatusWord1", 1)	// Слово состояния ПЧ1
	GetDataEx(StatusWord[1], "Local HMI", "04StatusWord1", 1)	// Слово состояния ПЧ2
	GetDataEx(StatusWord[2], "Local HMI", "05StatusWord1", 1)	// Слово состояния ПЧ3
	GetDataEx(StatusWord[3], "Local HMI", "06StatusWord1", 1)	// Слово состояния ПЧ4
	GetDataEx(StatusWord[4], "Local HMI", "07StatusWord1", 1)	// Слово состояния ПЧ5
	GetDataEx(StatusWord[4], "Local HMI", "08StatusWord1", 1)	// Слово состояния ПЧ6
	//	0 = Неизвестный ПЧ; 1 = ABB ACS310; 2 = ABB ACS580; 3 = Danfoss FC-051; 4 = ABB ACQ580;
	if FCModel == 1 or FCModel == 2 or FCModel then
		SetpointFC = PIDOutput * 20 							// Расчет задание для всех ABB
		SetDataEx(SetpointFC, "ABB_PCH", 4x, 0#1, 1)			// ABB поддерживают широко вещательные команды шлем задание сразу на все ПЧ
	else if FCModel == 3 then 									// Расчет задания для Danfoss FC-051
		SetpointFC = PIDOutput * 16.383
	end if
	while i < 16																	// Побитовый перебор
		ControlWord = 0																// Обнуление для правельной работы алгоритма
		If FCModel == 1 then														// ABB ACS310
			if (EnableFC & i) and not (StatusWord[y] & 0x800C) then  				// Проверяем надо ли включать и включен ли уже ПЧ, также проверяем наличие ошибки
				ControlWord = 0x2													// Включаем ПЧ
			else if not (EnableFC & i) and (StatusWord[y] & 0xC) and not (ResetErrorFC & 0x1) then
				ControlWord = 0x1													// Выключаем ПЧ
			else if ResetErrorFC & i and (StatusWord[y] & 0x8000) then              // Сброс аварии ПЧ
				ControlWord = 0x11													// Сброс аварии ПЧ
			end if
		else if FCModel == 3 then // Если Danfoss FC-051
		end if
		if ControlWord > 0 then
			If y == 0 then
				SetDataEx(ControlWord, "ABB_PCH", 4x, 2#30, 1)
			else if y == 1 then
				SetDataEx(ControlWord, "ABB_PCH", 4x, 3#30, 1)
			else if y == 2 then
				SetDataEx(ControlWord, "ABB_PCH", 4x, 4#30, 1)
			else if y == 3 then
				SetDataEx(ControlWord, "ABB_PCH", 4x, 5#30, 1)
			else if y == 4 then
				SetDataEx(ControlWord, "ABB_PCH", 4x, 6#30, 1)
			else if y == 5 then
				SetDataEx(ControlWord, "ABB_PCH", 4x, 7#30, 1)
			end if
		end if
		y = y + 1 					// Десятичный перебор
		i = i + i 					// Двоичный перебор
	wend
//	If EnableFC == 0 then       // Если нет команды на включение какого либо ПЧ, то стопаем все ПЧ
//	    SetDataEx(temp, "ABB_PCH", 4x, 2#30, 1)						//Слово управления
//    end if
end sub

macro_command main()
unsigned short zero=0
unsigned short QuantityPump=0
	while zero < 1
	GetFC()
	GetPLC()
	GetDataEx(QuantityPump, "Local HMI", "19QuantityPump", 1) 													// Общее количество насосов
	GetDataEx(Mode, "Local HMI", "01Mode", 1)																	// Режим работы
	GetDataEx(SysMs, "Local HMI", LW, 9030, 1)																	// Системное время в ms шаг 100 ms
	GetDataEx(FConverterPoweredPumps, "Local HMI", "01FConverterPoweredPumps", 1) 								// Кол-во насосов работающих от сети
	GetDataEx(MainsPoweredPumps, "Local HMI", "01MainsPoweredPumps", 1) 										// Кол-во насосов работающих от ПЧ
	// наработка насосов
	GetDataEx(PumpNumberOfStarts[0], "Local HMI", "150PumpNumberOfStarts1", 6) 									// Кол-во пуск. насосов
	GetDataEx(PumpRunHours[0], "Local HMI", "150PumpRunHours1", 6) 												// Наработка часов, насосов
	GetDataEx(NumberOfStartsPerHour[0], "Local HMI", "150NumberOfStartsPerHour1", 6) 							// Кол-во пусков за последний час, насосов
	GetDataEx(HoursSinceLastStartPump[0], "Local HMI", "150HoursSinceLastStartPump1", 6) 						// Часов с пуска, насоcов
	GetDataEx(HoursSinceLastStopPump[0], "Local HMI", "150HoursSinceLastStopPump1", 6) 							// Часов со стопа насоса																									// Часов со стопа насоса
	// Включение/выключение дополнительных насосов
	GetDataEx(FrequencyToTurnOnTheAuxiliaryPump, "Local HMI", "12FrequencyToTurnOnTheAuxiliaryPump", 1)			// Част. мастера на вкл. доп. насоса
	GetDataEx(PermissiblePressureDrop, "Local HMI", "12PermissiblePressureDrop", 1)								// Допустимая просадка давления
	GetDataEx(DelayWithAllowablePressureDrop, "Local HMI", "12DelayWithAllowablePressureDrop", 1)				// Задержка при допустимой просадке давления
	GetDataEx(CriticalPressureDrop, "Local HMI", "12CriticalPressureDrop", 1)									// Критическая просадка давления
	GetDataEx(DelayCriticalPressureDrop, "Local HMI", "12DelayCriticalPressureDrop", 1)							// Задержка при критической просадке давления
	GetDataEx(FixedFrequencyStartingPump, "Local HMI", "12FixedFrequencyStartingPump", 1)						// Фиксированная частота при пуске доп. насоса
	GetDataEx(DelayFixedFrequencyStartPump, "Local HMI", "12DelayFixedFrequencyStartPump", 1)					// Задержка ухода на фикс. частоту
	GetDataEx(FixedFrequencyTimeStartPump, "Local HMI", "12FixedFrequencyTimeStartPump", 1)						// Время работы на фикс. частоте
	GetDataEx(FrequencyToTurnOffTheAuxiliaryPump, "Local HMI", "13FrequencyToTurnOffTheAuxiliaryPump", 1)		// Част. мастера на выкл. доп. насоса
	GetDataEx(PermissibleOverpressure, "Local HMI", "13PermissibleOverpressure", 1)								// Допустимое превышение давления
	GetDataEx(DelayPermissibleOverpressure, "Local HMI", "13DelayPermissibleOverpressure", 1)					// Задержка при допустимом превышении давления
	GetDataEx(CriticalOverpressure, "Local HMI", "13CriticalOverpressure", 1)									// Критическое превышение давления
	GetDataEx(DelayCriticalOverpressure, "Local HMI", "13DelayCriticalOverpressure", 1)							// Задержка при критическом превышении давления
	GetDataEx(FixedFrequencyPumpStop, "Local HMI", "13FixedFrequencyPumpStop", 1)								// Фиксированная частота при стопе доп. насоса
	GetDataEx(DelayFixedFrequencyStopPump, "Local HMI", "13DelayFixedFrequencyStopPump", 1)						// Задержка ухода на фикс. частоту
	GetDataEx(FixedFrequencyTimeStopPump, "Local HMI", "13FixedFrequencyTimeStopPump", 1)						// Время работы на фикс. частоте
	GetDataEx(AdditionalPumpsStartsStop, "Local HMI", "80AdditionalPumpsStartsStop", 1)							// Биты старта дополнительных насосов
	GetDataEx(AdditionalPumpsStartKritTime, "Local HMI", "80AdditionalPumpsStartKritTime", 1)					// Сохраненое время для старта доп насоса по критической просадке
	GetDataEx(AdditionalPumpsStartTime, "Local HMI", "80AdditionalPumpsStartTime", 1)							// Сохраненное время для старта допа при обычной просадки
	GetDataEx(AdditionalPumpsStopKritTime, "Local HMI", "80AdditionalPumpsStopKritTime", 1)						// Сохранённое время для стопа доп насоса по критической превышении
	GetDataEx(AdditionalPumpsStopTime, "Local HMI", "80AdditionalPumpsStopKritTime", 1)							// Сохраненное время для стопа допа при обычном превышении
	// Переменные контроллера
	GetDataEx(DigitalInput16, "Local HMI", "02DigitalInput16", 1) 												// Состояние ЦВХ 1-16
	GetDataEx(DigitalOutput16, "Local HMI", "02DigitalOutput16", 1) 											// Состояние ЦВО 1-16
	// Переменные частотников
	GetDataEx(DigitalInputStatus1[0], "Local HMI", "03DigitalInputStatus1", 1)									// Считываем ЦВХ ПЧ
	GetDataEx(FrequencyFC[0], "Local HMI", "03Frequency", 1)													// считываем частоту ПЧ 1
	GetDataEx(FrequencyFC[1], "Local HMI", "04Frequency", 1)													// считываем частоту ПЧ 2
	GetDataEx(FrequencyFC[2], "Local HMI", "05Frequency", 1)													// считываем частоту ПЧ 3
	GetDataEx(FrequencyFC[3], "Local HMI", "06Frequency", 1)													// считываем частоту ПЧ 4
	GetDataEx(FrequencyFC[4], "Local HMI", "07Frequency", 1)													// считываем частоту ПЧ 5
	GetDataEx(FrequencyFC[5], "Local HMI", "08Frequency", 1)													// считываем частоту ПЧ 6
	// Датчики
	GetDataEx(RangeSuctionSensor, "Local HMI", "16RangeSuctionSensor", 1)										// Номинал датчика давления на всасе.
	GetDataEx(RangeDischargeSensor, "Local HMI", "16RangeDischargeSensor", 1)									// Номинал датчика давления на нагнетании.
	// Для Pid
	GetDataEx(SoftFillingOut, "Local HMI", "15SoftFillingOut", 1)					                            // Режим плавного наполнения
	GetDataEx(SoftFillingOutControl, "Local HMI", "80SoftFillingOutControl", 1)		                            // Биты управления алгоритма плавного наполнения.
	GetDataEx(SoftFillingOutTime, "Local HMI", "80SoftFillingOutTime", 1)			                            // Плавное наполнение. Время текущего шага. 32 бита.
	GetDataEx(SetpointPID, "Local HMI", "80SetpointPID", 1)							                            // Рассчитанная уставка для PID регулятора
	GetDataEx(Setpoint, "Local HMI", "01Setpoint", 1) 															// Текущ. уставка давления
	GetDataEx(IntegrationTime, "Local HMI", "17IntegrationTime", 1)												// Время интегрирования в секундах
	GetDataEx(ProportionalCoefficient, "Local HMI", "17ProportionalCoefficient", 1)								// Пропорциональный коэффициент
	GetDataEx(IntegralCoefficient, "Local HMI", "17IntegralCoefficient", 1)										// Интегральный коэффициент
	GetDataEx(DifferentialCoefficient, "Local HMI", "17DifferentialCoefficient", 1)								// Дифференциальный коэффициент
    GetDataEx(PIDError, "Local HMI", "01PIDError", 1)
	GetDataEx(PIDErrorSum, "Local HMI", "01PIDErrorSum", 1)
	GetDataEx(PIDErrorDiff, "Local HMI", "01PIDErrorDiff", 1)
	GetDataEx(PIDProportional, "Local HMI", "01PIDProportional", 1)
	GetDataEx(PIDProportional, "Local HMI", "01PIDProportional", 1)
	GetDataEx(PIDIntegral, "Local HMI", "01PIDIntegral", 1)
	GetDataEx(PIDDerivative, "Local HMI", "01PIDDerivative", 1)
    GetDataEx(ErrorPrev, "Local HMI", "01ErrorPrev", 1)
	GetDataEx(PIDOutput, "Local HMI", "01PIDOutput", 1)
    GetDataEx(PIDIterationTime, "Local HMI", "80PIDiterationTime", 1)                                           // Последнее время исполнения PID регулятора
	// РПД
	GetDataEx(PumpStarted, "Local HMI", "01PumpStarted", 1)								                        // Сигналы подтверждения запуска насосов.
	GetDataEx(PumpStartConfirmationFrequency, "Local HMI", "14PumpStartConfirmationFrequency", 1)				// Частота отслеживания подтверждения запуска насоса
	GetDataEx(PumpStartConfirmationAlarmDelay, "Local HMI", "14PumpStartConfirmationAlarmDelay", 1)				// Задержка аварии подтверждения запуска насоса
	GetDataEx(MaxAlarmConfirmationStartPump, "Local HMI", "14MaxAlarmConfirmationStartPump", 1)					// Максимальное число аварий подтверждения запуска насоса
	GetDataEx(StartPumpDetectionTrig, "Local HMI", "80StartPumpDetectionTrig", 1)								// Биты алгоритма РПД. Триггеры отслеживания работы
	GetDataEx(StartPumpDetectionTimePump[0], "Local HMI", "80StartPumpDetectionTimePump1", 6)					// Время срабатывания алгоритма РПД
	GetDataEx(SumStartPumpDetectionAlarm[0], "Local HMI", "80SumStartPumpDetectionAlarm1", 6)					// Суммарное число аварий по отсутствию подтверждения пуска насосов
	// Аварии
	GetDataEx(SensorsAlarm, "Local HMI", "09SensorsAlarm", 1)													// Аварии датчиков
	GetDataEx(AlarmNotStartPump, "Local HMI", "09AlarmNotStartPump", 1)											// Аварии по отсутствию подтверждения пуска
	GetDataEx(CycleAlarmNotStartPump, "Local HMI", "09CycleAlarmNotStartPump", 1)								// Циклические аварии по отсутствию запуска насоса (Критические аварии)
	GetDataEx(AlarmNasos, "Local HMI", "09AlarmNasos", 1)														// Общие аварии насосов

	GetDataEx(WorkingQuantityPump, "Local HMI", "19WorkingQuantityPump", 1)										// Количество рабочих насосов

	GetDataEx(MinimumFrequency, "Local HMI", "11MinimumFrequency", 1)											// Минимальная рабочея частота
	GetDataEx(MaximumFrequency, "Local HMI", "11MaximumFrequency", 1)											// Максимальная рабочая частота
	GetDataEx(PumpOptions, "Local HMI", "11PumpOptions", 1)														// Различные настройки связанные с мастер насосом

	// Крит
	GetDataEx(ModeOfCriticalPressure, "Local HMI", "14ModeOfCriticalPressure", 1)								// Работа при критическом давлении, данный параметр определяет логику работы установки при аварийном сигнале критическое давление.
	GetDataEx(CriticalPressureAlarmThreshold, "Local HMI", "14CriticalPressureAlarmThreshold", 1) 				// Порог аварии критическое давление
	GetDataEx(DelayCriticalPressureAlarm, "Local HMI", "14DelayCriticalPressureAlarm", 1) 						// Задержка аварии критическое давление
	GetDataEx(MaxNumberOfAlarmCritPressure, "Local HMI", "14MaxNumberOfAlarmCritPressure", 1)					// Максимальное число аварий критическое давление
	GetDataEx(CriticalPressure, "Local HMI", "80CriticalPressure", 1)											// Биты алгоритма анализа критического давления
																													// Бит 0 = Триггер запуска аварии крит. давление
																													// Бит 1 = Триггер сброса аварии крит давление
	GetDataEx(CriticalPressureTime, "Local HMI", "80CriticalPressureTime", 1)									// Время детекции/сброса крит давления
	GetDataEx(CounterCyclicAlarmCriticalPressure, "Local HMI", "80CounterCyclicAlarmCriticalPressure", 1) 		// Количество аварий критическое давление

	// Сухой ход
	GetDataEx(DryPressureTracking, "Local HMI", "14DryPressureTracking", 1)										// Тип детекции сухого хода
	GetDataEx(DryRunningWarningPressure, "Local HMI", "14DryRunningWarningPressure", 1) 						// Давление предупреждения о сухом ходе
	GetDataEx(DryRunningEmergencyPressure, "Local HMI", "14DryRunningEmergencyPressure", 1)						// Аварийное давление сухого хода
	GetDataEx(MaxNumberEmergencyDryRunning, "Local HMI", "14MaxNumberEmergencyDryRunning", 1)					// Максимальное число аварий сухой ход
	GetDataEx(AlarmDryRunningDelay, "Local HMI", "14AlarmDryRunningDelay", 1)									// Задержка аварии сухого хода
	GetDataEx(AlarmWord1, "Local HMI", "09AlarmWord1", 1)														// 16 битное слово данных. Аварии
	GetDataEx(WarningWord1, "Local HMI", "09WarningWord1", 1)													// Слово предупреждений
	GetDataEx(DryRunning, "Local HMI", "80DryRunning", 1)														// Биты алгоритма анализа сухого хода
	GetDataEx(DryRunningTime, "Local HMI", "80DryRunningTime", 1)												// Время детекции сухого хода
	GetDataEx(CounterCyclicAlarmDryRunning, "Local HMI", "80CounterCyclicAlarmDryRunning", 1)					// Счетчик количества аварий сухойго хода


	GetDataEx(PowerSavingModeTimeShtamp, "Local HMI", "80PowerSavingModeTimeShtamp", 1)							// Время предыдущего выполнения алгоритма
	GetDataEx(PowerSavingModeOutput, "Local HMI", "80PowerSavingModeOutput", 1)									// Выход алгоритма энергосбережения
	GetDataEx(PowerSavingModeExitPresure, "Local HMI", "15PowerSavingModeExitPresure", 1)						// Давление отклонения от уставки для выхода из режима энергосбережения.
	GetDataEx(PowerSavingModeIntegrationTime, "Local HMI", "15PowerSavingModeIntegrationTime", 1)				// Время интегрирования размаха
	GetDataEx(PowerSavingAllowablePressureSwing, "Local HMI", "15PowerSavingAllowablePressureSwing", 1)			// Допустимый размах давления
	GetDataEx(PowerSavingPermissibleFrequencySpan, "Local HMI", "15PowerSavingPermissibleFrequencySpan", 1)		// Допустимый размах частата

	GetDataEx(PowerSavingModeBit, "Local HMI", "80PowerSavingModeBit", 1)										// Биты алгоритма энергосбережения
	GetDataEx(PowerSavingMode, "Local HMI", "15PowerSavingMode", 1)												// Режим работы спящего режима
	GetDataEx(PowerSavingModeTime, "Local HMI", "15PowerSavingModeTime", 1)										// Выполнять алгоритм спящего режима раз в сек.
	GetDataEx(PowerSavingModeAmplitudeTime, "Local HMI", "80PowerSavingModeAmplitudeTime", 1)					// Время для расчета амплитудных значений


	GetDataEx(PowerSavingModeSignalMaxPressure, "Local HMI", "80PowerSavingModeSignalMaxPressure", 1)			// Максимальное значение давления за минуту
	GetDataEx(PowerSavingModeSignalMinPressure, "Local HMI", "80PowerSavingModeSignalMinPressure", 1)			// Минимальное значение давление за минуту
	GetDataEx(PowerSavingModeSignalMaxFrequency, "Local HMI", "80PowerSavingModeSignalMaxFrequency", 1)			// Максимальное значение частоты за минуту
	GetDataEx(PowerSavingModeSignalMinFrequency, "Local HMI", "80PowerSavingModeSignalMinFrequency", 1) 		// Минимальное значение давления за минуту

	GetDataEx(PowerSavingPeakToPeakPressure, "Local HMI", "80PowerSavingPeakToPeakPressure", 1)					// Амплитудное значение давления
	GetDataEx(PowerSavingPeakToPeakFrequency, "Local HMI", "80PowerSavingPeakToPeakFrequency", 1)				// Амплитудное значение частоты

	GetDataEx(PowerSavingModePressureIncrease, "Local HMI", "15PowerSavingModePressureIncrease", 1)				// Давление, на которое происходит накачка

	GetDataEx(StatusWord1, "Local HMI", "09StatusWord1", 1)														// 16 битное слово данных. Состояния системы
	GetDataEx(PumpMaintenance, "Local HMI", "20PumpMaintenance", 1)												// Блокировка пуска насосов
	GetDataEx(UnixTime, "Local HMI", "01UnixTime", 1)															//Время в unix формате


//**********************************************************************************************************************************************************************************
// Различные блокировки
//**********************************************************************************************************************************************************************************
	SetDataEx(PumpMaintenance, "Local HMI", "09lock", 1)                                                                   // Различные блокировки

//**********************************************************************************************************************************************************************************
// Режимы работы станции (Автомат Ручной Стоп)
//**********************************************************************************************************************************************************************************
	If DigitalInputStatus1[0] & 0x4 and not DigitalInputStatus1[0] & 0x2 then 			// Если автоматический и не ручной
		Mode = 0x1	                                                            		// Автоматический режим
	else if DigitalInputStatus1[0] & 0x2 and not DigitalInputStatus1[0] & 0x4 then 		// Если ручной режим
		Mode = 0x2
	else 																				// Если стоп
		Mode = 0
	end if

//	If DigitalInput16 & AutoMode and not DigitalInput16 & ManualMode then           // Если автоматический режим
//		Mode = 0b000000000000010	                                                            // Автоматический режим
//	else if DigitalInput16 & ManualMode and not DigitalInput16 & AutoMode then      // Ручной режим
//		Mode = 0b000000000000100	                                                            // Ручной режим
//	else 														                                // Не ручной и не автоматический
//		Mode = 0b000000000000010	                                                            // Значит стоп
//	end if

//**********************************************************************************************************************************************************************************
// Подсчет количества запущеных насосов
//**********************************************************************************************************************************************************************************
	y = 0
	i = 1
	NumberOfRunningPumps = 0
	SumFrequencyFC = 0
	NumberOfRunningPumpsFC = 0
	while y < QuantityPump
		if (FConverterPoweredPumps | MainsPoweredPumps) & i then
			NumberOfRunningPumps = NumberOfRunningPumps + 1 			// Общее число работающих насосов
		end if
		if FConverterPoweredPumps & i then 								// Средняя частота всех ПЧ
			NumberOfRunningPumpsFC = NumberOfRunningPumpsFC + 1			// Число насосов работающий от ПЧ
			SumFrequencyFC = SumFrequencyFC + FrequencyFC[y]
		end if
		y = y + 1 														// Десятичный перебор
		i = i<<1 														// Двоичный перебор
	wend
	SumFrequencyFC = SumFrequencyFC / NumberOfRunningPumpsFC			// Вычисляем среднее значение частоты
	// Добавить обработку подсчета частоты в зависимости от типа системы !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	SumFrequencyFC = FrequencyFC[0] 

//**********************************************************************************************************************************************************************************
// Алгоритм сортировки насосов
//**********************************************************************************************************************************************************************************
	unsigned short TempTimeToStop=0, TempTimeToStart=65535, TempTimeToStartPriority=0, TempQuantityStarts=65535, TempTimeToStartIsRun=65535
	unsigned short NumberPumpToStarts=64, NumberPumpToStartIsRun=64, NumberPumpToStop=0
	unsigned short TempPumpHighestStopedTime=0, TempPumpHighestRunningTime=0, PumpHighestRunningTime=64, PumpHighestStopedTime=64

	y = 0
	i = 1
	while y < QuantityPump
		// сортировка не запущеных
		//			Насосы не включены----------------------------------------------	Не авария--------------  Не блокировка ----------------- авария насос не запустился
		if (not ((FConverterPoweredPumps & i) or (MainsPoweredPumps & i))) and (not (AlarmNasos & i)) and (not (PumpMaintenance & i)) and (not (AlarmNotStartPump & i)) then // Условия входа
			// приоритет у долгоневключающихся насосов
			if (HoursSinceLastStopPump[y] >= 72 and HoursSinceLastStopPump[y] >= TempTimeToStartPriority) then
				TempTimeToStartPriority = HoursSinceLastStopPump[y]
				NumberPumpToStarts = i																	// Номер насоса для пуска
			// 			Оптимизация по часам 				оптимизация по пускам							приотеризация насоса, долго не включается 										оптимизация по количеству стартов
			else if ((PumpRunHours[y] <= TempTimeToStart) and (PumpNumberOfStarts[y] <= TempQuantityStarts)) and (TempTimeToStartPriority == 0) then
			//if ((PumpRunHours[y] <= TempTimeToStart and not HoursSinceLastStopPump[y] >= 72) or (HoursSinceLastStopPump[y] >= 72 and HoursSinceLastStopPump[y] >= TempTimeToStartPriority) or (PumpNumberOfStarts[y] <= TempQuantityStarts)) then
				//TempTimeToStartPriority = HoursSinceLastStopPump[y]
				TempTimeToStart = PumpRunHours[y]
				TempQuantityStarts = PumpNumberOfStarts[y]
				NumberPumpToStarts = i																	// Номер насоса для пуска
			end if
		end if
		// Выбор насоса из запущеных с наименьшей наработкой
		if ((FConverterPoweredPumps & i) or (MainsPoweredPumps & i)) and (PumpRunHours[y] <= TempTimeToStart) then
			TempTimeToStartIsRun = PumpRunHours[y]
			NumberPumpToStartIsRun = i
		end if
		// Выбор насоса на отключе+нияие из уже запущеных
		if PumpRunHours[y] >= TempTimeToStop then
			if (MainsPoweredPumps & i) or (MainsPoweredPumps == 0 and FConverterPoweredPumps & i) then
				TempTimeToStop = PumpRunHours[y]
				NumberPumpToStop = i 												// Номер насоса для стопа
			end if
		end if
		// выбор насоса с наибольшей наработкой с момента пуска насоса
		if ((FConverterPoweredPumps & i) or (MainsPoweredPumps & i)) and (HoursSinceLastStartPump[y] >= TempPumpHighestRunningTime) then
			TempPumpHighestRunningTime = HoursSinceLastStartPump[y]									// ВЫбираем насос с наибольшей наработкой с момента пуска
			PumpHighestRunningTime = y
		end if
		// Поиск насоса с наибольшим простоем
		//			Насосы не включены----------------------------------------------	Не авария--------------  Не блокировка ----------------- авария насос не запустился
		if (not((FConverterPoweredPumps & i) or (MainsPoweredPumps & i))) and (not(AlarmNasos & i)) and (not(PumpMaintenance & i)) and (not(AlarmNotStartPump & i)) then // Условия входа
			if (HoursSinceLastStopPump[y] >= 72) then
				//TempPumpHighestStopedTime = HoursSinceLastStopPump[y]
				PumpHighestStopedTime = i
			end if
		end if
		y = y+1 																	// Десятичный перебор
		i = i+i 																	// Двоичный перебор
	wend
//**********************************************************************************************************************************************************************************
// Расчет показаний датчиков
//**********************************************************************************************************************************************************************************
	GetDataEx(TempShort, "Local HMI", "03AnalogInput1", 1)							// Записываем АВХ1 В HMI
	SuctionSensorMaValue = 50 * 2 													// Преобразование в Ma (Просто умножаем на 2 (100*2=200, получаем 20ma). Получаем шаг измерения 0.2Ma
	if TempShort > 170 and TempShort < 1030 then 									// Проверяем попадаем ли в рабочий диапазон (4..20ma, 20..100%, с учетом погрешности 17..103)
		if TempShort >= 200 then
			TempUInt = TempShort - 200
			TempUInt = TempUInt * RangeSuctionSensor / 800							// Если все норм то вычисляем давление (значение * на номинал / 100) (В шорт не уложимся, расшитрить переменную)
			SuctionPressure = TempUInt
		else
			SuctionPressure = 0
		end if
		SensorsAlarm = SensorsAlarm & ~0x3 											// Сброс аварий датчика
	else if 50 < 17 then
		SuctionPressure = 0
		SensorsAlarm = SensorsAlarm | 0x1											// Выставляем обрыв
	else
		SuctionPressure = RangeSuctionSensor										// давление равно верхниму диапазону датчика
		SensorsAlarm = SensorsAlarm | 0x2 											// Выставляем КЗ
	end if
	GetDataEx(TempShort, "Local HMI", "03AnalogInput2", 1)							// Записываем АВХ1 В HMI
	DischargeSensorMaValue = TempShort * 2											// Преобразование в Ma (Просто умножаем на 2 (100*2=200, получаем 20ma). Получаем шаг измерения 0.2Ma
	if TempShort > 170 and TempShort < 1030 then 									// Проверяем попадаем ли в рабочий диапазон (4..20ma, 20..100%, с учетом погрешности 17..103)
		if TempShort >= 200 then
			TempUInt = TempShort - 200
			TempUInt = TempUInt * RangeDischargeSensor / 800						// Если все норм то вычисляем давление (значение * на номинал / 100) (В шорт не уложимся, расшитрить переменную)
			DischargePressure = TempUInt
		else
			DischargePressure = 0
		end if
		SensorsAlarm = SensorsAlarm & ~0xC 											// Сброс аварий датчика
	else if TempShort < 170 then
		DischargePressure = 0
		SensorsAlarm = SensorsAlarm | 0x4 		    								// Выставляем обрыв
	else
		DischargePressure = RangeDischargeSensor									// давление равно верхниму диапазону датчика
		SensorsAlarm = SensorsAlarm | 0x8 											// Выставляем КЗ
	end if
	DifferencePressure = DischargePressure - SuctionPressure						// Перепад давления
//**********************************************************************************************************************************************************************************

	If mode == 0x1 then // Если автоматический режим
//**********************************************************************************************************************************************************************************
// ПИД Регулятор
//**********************************************************************************************************************************************************************************
		if NumberOfRunningPumps == 0 then 																// Если число запущеных насосов 0
			SoftFillingOutControl = SoftFillingOutControl | 0x1											// Разрешаем плавное наполение
		end if
		if PIDOutput >= 950 then					// Отключение алгоритма заполнения, если число рабочих достигло максимума
			SoftFillingOutControl = 0																	// Выключаем наполнение
		end if
		If (SoftFillingOut >= 1) and (SoftFillingOutControl & 0x1) Then  								// Проверяем разрешон ли режим наполнения
			if not (SoftFillingOutControl & 0x2) then 													// Проверяем запущен ли алгоритм плавного заполнения если не запущен то
				SoftFillingOutControl = SoftFillingOutControl | 0x2 									// Ставим пометку о запуске алгоритма
				SoftFillingOutTime = SysMs																// Запоминаем время старта
				SetpointPID = DischargePressure + 20 													// уставка алгоритма заполнения = выходному давлению
			else if DischargePressure + 5 >=  SetpointPID then 											// Если текущая уставка = выходу или уставка алгоритма больше обычной уставки
				if SetpointPID >= Setpoint then 														// Если уставка алгоритма = уставки обычной
					SoftFillingOutControl = 0															// Выключаем алгоритм наполнеиня
				else if SysMs >= SoftFillingOutTime + SoftFillingOut or (SoftFillingOutTime + SoftFillingOut >= SoftFillingOutTime and SysMs < SoftFillingOutTime) then
					SoftFillingOutTime = SysMs
					SetpointPID = SetpointPID + 10														// уставка алгоритма заполнения
				end if
			else if SoftFillingOut > 1 then
				if SetpointPID < Setpoint then 															// если задание алгоритма не достигла задания пользователя
					if SysMs >= SoftFillingOutTime + SoftFillingOut or (SoftFillingOutTime + SoftFillingOut >= SoftFillingOutTime and SysMs < SoftFillingOutTime) then
						SoftFillingOutTime = SysMs
						SetpointPID = SetpointPID + 10													// уставка алгоритма заполнения
					end if
				else
					SoftFillingOutControl = 0															// Выключаем алгоритм наполнеиня
					SetpointPID = Setpoint
				end if
			end if
		else if (PowerSavingModePressureIncrease >= 1) and (PowerSavingModeBit & 0x01) and (NumberOfRunningPumps <= 1) then					// Если разрешена накачка давления во время спящего режима
			SoftFillingOutControl = 0
			if SetpointPID >=  Setpoint + PowerSavingModePressureIncrease then
				SetpointPID = Setpoint + PowerSavingModePressureIncrease
			else
				if SetpointPID < Setpoint then
					SetpointPID = Setpoint
				else
					SetpointPID = SetpointPID + 1
				end if
			end if																						// Выключаем алгоритм наполнеиня
		else
			SoftFillingOutControl = 0																	// Выключаем алгоритм наполнеиня
			SetpointPID = Setpoint
		end if
		TempUInt = IntegrationTime * 10                           										// Преобразование коэффицента во время
		if (SysMs >= PIDIterationTime + TempUInt) or (SysMs < PIDIterationTime) then 					// Выполняем ПИД с учетом времени интегрирования
			PIDIterationTime = SysMs
			PIDError = SetpointPID-DischargePressure                                           			// ошибка регулирования
			PIDProportional = PIDError * ProportionalCoefficient	 									// пропорционально ошибке регулирования
			PIDErrorDiff = ErrorPrev - DischargePressure 												// изменение входного сигнала
			PIDDerivative = PIDErrorDiff * DifferentialCoefficient / IntegrationTime
			PIDIntegral = PIDIntegral + (PIDError * IntegralCoefficient * IntegrationTime)  			// расчёт интегральной составляющей
			If PIDIntegral <= 0 Then                                     								// замараживаем интегральную состовляющую
				PIDIntegral = 0
			else if PIDIntegral >= 1000 - PIDProportional then
				PIDIntegral = 1000 - PIDProportional
			end if
			PIDOutput = PIDProportional + PIDIntegral + PIDDerivative
			ErrorPrev = DischargePressure																// Сохраняем значение ошибки как предыдущее
			if PIDOutput < (MinimumFrequency * 2) then                                          		// Ограничение выхода ПИД
				if PIDOutput < 0 then																	// Не даем уйти пиду в минус
					PIDOutput = 0
				end if
				if (not (PumpOptions & 0x01) and (SumFrequencyFC < (MinimumFrequency * 2))) then 		// Проверяем разрешон ли пуск мастера с 0
					PIDIntegral = ((MinimumFrequency * 2) - PIDProportional) + 1 						// Заморозка интегральной состовляющей
					PIDOutput = (MinimumFrequency * 2) + 1
				end if
			else If PIDOutput >= 1000 then
				PIDOutput = 1000
			else if PIDOutput >= (MaximumFrequency * 2) then
				PIDIntegral = ((MaximumFrequency * 2) - PIDProportional) - 1					 		// Заморозка интегральной состовляющей
				PIDOutput = MaximumFrequency * 2
			end if
		end if
		if AdditionalPumpsStartsStop & 0x10 then 																	// Проверяем есть ли пометка о запуске допа
			GetDataEx(TempUInt, "Local HMI", "80AdditionalPumpsStarted", 1)											// Фактическое время старта допа
			if (SysMs >= TempUInt + DelayFixedFrequencyStartPump) or (TempUInt + DelayFixedFrequencyStartPump >= TempUInt and (SysMs < TempUInt)) then 								// Проверяем пора ли уходить в тень
				if (SysMs >= TempUInt + DelayFixedFrequencyStartPump + FixedFrequencyTimeStartPump) or (TempUInt + DelayFixedFrequencyStartPump + FixedFrequencyTimeStartPump >= TempUInt and SysMs < TempUInt) then                  // Проверяем пора ли выходить на пид
					AdditionalPumpsStartsStop = AdditionalPumpsStartsStop & ~0x10									// Сбрасываем метку запуска допа
				else
					PIDOutput = ((FixedFrequencyStartingPump * 10) / MaximumFrequency) * 100						// Подменяем выход пида на фиксированную частоту
					PIDIntegral = PIDOutput - PIDError 																// Возврад на ПИД с текущей частоты
				end if
			end if
		else if AdditionalPumpsStartsStop & 0x20 then 																// Проверяем есть ли пометка об отключении доп насоса
			GetDataEx(TempUInt, "Local HMI", "80AdditionalPumpsStoped", 1)											// Фактическое время стопа допа
			if (SysMs >= TempUInt + DelayFixedFrequencyStopPump) or (TempUInt + DelayFixedFrequencyStopPump >= TempUInt and SysMs < TempUInt) then 							// Проверяем пора ли уходить в тень
				if (SysMs >= TempUInt + DelayFixedFrequencyStopPump + FixedFrequencyTimeStopPump) or (TempUInt + DelayFixedFrequencyStopPump + FixedFrequencyTimeStopPump >= TempUInt and SysMs < TempUInt) then 						// Проверяем пора ли сново выходить на ПИД
					AdditionalPumpsStartsStop = AdditionalPumpsStartsStop & ~0x20															// Сбрасываем метку стопа допа
				else
					PIDOutput = ((FixedFrequencyPumpStop * 10) / MaximumFrequency) * 100							// Подменяем уставку пида на фикс скорость
					PIDIntegral = PIDOutput - PIDError
				end if
			end if
		end if
		FrequencySetpoint = (PIDOutput * MaximumFrequency) / 1000 													// Переводим выход пида в частоту
//**********************************************************************************************************************************************************************************
// Спящий режим
//**********************************************************************************************************************************************************************************
		// Считаем размах колебаний за последнию минуту давление и частота
		if not (PowerSavingModeBit & 0x2) then																		// Запускался ли алгоритм
			PowerSavingModeBit = PowerSavingModeBit | 0x2															// Ставим пометку о запуске алгоритма
			PowerSavingModeAmplitudeTime = SysMs + PowerSavingModeIntegrationTime									// Запоминаем текущее время
			PowerSavingModeSignalMinPressure = 65535
			PowerSavingModeSignalMinFrequency = 65535
			PowerSavingModeSignalMaxPressure = 0
			PowerSavingModeSignalMaxFrequency = 0
		else if SysMs < PowerSavingModeAmplitudeTime then 															// Считаем размах колебаний за минуту
			If DischargePressure > PowerSavingModeSignalMaxPressure then
				PowerSavingModeSignalMaxPressure = DischargePressure
			else if DischargePressure < PowerSavingModeSignalMinPressure then
				PowerSavingModeSignalMinPressure = DischargePressure
			end if
			If FrequencySetpoint > PowerSavingModeSignalMaxFrequency then
				PowerSavingModeSignalMaxFrequency = FrequencySetpoint
			else if FrequencySetpoint < PowerSavingModeSignalMinFrequency then
				PowerSavingModeSignalMinFrequency = FrequencySetpoint
			end if
		else
			PowerSavingPeakToPeakPressure = PowerSavingModeSignalMaxPressure - PowerSavingModeSignalMinPressure  	// Расчет амплитудных значений
			PowerSavingPeakToPeakFrequency = PowerSavingModeSignalMaxFrequency - PowerSavingModeSignalMinFrequency	// Расчет амплитудных значений
			PowerSavingModeBit = PowerSavingModeBit & ~0x2															// Снимаем пометкеу о запуске алгоритма
		end if
		if PowerSavingMode & 0x01 then
			if (DischargePressure + 10) >= Setpoint then 															// Провяряем достигло ли давление задания + гистерезис
				if not (PowerSavingModeBit & 0x01) then																// проверяем запущен ли алгоритм сна
					if (PowerSavingPeakToPeakPressure <= PowerSavingAllowablePressureSwing) and (PowerSavingPeakToPeakFrequency <= PowerSavingPermissibleFrequencySpan) then	// Проверяем амплитудные значения
						if (SysMs >= PowerSavingModeTimeShtamp + PowerSavingModeTime) or ((PowerSavingModeTimeShtamp + PowerSavingModeTime >= PowerSavingModeTimeShtamp) and (SysMs < PowerSavingModeTimeShtamp)) then											// Пора ли включать режим энерго сбережения
							PowerSavingModeOutput = PIDOutput
							PowerSavingModeTimeShtamp =	SysMs														// Запомнили время включения
							PowerSavingModeBit = PowerSavingModeBit | 0x01 											// Включаем алгоритм энергосбережения
							TRACE("sleep mode started")
						end if
					end if
				end if
			else if (PowerSavingModeBit & 0x01) and (PowerSavingModeOutput <= 10) then 								// Если алгоритм сна завершил свою работу Zzz
				if DischargePressure <= (Setpoint - PowerSavingModeExitPresure) then
					PowerSavingModeBit = PowerSavingModeBit & ~0x1 													// Отключаем режим энэргосбережения
				end if
			else if PowerSavingModeBit & 0x01 then
				PowerSavingModeBit = PowerSavingModeBit & ~0x1 														// Отключаем режим энэргосбережения
				PowerSavingModeBit = PowerSavingModeBit & ~0x4														// Снимаем флаг накачки давления
			end if
			if PowerSavingModeBit & 0x01 then 																		// Если есть разрешение работы алгоритма
				StatusWord1 = StatusWord1 | 0x1																		// Записываем в слово состояние что алгоритм включен
				if ((PowerSavingModePressureIncrease <= 0) or (DischargePressure >= ((Setpoint + PowerSavingModePressureIncrease) - 10)) or (NumberOfRunningPumps >= 2)) and not (PowerSavingModeBit & 0x04) then
					PowerSavingModeBit = PowerSavingModeBit | 0x4													// Ставим флаг накачки
					PowerSavingModeOutput = PIDOutput
				end if
				if PowerSavingModeBit & 0x04 then
					if NumberOfRunningPumps >= 2 then 																// Если в работе несколько насосов, то ограничить частоту минимальной
						if PowerSavingModeOutput <= (((MinimumFrequency * 10) / MaximumFrequency) * 100) then
							PowerSavingModeOutput = ((MinimumFrequency * 10) / MaximumFrequency) * 100 				// Ограничиваем минимальной частотой
						else
							PowerSavingModeOutput = PowerSavingModeOutput - 10
						end if
						if (PowerSavingModeOutput <= 0) or (PowerSavingModeOutput >= 20000) then
							PowerSavingModeOutput = 0
						end if
					else 																							// Если остался только один насос, частота опускается до нуля
						if (PowerSavingModeOutput >= 1) and (PowerSavingModeOutput <= 20000) then
							PowerSavingModeOutput = PowerSavingModeOutput - 10 										// Уменьшение частоты
						end if
						if (PowerSavingModeOutput <= 0 or PowerSavingModeOutput >= 21000) then
							PowerSavingModeOutput = 0
						end if
					end if
					PIDOutput = PowerSavingModeOutput
					PIDIntegral = PowerSavingModeOutput - PIDError 												// Возврад на ПИД с текущей частоты
				end if
			else
				PowerSavingModeBit = PowerSavingModeBit & ~0x4													// Снимаем флаг накачки давления
				StatusWord1 = StatusWord1 & ~0x1																// Записываем в слово состояние что алгоритм выключен
			end if
		else
			StatusWord1 = StatusWord1 & ~0x1																	// Записываем в слово состояние что алгоритм выключен
			PowerSavingModeBit = PowerSavingModeBit & ~0x1 														// Отключаем режим энэргосбережения
			PowerSavingModeBit = PowerSavingModeBit & ~0x4														// Снимаем флаг накачки давления
			PowerSavingModeOutput = 0
		end if
//**********************************************************************************************************************************************************************************
// Выбор мастер насоса
//**********************************************************************************************************************************************************************************
		if (FConverterPoweredPumps == 0) and (NumberPumpToStarts <> 64) then 									// Если нет насосов работающих от ПЧ, то значит мастер насос не выбран. Также проверяем удалось ли отсортировать
			FConverterPoweredPumps =  FConverterPoweredPumps | NumberPumpToStarts								// Выбераем мастер насос
			MainsPoweredPumps = MainsPoweredPumps & ~NumberPumpToStarts 										// Отключаем данный насос от сети на всякий случай
			AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x40										// Ставим пометку старта основного насоса
			TRACE("1 SelectMaster FC = %d", FConverterPoweredPumps)
		else if (FConverterPoweredPumps == 0) and (NumberPumpToStartIsRun <> 64) then									// Запуск из уже запущеных
			FConverterPoweredPumps =  FConverterPoweredPumps | NumberPumpToStartIsRun
			MainsPoweredPumps = MainsPoweredPumps & ~NumberPumpToStartIsRun 										// Отключаем данный насос от сети на всякий случай
			AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x40										// Ставим пометку старта основного насоса
			TRACE("2 SelectMaster FC = %d", FConverterPoweredPumps)
		end if
//**********************************************************************************************************************************************************************************
// Запуск дополнительных насосов
//**********************************************************************************************************************************************************************************
		if SumFrequencyFC >= FrequencyToTurnOnTheAuxiliaryPump and NumberPumpToStarts <> 64 then 				// Частота достигла уставки включения допов
			If not AdditionalPumpsStartsStop & 0x10 and not AdditionalPumpsStartsStop & 0x20 and not AdditionalPumpsStartsStop & 0x40 then				// Проверяем был ли запущен или остановлен насос
				if not SoftFillingOutControl & 0x2 and FConverterPoweredPumps <> 0 then 		// проверяем чтоб небыло режима заполнения
					if not AlarmWord1 & 0x4 then 																	// Проверяем чтоб небыло кретического давления
						if NumberOfRunningPumps < WorkingQuantityPump then 											// Проверяем не достигло ли число рабочих насосов максимального
							if DischargePressure <= Setpoint-CriticalPressureDrop then								// Проверяем критическое отстование давления
								If not AdditionalPumpsStartsStop & 0x1 then 										// Проверяем запускался ли этот алгоритм на предыдущей итерации
									AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x1  					// ставим пометку о запуске алгоритма
									AdditionalPumpsStartKritTime = SysMs 											// Временная переменная для старта насоса (Время прошлого запуска по криту)
								else if SysMs >= AdditionalPumpsStartKritTime + DelayCriticalPressureDrop or (AdditionalPumpsStartKritTime + DelayCriticalPressureDrop >= AdditionalPumpsStartKritTime and SysMs < AdditionalPumpsStartKritTime) then		// Проверяем пора ли включать доп
									if NumberPumpToStarts <> 64 then 												// Если удалось выбрать насос
										AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x1 				// Временная переменая идентификатор запуска алгоритма старта допов
										MainsPoweredPumps = MainsPoweredPumps | NumberPumpToStarts					// Включаем насос от сети
										AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x10				// Ставим пометку старта допа
										SetDataEx(SysMs, "Local HMI", "80AdditionalPumpsStarted", 1)				// Запоминаем фактическое время старта допа
									end if
								End if
							else
								AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x1						// Временная переменая идентификатор запуска алгоритма старта допов
							end if
							if DischargePressure <= Setpoint-PermissiblePressureDrop then							// Проверяем допустимое отстование давления
								if not AdditionalPumpsStartsStop & 0x2 then 										// Проверяем запускался ли этот алгорит�� на предыдущей итерации
									AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x2  					// ставим пометку о запуске алгоритма
									AdditionalPumpsStartTime = SysMs 												// Временная переменная для старта насоса (Время прошлого запуска)
								else if SysMs >= AdditionalPumpsStartTime + DelayWithAllowablePressureDrop or (AdditionalPumpsStartTime + DelayWithAllowablePressureDrop >= AdditionalPumpsStartTime and SysMs < AdditionalPumpsStartTime) then		// Проверяем пора ли включать доп
									if NumberPumpToStarts <> 64 then 												// Если удалось выбрать насос
										AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x2 				// Временная переменая идентификатор запуска алгоритма старта допов
										MainsPoweredPumps = MainsPoweredPumps | NumberPumpToStarts					// Включаем насос от сети
										AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x10				// Ставим пометку старта допа
										SetDataEx(SysMs, "Local HMI", "80AdditionalPumpsStarted", 1)				// Запоминаем фактическое время старта допа
									end if
								end if
							else
								AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x2 						// Временная переменая идентификатор запуска алгоритма старта допов
							end if
						end if
					end if
				end if
			end if
		else
			AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x1 										// Временная переменая идентификатор запуска алгоритма старта допов
			AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x2 										// Временная переменая идентификатор запуска алгоритма старта допов
		end if
//**********************************************************************************************************************************************************************************
// Остановка дополнительных насосов штатная остановка
//**********************************************************************************************************************************************************************************
		if NumberOfRunningPumps > 1 and NumberPumpToStop <> 64 then 									//  количество запущеных насосов больше одного
			If not AdditionalPumpsStartsStop & 0x10 and not AdditionalPumpsStartsStop & 0x20 and not AdditionalPumpsStartsStop & 0x40 then		// Проверяем был ли запущен или остановлен насос
				if DischargePressure >= Setpoint+CriticalOverpressure then								// Проверяем критическое превышение давления
					If not AdditionalPumpsStartsStop & 0x4 then 										// Проверяем запускался ли этот алгоритм на предыдущей итерации
						AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x4  					// ставим пометку о запуске алгоритма
						AdditionalPumpsStopKritTime = SysMs 											// Временная переменная для старта насоса (Время прошлого запуска по криту)
					else if SysMs >= AdditionalPumpsStopKritTime + DelayCriticalOverpressure or (AdditionalPumpsStopKritTime + DelayCriticalOverpressure >= AdditionalPumpsStopKritTime and SysMs < AdditionalPumpsStopKritTime) then		// Проверяем пора ли включать доп
						if NumberPumpToStop <> 64 then 													// Если удалось выбрать насос
							AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x4 				// Временная переменая идентификатор запуска алгоритма старта допов
							MainsPoweredPumps = MainsPoweredPumps & ~NumberPumpToStop					// Отключаем двигатель
							AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x20				// Ставим пометку стопа допа
							SetDataEx(SysMs, "Local HMI", "80AdditionalPumpsStoped", 1)					// Запоминаем фактическое время стопа допа
						end if
					End if
				else
					AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x4						// Временная переменая идентификатор запуска алгоритма старта допов
				end if
				if SumFrequencyFC <= FrequencyToTurnOffTheAuxiliaryPump  and DischargePressure >= Setpoint+PermissiblePressureDrop then							// Частота достигла уставки выключения допов, Проверяем допустимое превышение давления
					if not AdditionalPumpsStartsStop & 0x8 then 										// Проверяем запускался ли этот алгоритм на предыдущей итерации
						AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x8  					// ставим пометку о запуске алгоритма
						AdditionalPumpsStopTime = SysMs 												// Временная переменная для старта насоса (Время прошлого запуска)
					else if SysMs >= AdditionalPumpsStopTime + DelayWithAllowablePressureDrop or (AdditionalPumpsStopTime + DelayWithAllowablePressureDrop >= AdditionalPumpsStopTime and SysMs < AdditionalPumpsStopTime) then		// Проверяем пора ли включать доп
						if NumberPumpToStop <> 64 then 													// Если удалось выбрать насос
							AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x8 				// Временная переменая идентификатор запуска алгоритма старта допов
							MainsPoweredPumps = MainsPoweredPumps & ~NumberPumpToStop					// Отключаем двигатель
							AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x20				// Ставим пометку стопа допа
							SetDataEx(SysMs, "Local HMI", "80AdditionalPumpsStoped", 1)					// Запоминаем фактическое время стопа допа
						end if
					end if
				else
					AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x8 						// Временная переменая идентификатор запуска алгоритма старта допов
				end if
			end if
		else
			AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x4 								// Временная переменая идентификатор запуска алгоритма старта допов
			AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x8 								// Временная переменая идентификатор запуска алгоритма старта допов
		end if

//**********************************************************************************************************************************************************************************
// Аварийный стоп насосов
//**********************************************************************************************************************************************************************************
		y = 0
		i = 1
		while y < 32
			// Стоп по сборной аварии насоса и по блокировке насоса
			if (AlarmNasos & i) or (PumpMaintenance & i) then
				FConverterPoweredPumps =  FConverterPoweredPumps & ~i
				MainsPoweredPumps = MainsPoweredPumps & ~i
				TRACE("Alarm stop, general alarm pump= %d", y)
			end if
			// Стоп ПО РПД
			if (AlarmNotStartPump & i) and (FConverterPoweredPumps & i) Then
				FConverterPoweredPumps =  FConverterPoweredPumps & ~i
				TRACE("Alarm stop, RPD alarm pump FC= %d", y)
			else if AlarmNotStartPump & i then
				MainsPoweredPumps = MainsPoweredPumps & ~i
				TRACE("Alarm stop, RPD alarm pump= %d", y)
			end if
			// Отключение допов при критическом давлении
			if (AlarmWord1 & 0x8) then											// если есть пометка о циклической аварии критическое давление
				FConverterPoweredPumps =  FConverterPoweredPumps & ~i			// Стопаем все
				MainsPoweredPumps = MainsPoweredPumps & ~i						// Стопаем все
			else if (AlarmWord1 & 0x4) and NumberOfRunningPumps > 1 and  NumberPumpToStop <> 64 then	// если сухой ход но есть допы
				MainsPoweredPumps = MainsPoweredPumps & ~NumberPumpToStop		// Отключаем двигатель
			else if (AlarmWord1 & 0x4) then										// Если критическое давление
				FConverterPoweredPumps =  FConverterPoweredPumps & ~i			// Стопаем все
				MainsPoweredPumps = MainsPoweredPumps & ~i						// Стопаем все
			end if
			y = y + 1 											// Десятичный перебор
			i = i+i 											// Двоичный перебор
		wend

//**********************************************************************************************************************************************************************************
// Ротация насосов
//**********************************************************************************************************************************************************************************
		// Вывести в журнал сообщение о ротации насоса
		unsigned short PumpOptions=0
		GetDataEx(PumpOptions, "Local HMI", "11PumpOptions", 1) 										// Общие настройки насосов
		PumpOptions = 0x4
		if PumpOptions & 0x4 then
			if NumberOfRunningPumps <= QuantityPump and NumberOfRunningPumps >= 1 then					// если включены все насосы то не чего не делать, условие бесполезно, но так безопаснее													// Проверяем разрешена ли ротация насосов
			// Если текущее время попадает в диапазон ротации
				if PumpHighestStopedTime <> 64 then 													// Проверяем удалось ли выбрать новый мастер насос
					if PumpHighestRunningTime <> 64 then
						if HoursSinceLastStartPump[PumpHighestRunningTime] >= 1 then						// Если время с момента включения текущего мастера больше часа
							TRACE("Rotation completed %d",PumpHighestStopedTime)													// Если работает больше одного насос
							FConverterPoweredPumps = 0													// Выключем текущий мастер
							FConverterPoweredPumps =  FConverterPoweredPumps | PumpHighestStopedTime	// Выбераем мастер насос
							MainsPoweredPumps = MainsPoweredPumps & ~PumpHighestStopedTime 				// Отключаем данный насос от сети на всякий случай
							AdditionalPumpsStartsStop = AdditionalPumpsStartsStop | 0x40				// Ставим пометку старта основного насоса
						end if
					end if
				end if
			end if
		end if
//**********************************************************************************************************************************************************************************
// Блок детекции сухого хода
//**********************************************************************************************************************************************************************************
		// 09WarningWord1
		// Бит 0 = Низкое давление
		// Слово отказов 1	09AlarmWord1
		// 09AlarmDryRunning	Бит 0 = Авария сухой ход
		// 09AlarmCycleDryRunning	Бит 1 = Авария циклический сухой ход (Критическая)
		// 09AlarmCriticalPressure	Бит 2 = Авария критическое давление
		// 09AlarmCycleCriticalPressure	Бит 3 = Авария циклическое критическое давление (Критическая)
		// Предупреждение сухой ход
		if SuctionPressure < DryRunningWarningPressure and SuctionPressure > DryRunningEmergencyPressure and not AlarmWord1 & 0x1 then 			// Предупреждение о низком давлении
			WarningWord1 = WarningWord1 | 0x1 																			// Выставляем предупреждение о низком давлении
		else
			WarningWord1 = WarningWord1 & ~0x1 																			// Убераем предупреждение о сухом ходе
		end if
		// Авария сухой ход
		if SuctionPressure < DryRunningEmergencyPressure and not AlarmWord1 & 0x2 then 									// Авария Сухой ход
			DryRunning = DryRunning & ~0x2 																				// Сброс пометки о начале отсчета сброса аварии
			If not DryRunning & 0x1 then 																				// Проверяем запускался ли алгоритм
				DryRunning = DryRunning | 0x1																			// Ставим пометку о запуске алгоритма
				DryRunningTime = SysMs																					// Запоминаем время
			else if SysMs >= DryRunningTime + AlarmDryRunningDelay or (DryRunningTime + AlarmDryRunningDelay >= DryRunningTime and SysMs < DryRunningTime) then						// Проверяем пора ли включать сухой ход
					AlarmWord1 = AlarmWord1 | 0x1  																			// Выставляем аварию сухого хода
					CounterCyclicAlarmDryRunning = CounterCyclicAlarmDryRunning + 1
					TRACE("Low in pressure")
			end if
		else
			DryRunning = DryRunning & ~0x1																					// Сброс бита запуска алгоритма детекции сухого хода
			if not DryRunning & 0x2 then 																				// Проверяем запускался ли алгоритм
				DryRunning = DryRunning | 0x2																			// Ставим пометку о запуске алгоритма
				DryRunningTime = SysMs																					// Запоминаем время
			else
				if AlarmWord1 & 0x1 then
					if SysMs >= DryRunningTime + AlarmDryRunningDelay or (DryRunningTime + AlarmDryRunningDelay >= DryRunningTime and SysMs < DryRunningTime) then
						AlarmWord1 = AlarmWord1 & ~0x1 																		// Сброс аварии
						TRACE("Reset low in pressure")
					end if
					if SysMs >= DryRunningTime + 6000 or (DryRunningTime + 6000 >= DryRunningTime and SysMs < DryRunningTime) then
						CounterCyclicAlarmDryRunning = 0																	// Сброс счетчика аварий
					end if
				end if
			end if
		end if
		iF (CounterCyclicAlarmDryRunning >= MaxNumberEmergencyDryRunning) and MaxNumberEmergencyDryRunning > 0 then
			AlarmWord1 = AlarmWord1 | 0x2  																				// выставляем циклическую аварию сухой ход
			TRACE("Low in pressure, cikle")
		end if
//**********************************************************************************************************************************************************************************
// РПД обработка аварий
//**********************************************************************************************************************************************************************************
		// Сдесь надо делать обратную совместимость для разных схем работы РПД
		if ((MainsPoweredPumps & 1) or (FConverterPoweredPumps & 1)) and (DigitalInput16 & 1) then																				// Побитовый перебор
			PumpStarted = PumpStarted | 0x1
		else
			PumpStarted = PumpStarted & ~0x1
		end if
		if ((MainsPoweredPumps & 2)or(FConverterPoweredPumps & 2)) and (DigitalInput16 & 2) then
			PumpStarted = PumpStarted | 0x2
		else
			PumpStarted = PumpStarted & ~0x2
		end if
		if ((MainsPoweredPumps & 4)or(FConverterPoweredPumps & 4)) and (DigitalInput16 & 4) then
			PumpStarted = PumpStarted | 0x4
		else
			PumpStarted = PumpStarted & ~0x4
		end if

		y = 0
		i = 1
		while i < 32
			if 1==1 then 																				// Если каскад с одним ПЧ
				TempUshort = FrequencyFC[0]																// То берем обратную связь с первого ПЧ
			else
				TempUshort = FrequencyFC[y] 															// Обратная связь со всех ПЧ
			end if
			if ((MainsPoweredPumps & i) or ((FConverterPoweredPumps & i) and (TempUshort >= PumpStartConfirmationFrequency))) and not (PumpStarted & i) then
				if not (StartPumpDetectionTrig & i) then 												// запускался ли алоритм ранее
					StartPumpDetectionTrig = StartPumpDetectionTrig | i 								// Ставим пометку о запуске алгоритма
					StartPumpDetectionTimePump[y] = SysMs												// Запоминаем время запуска
				else if ((SysMs >= StartPumpDetectionTimePump[y] + PumpStartConfirmationAlarmDelay) or (StartPumpDetectionTimePump[y] + PumpStartConfirmationAlarmDelay >= StartPumpDetectionTimePump[y] and SysMs < StartPumpDetectionTimePump[y])) and not (AlarmNotStartPump & i) then 	// проверяем пора ли формировать аварию
					AlarmNotStartPump = AlarmNotStartPump | i											// Формируем аварию
					SumStartPumpDetectionAlarm[y] = SumStartPumpDetectionAlarm[y] + 1 					// Увиличиваем счетчик аварий
				end if
				if AlarmNotStartPump & i then
					StartPumpDetectionTimePump[y] = SysMs												// Постоянно обнавляем время, для дальнейшего сброса аварии
				end if
			else if (SysMs >= StartPumpDetectionTimePump[y] + PumpStartConfirmationAlarmDelay) or (StartPumpDetectionTimePump[y] + PumpStartConfirmationAlarmDelay >= StartPumpDetectionTimePump[y] and SysMs < StartPumpDetectionTimePump[y]) Then		// Сброс аварии также с задержкой
				AlarmNotStartPump = AlarmNotStartPump & ~i												// Сброс аварии рпд
				StartPumpDetectionTrig = StartPumpDetectionTrig & ~i 									// Убераем пометку о запуске алгоритма

				// Сделать обнуление циклических аварий
				// SumStartPumpDetectionAlarm[y] = 0 														// Обнуляем счетчик циклических аварий
			else if not (AlarmNotStartPump & i) and ((FConverterPoweredPumps & i) and (TempUshort > PumpStartConfirmationFrequency)) then		// Если частота ниже и не авария
				StartPumpDetectionTrig = StartPumpDetectionTrig & ~i 									// Убераем пометку о запуске алгоритма
			end if
			if (((MainsPoweredPumps & i) and not (AdditionalPumpsStartsStop & 0x10)) or ((FConverterPoweredPumps & i) and (TempUshort >= PumpStartConfirmationFrequency))and not(AdditionalPumpsStartsStop & 0x40)) and (PumpStarted & i) then 																	// Если РПД сработало
				SumStartPumpDetectionAlarm[y] = 0 														// Обнуляем счетчик циклических аварий
			end if
			If (SumStartPumpDetectionAlarm[y] >= MaxAlarmConfirmationStartPump) and (MaxAlarmConfirmationStartPump > 0) then
				CycleAlarmNotStartPump = CycleAlarmNotStartPump | i 									// Циклическая авария РПД
				AlarmNasos = AlarmNasos | i																// Помечаем насос как аварийный
			end if
			y = y + 1 																				    // Десятичный перебор
			i = i+i 																				    // Двоичный перебор
		wend
//**********************************************************************************************************************************************************************************
// Критическое давление
//**********************************************************************************************************************************************************************************
		// Слово отказов 1	09AlarmWord1
		// 09AlarmDryRunning	Бит 0 = Авария сухой ход
		// 09AlarmCycleDryRunning	Бит 1 = Авария циклический сухой ход (Критическая)
		// 09AlarmCriticalPressure	Бит 2 = Авария критическое давление
		// 09AlarmCycleCriticalPressure	Бит 3 = Авария циклическое критическое давление (Критическая)
		if DischargePressure >= CriticalPressureAlarmThreshold then															// Проверяем наличие критического давления
			CriticalPressure = CriticalPressure & ~0x2 																		// Сброс пометки о начале отсчета сброса аварии
			If not CriticalPressure & 0x1 then 																				// Проверяем запускался ли алгоритм
				CriticalPressure = CriticalPressure | 0x1																	// Ставим пометку о запуске алгоритма
				CriticalPressureTime = SysMs																				// Запоминаем время
			else if (SysMs >= CriticalPressureTime + DelayCriticalPressureAlarm or (CriticalPressureTime + DelayCriticalPressureAlarm >= CriticalPressureTime and SysMs < CriticalPressureTime)) and not (AlarmWord1 & 0x4) and not (AlarmWord1 & 0x8) then						// Проверяем пора ли включать сухой ход
				AlarmWord1 = AlarmWord1 | 0x4  																			// Выставляем аварию критическое давление
				CounterCyclicAlarmCriticalPressure = CounterCyclicAlarmCriticalPressure + 1								// Подсчет аварий
				TRACE("Critical presure")
			end if
		else
			CriticalPressure = CriticalPressure & ~0x1																		// Сброс бита запуска алгоритма детекции крита
			if not CriticalPressure & 0x2 then 																				// Проверяем запускался ли алгоритм
				CriticalPressure = CriticalPressure | 0x2																	// Ставим пометку о запуске алгоритма
				CriticalPressureTime = SysMs																				// Запоминаем время
			else
				if AlarmWord1 & 0x4 then
					if SysMs >= CriticalPressureTime + DelayCriticalPressureAlarm + 50 or (CriticalPressureTime + DelayCriticalPressureAlarm + 50 >= CriticalPressureTime and SysMs < CriticalPressureTime) then
						AlarmWord1 = AlarmWord1 & ~0x4 																			// Сброс аварии
						TRACE("Reset critical presure")
					end if
					if (SysMs >= CriticalPressureTime + 6000 or (CriticalPressureTime + 6000 >= CriticalPressureTime and SysMs < CriticalPressureTime)) and not (AlarmWord1 & 0x8)   then
						CounterCyclicAlarmCriticalPressure = 0																	// Сброс счетчика аварий
					end if
				end if
			end if
		end if
		// Циклическая авария
		iF CounterCyclicAlarmCriticalPressure > MaxNumberOfAlarmCritPressure then
			TRACE("Critical presure, cikle")
			AlarmWord1 = AlarmWord1 | 0x8  																				// выставляем циклическую аварию сухой ход
			AlarmWord1 = AlarmWord1 & ~0x4 																				// Сброс аварии
		end if
	End if

//**********************************************************************************************************************************************************************************
// Ручное управление
//**********************************************************************************************************************************************************************************




//**********************************************************************************************************************************************************************************
// Режим стоп
//**********************************************************************************************************************************************************************************
	If mode == 0 or Mode == 2 then 							// Если режим стоп
		PIDOutput = 0 										// Выход ПИД 0
		PIDIterationTime = 0
		PIDError = 0                                        // ошибка регулирования
		PIDProportional = 0	 								// пропорционально ошибке регулирования
		PIDErrorDiff = 0 									// изменение входного сигнала
		PIDDerivative = 0
		PIDIntegral = 0
		FConverterPoweredPumps = 0 							// Выкл насосов от ПЧ
		MainsPoweredPumps = 0								// Выкл насосов от сети
		FrequencySetpoint = 0 								// Задание частоты в 0
		AlarmWord1 = 0 										// Сброс аварий
		CycleAlarmNotStartPump = 0 							// Сброс циклических аварий РПД
		AlarmNotStartPump = 0 								// Сброс Аварий РПД
		StartPumpDetectionTrig = 0 							// Сброс триггеров РПД
		AlarmNasos = 0 										// Сброс общих аварий насосов
		CounterCyclicAlarmCriticalPressure = 0				// Сброс счетчика аварий критическое давление
		CriticalPressure = 0								// Сброс бита запуска алгоритма детекции крита
		WarningWord1 = 0									// Сброс слова предупреждений
		DryRunning = 0
		CounterCyclicAlarmDryRunning = 0					// Сброс счетчика аварий циклический сухой ход
		AdditionalPumpsStartsStop = 0						// Сброс пометок о старте стопе допов
		PowerSavingModeBit = 0								// Выкл алгоритма энергосбережения
		SoftFillingOutControl = 0							// Выключаем алгоритм наполнения
		for i = 0 to 5
			StartPumpDetectionTimePump[i] = 0				// время сработки РПД
			SumStartPumpDetectionAlarm[i] = 0				// Сброс циклических аварий РПД
		next
	end if
	AdditionalPumpsStartsStop = AdditionalPumpsStartsStop  & ~0x40			// убираем пометку старта основного насоса


//**********************************************************************************************************************************************************************************
// Защитные маски (не используемые биты всегда должны быть в нуле)
//**********************************************************************************************************************************************************************************

//**********************************************************************************************************************************************************************************
// Тренды
//**********************************************************************************************************************************************************************************
	SetDataEx(SuctionPressure, "Local HMI", "70SuctionPressure", 1)					// Давление на входе
	SetDataEx(DischargePressure, "Local HMI", "70DischargePressure ", 1)			// Давление на выходе
	SetDataEx(DifferencePressure, "Local HMI", "70DifferencePressure", 1)			// Перепад давления
	SetDataEx(Setpoint, "Local HMI", "70Setpoint", 1)								// Уставка давления
	SetDataEx(FrequencySetpoint, "Local HMI", "70FrequencySetpoint", 1)				// Частота задание
	SetDataEx(SumFrequencyFC, "Local HMI", "70SumFrequencyFC", 1)					// Частота обратная связь
	// Пределы
	TempUshort = 0
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitLoChanel1", 1)	// Динамический предел нижний канал 1 (Давление на входе)
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitLoChanel2", 1)	// Динамический предел нижний канал 2 (Давление на выходе)
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitLoChanel3", 1)	// Динамический предел нижний канал 3 (Перепад давления)
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitLoChanel4", 1)	// Динамический предел нижний канал 4 (Уставка давления)
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitLoChanel5", 1)	// Динамический предел нижний канал 5 (Частота задание)
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitLoChanel6", 1)	// Динамический предел нижний канал 6 (Частота обратная связь)
	TempUshort = 1000
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitHiChanel1", 1)			// Динамический предел верхний канал 1 (Давление на входе)
	TempUshort = 1600
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitHiChanel2", 1)			// Динамический предел верхний канал 2 (Давление на выходе)
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitHiChanel3", 1)			// Динамический предел верхний канал 3 (Перепад давления)
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitHiChanel4", 1)			// Динамический предел верхний канал 4 (Уставка давления)
	TempUshort = 500
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitHiChanel5", 1)			// Динамический предел верхний канал 5 (Частота задание)
	SetDataEx(TempUshort, "Local HMI", "70OnlineTrendsDynamicLimitHiChanel6", 1)			// Динамический предел верхний канал 6 (Частота обратная связь)


	SetDataEx(SumFrequencyFC, "Local HMI", "01SumFrequencyFC", 1)										// Частота обратная связь

	SetDataEx(AdditionalPumpsStopKritTime, "Local HMI", "80AdditionalPumpsStopKritTime", 1)				// Сохранённое время для стопа доп насоса по критической превышении
	SetDataEx(AdditionalPumpsStopTime, "Local HMI", "80AdditionalPumpsStopTime", 1)						// Сохраненное время для стопа допа при обычном превышении

	SetDataEx(NumberPumpToStarts, "Local HMI", "01NumberPumpToStarts", 1)								// Номер насоса для старта
	SetDataEx(NumberPumpToStartIsRun, "Local HMI", "01NumberPumpToStartIsRun", 1) 						// Номер насоса из запущеных

	SetDataEx(NumberPumpToStop, "Local HMI", "01NumberPumpToStop", 1)									// Номер насоса для стопа
	// Старт стоп дополнительных насосов
	SetDataEx(AdditionalPumpsStartsStop, "Local HMI", "80AdditionalPumpsStartsStop", 1)					// Биты старта дополнительных насосов
	SetDataEx(AdditionalPumpsStartKritTime, "Local HMI", "80AdditionalPumpsStartKritTime", 1)			// Сохраненое время для старта доп насоса по критической просадке
	SetDataEx(AdditionalPumpsStartTime, "Local HMI", "80AdditionalPumpsStartTime", 1)					// Сохраненное время для старта допа при обычной просадки

	SetDataEx(FConverterPoweredPumps, "Local HMI", "01FConverterPoweredPumps", 1) 						// Кол-во насосов работающих от сети
	SetDataEx(MainsPoweredPumps, "Local HMI", "01MainsPoweredPumps", 1) 								// Кол-во насосов работающих от ПЧ
	SetDataEx(FrequencySetpoint, "Local HMI", "01FrequencySetpoint", 1)									// Задание частоты отправляемое на частотный преобразователь (ли)
	// РПД
	SetDataEx(SetpointPID, "Local HMI", "80SetpointPID", 1)												// Рассчитанная уставка для PID регулятора
	SetDataEx(AlarmNotStartPump, "Local HMI", "09AlarmNotStartPump", 1)									// Аварии по отсутствию подтверждения пуска
	SetDataEx(CycleAlarmNotStartPump, "Local HMI", "09CycleAlarmNotStartPump", 1)						// Циклические аварии по отсутствию запуска насоса (Критические аварии)
	SetDataEx(StartPumpDetectionTrig, "Local HMI", "80StartPumpDetectionTrig", 1)						// Биты алгоритма РПД. Триггеры отслеживания работы
	SetDataEx(StartPumpDetectionTimePump[0], "Local HMI", "80StartPumpDetectionTimePump1", 6)			// Время срабатывания алгоритма РПД
	SetDataEx(SumStartPumpDetectionAlarm[0], "Local HMI", "80SumStartPumpDetectionAlarm1", 6)			// Суммарное число аварий по отсутствию подтверждения пуска насосов
	// Датчики
	SetDataEx(DifferencePressure, "Local HMI", "01DifferencePressure", 1)								// Перепад давления
	SetDataEx(SuctionPressure, "Local HMI", "01SuctionPressure", 1)										// Текущее давление на всасывании насосной станции.
	SetDataEx(DischargePressure, "Local HMI", "01DischargePressure", 1)									// Текущее давление нагнетания насосной станции.
	SetDataEx(SuctionSensorMaValue, "Local HMI", "01SuctionSensorMaValue", 1)							// Значение мили ампер, датчика на всасе
	SetDataEx(DischargeSensorMaValue, "Local HMI", "01DischargeSensorMaValue", 1)						// Значение мили ампер, датчика на нагнетании
	SetDataEx(SensorsAlarm, "Local HMI", "09SensorsAlarm", 1)											// Аварии датчиков
	// PID Выходные переменные
	SetDataEx(SoftFillingOutControl, "Local HMI", "80SoftFillingOutControl", 1)							// Биты управления алгоритма плавного наполнения.
	SetDataEx(SoftFillingOutTime, "Local HMI", "80SoftFillingOutTime", 1)								// Плавное наполнение. Время текущего шага. 32 бита.
	SetDataEx(PIDIterationTime, "Local HMI", "80PIDiterationTime", 1)               					// Последнее время исполнения PID регулятора

    SetDataEx(PIDError, "Local HMI", "01PIDError", 1)
	SetDataEx(PIDErrorSum, "Local HMI", "01PIDErrorSum", 1)
	SetDataEx(PIDErrorDiff, "Local HMI", "01PIDErrorDiff", 1)
	SetDataEx(PIDProportional, "Local HMI", "01PIDProportional", 1)
	SetDataEx(PIDProportional, "Local HMI", "01PIDProportional", 1)
	SetDataEx(PIDIntegral, "Local HMI", "01PIDIntegral", 1)
	SetDataEx(PIDDerivative, "Local HMI", "01PIDDerivative", 1)
    SetDataEx(ErrorPrev, "Local HMI", "01ErrorPrev", 1)
	SetDataEx(PIDOutput, "Local HMI", "01PIDOutput", 1)
	// Переменные наполнения трубопровода
	SetDataEx(Mode, "Local HMI", "01Mode", 1)																	// Режим работы
	//SetDataEx(SoftFillingOutTime, "Local HMI", "80SoftFillingOutTime", 1)										// Время текущего шага. 32 бита.

	SetDataEx(AlarmNasos, "Local HMI", "09AlarmNasos", 1)														// Общие аварии насосов

	SetDataEx(PowerSavingModeBit, "Local HMI", "80PowerSavingModeBit", 1)										// Биты алгоритма энергосбережения
	SetDataEx(PowerSavingModeAmplitudeTime, "Local HMI", "80PowerSavingModeAmplitudeTime", 1)					// Время для расчета амплитудных значений
	SetDataEx(PowerSavingModeSignalMaxPressure, "Local HMI", "80PowerSavingModeSignalMaxPressure", 1)			// Максимальное значение давления за минуту
	SetDataEx(PowerSavingModeSignalMinPressure, "Local HMI", "80PowerSavingModeSignalMinPressure", 1)			// Минимальное значение давление за минуту
	SetDataEx(PowerSavingModeSignalMaxFrequency, "Local HMI", "80PowerSavingModeSignalMaxFrequency", 1)			// Максимальное значение частоты за минуту
	SetDataEx(PowerSavingModeSignalMinFrequency, "Local HMI", "80PowerSavingModeSignalMinFrequency", 1) 		// Минимальное значение давления за минуту
	SetDataEx(PowerSavingPeakToPeakPressure, "Local HMI", "80PowerSavingPeakToPeakPressure", 1)					// Амплитудное значение давления
	SetDataEx(PowerSavingPeakToPeakFrequency, "Local HMI", "80PowerSavingPeakToPeakFrequency", 1)				// Амплитудное значение частоты

	SetDataEx(PowerSavingModeTimeShtamp, "Local HMI", "80PowerSavingModeTimeShtamp", 1)							// Время предыдущего выполнения алгоритма
	SetDataEx(PowerSavingModeOutput, "Local HMI", "80PowerSavingModeOutput", 1)									// Выход алгоритма энергосбережения

	SetDataEx(StatusWord1, "Local HMI", "09StatusWord1", 1)														// 16 битное слово данных. Состояния системы


	SetDataEx(PumpStarted, "Local HMI", "01PumpStarted", 1)								                        // Сигналы подтверждения запуска насосов.


	// Крит
	SetDataEx(CounterCyclicAlarmDryRunning, "Local HMI", "80CounterCyclicAlarmDryRunning", 1)					// Количество аварий сухой ход
	SetDataEx(CriticalPressure, "Local HMI", "80CriticalPressure", 1)											// Биты алгоритма анализа критического давления
																												// Бит 0 = Триггер запуска аварии крит. давление
																												// Бит 1 = Триггер сброса аварии крит давление
	SetDataEx(CriticalPressureTime, "Local HMI", "80CriticalPressureTime", 1)									// Время детекции/сброса крит давления
	SetDataEx(CounterCyclicAlarmCriticalPressure, "Local HMI", "80CounterCyclicAlarmCriticalPressure", 1) 		// Количество аварий критическое давление
	// Сухой ход
	SetDataEx(AlarmWord1, "Local HMI", "09AlarmWord1", 1)														// 16 битное слово данных. Аварии
	SetDataEx(WarningWord1, "Local HMI", "09WarningWord1", 1)													// Слово предупреждений
	SetDataEx(DryRunning, "Local HMI", "80DryRunning", 1)														// Биты алгоритма анализа сухого хода
	SetDataEx(DryRunningTime, "Local HMI", "80DryRunningTime", 1)												// Время детекции сухого хода
	SetDataEx(CounterCyclicAlarmDryRunning, "Local HMI", "80CounterCyclicAlarmDryRunning", 1)					// Счетчик количества аварий сухойго хода



	// Рассортировываем последовательность битов через 1 (111111 = 10101010101)
	FConverterPoweredPumps = (FConverterPoweredPumps & 0x1)|(FConverterPoweredPumps<<1 & 0x4)|(FConverterPoweredPumps<<2 & 0x10)|(FConverterPoweredPumps<<3 & 0x40)|(FConverterPoweredPumps<<4 & 0x100)|(FConverterPoweredPumps<<5 & 0x400)
	// Рассортировываем последовательность битов через 1 (111111 = 010101010101)
	MainsPoweredPumps = (MainsPoweredPumps<<1 & 0x2)|(MainsPoweredPumps<<2 & 0x8)|(MainsPoweredPumps<<3 & 0x20)|(MainsPoweredPumps<<4 & 0x80)|(MainsPoweredPumps<<5 & 0x200)|(MainsPoweredPumps<<6 & 0x800)

	//TempUshort = FConverterPoweredPumps | MainsPoweredPumps


	GetDataEx(FConverterPoweredPumpsPrev, "Local HMI", "80FConverterPoweredPumpsPrev", 1)	// Предыдущее значение пущеных ПЧ
	GetDataEx(FCRunStatus, "Local HMI", "80FCRunStatus", 1)				// Состояние ПЧ включен выколючен
	// Защита от выключения, переключения частотника на ходу
	if FConverterPoweredPumps <> FConverterPoweredPumpsPrev then 						// Если  произошло переключение на другой ПЧ
		SetControlFC(0,0,0,0)															// Стоп ПЧ
		if FCRunStatus <= 0 then														// Проверяем остановился ли ПЧ
			FConverterPoweredPumpsPrev = FConverterPoweredPumps							// Запоминаем текущий ПЧ
		end if
	else
		if FConverterPoweredPumps <= 0 then
			SetControlFC(0,0,0,0)
		else
		 	if (PowerSavingModeBit & 1) and SumFrequencyFC <= 5 then
				SetControlFC(0,0,0,0)
			else
				SetControlFC(1,0,PIDOutput,0)
			end if
		end if
	end if



	TempUshort = FConverterPoweredPumpsPrev | MainsPoweredPumps
	SetDataEx(TempUshort, "ABB_PCH", 4x, 1#1, 1)											// Переключаем ПЧ
	SetDataEx(FConverterPoweredPumpsPrev, "Local HMI", "80FConverterPoweredPumpsPrev", 1)	// Предыдущее значение пущеных ПЧ


	//	If FConverterPoweredPumps <> DigitalOutput16 then									// сравниваем текущее значение выходов с новым
		//SetDataEx(TempUshort, "ABB_PCH", 4x, 1#1, 1) 										// Отправляем данные на наш контроллер
	//	end if

	wend
end macro_command