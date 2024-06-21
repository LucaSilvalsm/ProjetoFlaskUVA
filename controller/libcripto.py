import hashlib
import random
import base64

class CriptoSenha:
    def encriptar(self, senha):
        salt = [random.randint(0,255) for i in range(32)]
        senhab = salt + [ord(c) for c in senha]
        md = hashlib.sha3_256()
        md.update(bytes(senhab))
        senhaCripto = bytes(salt) + md.digest()
        return str(base64.encodebytes(senhaCripto),"utf-8")
        
    def verificar(self, senha, senhaCripto):
        senhac = bytes(senhaCripto,"utf-8")
        senhac = base64.decodebytes(senhac)
        salt = [c for c in senhac[0:32]]
        senhab = salt + [ord(c) for c in senha]
        md = hashlib.sha3_256()
        md.update(bytes(senhab))
        return md.digest() == senhac[32:]


if __name__ == "__main__":
    cs = CriptoSenha()
    senhaCripto = cs.encriptar("TESTE");
    print(senhaCripto)
    print(cs.verificar("TESTE", senhaCripto))
    print(cs.verificar("TESTe", senhaCripto))
    
        
        