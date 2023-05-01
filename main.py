from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal


class GenerateThread(QThread):
    text_generated = pyqtSignal(str)

    def __init__(self, model, input_text):
        super().__init__()
        self.model = model
        self.input_text = input_text
        self._is_running = True

    def run(self):
        def new_text_callback(text):
            if self._is_running:
                self.text_generated.emit(text)

        self.model.generate(self.input_text, n_predict=2048, new_text_callback=new_text_callback)

    def stop(self):
        self._is_running = False


class GPT4AllApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("GPT4All App")

        # Create widgets
        self.label = QLabel("물어볼 거 : ")
        self.input_box = QTextEdit()
        self.generate_button = QPushButton("Generate")
        self.stop_button = QPushButton("Stop")
        self.result_label = QLabel("결과 : ")
        self.result_box = QTextEdit()

        # Set result_box to read-only mode
        self.result_box.setReadOnly(True)

        # Create layout
        vbox = QVBoxLayout()

        vbox.addWidget(self.label)
        vbox.addWidget(self.input_box)
        vbox.addWidget(self.generate_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.result_box)

        # Set the layout
        self.setLayout(vbox)

        # Connect generate_button to generate_text
        self.generate_button.clicked.connect(self.generate_text)
        self.stop_button.clicked.connect(self.stop_thread)

        # Show the window
        self.show()

        # Load the GPT model
        self.model = None

    def generate_text(self):
        if not self.model:
            file_path, _ = QFileDialog().getOpenFileName()
            if len(file_path) == 0:
                return
            if "ggml-gpt4all-j" in file_path:
                from pygpt4all.models.gpt4all_j import GPT4All_J
                self.model = GPT4All_J(file_path)
            else:
                from pygpt4all.models.gpt4all import GPT4All
                self.model = GPT4All(file_path)

        input_from_user = self.input_box.toPlainText()

        # Clear previous result
        self.result_box.clear()

        # Create and start the thread
        self.generate_thread = GenerateThread(self.model, input_from_user)
        self.generate_thread.text_generated.connect(self.update_result_box)
        self.generate_thread.start()

    def update_result_box(self, text):
        self.result_box.setText(self.result_box.toPlainText() + text)

    def stop_thread(self):
        if self.generate_thread.isRunning():
            self.generate_thread.stop()


if __name__ == '__main__':
    app = QApplication([])
    gpt4all_app = GPT4AllApp()
    app.exec_()
