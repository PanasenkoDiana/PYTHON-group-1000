from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel
from modules.app import app

main_window = QMainWindow()

MAIN_WINDOW_HEIGHT = 800
MAIN_WINDOW_WIDTH = 1024

primary_screen = app.primaryScreen()
primary_screen_size = primary_screen.size()
primary_screen_width = primary_screen_size.width()
primary_screen_height = primary_screen_size.height()

main_window.setGeometry(
    (primary_screen_width // 2) - (MAIN_WINDOW_WIDTH // 2),
    (primary_screen_height // 2) - (MAIN_WINDOW_HEIGHT // 2),
    MAIN_WINDOW_WIDTH,
    MAIN_WINDOW_HEIGHT,
)

frame1 = QFrame(parent=main_window)
# QFrame - створює новий фрейм-віджет
# parent= - вказуємо батьківський фрейм-віджет у якому він буде створений
frame1.setStyleSheet("background-color: gray")
# setStyleSheet - метод який дозволяє задавати зовнішній вигляд елементу
frame1.setFixedSize(600, 600)
# setFixedSize - забороняє користувачу змінювати розмір цього єлементу

# Лейаут - це механізм який допомагає розташовувати єлементи у конкретному напряму
# 1. Вертикальний QVBoxLayout
# 2. Горизонтальний QHBoxLayout
# 3. Сіткою QGridLayout

# QLabel - єлемент для відображення тексту чи зображення

# На цій строчці ми створюємо правило того як будуть розташовуватися єлементи
frame1_layout = QVBoxLayout()
# setLayout - дозволяє встановити правило розміщення єлементів для конкретного фрейму
frame1.setLayout(frame1_layout)

element_frame1 = QFrame(parent=frame1)
element_frame1.setStyleSheet("background-color: green")
element_frame1.setFixedSize(100, 100)
frame1_layout.addWidget(element_frame1)
# addWidget - метод який окремо додає віджет в лейаут.
# Це необхідний єтап для розміщення віджета за правилами лейаут

element_frame2 = QFrame(parent=frame1)
element_frame2.setStyleSheet("background-color: blue")
element_frame2.setFixedSize(100, 100)
frame1_layout.addWidget(element_frame2)

element_frame3 = QFrame(parent=frame1)
element_frame3.setStyleSheet("background-color: orange")
element_frame3.setFixedSize(100, 100)
frame1_layout.addWidget(element_frame3)


element_frame4 = QFrame(parent=frame1)
element_frame4.setStyleSheet("background-color: orange")
element_frame4.setFixedSize(100, 100)
frame1_layout.addWidget(element_frame4)