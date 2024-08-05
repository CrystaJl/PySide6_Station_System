from pymodbus.client import ModbusTcpClient
import logging

# Настройка логирования для отладки
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def main():
    # Настройка подключения
    client = ModbusTcpClient('127.0.0.1')  # Укажите IP адрес вашего Modbus TCP сервера

    # Подключение
    if client.connect():
        print("Подключено к серверу")

        # Чтение данных
        # Чтение Holding Registers (адрес 0, количество 2 регистров)
        result = client.read_holding_registers(0, 2)
        if result.isError():
            print("Ошибка при чтении данных:", result)
        else:
            print("Данные из регистров:", result.registers)

        # Запись данных
        # Запись в Holding Register (адрес 0, значение 1234)
        write_result = client.write_register(7, 1234)
        if write_result.isError():
            print("Ошибка при записи данных:", write_result)
        else:
            print("Данные успешно записаны")

        # Закрытие подключения
        client.close()
    else:
        print("Не удалось подключиться к серверу")

if __name__ == '__main__':
    main()
