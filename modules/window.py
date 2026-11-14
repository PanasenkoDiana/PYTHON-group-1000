from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QFrame
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
        
        self.setStyleSheet(f"background-color: {self.background_color};")
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height )

        self.main_frame = QFrame(parent=self)
        self.setCentralWidget(self.main_frame)

        self.main_layout = QHBoxLayout()
        self.main_frame.setLayout(self.main_layout)
        self.button = QPushButton(text="Click me!", parent=self.main_frame)
        self.button.setFixedSize(200, 50)
        self.button.setStyleSheet("""
            background-color: blue;
            color: black;
            font-size: 16px;
            padding: 5px;
        """)
        self.main_layout.addWidget(self.button)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # Указываем название города, для которого хотим получить информацию о погоде.
        # В дальнейшем пользователь сможет самостоятельно вводить название города.
        city_name = "Dnipro"


        # API-ключ — это специальный код, который выдаётся сайтом.
        # Он позволяет нашей программе пользоваться возможностями этого сайта.
        # Многие сайты требуют такой ключ, чтобы понимать, кто обращается к их сервису.
        api_key = "api_key"


        # requests.get() используется для получения информации из интернета.
        # С его помощью наша программа обращается к другому сайту и просит предоставить данные.
        #
        # Внутри мы указываем специальный адрес сайта (URL).
        # q={city_name} — передаём название города, погоду которого хотим узнать.
        # appid={api_key} — передаём наш специальный ключ.
        #
        # Полученную от сайта информацию сохраняем в переменную response.
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        )


        # .json() используется для получения информации в специальном формате JSON.
        # Этот формат часто используется сайтами для передачи информации между программами.
        # Благодаря ему Python может удобно работать с полученными данными.
        #
        # Результат сохраняем в переменную response_data.
        response_data = response.json()


        # print() выводит полученную информацию в консоль.
        # В результате мы увидим данные о погоде выбранного города.
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
    
main_window = MainWindow(800, 600, 0, 0, "grey", "mashina")


        
