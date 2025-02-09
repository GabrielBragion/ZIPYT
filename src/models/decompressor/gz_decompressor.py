import gzip
import shutil
import os

class GZDecompressor:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def extract_gz(self, extract_path=None):
        """
        Método para descompactar arquivos GZ.

        :param extract_path: Diretório de extração. Se None, extrai no mesmo diretório do arquivo.
        """
        if extract_path is None:
            extract_path = os.path.dirname(self.archive_name)

        output_file = os.path.join(extract_path, os.path.splitext(os.path.basename(self.archive_name))[0])

        try:
            with gzip.open(self.archive_name, 'rb') as f_in:
                with open(output_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            return f"Arquivo {os.path.basename(self.archive_name)} descompactado com sucesso para {output_file}"
        except (OSError, gzip.BadGzipFile) as e:
            raise Exception(f"Erro ao descompactar o arquivo GZ: {str(e)}")
