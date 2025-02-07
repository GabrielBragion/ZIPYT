import zipfile
import os

class ZipCompressor:
    def __init__(self, archive_name, compression_method, compression_level, password=None):
        self.archive_name = archive_name
        self.compression_method = compression_method
        self.compression_level = compression_level
        self.password = password

    def create_zip(self, files):
        """
        Cria um arquivo ZIP com os arquivos fornecidos.
        
        :param files: Lista de caminhos de arquivos a serem adicionados ao ZIP.
        :return: Nome do arquivo ZIP criado.
        """
        compression = self._get_compression_method()
        with zipfile.ZipFile(self.archive_name, 'w', compression, compresslevel=self.compression_level) as zipf:
            if self.password:
                zipf.setpassword(self.password.encode())
            for file in files:
                if os.path.exists(file):
                    zipf.write(file, os.path.basename(file))
                else:
                    print(f"Arquivo {file} não encontrado e será ignorado.")
        return self.archive_name

    def _get_compression_method(self):
        """
        Retorna o método de compressão apropriado com base na configuração.
        """
        if self.compression_method == 'Padrão':
            return zipfile.ZIP_DEFLATED
        elif self.compression_method == 'BZIP2':
            return zipfile.ZIP_BZIP2
        elif self.compression_method == 'LZMA':
            return zipfile.ZIP_LZMA
        else:
            raise ValueError(f"Método de compressão desconhecido: {self.compression_method}")
