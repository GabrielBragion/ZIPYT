import tarfile
import os


class TarDecompressor:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def extract_tar(self, extract_path=None):
        """
        Método para descompactar arquivos TAR.

        :param extract_path: Diretório onde o arquivo será extraído. Se None, extrai no diretório do arquivo TAR.
        """
        if extract_path is None:
            extract_path = os.path.dirname(
                self.archive_name
            )  # Diretório do arquivo TAR

        try:
            # Verifica se o arquivo é um TAR válido
            if not tarfile.is_tarfile(self.archive_name):
                raise Exception(
                    f"O arquivo {self.archive_name} não é um arquivo TAR válido."
                )

            with tarfile.open(self.archive_name, "r") as tar:
                tar.extractall(path=extract_path)

            return f"Arquivo '{self.archive_name}' descompactado com sucesso em '{extract_path}'"

        except tarfile.TarError as e:
            raise Exception(f"Erro ao descompactar o arquivo TAR: {str(e)}")
