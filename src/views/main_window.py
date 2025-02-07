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
        
        index = self.select_compress.findText("Padrão") # Remove a opção padrão do select_compress quando inicia o programa
        if index != -1:
            self.select_compress.removeItem(index)
        self.input_password.hide() # Oculta o campo de senha
        self.label_password.hide()
        self.input_repeat.hide() # Oculta o campo de confirmação de senha
        self.label_repeat.hide()
        self.slider_level.hide() # Oculta a label de números
        self.label_level.hide() # Oculta a label de nível de compressão
        self.hide_layout(self.label_numbers) # Oculta os números

        
        
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
        
    def update_file_count(self, count):
        self.label_file_count.setText(f"{count}")
        
    def hide_layout(self, layout):
        """Esconde todos os widgets dentro de um layout."""
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.hide()
                
    def show_layout(self, layout):
        """Esconde todos os widgets dentro de um layout."""
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.show()