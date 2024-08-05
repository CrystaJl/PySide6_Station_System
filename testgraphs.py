import sys
import json
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from io import BytesIO

class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def plot(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y, marker='o')
        self.ax.set_xlabel('X axis')
        self.ax.set_ylabel('Y axis')
        self.ax.set_title('Sample Graph')
        self.draw()

    def figure_to_image(self):
        # Save figure to an image buffer
        buf = self.figure_to_buffer()
        img = QImage()
        img.loadFromData(buf.getvalue())
        return img

    def figure_to_buffer(self):
        buf = BytesIO()
        self.figure.savefig(buf, format='png')
        buf.seek(0)
        return buf

class MainWindow(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setRenderHint(QPainter.TextAntialiasing)
        
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Load data from JSON
        with open('testing.json', 'r') as file:
            data = json.load(file)
        
        x = data['x']
        y = data['y']

        # Create matplotlib widget
        self.matplotlib_widget = MatplotlibWidget()
        self.matplotlib_widget.plot(x, y)

        # Save matplotlib figure to QPixmap
        img = self.matplotlib_widget.figure_to_image()
        pixmap = QPixmap.fromImage(img)

        # Create QGraphicsPixmapItem and add to scene
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmap_item)

        # Enable scaling
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setRenderHint(QPainter.TextAntialiasing)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.setSceneRect(self.scene.itemsBoundingRect())
        self.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
