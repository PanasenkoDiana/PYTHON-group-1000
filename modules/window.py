
from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from modules.app import app

main_window = QMainWindow()

MAIN_WINDOW_WIDTH = 1024
MAIN_WINDOW_HEIGHT = 800

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

# Створюємо головний фрейм який будет створений у вікні main_window
frame1 = QFrame(parent=main_window)
frame1.setStyleSheet("background-color: green")
frame1.setFixedSize(MAIN_WINDOW_WIDTH,MAIN_WINDOW_HEIGHT)

frame1_layout = QHBoxLayout()

frame1_layout.setSpacing(0)
frame1_layout.setContentsMargins(100, 0, 0, 0)

frame1_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

frame1.setLayout(frame1_layout)

frame2 = QFrame(parent=frame1)
frame2.setStyleSheet("background-color: gray")
frame2.setFixedSize(100, 100)
frame1_layout.addWidget(frame2)

frame3 = QFrame(parent=frame1)
frame3.setStyleSheet("background-color: black")
frame3.setFixedSize(100, 100)
frame1_layout.addWidget(frame3)

frame4 = QFrame(parent=frame1)
frame4.setStyleSheet("background-color: white")
frame4.setFixedSize(100, 100)
frame1_layout.addWidget(frame4)
