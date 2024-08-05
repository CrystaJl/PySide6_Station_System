import sys
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from PySide6.QtCore import QTimer, Qt, QRect
from PySide6.QtGui import QPen
from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QMainWindow

def load_json_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

def update_graph(graphics_view, json_file):
    data = load_json_data(json_file)
    scene = graphics_view.scene()
    scene.clear()
    pen = QPen(Qt.blue)
    if 'values' in data:
        values = data['values']
        for i in range(len(values) - 1):
            line = QGraphicsLineItem(i * 100, values[i], (i + 1) * 100, values[i + 1])
            line.setPen(pen)
            scene.addItem(line)

def on_modified(event, graphics_view, json_file):
    if event.src_path.endswith(json_file):
        update_graph(graphics_view, json_file)

def main():
    json_file = 'testing.json'
    app = QApplication(sys.argv)
    
    main_window = QMainWindow()
    main_window.setWindowTitle("Real-Time Graph Viewer")
    main_window.resize(800, 600)
    
    scene = QGraphicsScene(graphics_view)
    graphics_view.setScene(scene)
    main_window.setCentralWidget(graphics_view)
    
    update_graph(graphics_view, json_file)
    
    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            on_modified(event, graphics_view, json_file)
    
    observer = Observer()
    event_handler = Handler()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    
    timer = QTimer()
    timer.timeout.connect(lambda: update_graph(graphics_view, json_file))
    timer.start(1000)  # Обновление каждую секунду
    
    main_window.show()

    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
