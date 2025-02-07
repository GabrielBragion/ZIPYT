from pathlib import Path
import os
from ..models.compressor.tar_compressor import TarCompressor
from ..models.compressor.gz_compressor import GzCompressor
from ..models.encryptor.encryptor import Encryptor
from ..models.compressor.zip_compressor import ZipCompressor


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
        self.view.select_compress.currentTextChanged.connect(
            self.check_secondary_combobox
        )
        self.view.btn_exec.clicked.connect(self.compress_files)

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
            self.view.select_compress.currentTextChanged.connect(
                self.check_secondary_combobox
            )

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
            index_nenhum = self.view.select_compress.findText("Nenhum")
            index_gzip = self.view.select_compress.findText("GZIP")

            if index_nenhum != -1:
                self.view.select_compress.removeItem(index_nenhum)

            if index_gzip != -1:
                self.view.select_compress.removeItem(index_gzip)

            # Volta a adicionar a opção Padrão que possa ter sido removida quando mudou o metodo
            self.view.select_compress.insertItem(0, "Padrão")
            self.view.select_compress.setCurrentIndex(0)

            # Lida com a segunda opção do metodo de compressão (que pode ser escolhido no modo TAR ou ZIP)
            self.view.select_compress.currentTextChanged.connect(
                self.check_secondary_combobox
            )

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

    def load_files(self):
        init_dir = self.view.input_files.text() or str(Path.home())
        self.view.input_files.setText(
            init_dir
        )  # Atualiza o input_files com o diretório inicial
        files, _ = self.view.open_file_dialog(init_dir)

        if files:
            # Atualiza o input_files com o diretório dos arquivos selecionados
            selected_dir = str(Path(files[0]).parent)
            self.view.input_files.setText(selected_dir)

            # Salva o diretório selecionado para uso posterior
            self.selected_dir = selected_dir

        self.add_files(files)

    def compress_files(self):
        """
        Método para comprimir os arquivos selecionados.
        """
        try:
            if not self._files:
                self.view.show_message(
                    "Erro", "Nenhum arquivo selecionado para compressão."
                )
                return

            selected_format = self.view.select_method.currentText()
            selected_compress = self.view.select_compress.currentText()
            password = self.view.input_password.text()
            password_repeat = self.view.input_repeat.text()
            compression_level = self.view.slider_level.value()

            if selected_format == "TAR":
                # Usa o diretório selecionado para criar o arquivo TAR
                archive_name = os.path.join(self.selected_dir, "meu_arquivo.tar")
                compressor = TarCompressor(archive_name)
                compressor.create_tar(list(self._files))

                if selected_compress == "GZIP":
                    gz_archive_name = f"{archive_name}.gz"
                    compressor = GzCompressor(archive_name)
                    compressor.create_gz(archive_name)
                    os.remove(
                        archive_name
                    )  # Remove o arquivo TAR original após criar o GZ

                    if len(password) > 0:
                        encryptor = Encryptor(password, password_repeat)
                        encryptor.encrypt_file(gz_archive_name)
                        os.remove(
                            gz_archive_name
                        )  # Remove o arquivo TAR.GZ original após criar o TAR.GZ.ENC

            elif selected_format == "GZ":
                for file in self._files:
                    compressor = GzCompressor(file)
                    gz_file = compressor.create_gz(file)

                    if len(password) > 0:
                        encryptor = Encryptor(password, password_repeat)
                        encryptor.encrypt_file(gz_file)
                        os.remove(
                            gz_file
                        )  # Remove o arquivo GZ original após criar o GZ.ENC

            elif selected_format == "ZIP":
                # Usa o diretório selecionado para criar o arquivo ZIP
                archive_name = os.path.join(self.selected_dir, "meu_arquivo.zip")
                if len(password) > 0 and password == password_repeat:
                    compressor = ZipCompressor(
                        archive_name,
                        compression_method=selected_compress,
                        compression_level=compression_level,
                        password=password,
                    )
                    compressor.create_zip(list(self._files))
                else:
                    self.view.show_message("Erro", "Palavras passes diferentes")

            # Exclui os arquivos originais se a opção estiver marcada
            self.delete_original_files(self._files)

            # Reseta a view após a compressão
            self.view.reset_view()
            self._files = set()  # Limpa a lista de arquivos
            self._filesCount = 0

            # Mostra a mensagem de sucesso
            self.view.show_message("Sucesso", "Arquivos comprimidos com sucesso!")

        except Exception as e:
            self.view.show_message(
                "Erro", f"Ocorreu um erro durante a compressão: {str(e)}"
            )

    def delete_original_files(self, files):
        if self.view.checkbox_delete.isChecked():
            for file in files:
                try:
                    os.remove(file)
                except Exception as e:
                    self.view.show_message(
                        "Erro", f"Não foi possível excluir o arquivo {file}: {str(e)}"
                    )

    def encrypt_file(self, file, password, password_confirm):
        # Criptografa o arquivo se uma senha for fornecid
        if password == password_confirm:
            encryptor = Encryptor(password)
            encryptor.encrypt_file(file)
        else:
            self.view.show_message("Erro", "Palavras passes diferentes")
