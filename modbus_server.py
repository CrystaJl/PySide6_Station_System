from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

def run_server():
    # Создание блока данных для хранения регистров
    block = ModbusSequentialDataBlock(0, [0] * 100)
    store = ModbusSlaveContext(hr=block, di=block, co=block, ir=block)
    context = ModbusServerContext(slaves=store, single=True)

    # Настройка идентификационной информации сервера
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
    identity.ProductName = 'pymodbus Server'
    identity.ModelName = 'pymodbus Server'
    identity.MajorMinorRevision = '1.0'

    # Запуск сервера на порту 5020
    StartTcpServer(context, identity=identity, address=("localhost", 5020))

if __name__ == "__main__":
    run_server()
