import os
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QIcon, QPixmap, QPainter
from PySide6.QtCore import Qt

def set_svg_icon(button, icons_dir, svg_filename):
    svg_path = os.path.join(icons_dir, svg_filename)

    # Создаем QSvgWidget и загружаем SVG-файл
    svg_widget = QSvgWidget(svg_path)
    svg_widget.renderer().load(svg_path)
    
    # Получаем размер оригинального SVG
    original_size = svg_widget.renderer().defaultSize()
    width = original_size.width()
    height = original_size.height()

    # Создаем QPixmap и отрисовываем SVG на нем
    svg_image = QPixmap(width, height)
    svg_image.fill(Qt.transparent)  # Делаем фон прозрачным

    painter = QPainter(svg_image)
    svg_widget.renderer().render(painter)
    painter.end()

    # Создаем иконку из QPixmap
    icon = QIcon(svg_image)

    # Устанавливаем иконку для кнопки
    button.setIcon(icon)
    button.setIconSize(svg_image.size())
    button.setText('')  # Убираем текст с кнопки

# Пример использования
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout, QWidget
    
    app = QApplication([])
    
    main_window = QMainWindow()
    central_widget = QWidget()
    layout = QVBoxLayout()
    central_widget.setLayout(layout)
    main_window.setCentralWidget(central_widget)
    
    button = QPushButton()
    layout.addWidget(button)
    
    icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    set_svg_icon(button, icons_dir, 'erere.svg')
    
    main_window.show()
    
    app.exec()
