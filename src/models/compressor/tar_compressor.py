import tarfile

# Cria o arquivo TAR
def create_tar(archive_name, files):
    with tarfile.open(archive_name, 'w') as tar:
        for file in files:
            tar.add(file)
    return archive_name