from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from config import ConfigService

class EncryptionService:
    def __init__(self):
        salt = b'\x12jk\xa3~\xfbc.1\xf7O\xea\xad\xeb\xb5\xbaT\x97\x08+$\x8fi)\x08\x0e;\x06\x07\xc0\xb9#'
        self.iv = b'03h\x90\xa4\x8a\tTRu63Z\xed\x17\xa0'

        self.config = ConfigService()
        self.password=self.config.get('MASTER')
        self.key = PBKDF2(self.password, salt, dkLen=32)
  
    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CFB, iv=self.iv) 
        return cipher.encrypt(data.encode('utf-8'))
 
    def decrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CFB, iv=self.iv) 
        return cipher.decrypt(data).decode('utf-8')
       
 