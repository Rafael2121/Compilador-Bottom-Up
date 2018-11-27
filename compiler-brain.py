
"""

LEXER OK

PARSER

SINTATIC

SEMANTIC

"""
from LEXER import Lexer
from PARSER import Parser

class compilerBrain:

    def __init__(self):
        self.listaTokens = []

    def compilermain(self):
        """
            Este será o módulo principal do programa, considerado o cerebro do Compilador Portugolo
        """
        lexer = Lexer()
        lexer.lexermain()

        #parser = Parser()
        #parser.parsermain(lexer.get_lista_tokens())


    def main(self):

        self.compilermain()


if __name__ == "__main__":
    head = compilerBrain()
    head.main()