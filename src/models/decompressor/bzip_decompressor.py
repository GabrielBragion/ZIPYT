import bz2
import os

class Bzip2Decompressor:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def extract_bzip2(self, extract_path=None):
        """
        Método para descompactar arquivos BZIP2.

        :param extract_path: Diretório de extração. Se None, extrai no mesmo diretório do arquivo.
        """
        if extract_path is None:
            extract_path = os.path.dirname(self.archive_name)

        output_file = os.path.join(extract_path, os.path.splitext(os.path.basename(self.archive_name))[0])

        try:
            with bz2.BZ2File(self.archive_name, 'rb') as f_in:
                with open(output_file, 'wb') as f_out:
                    f_out.write(f_in.read())
            return f"Arquivo {os.path.basename(self.archive_name)} descompactado com sucesso para {output_file}"
        except (OSError, IOError) as e:
            raise Exception(f"Erro ao descompactar o arquivo BZIP2: {str(e)}")
