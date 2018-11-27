# Programa destinado a ser o LEXER do portugolo
import sys

from ob_token import Token
from tag import TAGs

class Lexer:

    def __init__(self):
        self.n_linha = 0
        self.m_coluna = 0
        self.estado = 1
        self.lexema = ""  # Definição da variável de acumulação de caracteres para a formação do TOKEN composto
        self.cursor = ""
        self.tabelaSimbolos = TAGs().simbolos
        self.tabelaTags = TAGs().tags
        self.lista_Tokens = []
        self.is_panico = False
        self.lista_erros = []

    def get_lista_tokens(self):
        return self.lista_Tokens

    def lexermain(self):
        """
            Este módulo do programa tem o objetivo de extrair  os tokens do arquivo  --> LEXER      ###

            Este módulo ainda precisa de uma análise em busca de compactar o codigo, que ainda é um pouco confuso.
            Infelizmente, à um problema que obriga a ter uma linha a mais alem da linha "fim", por algum problema de leitura EOF do Python,
            então no caso do LEXER nesta primeira versão, isso é obrigatório para nao ter erros.

        """

        ref_arquivo = open("Novo Documento de Texto.txt", 'r')

        # Para cada linha passar o olhar do extrator em busca de tokens
        for linha in ref_arquivo:
            self.n_linha += 1
            self.extrator_tokens(linha)

        ref_arquivo.close()

        self.lista_Tokens.append(Token('KW_RES_EOF', "$", self.n_linha, self.m_coluna))

        for i in self.lista_Tokens:
            if not i.tag == 'TAB':
                print(i)

        for i in self.lista_erros:
            if not i[1]:
                print(i[0])

    def extrator_tokens(self, linha):
        # metodo que irá ler linha do arquivo, buscando por tokens
        self.m_coluna = 0 # Posição inicial do cursor do lexer, primeiro caractere da linha
        cont_tab = 0
        for char in linha:
        #while self.m_coluna < len(linha): # Enquanto existir caractere continuar lendo linha
            #self.cursor = linha[self.m_coluna]
            self.cursor = char
            self.m_coluna += 1 #Controle de posição
            if self.estado == 1:
                # 47 ~ 52 irá adquirir informação sobre tabulação, caso tenha 3 espaços em branco um token TAB é criado
                if self. cursor == " ":
                    cont_tab += 1
                    if cont_tab == 3:
                        cont_tab = 0
                        self.lista_Tokens.append(Token('TAB', "   ", self.n_linha, self.m_coluna))  # Tabulação

                else:
                    cont_tab = 0
                    if self.cursor == ";":
                        self.lista_Tokens.append(Token('OP_PV', ";", self.n_linha, self.m_coluna)) # Operador Ponto Virgula
                        self.estado = 1
                    elif self.cursor == "(":
                        self.lista_Tokens.append(Token('OP_AP', "(", self.n_linha, self.m_coluna)) # Operador Abre Parenteses
                        self.estado = 1
                    elif self.cursor == ")":
                        self.lista_Tokens.append(Token('OP_FP', ")", self.n_linha, self.m_coluna)) # Operador Fecha Parenteses
                        self.estado = 1
                    elif self.cursor == ",":
                        self.lista_Tokens.append(Token('OP_VIR', ",", self.n_linha, self.m_coluna)) # Operador Virgula
                        self.estado = 1
                    elif self.cursor == "=":
                        self.lista_Tokens.append(Token('OP_EQ', "=", self.n_linha, self.m_coluna)) # Operador Igual
                        self.estado = 1
                    elif self.cursor == "<":
                        self.estado = 13
                    elif self.cursor == ">":
                        self.estado = 10
                    elif self.cursor == "+":
                        self.lista_Tokens.append(Token('OP_SUM', "+", self.n_linha, self.m_coluna)) # Operador Soma
                        self.estado = 1
                    elif self.cursor == "-":
                        self.lista_Tokens.append(Token('OP_SUB', "-", self.n_linha, self.m_coluna)) # Operador Subtração
                        self.estado = 1
                    elif self.cursor == "*":
                        self.lista_Tokens.append(Token('OP_MUL', "*", self.n_linha, self.m_coluna)) # Operador Multiplicação
                        self.estado = 1
                    elif self.cursor == "/":
                        self.estado = 3
                    elif self.cursor.isalpha():
                        self.lexema += self.cursor
                        self.estado = 27
                    elif self.cursor.isdigit():
                        self.lexema += self.cursor
                        self.estado = 26
                    elif self.cursor == '"':
                        self.lexema += self.cursor
                        self.estado = 23

            # Estados que envolvem q0 -> "<"
            elif self.estado == 13:
                if self.cursor == "=":
                    self.lista_Tokens.append(Token('OP_MEEQ', "<=", self.n_linha, self.m_coluna)) # Operador Menor Igual
                    self.estado = 1
                elif self.cursor == "-":
                    self.estado = 16
                elif self.cursor == ">":
                    self.lista_Tokens.append(Token('OP_DIF', "<>", self.n_linha, self.m_coluna)) # Operador Diferente
                    self.estado = 1
                else:
                    self.m_coluna -= 1
                    self.lista_Tokens.append(Token('OP_MEN', "<", self.n_linha, self.m_coluna)) # Operador Menor
                    self.estado = 1
            elif self.estado == 16:
                if self.cursor == "-":
                    self.lista_Tokens.append(Token('OP_ATR', "<--", self.n_linha, self.m_coluna)) # Operador Atribuição
                    if self.is_panico:
                        self.is_panico = False
                    self.estado = 1
                elif ((self.cursor == "\n") or (self.cursor == "\r") or (self.cursor == "\t")):
                    self.lista_erros.append([Token('LEX_QL', "Quebra de linha inválida:" + repr(self.cursor), self.n_linha, self.m_coluna), self.is_panico])
                    if not (self.is_panico):
                        self.is_panico = True
                else:
                    self.lista_erros.append([Token('LEX_CI', "Caractere inválido:" + repr(self.cursor), self.n_linha, self.m_coluna), self.is_panico])
                    if not (self.is_panico):
                        self.is_panico = True

            # Estados que envolvem q0 -> ">"
            elif self.estado == 10:
                if self.cursor == "=":
                    self.lista_Tokens.append(Token('OP_MAEQ', ">=", self.n_linha, self.m_coluna)) # Operador Maior Igual
                    self.estado = 1
                else:
                    self.m_coluna -= 1
                    self.lista_Tokens.append(Token('OP_MAI', ">", self.n_linha, self.m_coluna)) # Operador Maior
                    self.estado = 1

            # Estados que envolvem q0 -> "/"
            elif self.estado == 3:
                if self.cursor == "*":
                    self.estado = 5
                elif self.cursor == "/":
                    self.estado = 8
                else:
                    self.m_coluna -= 1
                    self.lista_Tokens.append(Token('OP_DIV', "/", self.n_linha, self.m_coluna)) # Operador Divisão
                    self.estado = 1
            # /*
            elif self.estado == 5:
                if self.cursor == "*":
                    self.estado = 6
            elif self.estado == 6:
                if self.cursor == "*":
                    pass
                elif self.cursor == "/":
                    self.estado = 1
                else:
                    self.estado = 5
            # //
            elif self.estado == 8:
                if self.cursor == "\n":
                    self.estado = 1

            # Estados que envolvem q0 -> alfabeto
            # Enquanto encontrar caracteres, o token será formado e retornará um ID ou uma chave resevada
            elif self.estado == 27:
                if self.cursor.isalnum():
                    self.lexema += self.cursor
                else:
                    aux = 'KW_RES_ID'
                    for num in range(len(self.tabelaSimbolos)):
                        if self.tabelaSimbolos[num] == self.lexema.lower():
                            aux = self.tabelaTags[self.lexema.lower()]
                    self.m_coluna -= 1
                    self.lista_Tokens.append(Token(aux, self.lexema, self.n_linha, self.m_coluna)) # Key Word, se for encontrada na lista de reservadas será destacada
                    self.lexema = ""
                    self.estado = 1

            # Estados que envolvem q0 ->  de numero
            # Retorna um INT ou um FLOAT
            elif self.estado == 26:
                if self.cursor.isdigit():
                    self.lexema += self.cursor
                elif self.cursor == ".":
                    self.estado = 30
                    self.lexema += self.cursor
                else:
                    self.m_coluna -= 1
                    self.lista_Tokens.append(Token('INT', self.lexema, self.n_linha, self.m_coluna)) # Inteiro
                    self.estado = 1
                    self.lexema = ""

            # FLOAT
            elif self.estado == 30:
                if self.cursor.isdigit():
                    self.lexema += self.cursor
                    if self.is_panico:
                        self.is_panico = False
                    self.estado = 31
                elif ((self.cursor == "\n") or (self.cursor == "\r") or (self.cursor == "\t")):
                    # estado de exceção
                    self.lista_erros.append([Token('LEX_QL', "Quebra de linha inválida:" + repr(self.cursor), self.n_linha, self.m_coluna),self.is_panico])
                    if not (self.is_panico):
                        self.is_panico = True
                else:
                    # estado de exceção
                    self.lista_erros.append([Token('LEX_CI', "Caractere inválido:" + repr(self.cursor), self.n_linha, self.m_coluna),self.is_panico])
                    if not (self.is_panico):
                        self.is_panico = True
            elif self.estado == 31:
                if self.cursor.isdigit():
                    self.lexema += self.cursor
                else:
                    self.m_coluna -= 1
                    self.lista_Tokens.append(Token('FLOAT', self.lexema, self.n_linha, self.m_coluna)) # Float decimal
                    self.estado = 1
                    self.lexema = ""

            # Estados de contrução string q0 -> " "
            # Contrutor de string literal, aonde ela não pode ser vazia
            elif self.estado == 23:
                if self.cursor.isalnum():
                    self.lexema += self.cursor
                    if self.is_panico:
                        self.is_panico = False
                    self.estado = 24
                elif ((self.cursor == "\n") or (self.cursor == "\r") or (self.cursor == "\t")):
                    # estado de exceção
                    self.lista_erros.append([Token('LEX_QL', "Quebra de linha inválida:" + repr(self.cursor), self.n_linha, self.m_coluna), self.is_panico])
                    if not (self.is_panico):
                        self.is_panico = True

            elif self.estado == 24:
                if self.cursor == '"':
                    self.lexema += self.cursor
                    self.lista_Tokens.append(Token('STRING', self.lexema, self.n_linha, self.m_coluna)) # String
                    if self.is_panico:
                        self.is_panico = False
                    self.estado = 1
                    self.lexema = ""
                elif (self.cursor.isalnum() or self.cursor == " "):
                    self.lexema += self.cursor
                elif ((self.cursor == "\n") or (self.cursor == "\r") or (self.cursor == "\t")):
                    # estado de exceção
                    self.lista_erros.append([Token('LEX_QL', "Quebra de linha inválida:" + repr(self.cursor), self.n_linha, self.m_coluna), self.is_panico])
                    if not (self.is_panico):
                        self.is_panico = True

            else:
                pass

        # Fim do While
