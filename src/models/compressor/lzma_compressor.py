import lzma

class LzmaCompressor:
    def __init__(self, archive_name=None):
        self.archive_name = archive_name

    def create_lzma(self, file_path):
        """
        Cria um arquivo LZMA (.xz) a partir do arquivo fornecido.

        :param file_path: Caminho do arquivo a ser compactado.
        :return: Nome do arquivo LZMA criado.
        """
        # Se o nome do arquivo de saída não for definido, cria automaticamente
        lzma_file_path = f"{file_path}.xz"

        # Compactação usando LZMA
        with open(file_path, 'rb') as f_in:
            with lzma.open(lzma_file_path, 'wb') as f_out:
                while chunk := f_in.read(1024 * 1024):  # Lê em blocos de 1 MB
                    f_out.write(chunk)

        return lzma_file_path
