from PyQt6.QtWidgets import QLabel, QMainWindow, QHBoxLayout, QPushButton, QFrame
# PyQt6.QtGui — это модуль библиотеки PyQt6, который содержит классы для работы с:
# графикой, изображениями, шрифтами, цветами и другими визуальными элементами.
from PyQt6.QtGui import QImage, QMouseEvent, QPixmap
from PyQt6.QtCore import Qt

from PIL import Image
from PIL.ImageQt import ImageQt

import os
import dotenv
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

        # 1. Открываем изображение
        # Image — класс из библиотеки Pillow для работы с изображениями.
        # open() — метод, который открывает изображение по указанному пути.
        image = Image.open("assets/images/images.jpg")

        # 2. Преобразуем изображение для Qt
        # ImageQt() преобразует изображение Pillow в формат, с которым может работать Qt (PyQt6).
        # Это необходимо, потому что Pillow и PyQt6 используют разные классы для работы с изображениями.
        QtImage = ImageQt(image)

        # 3. Создаём QPixmap
        # QImage — класс Qt для хранения и обработки изображений.
        # QPixmap — класс Qt, предназначенный для отображения изображений в интерфейсе.
        pixmap = QPixmap(QImage(QtImage))

        # 4. Задаём размер изображения
        # Метод scaled() изменяет размер изображения до 200 × 200 пикселей.
        pixmap = pixmap.scaled(200, 200)

        # 5. Создаём область для изображения
        # QLabel используется для отображения текста или изображений в окне приложения.
        self.label = QLabel(parent=self)

        # 6. Устанавливаем размер области
        self.label.setFixedSize(200, 200)

        # 7. Отображаем изображение
        # Метод setPixmap() помещает изображение внутрь QLabel.
        self.label.setPixmap(pixmap)

    def button_clicked(self):
        dotenv.load_dotenv()
       
        city_name = "Dnipro"
        api_key = os.getenv("API_KEY")

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        )

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
    
main_window = MainWindow(800, 600, 0, 0, "grey", "mashina")


        
