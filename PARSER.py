# Programa destinado a análise dos objetos recuperados pelo LEXER

from Stack import stack
from ob_token import Token

class Parser:

    def __init__(self):
        self.entrada = None
        self.cursor = None # Variavel de controle de entrada da lista de tokens
        self.estado = 1
        self.pilha = stack()


    def parsermain(self, lista_Tokens):
        """
        Módulo que compara os tokens reconhecidos pelo PARSER com a gramatica portugolo
        No final desta classe está em comentário TODA a gramática, que será retirada nas versões que aceitarão qualquer uma
        O objetivo final é um parser bottom up com um módulo que entenda um padrão de escrita de gramática, que se estiver minimamente
        boa, poderá ser reconhecida e aplicada
        """
        # TABELA -------> PILHA | ENTRADA | AÇÃO
        self.lista_Tokens = lista_Tokens # entrada
        self.pilha.pack('$')
        self.parser_analisys()

    def estado_1(self):
        """
        + Compilador: •Programa : EOF
        + Programa: •"algoritmo" DeclaraVar ListaCmd "fim" "algoritmo" ListaRotina : EOF
        """
        if (self.entrada == 'KW_RES_algotith'):
            return estado_3()
        if (self.entrada == 'Programa'):
            return estado_2()
    def estado_2(self):
        """
        + Compilador: Programa • EOF
        """

    def estado_3(self):
        """
        + Programa: "algoritmo" •DeclaraVar ListaCmd "fim" "algoritmo" ListaRotina : EOF
        + DeclaraVar: •"declare" ListaID Tipo ";" ListaDeclaraVar: ListaCmd
        """
        if (self.entrada == 'KW_RES_var'):
            return estado_4()
        if (self.entrada == 'DeclaraVar'):
            return
    def estado_4(self):
        """
        + DeclaraVar: "declare" •ListaID Tipo ";" ListaDeclaraVar: ListaCmd
        + ListaID: •ID ListaAdd : Tipo
        """
        if (self.entrada == 'KW_RES_ID'):
            return estado_5()
        elif (self.entrada == 'ListaID'):
            return estado_11()
    def estado_5(self):
        """
        + ListaID: ID •ListaAdd : Tipo
        + ListaAdd: •", " ListaID : Tipo
        + ListaAdd: •ε : Tipo
        """
        if (self.entrada == ','):
            return estado_7()
        elif (self.entrada == 'ListaAdd'):
            return estado_6()
        else:
            return estado_8()
    def estado_6(self):
        """
        + ListaID: ID ListaAdd• : Tipo
        """
        return
    def estado_7(self):
        """
        + ListaAdd: ", " •ListaID : Tipo
        + ListaID: •ID ListaAdd : Tipo
        """
        if (self.entrada == 'KW_RES_ID'):
            return estado_5()
        elif (self.entrada == 'ListaID'):
            return estado_10()
    def estado_8(self):




    def parser_analisys(self):
        avanca = False
        estado = 1
        self.pilha.pack(estado)
        for token in self.lista_Tokens:
            while not(avanca):
                entrada = token.lexema

                if (estado == 1):
                    """
                    + Compilador: •Programa : EOF
                    + Programa: •"algoritmo" DeclaraVar ListaCmd "fim" "algoritmo" ListaRotina : EOF
                    """
                    if(entrada == 'KW_RES_algorithm'):
                        estado = 3
                    elif(entrada == 'Programa'):
                        estado = 2
                elif (estado == 2):
                    """
                    + Compilador: Programa • EOF
                    """
                elif (estado == 3):
                    """
                    + Programa: "algoritmo" •DeclaraVar ListaCmd "fim" "algoritmo" ListaRotina : EOF
                    + DeclaraVar: •"declare" ListaID Tipo ";" ListaDeclaraVar: ListaCmd
                    """
                    if (entrada == 'KW_RES_var'):
                        estado = 4
                    elif(entrada == 'DeclaraVar'):
                        estado = 0
                elif (estado == 4):
                    """
                    + DeclaraVar: "declare" •ListaID Tipo ";" ListaDeclaraVar: ListaCmd
                    + ListaID: •ID ListaAdd : Tipo
                    """
                    if (entrada == 'KW_RES_ID'):
                        estado = 5
                    elif (entrada == 'ListaID'):
                        estado = 11
                elif (estado == 5):
                    """
                    + ListaID: ID •ListaAdd : Tipo
                    + ListaAdd: •", " ListaID : Tipo
                    + ListaAdd: •ε : Tipo
                    """
                    if (entrada == ','):
                        estado = 7
                    elif (entrada == 'ListaAdd'):
                        estado = 6
                    else:
                        estado = 8
                elif (estado == 6):
                    """
                    + ListaID: ID ListaAdd• : Tipo
                    """
                    entrada = 'ListaAdd'
                    estado = 4
                elif (estado == 7):
                    """
                    + ListaAdd: ", " •ListaID : Tipo
                    + ListaID: •ID ListaAdd : Tipo
                    """
                    if (entrada == 'ID'):
                        estado = 5
                    elif(entrada == 'ListaID'):
                        estado = 10
                elif (estado == 8):
                    """
                    + ListaAdd: ε• : Tipo
                    """
                    entrada = 'listaAdd'
                    estado = 5
                elif (estado == 2):
                    """
                    + Compilador: Programa • EOF
                    """
                else:




    """
    Compilador → Programa EOF
    Programa → algoritmo DeclaraVar ListaCmd fim algoritmo ListaRotina
    DeclaraVar → declare ListaID Tipo; ListaDeclaraVar | ε
    ListaDeclaraVar → ListaID Tipo ";" ListaDeclaraVar | ε
    ListaRotina → Rotina ListaRotina | ε
    Rotina → subrotina ID ( Param ) DeclaraVar ListaCmd Retorno fim subrotina
    Param → ListaID Tipo ListaParam
    ListaPAram → , Param | ε
    ListaId → ID ListaAdd
    ListaAdd → , ListaID | ε
    Retorno → retorne Expressao | ε
    Tipo → logico | numerico | literal | nulo
    ListaCmd → Cmd ListaCmd | ε
    Cmd → CmdSe | CmdEnquanto | CmdPara| CmdRepita| CmdAtrib | CmdChamaRotina | CmdExcreva| CmdLeia
    CmdSe → se ( Expressao ) faca inicio ListaCmd fim CmdSN
    CmdSN → senao inicio ListaCmd fim | ε
    ComandoPara → para CmdAtrib ate Expressao faca inicio ListaCmd fim
    ComandoRepita → repita ListaCmd ate Expressao
    CmdAtrib → ID <-- Expressao ;
    CmdChamaRotina → ID X ;
    CmdEscreva → escreva ( Expressao );
    CmdLeia → leia ( ID );
    
    Expressao → Expressao1 ListaExpressao
    ListaExpressao → OperadorRelacional Expressao | ε 
    OperadorRelacional → < | <= | > | >= | <> | =
    Expressao1 → Expressao2 ListaExpressao1
    ListaExpressao1 → OperadorLogico Expressao 1 | ε
    OperadorLogico → e | ou
    Expressao2 → Valor ListaExpressao2
    ListaExpressao2 → OperadorMatematico Expressao2 | ε
    OperadorMatematico → + | - | OperadorMatematico2
    OperadorMatematico2 → * | /
    Valor → verdadeiro | falso | literal | ( Expressao ) | Numerico| ID ListaParametros | Negacao Expressao
    Negacao → nao Negacao | ε
    
    Parametros → ( ListaParametros ) | ε
    ListaParametros → Valor AddParametros
    AddParametros → , ListaParametros | ε
    """
