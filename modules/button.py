from PyQt6.QtWidgets import QPushButton
class Button(QPushButton):
    def __init__(self, text, parent, width, height, background, text_color ):
        super().__init__(text, parent)
        self.width = width
        self.height = height
        self.background = background
        self.text_color = text_color
        self.setStyleSheet(
            f'background-color: {self.background};'
            f'color: {self.text_color};'  
        )
        self.setFixedSize(self.width, self.height)
    