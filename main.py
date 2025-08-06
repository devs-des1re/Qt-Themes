# Libraries
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton,
    QLineEdit, QTextEdit,
    QComboBox, QSlider,
    QCheckBox, QRadioButton
)
from PySide6.QtCore import Qt
import sys

# Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.WIDTH = 500
        self.HEIGHT = 500
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setWindowTitle("Themes")

        self.__init__UI()
        self.set_stylesheet("dark", "red")

    def __init__UI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Push Button
        self.button_label = QLabel("Push Button:")
        self.button = QPushButton("Click Me!")

        self.main_layout.addWidget(self.button_label)
        self.main_layout.addWidget(self.button)

        # Line Edit
        self.lineedit_label = QLabel("Line Edit:")
        self.lineedit = QLineEdit(placeholderText="Enter Text Here...")

        self.main_layout.addWidget(self.lineedit_label)
        self.main_layout.addWidget(self.lineedit)
        
        # Text Edit
        self.textedit_label = QLabel("Text Edit:")
        self.textedit = QTextEdit(placeholderText="Enter Text Here...")

        self.main_layout.addWidget(self.textedit_label)
        self.main_layout.addWidget(self.textedit)

        # Combo Box
        self.combobox_label = QLabel("Combo Box:")
        self.combobox = QComboBox()
        self.combobox.addItems(["Option 1", "Option 2", "Option 3"])

        self.main_layout.addWidget(self.combobox_label)
        self.main_layout.addWidget(self.combobox)

        # Check Box / Radio Button (Selection Category)
        self.selection_layout = QHBoxLayout()
        self.main_layout.addLayout(self.selection_layout)

        self.checkbox_layout = QVBoxLayout()
        self.radio_layout = QVBoxLayout()
        self.selection_layout.addLayout(self.checkbox_layout)
        self.selection_layout.addLayout(self.radio_layout)

        ### Check Box
        self.checkbox_label = QLabel("Check Box:")
        self.checkbox = QCheckBox("Check Box")

        self.checkbox_layout.addWidget(self.checkbox_label)
        self.checkbox_layout.addWidget(self.checkbox)

        ### Radio Button
        self.radio_label = QLabel("Radio Button:")

        self.radiobuttons_layout = QHBoxLayout()
        self.radio1_button = QRadioButton("Radio 1")
        self.radio2_button = QRadioButton("Radio 2")
        self.radio1_button.setChecked(True)
        self.radiobuttons_layout.addWidget(self.radio1_button)
        self.radiobuttons_layout.addWidget(self.radio2_button)

        self.radio_layout.addWidget(self.radio_label)
        self.radio_layout.addLayout(self.radiobuttons_layout)

        # Slider
        self.slider_label = QLabel("Slider:")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setValue(50)

        self.main_layout.addWidget(self.slider_label)
        self.main_layout.addWidget(self.slider)

    def set_stylesheet(self, apperance, stylesheet):
        with open(f"stylesheets/{apperance}/{stylesheet}.txt", "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

# Main
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()