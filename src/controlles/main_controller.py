from pathlib import Path

class MainController:
    def __init__(self, view):
        self.view = view
        self._files = set()  # Permite apenas arquivos unicos na lista
        self._filesCount = len(self._files)
        self._connect_signals()

    def _connect_signals(self):
        self.view.btn_load.clicked.connect(self.load_files)
        self.view.file_dropped.connect(self.add_files)
        self.view.select_method.currentTextChanged.connect(self.update_ui_controls)

    def update_ui_controls(self, selected_format):
        """
        Atualiza a visibilidade dos controles de senha e nível de compressão
        com base na opção selecionada no QComboBox.
        """
        if selected_format == "TAR":
            # Desabilita as labels e inputs desnecessarios
            self.view.input_password.hide()
            self.view.label_password.hide()
            self.view.input_repeat.hide()
            self.view.label_repeat.hide()
            self.view.slider_level.hide()
            self.view.label_level.hide()
            self.view.hide_layout(self.view.label_numbers)
            
            # Habilita as label e select do tipo de compressao
            self.view.label_compress.show()
            self.view.select_compress.show()
            
            # Remove opção Padrão que não é usada no TAR
            index = self.view.select_compress.findText("Padrão")
            if index != -1:
                self.view.select_compress.removeItem(index)
                
            # Volta a adicionar a opção Nenhum que possa ter sido removida quando mudou o metodo    
            self.view.select_compress.insertItem(0, "Nenhum")
            self.view.select_compress.setCurrentIndex(0)
            
            # Lida com a segunda opção do metodo de compressão (que pode ser escolhido no modo TAR ou ZIP)
            self.view.select_compress.currentTextChanged.connect(self.check_secondary_combobox)
            
        elif selected_format == "ZIP":
            
            # Habilita as labels e inputs nescessarios
            self.view.input_password.show()
            self.view.label_password.show()
            self.view.input_repeat.show()
            self.view.label_repeat.show()
            self.view.slider_level.show()
            self.view.label_level.show()
            self.view.show_layout(self.view.label_numbers)
            self.view.label_compress.show()
            self.view.select_compress.show()
            
            # Remove opção Nenhum que não é usada no ZIP
            index = self.view.select_compress.findText("Nenhum")
            if index != -1:
                self.view.select_compress.removeItem(index)
                
            # Volta a adicionar a opção Padrão que possa ter sido removida quando mudou o metodo
            self.view.select_compress.insertItem(0, "Padrão")
            self.view.select_compress.setCurrentIndex(0)
            
            # Lida com a segunda opção do metodo de compressão (que pode ser escolhido no modo TAR ou ZIP)
            self.view.select_compress.currentTextChanged.connect(self.check_secondary_combobox)
            
        elif selected_format == "GZ" or selected_format == "LZMA":
            
            # Habilita as labels e inputs nescessarios
            self.view.input_password.show()
            self.view.label_password.show()
            self.view.input_repeat.show()
            self.view.label_repeat.show()
            
            # Desabilita as labels e inputs desnecessarios
            self.view.slider_level.hide()
            self.view.label_level.hide()
            self.view.hide_layout(self.view.label_numbers)
            self.view.label_compress.hide()
            self.view.select_compress.hide()
            
            # Remove a opção Nenhum pois sera adicionado no modo TAR
            index = self.view.select_compress.findText("Nenhum")
            if index != -1:
                self.view.select_compress.removeItem(index)
            
    def check_secondary_combobox(self, current_text):
        """
        Verifica a seleção do QComboBox secundário e exibe os campos de senha
        se a opção selecionada não for "Nenhum".
        """
        # Habilita as labels e inputs nescessarios se o modo escolhido for 
        # TAR e o modo de compressão for diferente de Nenhum
        if current_text != "Nenhum":
            self.view.input_password.show()
            self.view.label_password.show()
            self.view.input_repeat.show()
            self.view.label_repeat.show()
        else:
            self.view.input_password.hide()
            self.view.label_password.hide()
            self.view.input_repeat.hide()
            self.view.label_repeat.hide()

        if current_text == "Padrão":
            self.view.slider_level.show()
            self.view.label_level.show()
            self.view.show_layout(self.view.label_numbers)
        else:
            self.view.slider_level.hide()
            self.view.label_level.hide()
            self.view.hide_layout(self.view.label_numbers)

    def load_files(self):
        init_dir = self.view.input_files.text() or str(Path.home())
        files, _ = self.view.open_file_dialog(init_dir)

        self.add_files(files)

    def add_files(self, files):
        for file in files:
            file_path = Path(file)
            if (
                file_path.exists() and file_path not in self._files
            ):  # Verifica se o arquivo existe e se já não foi adicionado
                self._files.add(file_path)
                self.view.list_files.addItem(file_path.name)
        self._filesCount = len(self._files)
        self.view.update_file_count(self._filesCount)
