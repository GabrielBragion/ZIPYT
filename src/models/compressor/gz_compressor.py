import gzip
import shutil

class GzCompressor:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def create_gz(self, file_path):
        """
        Cria um arquivo GZ a partir do arquivo fornecido.
        
        :param file_path: Caminho do arquivo a ser compactado.
        :return: Nome do arquivo GZ criado.
        """
        gz_file_path = f"{file_path}.gz"
        with open(file_path, 'rb') as f_in:
            with gzip.open(gz_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return gz_file_path