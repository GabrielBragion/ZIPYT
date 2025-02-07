from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class Encryptor:
    def __init__(self, password):
        self.password = password.encode()  # Converte a senha para bytes
        self.backend = default_backend()

    def derive_key(self, salt):
        # Deriva uma chave da senha usando PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=self.backend
        )
        return kdf.derive(self.password)

    def encrypt_file(self, file_path):
        # Criptografa o arquivo fornecido
        salt = os.urandom(16)  # Gera um salt aleatório
        key = self.derive_key(salt)
        iv = os.urandom(16)  # Gera um IV aleatório
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()

        with open(file_path, 'rb') as f:
            data = f.read()

        padded_data = padder.update(data) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        encrypted_file_path = f"{file_path}.enc"
        with open(encrypted_file_path, 'wb') as f:
            f.write(salt + iv + encrypted_data)

        return encrypted_file_path

    def decrypt_file(self, encrypted_file_path):
        # Descriptografa o arquivo fornecido
        with open(encrypted_file_path, 'rb') as f:
            salt = f.read(16)  # Lê o salt
            iv = f.read(16)  # Lê o IV
            encrypted_data = f.read()

        key = self.derive_key(salt)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

        decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
        decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

        decrypted_file_path = encrypted_file_path.replace('.enc', '')
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted_data)

        return decrypted_file_path
