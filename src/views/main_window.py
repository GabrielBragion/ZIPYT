# views/main_window.py
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from .ui.Window import Ui_Window


class Window(QWidget, Ui_Window):
    file_dropped = Signal(list)  # Sinal customizado para drag-and-drop

    def __init__(self):
        super().__init__()
        self._setup_UI()
        self.drag_and_drop.hide()  # Oculta o Qframe

        index = self.select_compress.findText(
            "Padrão"
        )  # Remove a opção padrão do select_compress quando inicia o programa
        if index != -1:
            self.select_compress.removeItem(index)
        self.input_password.hide()  # Oculta o campo de senha
        self.label_password.hide()
        self.input_repeat.hide()  # Oculta o campo de confirmação de senha
        self.label_repeat.hide()
        self.slider_level.hide()  # Oculta a label de números
        self.label_level.hide()  # Oculta a label de nível de compressão
        self.hide_layout(self.label_numbers)  # Oculta os números
        self.btn_exec.setDisabled(True)

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

    def reset_view(self):
        """Reseta os campos de input e outros widgets ao estado inicial do programa."""
        self.input_files.clear()  # Limpa o campo de input de arquivos
        self.list_files.clear()  # Limpa a lista de arquivos
        self.select_method.setCurrentIndex(
            0
        )  # Reseta o método de compressão para o padrão
        self.select_compress.setCurrentIndex(
            0
        )  # Reseta o tipo de compressão para o padrão
        self.input_password.clear()  # Limpa o campo de senha
        self.input_repeat.clear()  # Limpa o campo de repetição de senha
        self.slider_level.setValue(0)  # Reseta o slider de nível de compressão
        self.hide_layout(self.label_numbers)  # Esconde o layout de números
        self.label_password.hide()  # Esconde a label de senha
        self.input_password.hide()  # Esconde o campo de senha
        self.label_repeat.hide()  # Esconde a label de repetição de senha
        self.input_repeat.hide()  # Esconde o campo de repetição de senha
        self.label_level.hide()  # Esconde a label de nível de compressão
        self.slider_level.hide()  # Esconde o slider de nível de compressão
        self.label_file_count.setText("")
        self.checkbox_delete.setChecked(
            False
        )  # Desmarca a opção de deletar arquivos originais

    def show_message(self, title, message):
        """Mostra uma mensagem tipo toast."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
