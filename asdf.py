import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt, QTimer


class ProgressBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Progress Bar Demo")
        self.setGeometry(100, 100, 400, 200)

        # Create central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Create progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)

        # Create start button
        self.start_button = QPushButton("Start Progress")
        self.start_button.clicked.connect(self.start_progress)

        # Create reset button
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_progress)

        # Add widgets to layout
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)

        # Set central widget
        self.setCentralWidget(central_widget)

        # Create timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        # Initialize progress value
        self.progress_value = 0

    def start_progress(self):
        # Start timer to update progress every 100ms
        if not self.timer.isActive():
            self.start_button.setEnabled(False)
            self.timer.start(100)

    def update_progress(self):
        # Update progress value
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar.setValue(self.progress_value)
        else:
            self.timer.stop()
            self.start_button.setEnabled(True)

    def reset_progress(self):
        # Reset progress bar
        self.timer.stop()
        self.progress_value = 0
        self.progress_bar.setValue(0)
        self.start_button.setEnabled(True)


def main():
    # Create application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = ProgressBarDemo()
    window.show()

    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
