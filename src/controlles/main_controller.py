"""
TODO
- se ja tiver um arquivo com o mesmo nome do diretorio qunado estiver criando, adicionar (1) e ir incrementando
- corrigir descompactador LZMA
- corrigir encriptacao e decriptacao
- refatorar tudo e tirar todo esses trechos de codigo repetidos
"""

from pathlib import Path
import os

# Compressor
from ..models.compressor.tar_compressor import TarCompressor
from ..models.compressor.gz_compressor import GzCompressor
from ..models.compressor.zip_compressor import ZipCompressor
from ..models.compressor.lzma_compressor import LzmaCompressor
from ..models.compressor.bzip_compressor import Bzip2Compressor

# Decompressor
from ..models.decompressor.tar_decompressor import TarDecompressor
from ..models.decompressor.zip_decompressor import ZipDecompressor
from ..models.decompressor.gz_decompressor import GZDecompressor
from ..models.decompressor.bzip_decompressor import Bzip2Decompressor
from ..models.decompressor.lzma_decompressor import LZMADecompressor

# Encryptor
from ..models.encryptor.encryptor import Encryptor


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
        self.view.btn_exec.clicked.connect(self.handle_action)

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

            # Volta a adicionar a opções que possa ter sido removida quando mudou o metodo
            self.view.select_compress.insertItem(0, "Nenhum")
            self.view.select_compress.insertItem(2, "GZIP")
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
            for option in ["Nenhum", "GZIP"]:
                index = self.view.select_compress.findText(option)
                if index != -1:
                    self.view.select_compress.removeItem(index)

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

            # Remove a opções pois seram adicionadas no modo TAR
            for option in ["Nenhum", "GZIP", "Padrão"]:
                index = self.view.select_compress.findText(option)
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
            if file_path.exists() and file_path not in self._files:
                self._files.add(file_path)
                self.view.list_files.addItem(file_path.name)

        # Atualiza o diretório no campo de input_files com o diretório do primeiro arquivo
        if files:
            selected_dir = str(Path(files[0]).parent)
            self.view.input_files.setText(selected_dir)
            self.selected_dir = (
                selected_dir  # Atualiza o diretório selecionado para compressão
            )

        self._filesCount = len(self._files)
        self.view.update_file_count(self._filesCount)
        self.update_interface_based_type_file()

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

    def handle_action(self):
        # Primeiro, verifica se todos os arquivos têm o sufixo .enc
        enc_files = [file for file in self._files if file.suffix == ".enc"]

        if enc_files:
            password = self.view.input_password.text()
            password_confirm = self.view.input_repeat.text()

            # Verifica se as senhas coincidem
            if password != password_confirm:
                self.view.show_message("Erro", "As senhas não coincidem.")
                return

            # Descriptografa todos os arquivos com sufixo .enc
            try:
                for file in enc_files:
                    self.decrypt_file(file, password, password_confirm)
                self.view.show_message("Sucesso", "Arquivos descriptografados com sucesso!")
            except Exception as e:
                self.view.show_message("Erro", f"Erro ao descriptografar: {str(e)}")

        # Verifica se os arquivos não são criptografados (não possuem o sufixo .enc)
        if all(file.suffix in [".tar", ".gz", ".zip", ".lzma", ".bz2"] for file in self._files):
            self.decompress_files()  # Caso os arquivos não sejam .enc, descompacta
        else:
            self.compress_files()  # Caso contrário, realiza a compressão


    def decompress_files(self):
        try:
            for file in self._files:
                if file.suffix == ".tar":
                    decompressor = TarDecompressor(file)
                    decompressor.extract_tar()
                elif file.suffix == ".gz":
                    decompressor = GZDecompressor(file)
                    decompressor.extract_gz()
                elif file.suffix == ".zip":
                    decompressor = ZipDecompressor(file)
                    decompressor.extract_zip()
                elif file.suffix == ".lzma":
                    decompressor = LZMADecompressor(file)
                    decompressor.extract_lzma()
                elif file.suffix == ".bz2":
                    decompressor = Bzip2Decompressor(file)
                    decompressor.extract_bzip2()
                else:
                    self.view.show_message(
                        "Erro", f"Formato não suportado: {file.name}"
                    )

            self.view.show_message("Sucesso", "Arquivos descompactados com sucesso!")

            # Exclui os arquivos originais se a opção estiver marcada
            self.delete_original_files(self._files)

            self.reset_view_after_sucess()

        except Exception as e:
            self.view.show_message("Erro", f"Erro ao descompactar: {str(e)}")

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
                first_file = next(iter(self._files))  # Obtém o primeiro arquivo do set
                archive_name = os.path.join(self.selected_dir, f"{first_file.stem}.tar")
                compressor = TarCompressor(archive_name)
                compressor.create_tar(list(self._files))

                if selected_compress == "GZIP":
                    gz_archive_name = archive_name
                    compressor = GzCompressor(archive_name)
                    compressor.create_gz(archive_name)
                    os.remove(
                        archive_name
                    )  # Remove o arquivo TAR original após criar o GZ

                    if len(password) > 0:
                        encryptor = Encryptor(password)
                        encryptor.encrypt_file(gz_archive_name)
                        os.remove(
                            gz_archive_name
                        )  # Remove o arquivo TAR.GZ original após criar o TAR.GZ.ENC
                elif selected_compress == "LZMA":
                    lzma_archive_name = archive_name
                    compressor = LzmaCompressor(archive_name)
                    compressor.create_lzma(archive_name)
                    os.remove(
                        archive_name
                    )  # Remove o arquivo TAR original após criar o GZ

                    if len(password) > 0:
                        encryptor = Encryptor(password)
                        encryptor.encrypt_file(lzma_archive_name)
                        os.remove(lzma_archive_name)

                elif selected_compress == "BZIP2":
                    bzip2_archive_name = f"{archive_name}.bz2"
                    compressor = Bzip2Compressor(bzip2_archive_name)
                    compressor.create_bzip2(archive_name)
                    os.remove(
                        archive_name
                    )  # Remove o arquivo TAR original após criar o TAR.BZ2

                    if len(password) > 0:
                        encryptor = Encryptor(password)
                        encryptor.encrypt_file(bzip2_archive_name)
                        os.remove(
                            bzip2_archive_name
                        )  # Remove o arquivo TAR.BZ2 após criar o TAR.BZ2.ENC

            elif selected_format == "GZ":
                for file in self._files:
                    compressor = GzCompressor(file)
                    gz_file = compressor.create_gz(file)

                    if len(password) > 0:
                        encryptor = Encryptor(password)
                        encryptor.encrypt_file(gz_file)
                        os.remove(
                            gz_file
                        )  # Remove o arquivo GZ original após criar o GZ.ENC

            elif selected_format == "ZIP":
                # Usa o diretório selecionado para criar o arquivo ZIP
                first_file = next(iter(self._files))  # Obtém o primeiro arquivo do set
                archive_name = os.path.join(self.selected_dir, f"{first_file.stem}.zip")
                if password == password_repeat:
                    compressor = ZipCompressor(
                        archive_name,
                        compression_method=selected_compress,
                        compression_level=compression_level,
                        password=password,
                    )
                    compressor.create_zip(list(self._files))
                else:
                    self.view.show_message("Erro", "Palavras passes diferentes")

            elif selected_format == "LZMA":
                for file in self._files:
                    compressor = LzmaCompressor(file)
                    lzma_file = compressor.create_lzma(file)

                    if len(password) > 0:
                        encryptor = Encryptor(password, password_repeat)
                        encryptor.encrypt_file(lzma_file)
                        os.remove(lzma_file)

            # Exclui os arquivos originais se a opção estiver marcada
            self.delete_original_files(self._files)

            # Reseta a view após a compressão
            self.reset_view_after_sucess()

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
            
    def decrypt_file(self, file):
        """
        Solicita a senha ao usuário e tenta descriptografar o arquivo.
        """
        if file.suffix == ".enc":
            password = self.view.input_password.text()
            try:
                decryptor = Encryptor(password)
                decrypted_file = decryptor.decrypt_file(file)  # Chama a função correta

                self.view.show_message("Sucesso", f"Arquivo {file.name} foi descriptografado com sucesso!")

            except ValueError:  # Se a senha estiver errada, o Encryptor pode lançar um erro
                self.view.show_message("Erro", "Senha incorreta!")

            except Exception as e:
                self.view.show_message("Erro", f"Erro ao descriptografar {file.name}: {str(e)}")

        else:
            self.view.show_message("Erro", "Este arquivo não está criptografado.")



    def reset_view_after_sucess(self):
        self.view.reset_view()
        self._files = set()  # Limpa a lista de arquivos
        self._filesCount = 0
        self.view.btn_exec.setText("Executar")
        self.view.btn_exec.setDisabled(True)
        self.view.select_method.show()
        self.view.select_compress.show()
        self.view.label_method.show()
        self.view.label_compress.show()

    def update_interface_based_type_file(self):
        """
        Atualiza o texto do botão de execução com base no tipo de arquivo selecionado.
        """

        self.view.btn_exec.setDisabled(False)
        # Verifica se todos os arquivos são de formatos compactados
        if all(file.suffix in [".tar", ".gz", ".zip", ".lzma", ".bz2"] for file in self._files):
            self.view.btn_exec.setText("Descompactar")
            self.view.select_method.hide()
            self.view.select_compress.hide()
            self.view.label_method.hide()
            self.view.label_compress.hide()
        elif all(file.suffix in [".enc"] for file in self._files):
            self.view.btn_exec.setText("Desencriptar")
        else:
            self.view.btn_exec.setText("Compactar")