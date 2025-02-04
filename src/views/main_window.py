# views/main_window.py
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QFileDialog
from .ui.Window import Ui_Window

class Window(QWidget, Ui_Window):
    file_dropped = Signal(list)  # Sinal customizado para drag-and-drop

    def __init__(self):
        super().__init__()
        self._setup_UI()        
        self.drag_and_drop.hide()  # Oculta o Qframe
        
    def _setup_UI(self):
        self.setupUi(self)

    def open_file_dialog(self, init_dir):
        return QFileDialog.getOpenFileNames(self, "Escolha os arquivos:", init_dir)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.drag_and_drop.show()
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            files = [url.toLocalFile() for url in event.mimeData().urls()]
            self.drag_and_drop.hide()  # Oculta o Qframe            
            self.file_dropped.emit(files)

    # Detecta quando o arrasto sai da área sem soltar
    def dragLeaveEvent(self, event):
        self.drag_and_drop.hide()  # Oculta o Qframe
        event.accept()