from PyQt6.QtWidgets import QMainWindow , QFrame , QHBoxLayout 
from .button import *
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtCore import Qt
import requests

#setFixedSize - встановлює фіксований розмір лише  ширини та  висоти
#setGeometry - встановлює позицію х та у ширину та висоту


class MainWindow(QMainWindow):
    def __init__(self, width, height, x, y, background, title):
        QMainWindow.__init__(self) 
        self.width = width
        self.height = height
        self.x = x 
        self.y = y
        self.title = title
        self.background_color = background
        
        self.setStyleSheet(f"""background-color: {self.background_color};""")
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.frame = QFrame(parent=self)
        self.setCentralWidget(self.frame)
        self.layout = QHBoxLayout()
        self.frame.setLayout(self.layout)
        self.button = Button("Click me", self.frame, 100, 50, "green","black")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.mouseClick)
        
    def mouseClick(self):
        # print("cliclre")        
        
        city_name = "Dnipro"
        api_key = 
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        )

        # Змінна яка буде зберігати отримані данні у вигляді json
        # JSON (JavaScript Object Notation) - це легкий текстовий формат
        # для обміну даними. Він базується на синтаксисі JavaScript, але є
        # незалежним від мов програмування
        # Які типи даних приймає json:
        # 1. Рядок (String)
        # 2. Число (Number)
        # 3. Логічний тип (Boolean)
        # 4. Масив (Array)
        # 5. Об'єкт (Object)
        # 6. Null - відсутність даних
        response_data = response.json()
        print(response_data)

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


main_window = MainWindow(800, 400, 0, 0, "grey", "mashina")


        
