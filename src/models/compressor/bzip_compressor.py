import bz2
from pathlib import Path

class Bzip2Compressor:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def create_bzip2(self, file_path):
        """
        Cria um arquivo BZIP2 a partir do arquivo fornecido.

        :param file_path: Caminho do arquivo a ser compactado.
        :return: Nome do arquivo BZIP2 criado.
        """
        bzip2_file_path = f"{file_path}.bz2"
        with open(file_path, 'rb') as f_in:
            with bz2.open(bzip2_file_path, 'wb') as f_out:
                f_out.writelines(f_in)
        return bzip2_file_path
