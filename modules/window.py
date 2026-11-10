from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtCore import Qt
#setFixedSize - встановлює фіксований розмір лише  ширини та  висоти
#setGeometry - встановлює позицію х та у ширину та висоту


class MainWindow(QMainWindow):
    def __init__(self, width, height, x, y, background, title, text_color ):
        QMainWindow.__init__(self) 
        self.width = width
        self.height = height
        self.x = x 
        self.y = y
        self.title = title
        self.background_color = background
        self.text_color = text_color
        
        self.setStyleSheet(f"""background-color: {self.background_color};
                                color: {self.text_color}""")
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height )

    # a0 - це параметр (аргумент) який зберігає об'єкт події
    # В ньому зберігається інформація про клік: яка кнопка була натиснута та в якій координаті
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.RightButton:
            print("right mouse button")
        elif event.button() == Qt.MouseButton.LeftButton:
            print("more lefter mouse button")
            
        return super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.RightButton:
            print("right mouse button2")
        elif event.button() == Qt.MouseButton.LeftButton:
            print("more lefter mouse button2")
            
        return super().mouseReleaseEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent):
        print(event.pos())
        return super().mouseMoveEvent(event)
    
main_window = MainWindow(800, 100, 0, 500, "grey", "mashina", "blue")


        
