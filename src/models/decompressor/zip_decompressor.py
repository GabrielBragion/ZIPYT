import zipfile
import os


class ZipDecompressor:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def extract_zip(self, extract_path=None, password=None):
        """
        Método para descompactar arquivos ZIP.

        :param extract_path: Diretório onde o arquivo será extraído. Se None, extrai no diretório atual.
        :param password: Senha opcional para arquivos ZIP protegidos.
        """
        if extract_path is None:
            extract_path = os.path.dirname(
                self.archive_name
            )  # Extrai no mesmo diretório do ZIP

            try:
                with zipfile.ZipFile(self.archive_name, "r") as zipf:
                    # Verifica se o arquivo está protegido por senha
                    if (
                        zipf.namelist()
                        and zipf.getinfo(zipf.namelist()[0]).flag_bits & 0x1
                    ):
                        if password is None:
                            raise ValueError(
                                "O arquivo está protegido por senha. Forneça uma senha para descompactar."
                            )
                        zipf.setpassword(password.encode())

                        zipf.extractall(path=extract_path)

                return f"Arquivo {os.path.basename(self.archive_name)} descompactado com sucesso em {extract_path}"

            except (zipfile.BadZipFile, RuntimeError, ValueError) as e:
                raise Exception(f"Erro ao descompactar o arquivo ZIP: {str(e)}")
