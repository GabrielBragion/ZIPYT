import tarfile
import os

class TarCompressor:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def create_tar(self, files):
        """
        Cria um arquivo TAR com os arquivos fornecidos.

        :param files: Lista de caminhos de arquivos a serem adicionados ao TAR.
        :return: Nome do arquivo TAR criado.
        """
        with tarfile.open(self.archive_name, 'w') as tar:
            for file in files:
                try:
                    if os.path.isfile(file):
                        tar.add(file, arcname=os.path.basename(file))
                    else:
                        print(f"'{file}' não é um arquivo regular e será ignorado.")
                except Exception as e:
                    print(f"Erro ao adicionar '{file}': {e}")
        return self.archive_name
