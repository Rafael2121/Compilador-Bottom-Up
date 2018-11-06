
"""

LEXER OK

PARSER

SINTATIC

SEMANTIC

"""
import LEXER


class compilerBrain:

    def __init__(self):
        self.listaTokens = []

    def compilermain(self):
        """
            Este será o módulo principal do programa, considerado o cerebro do Compilador Portugolo



        """

        LEXER.lexermain()
        listaTokens = LEXER.get_lista_tokens




    def main(self):
        self.compilermain()


if __name__ == "__main__":
    head = compilerBrain()
    head.main()