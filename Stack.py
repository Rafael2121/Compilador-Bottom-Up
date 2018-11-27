"""
    Objeto pilha para controle de objetos para o parser do compilerBrain
"""

class stack:

    def __init__(self):
        self.data = []


    def pack(self, objeto):
        self.data.append(objeto)

    def unpack(self):
        if not self.is_empty():
            return self.data.pop(-1)

    def is_empty(self):
        return len(self.data) == 0