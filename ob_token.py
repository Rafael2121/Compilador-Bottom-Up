# Objeto token

class Token:

    def __init__(self, tag, lexema, linha, coluna):
        self.tag = tag
        self.lexema = lexema
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        desc = "<" + self.tag + ",'" + self.lexema + "'> linha:" + self.linha + " coluna:" + self.coluna
        return desc
