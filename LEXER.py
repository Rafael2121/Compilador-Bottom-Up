# Programa destinado a ser o LEXER do portugolo
import sys

from ob_token import Token
from tag import tag


# INTERFACE PRINCIPAL


class LEXER:

    def __init__(self):
        self.n_linha = 0
        self.m_coluna = 0
        self.cursor = 0  # armazena ultimo char
        self.tabelaSimbolos = tag
        self.lista_Tokens = []

    def lexermain(self):

        ref_arquivo = open("C:/Users/1511 FOX/Documents/lexer_exemplo/HelloJavinha.jvn", 'r')

        for linha in ref_arquivo:
            print(linha)
            self.n_linha += 1
            self.reconheceToken(linha.lower())

        ref_arquivo.close()

        print(self.lista_Tokens)

    def reconheceToken(self, linha):
        # metodo que irá ler o texto do arquivo, por token

        estado = 1
        m_coluna = 0
        aux_tamanhao = len(linha)
        lexema = ""

        while not (m_coluna < aux_tamanhao):
            # na leitura do proximo char, é incrementado a coluna
            caractere = linha[m_coluna]
            # print(caractere)
            if estado == 1:
                if caractere == ";":
                    self.lista_Tokens.append(Token('OP_PV', ";", self.n_linha, m_coluna))
                elif caractere == "(":
                    self.lista_Tokens.append(Token('OP_AP', "(", self.n_linha, m_coluna))
                elif caractere == ")":
                    self.lista_Tokens.append(Token('OP_FP', ")", self.n_linha, m_coluna))
                elif caractere == ",":
                    self.lista_Tokens.append(Token('OP_VIR', ",", self.n_linha, m_coluna))
                elif caractere == "=":
                    self.lista_Tokens.append(Token('OP_EQ', "=", self.n_linha, m_coluna))
                elif caractere == "<":
                    lexema += caractere
                    estado = 13
                elif caractere == ">":
                    lexema += caractere
                    estado = 10
                elif caractere == "+":
                    self.lista_Tokens.append(Token('OP_SUM', "+", self.n_linha, m_coluna))
                elif caractere == "-":
                    self.lista_Tokens.append(Token('OP_SUB', "-", self.n_linha, m_coluna))
                elif caractere == "*":
                    self.lista_Tokens.append(Token('OP_MUL', "*", self.n_linha, m_coluna))
                elif caractere == "/":
                    lexema += caractere
                    estado = 3
                elif caractere.isalpha():
                    lexema += caractere
                    estado = 27
                elif caractere.isdigit():
                    lexema += caractere
                    estado = 26
                elif caractere == '"':
                    lexema += caractere
                    estado = 23

            # Estado "<"
            elif estado == 13:
                if caractere == "=":
                    self.lista_Tokens.append(Token('OP_MEEQ', "<=", self.n_linha, m_coluna))
                    estado = 1
                elif caractere == "-":
                    estado = 16
                elif caractere == ">":
                    self.lista_Tokens.append(Token('OP_DIF', "<>", self.n_linha, m_coluna))
                    estado = 1
                else:
                    self.lista_Tokens.append(Token('OP_MEN', "<", self.n_linha, m_coluna))
                    estado = 1
                    m_coluna -= 1

            elif estado == 16:
                if caractere == "-":
                    self.lista_Tokens.append(Token('OP_ATR', "<--", self.n_linha, m_coluna))
                    estado = 1

            # Estado ">"
            elif estado == 10:
                if caractere == "=":
                    self.lista_Tokens.append(Token('OP_MAEQ', ">=", self.n_linha, m_coluna))
                    estado = 1
                else:
                    self.lista_Tokens.append(Token('OP_MAI', ">", self.n_linha, m_coluna))
                    estado = 1
                    m_coluna -= 1

            # Estado /
            elif estado == 3:
                if caractere == "*":
                    estado = 5
                elif caractere == "/":
                    estado = 8
                else:
                    self.lista_Tokens.append(Token('OP_DIV', "/", self.n_linha, m_coluna))
                    estado = 1
                    m_coluna -= 1

            elif estado == 5:
                if caractere == "*":
                    estado = 6
            elif estado == 8:
                if caractere == "/n":
                    estado = 1
            elif estado == 6:
                if caractere == "*":
                    pass
                elif caractere == "/":
                    estado = 1
                else:
                    estado = 5

            # Estado de letra
            elif estado == 27:
                if caractere.isalnum():
                    # enquanto encontrar
                    lexema += caractere

                else:
                    ## -------------------------------------------------
                    """
                    if self.tabelaSimbolos[lexema]:
                        aux = 'KW'
                    else:
                        aux = 'ID'
                    """
                    ## -------------------------------------------------
                    self.lista_Tokens.append(Token('KW', lexema, self.n_linha, m_coluna))
                    lexema = ""
                    m_coluna -= 1
                    estado = 1

            # Estado de numero
            elif estado == 26:
                if caractere.isdigit():
                    lexema += caractere
                elif caractere == ".":
                    estado = 30
                    lexema += caractere
                else:
                    self.lista_Tokens.append(Token('INT', lexema, self.n_linha, m_coluna))
                    estado = 1
                    lexema = ""
                    m_coluna -= 1

            elif estado == 30:
                if caractere.isdigit():
                    lexema += caractere
                else:
                    self.lista_Tokens.append(Token('FLOAT', lexema, self.n_linha, m_coluna))
                    estado = 1
                    lexema = ""
                    m_coluna -= 1

            # Estado de "
            elif estado == 23:
                if caractere == '"':
                    self.lista_Tokens.append(Token('STRING', lexema, self.n_linha, m_coluna))
                    estado = 1
                    lexema = ""
                else:
                    lexema += caractere
            else:
                pass
            m_coluna += 1
        # Fim do While

    def main(self):
        self.lexermain()

if __name__ == "__main__":
    i = LEXER()
    i.main()