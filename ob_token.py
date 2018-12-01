# Objeto token

class Token:

    def __init__(self, tag, lexema, linha, coluna):
        self.tag = tag
        self.lexema = lexema
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        return "< %s, '%s' > linha: %d coluna %d" % (self.tag, self.lexema, self.linha, self.coluna)

    def getTag(self):
        return self.tag