# Programa destinado a análise dos objetos recuperados pelo LEXER

from Stack import stack
from tag import TAGs
class Parser:

    def __init__(self):
        self.entrada = None
        self.cursor = 0 # Variavel de controle de entrada da lista de tokens
        self.estado = 0
        self.pilha = stack()
        self.is_goto = False

        self.skipperORreduced = False
        self.errors = 0
        self.countCharVazio = 0
    def parsermain(self, lista_Tokens):
        """
        Módulo que compara os tokens reconhecidos pelo PARSER com a gramatica portugolo
        O objetivo final é um parser bottom up

        """
        # TABELA -------> PILHA | ENTRADA | AÇÃO
        self.lista_Tokens = lista_Tokens # entrada
        self.SKIP(1, '$')
        self.parser_analisys()

    def SKIP(self, estado, lexema):
        self.skipperORreduced = True
        if self.is_goto:
            print('Output: Reduced a ' + str(lexema) + ' GOTO to state ' + str(estado))
        else:
            print('Output: Found a ' + str(lexema) + ' SKIP to state ' + str(estado))

        if self.is_goto == False and estado != 1 and lexema != 'Ɛ':
            self.cursor = self.cursor + 1

        if lexema == 'Ɛ' or lexema == 'Negacao':
            self.countCharVazio = self.countCharVazio + 1
        else:
            self.countCharVazio = 0

        self.is_goto = False
        self.estado = estado
        self.pilha.pack(lexema)
        self.pilha.pack(estado)
        self.pilha.print()

    def REDUCE(self, qtd_lexemas, lex_reduce):
        self.skipperORreduced = True
        for i in range(qtd_lexemas * 2):
            self.pilha.unpack()
        self.estado = self.pilha.entry()
        self.entrada = lex_reduce
        self.is_goto = True
        self.pilha.print()

    def parser_analisys(self):
        while(self.estado != 0 and self.errors <= 1):
            if self.is_goto == False:
                self.entrada = self.lista_Tokens[self.cursor].getTag()
            self.switch_case()
            self.look_its_A_error()
            self.skipperORreduced = False

    def look_its_A_error(self):
        if self.skipperORreduced == False:
            print('Error entrada não reconhecida: est: '+ str(self.estado) +''+ str(self.lista_Tokens[self.cursor]))
            self.errors = self.errors + 1
            self.cursor = self.cursor + 1
        elif self.countCharVazio >= 4:
            print('Error entrada ocasionou loop: est: ' + str(self.estado) +''+ str(self.lista_Tokens[self.cursor]))
            self.errors = self.errors + 1
            self.cursor = self.cursor + 1
            for i in range(4):
                self.pilha.unpack()

    def SYNC(self, Gram):
        temp = TAGs.FRISTS[Gram]
        for item in temp:
            if self.entrada == item:

                return
        else:

            pass


    def switch_case(self):
        estado = self.estado
        if (estado == 187 or estado == 140 or estado == 134 or estado == 129):
            estado = 124
        method_name = 'estado_' + str(estado)
        method = getattr(self, method_name, lambda: 'Estado inválido')
        method()

    def estado_0(self):
        print('Acabou')

    def estado_1(self):
        """
        + Compilador: •Programa : EOF
        + Programa: •"algoritmo" DeclaraVar ListaCmd "fim" "algoritmo" ListaRotina : EOF
        """
        if (self.entrada == 'KW_RES_algorithm'):
            self.SKIP(3,'KW_RES_algorithm')
        elif (self.entrada == 'Programa'):
            self.SKIP(2,"Programa")
        elif (self.entrada == 'Compilador'):
            self.SKIP(0, 'Compilador')
    def estado_2(self):
        """
        + Compilador: Programa• : EOF
        """
        self.REDUCE(1, 'Compilador')
    def estado_3(self):
        """
        + Programa: "algoritmo" •DeclaraVar ListaCmd "fim" "algoritmo" ListaRotina : EOF
        + DeclaraVar: •"declare" Tipo ListaID ";" ListaDeclaraVar: ListaCmd
        """
        if (self.entrada == 'KW_RES_var'):
            self.SKIP(11, 'KW_RES_var')
        elif (self.entrada == 'DeclaraVar'):
            self.SKIP(25, 'DeclaraVar')
        else:
            self.SKIP(311, 'Ɛ')
    def estado_311(self):
        """
        + DeclaraVar: Ɛ• : ListaCmd
        """
        self.REDUCE(1, 'DeclaraVar')
    def estado_4(self):
        """
        + DeclaraVar: "declare" Tipo •ListaID ";" ListaDeclaraVar: ListaCmd
        + ListaID: •ID ListaAdd : Tipo
        """
        if (self.entrada == 'KW_RES_ID'):
            self.SKIP(5, 'KW_RES_ID')
        elif (self.entrada == 'ListaID'):
            self.SKIP(16, 'ListaID')
    def estado_5(self):
        """
        + ListaID: ID •ListaAdd : Tipo
        + ListaAdd: •", " ListaID : Tipo
        + ListaAdd: •Ɛ : Tipo
        """
        if (self.entrada == 'OP_VIR'):
            self.SKIP(7, 'OP_VIR')
        elif (self.entrada == 'ListaAdd'):
            self.SKIP(6, 'ListaAdd')
        else:
            self.SKIP(8, 'Ɛ')
    def estado_6(self):
        """
        + ListaID: ID ListaAdd• : ";"
        """
        self.REDUCE(2, 'ListaID')
    def estado_7(self):
        """
        + ListaAdd: ", " •ListaID : ";"
        + ListaID: •ID ListaAdd : ";"
        """
        if (self.entrada == 'KW_RES_ID'):
            self.SKIP(5, 'KW_RES_ID')
        elif (self.entrada == 'ListaID'):
            self.SKIP(10,'ListaID')
    def estado_8(self):
        """
        + ListaAdd: Ɛ•: ";"
        """
        self.REDUCE(1, 'ListaAdd')
    def estado_10(self):
        """
        + ListaAdd: "," ListaID •: ";"
        """
        self.REDUCE(2, 'ListaAdd')
    def estado_11(self):
        """
        + DeclaraVar: "declare" •Tipo ListaID";" ListaDeclaraVar: ListaCmd
        + Tipo: •"logico" : ListaID
        + Tipo: •"numerico" : ListaID
        + Tipo: •"literal" : ListaID
        + Tipo: •"nulo" : ListaID
        """
        if (self.entrada == 'Tipo'):
            self.SKIP(4, 'Tipo')
        elif (self.entrada == 'KW_RES_logic'):
            self.SKIP(12, 'KW_RES_logic')
        elif (self.entrada == 'KW_RES_number'):
            self.SKIP(13, 'KW_RES_number')
        elif (self.entrada == 'KW_RES_string'):
            self.SKIP(14, 'KW_RES_string')
        elif (self.entrada == 'KW_RES_null'):
            self.SKIP(15, 'KW_RES_null')
    def estado_12(self):
        """
        + Tipo: "logico"• : ListaID
        """
        self.REDUCE(1, 'Tipo')
    def estado_13(self):
        """
        + Tipo: "numerico"• : ListaID
        """
        self.REDUCE(1, 'Tipo')
    def estado_14(self):
        """
        + Tipo: "literal"• : ListaID
        """
        self.REDUCE(1, 'Tipo')
    def estado_15(self):
        """
        + Tipo: "nulo"• : ListaID
        """
        self.REDUCE(1, 'Tipo')
    def estado_16(self):
        """
        + DeclaraVar: "declare" Tipo ListaID •";" ListaDeclaraVar: ListaCmd
        """
        if(self.entrada == 'OP_PV'):
            self.SKIP(17, 'OP_PV')
    def estado_17(self):
        """
        + DeclaraVar: "declare" Tipo ListaID ";" •ListaDeclaraVar: ListaCmd
        + ListaDeclaraVar: •Tipo ListaID "," ListaDeclaraVar : ListaCmd
        + ListaDeclaraVar: •Ɛ : ListaCmd
        + Tipo: •"logico" : ListaID
        + Tipo: •"numerico" : ListaID
        + Tipo: •"literal" : ListaID
        + Tipo: •"nulo" : ListaID
        """
        if (self.entrada == 'ListaDeclaraVar'):
            self.SKIP(18, 'ListaDeclaraVar')
        elif (self.entrada == 'Tipo'):
            self.SKIP(19, 'Tipo')
        elif (self.entrada == 'KW_RES_logic'):
            self.SKIP(12, 'KW_RES_logic')
        elif (self.entrada == 'KW_RES_number'):
            self.SKIP(13, 'KW_RES_number')
        elif (self.entrada == 'STRING'):
            self.SKIP(14, 'STRING')
        elif (self.entrada == 'KW_RES_null'):
            self.SKIP(15, 'KW_RES_null')
        else:
            self.SKIP(23, 'Ɛ')
    def estado_18(self):
        """
        + DeclaraVar: "declare" Tipo ListaID";" ListaDeclaraVar•: ListaCmd
        """
        self.REDUCE(5, 'DeclaraVar')
    def estado_19(self):
        """
         + ListaDeclaraVar: Tipo •ListaID ";" ListaDeclaraVar: ListaCmd
         + ListaID: •ID ListaAdd: ";"
        """
        if (self.entrada == 'ListaID'):
            self.SKIP(20, 'ListaID')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(5, 'KW_RES_ID')
    def estado_20(self):
        """
        + ListaDeclaraVar: Tipo ListaID •";" ListaDeclaraVar: ListaCmd
        """
        if (self.entrada == 'OP_PV'):
            self.SKIP(21, 'OP_PV')
    def estado_21(self):
        """
        + ListaDeclaraVar: Tipo ListaID  ";" •ListaDeclaraVar: ListaCmd
        + ListaDeclaraVar: •Tipo ListaID "," ListaDeclaraVar : ListaCmd
        + ListaDeclaraVar: •Ɛ : ListaCmd
        + Tipo: •"logico" : ListaID
        + Tipo: •"numerico" : ListaID
        + Tipo: •"literal" : ListaID
        + Tipo: •"nulo" : ListaID
        """
        if (self.entrada == 'ListaDeclaraVar'):
            self.SKIP(22, 'ListaDeclaraVar')
        elif (self.entrada == 'Tipo'):
            self.SKIP(19, 'Tipo')
        elif (self.entrada == 'KW_RES_logic'):
            self.SKIP(12, 'KW_RES_logic')
        elif (self.entrada == 'KW_RES_number'):
            self.SKIP(13, 'KW_RES_number')
        elif (self.entrada == 'STRING'):
            self.SKIP(14, 'STRING')
        elif (self.entrada == 'KW_RES_null'):
            self.SKIP(15, 'KW_RES_null')
        else:
            self.SKIP(23, 'Ɛ')
    def estado_22(self):
        """
        + ListaDeclaraVar: Tipo ListaID ";" ListaDeclaraVar•: ListaCmd
        """
        self.REDUCE(4, 'ListaDeclaraVar')
    def estado_23(self):
        """
        + ListaDeclaraVar: Ɛ•: ListaCmd
        """
        self.REDUCE(1, 'ListaDeclaraVar')
    def estado_24(self):
        pass
    def estado_25(self):
        """
        + Programa: "algoritmo" DeclaraVar •ListaCmd "fim" "algoritmo" ListaRotina : EOF
        + ListaCmd: •Cmd ListaCmd : "fim"
        + ListaCmd: •Ɛ: "fim"
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(89, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(26, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(28, 'Ɛ')
    def estado_26(self):
        """
        + ListaCmd: Cmd •ListaCmd : "fim"
        + ListaCmd: •Cmd ListaCmd : "fim"
        + ListaCmd: •Ɛ: "fim"
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(27, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(26, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(28, 'Ɛ')
    def estado_27(self):
        """
        + ListaCmd: Cmd ListaCmd•: "fim"
        """
        self.REDUCE(2, 'ListaCmd')
    def estado_28(self):
        """
        + ListaCmd: Ɛ•: "fim"
        """
        self.REDUCE(1, 'ListaCmd')
    def estado_29(self):
        """
        + Cmd: CmdSe•: ListaCmd
        """
        self.REDUCE(1, 'Cmd')
    def estado_30(self):
        """
        + Cmd: CmdPara•: ListaCmd
        """
        self.REDUCE(1, 'Cmd')
    def estado_31(self):
        """
        + Cmd: CmdRepita•: ListaCmd
        """
        self.REDUCE(1, 'Cmd')
    def estado_32(self):
        """
        + Cmd: CmdLeia•: ListaCmd
        """
        self.REDUCE(1, 'Cmd')
    def estado_33(self):
        """
        + Cmd: CmdAtrib•: ListaCmd
        """
        self.REDUCE(1, 'Cmd')
    def estado_34(self):
        """
        + Cmd: CmdChamaRotina•: ListaCmd
        """
        self.REDUCE(1, 'Cmd')
    def estado_35(self):
        """
        + Cmd: CmdEscreva•: ListaCmd
        """
        self.REDUCE(1, 'Cmd')
    def estado_360(self):
        """
        + Cmd: CmdEnquanto•: ListaCmd
        """
        self.REDUCE(1, 'Cmd')
    def estado_36(self):
        """
        + CmdSe: "se" •"(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        """
        if(self.entrada == 'OP_AP'):
            self.SKIP(37,'OP_AP')
    def estado_37(self):
        """
        + CmdSe: "se" "(" •Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + Expressao: •Expressao1 ListaExpressao : ")"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(38,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(140,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_38(self):
        """
        + CmdSe: "se" "(" Expressao •")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        """
        if (self.entrada == 'OP_FP'):
            self.SKIP(39, 'OP_FP')
    def estado_39(self):
        """
        + CmdSe: "se" "(" Expressao ")" •"inicio" ListaCmd "fim" CmdSN : ListaCmd
        """
        if (self.entrada == 'KW_RES_begin'):
            self.SKIP(40, 'KW_RES_begin')
    def estado_40(self):
        """
        + CmdSe: "se" "(" Expressao ")" "inicio" •ListaCmd "fim" CmdSN : ListaCmd
        + ListaCmd: •Cmd ListaCmd : "fim"
        + ListaCmd: •Ɛ: "fim"
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(41, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(26, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(28, 'Ɛ')
    def estado_41(self):
        """
        + CmdSe: "se" "(" Expressao ")" "inicio" ListaCmd •"fim" CmdSN : ListaCmd
        """
        if(self.entrada == 'KW_RES_end'):
            self.SKIP(42, 'KW_RES_end')
    def estado_42(self):
        """
        + CmdSe: "se" "(" Expressao ")" "inicio" ListaCmd "fim" •CmdSN : ListaCmd
        + CmdSN: •"senao" "inicio" ListaCmd "fim": ListaCmd
        + CmdSN: •Ɛ: ListaCmd
        """
        if (self.entrada == 'CmdSN'):
            self.SKIP(43, 'CmdSN')
        elif (self.entrada == 'KW_RES_else'):
            self.SKIP(44, 'KW_RES_else')
        else:
            self.SKIP(421, 'Ɛ')
    def estado_421(self):
        """
        + CmdSN: Ɛ•: ListaCmd
        """
        self.REDUCE(1, 'CmdSN')
    def estado_43(self):
        """
        + CmdSe: "se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN• : ListaCmd
        """
        self.REDUCE(8, 'CmdSe')
    def estado_44(self):
        """
        + CmdSN: "senao" •"inicio" ListaCmd "fim": ListaCmd
        """
        if (self.entrada == 'KW_RES_begin'):
            self.SKIP(45, 'KW_RES_begin')
    def estado_45(self):
        """
        + CmdSN: "senao" "inicio" •ListaCmd "fim": ListaCmd
        + ListaCmd: •Cmd ListaCmd : "fim"
        + ListaCmd: •Ɛ: "fim"
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(46, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(26, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(28, 'Ɛ')
    def estado_46(self):
        """
        + CmdSN: "senao" "inicio" ListaCmd •"fim": ListaCmd
        """
        if (self.entrada == 'KW_RES_end'):
            self.SKIP(47, 'KW_RES_end')
    def estado_47(self):
        """
        + CmdSN: "senao" "inicio" ListaCmd "fim"•: ListaCmd
        """
        self.REDUCE(4, 'CmdSN')
    def estado_48(self):
        """
        + CmdEnquanto: "enquanto" •"(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        """
        if (self.entrada == 'OP_AP'):
            self.SKIP(49, 'OP_AP')
    def estado_49(self):
        """
        + CmdEnquanto: "enquanto" "(" •Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + Expressao: •Expressao1 ListaExpressao : ")"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(50,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(140,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_50(self):
        """
        + CmdEnquanto: "enquanto" "(" Expressao •")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        """
        if (self.entrada == 'OP_FP'):
            self.SKIP(51, 'OP_FP')
    def estado_51(self):
        """
        + CmdEnquanto: "enquanto" "(" Expressao ")" •"faca" "inicio" ListaCmd "fim" : ListaCmd
        """
        if (self.entrada == 'KW_RES_DoIt'):
            self.SKIP(52, 'KW_RES_DoIt')
    def estado_52(self):
        """
        + CmdEnquanto: "enquanto" "(" Expressao ")" "faca" •"inicio" ListaCmd "fim" : ListaCmd
        """
        if (self.entrada == 'KW_RES_begin'):
            self.SKIP(53, 'KW_RES_begin')
    def estado_53(self):
        """
        + CmdEnquanto: "enquanto" "(" Expressao ")" "faca" "inicio" •ListaCmd "fim" : ListaCmd
        + ListaCmd: •Cmd ListaCmd : "fim"
        + ListaCmd: •Ɛ: "fim"
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(54, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(26, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(28, 'Ɛ')
    def estado_54(self):
        """
        + CmdEnquanto: "enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd •"fim" : ListaCmd
        """
        if (self.entrada == 'KW_RES_end'):
            self.SKIP(55, 'KW_RES_end')
    def estado_55(self):
        """
        + CmdEnquanto: "enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" •: ListaCmd
        """
        self.REDUCE(8, 'CmdEnquanto')
    def estado_56(self):
        """
        + CmdPara: "para" •CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": "ate"
        """
        if (self.entrada == 'CmdAtrib'):
            self.SKIP(61, 'CmdAtrib')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(57, 'KW_RES_ID')
    def estado_57(self):
        """
        + CmdAtrib: ID •"<--" Expressao ";": "ate"
        """
        if (self.entrada == 'OP_ATR'):
            self.SKIP(58, 'OP_ATR')
    def estado_58(self):
        """
        + CmdAtrib: ID "<--" •Expressao ";": "ate"
        + Expressao: •Expressao1 ListaExpressao : ")"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(59,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(124,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_59(self):
        """
        + CmdAtrib: ID "<--" Expressao •";": "ate"
        """
        if (self.entrada == 'OP_PV'):
            self.SKIP(58, 'OP_PV')
    def estado_60(self):
        """
        + CmdAtrib: ID "<--" Expressao ";"•: "ate"
        """
        self.REDUCE(4, 'CmdAtrib')
    def estado_61(self):
        """
        + CmdPara: "para" CmdAtrib •"ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        """
        if (self.entrada == 'KW_RES_dwhile'):
            self.SKIP(61, 'KW_RES_dwhile')
    ######################################################### EDITAR ABAIXO EXPRESSAO : FACA
    def estado_62(self):
        """
        + CmdPara: "para" CmdAtrib "ate" •Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + Expressao: •Expressao1 ListaExpressao : "faca"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(63,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(124,'Expressao1') # OLHAR AQ
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_63(self):
        """
        + CmdPara: "para" CmdAtrib "ate" Expressao •"faca" "inicio" ListaCmd "fim" : ListaCmd
        """
        if (self.entrada == 'KW_RES_DoIt'):
            self.SKIP(64, 'KW_RES_DoIt')
    def estado_64(self):
        """
        + CmdPara: "para" CmdAtrib "ate" Expressao "faca" •"inicio" ListaCmd "fim" : ListaCmd
        """
        if (self.entrada == 'KW_RES_begin'):
            self.SKIP(65, 'KW_RES_begin')
    def estado_65(self):
        """
        + CmdPara: "para" CmdAtrib "ate" Expressao "faca" "inicio" •ListaCmd "fim" : ListaCmd
        + ListaCmd: •Cmd ListaCmd : "fim"
        + ListaCmd: •Ɛ: "fim"
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(66, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(26, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(28, 'Ɛ')
    def estado_66(self):
        """
        + CmdPara: "para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd •"fim" : ListaCmd
        """
        if (self.entrada == 'KW_RES_end'):
            self.SKIP(65, 'KW_RES_end')
    def estado_67(self):
        """
        + CmdPara: "para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim"• : ListaCmd
        """
        self.REDUCE(8, 'CmdPara')
    def estado_68(self):
        """
        + CmdRepita: "repita" •ListaCmd "ate" Expressao : ListaCmd
        + ListaCmd: •Cmd ListaCmd : "ate"
        + ListaCmd: •Ɛ: "ate"
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(69, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(72, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(73, 'Ɛ')
    def estado_69(self):
        """
        + CmdRepita: "repita" ListaCmd •"ate" Expressao : ListaCmd
        """
        if (self.entrada == 'KW_RES_dwhile'):
            self.SKIP(70, 'KW_RES_dwhile')
        print('huehuasd - ' + str(self.skipperORreduced))
    def estado_70(self):
        """
        + CmdRepita: "repita" ListaCmd "ate" •Expressao : ListaCmd
        + Expressao: •Expressao1 ListaExpressao : ListaCmd
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(71,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(129,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_71(self):
        """
        + CmdRepita: "repita" ListaCmd "ate" Expressao• : ListaCmd
        """
        self.REDUCE(4, 'CmdRepita')
    def estado_72(self):
        """
        + ListaCmd: Cmd •ListaCmd : "ate"
        + ListaCmd: •Cmd ListaCmd : "ate"
        + ListaCmd: •Ɛ: "ate"
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(74, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(72, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(73, 'Ɛ')
    def estado_73(self):
        """
        + ListaCmd: Ɛ•: "ate"
        """
        self.REDUCE(1, 'ListaCmd')
    def estado_74(self):
        """
        + ListaCmd: Cmd ListaCmd• : "ate"
        """
        self.REDUCE(2, 'ListaCmd')
    def estado_75(self):
        """
        + CmdAtrib: ID •"<--" Expressao ";": ListaCmd
        + CmdChamaRotina: ID •Parametros ";": ListaCmd
        + Parametros: •"(" ListaParametros ")" : ";"
        + Parametros: •Ɛ : ";"
        """
        if (self.entrada == 'OP_ATR'):
            self.SKIP(76, 'OP_ATR')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(121, 'OP_AP')
        elif (self.entrada == 'Parametros'):
            self.SKIP(119, 'Parametros')
        else:
            self.SKIP(118, 'Ɛ')
    def estado_76(self):
        """
        + CmdAtrib: ID "<--" •Expressao ";": "ate"
        + Expressao: •Expressao1 ListaExpressao : ";"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(77,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(124,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_77(self):
        """
        + CmdAtrib: ID "<--" Expressao •";": "ate"
        """
        if (self.entrada == 'OP_PV'):
            self.SKIP(78, 'OP_PV')
    def estado_78(self):
        """
        + CmdAtrib: ID "<--" Expressao ";"•: "ate"
        """
        self.REDUCE(4, 'CmdAtrib')
    def estado_79(self):
        """
        + CmdEscreva: "escreva" •"(" Expressao ")" ";": ListaCmd
        """
        if (self.entrada == 'OP_AP'):
            self.SKIP(80, 'OP_AP')
    def estado_80(self):
        """
        + CmdEscreva: "escreva" "(" •Expressao ")" ";": ListaCmd
        + Expressao: •Expressao1 ListaExpressao : ")"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(81,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(140,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_81(self):
        """
        + CmdEscreva: "escreva" "(" Expressao •")" ";": ListaCmd
        """
        if (self.entrada == 'OP_FP'):
            self.SKIP(82, 'OP_FP')
    def estado_82(self):
        """
        + CmdEscreva: "escreva" "(" Expressao ")" •";": ListaCmd
        """
        if (self.entrada == 'OP_PV'):
            self.SKIP(83, 'OP_PV')
    def estado_83(self):
        """
        + CmdEscreva: "escreva" "(" Expressao ")" ";"•: ListaCmd
        """
        self.REDUCE(5, 'CmdEscreva')
    def estado_84(self):
        """
        + CmdLeia: "leia" •"(" ID ")" ";": ListaCmd
        """
        if (self.entrada == 'OP_AP'):
            self.SKIP(85, 'OP_AP')
    def estado_85(self):
        """
        + CmdLeia: "leia" "(" •ID ")" ";": ListaCmd
        """
        if (self.entrada == 'KW_RES_ID'):
            self.SKIP(86, 'KW_RES_ID')
    def estado_86(self):
        """
        + CmdLeia: "leia" "(" ID •")" ";": ListaCmd
        """
        if (self.entrada == 'OP_FP'):
            self.SKIP(87, 'OP_FP')
    def estado_87(self):
        """
        + CmdLeia: "leia" "(" ID ")" •";": ListaCmd
        """
        if (self.entrada == 'OP_PV'):
            self.SKIP(88, 'OP_PV')
    def estado_88(self):
        """
        + CmdLeia: "leia" "(" ID ")" ";"•: ListaCmd
        """
        self.REDUCE(5, 'CmdLeia')
    def estado_89(self):
        """
        + Programa: "algoritmo" DeclaraVar ListaCmd •"fim" "algoritmo" ListaRotina : EOF
        """
        if (self.entrada == 'KW_RES_end'):
            self.SKIP(90, 'KW_RES_end')
    def estado_90(self):
        """
        + Programa: "algoritmo" DeclaraVar ListaCmd "fim" •"algoritmo" ListaRotina : EOF
        """
        if (self.entrada == 'KW_RES_algorithm'):
            self.SKIP(91, 'KW_RES_algorithm')
    def estado_91(self):
        """
        + Programa: "algoritmo" DeclaraVar ListaCmd "fim" "algoritmo" •ListaRotina : EOF
        + ListaRotina: •Rotina ListaRotina: EOF
        + ListaRotina: •Ɛ : EOF
        + Rotina: •"subrotina" ID "(" Param ")" DeclaraVar ListaCmd Retorno "fim" "subrotina" : ListaRotina
        """
        if (self.entrada == 'ListaRotina'):
            self.SKIP(192, 'ListaRotina')
        elif (self.entrada == 'KW_RES_met'):
            self.SKIP(94, 'KW_RES_met')
        elif (self.entrada == 'Rotina'):
            self.SKIP(92, 'Rotina')
        else:
            self.SKIP(93, 'Ɛ')
    def estado_92(self):
        """
        + ListaRotina: Rotina •ListaRotina: EOF
        + ListaRotina: •Rotina ListaRotina: EOF
        + ListaRotina: •Ɛ : EOF
        + Rotina: •"subrotina" ID "(" Param ")" DeclaraVar ListaCmd Retorno "fim" "subrotina" : ListaRotina
        """
        if (self.entrada == 'ListaRotina'):
            self.SKIP(931, 'ListaRotina')
        elif (self.entrada == 'KW_RES_met'):
            self.SKIP(94, 'KW_RES_met')
        elif (self.entrada == 'Rotina'):
            self.SKIP(92, 'Rotina')
        else:
            self.SKIP(93, 'Ɛ')
    def estado_93(self):
        """
        + ListaRotina: Ɛ• : EOF
        """
        self.REDUCE(1, 'ListaRotina')
    def estado_931(self):
        """
        + ListaRotina: Rotina ListaRotina•: EOF
        """
        self.REDUCE(2, 'ListaRotina')

    def estado_94(self):
        """
        + Rotina: "subrotina" •ID "(" Param ")" DeclaraVar ListaCmd Retorno "fim" "subrotina" : ListaRotina
        """
        if (self.entrada == 'KW_RES_ID'):
            self.SKIP(95, 'KW_RES_ID')
    def estado_95(self):
        """
        + Rotina: "subrotina" ID •"(" Param ")" DeclaraVar ListaCmd Retorno "fim" "subrotina" : ListaRotina
        """
        if (self.entrada == 'OP_AP'):
            self.SKIP(96, 'OP_AP')
    def estado_96(self):
        """
        + Rotina: "subrotina" ID "(" •Param ")" DeclaraVar ListaCmd Retorno "fim" "subrotina" : ListaRotina
        + Param : •ListaID Tipo ListaParam : ")"
        + ListaID: •ID ListaAdd: Tipo
        """
        if (self.entrada == 'Param'):
            self.SKIP(106, 'Param')
        elif (self.entrada == 'ListaID'):
            self.SKIP(97, 'ListaID')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(5, 'KW_RES_ID')
    def estado_97(self):
        """
        + Param : ListaID •Tipo ListaParam : ")"
        + Tipo: •"logico" : ListaParam
        + Tipo: •"numerico" : ListaParam
        + Tipo: •"literal" : ListaParam
        + Tipo: •"nulo" : ListaParam
        """
        if (self.entrada == 'Tipo'):
            self.SKIP(98, 'Tipo')
        elif (self.entrada == 'KW_RES_logic'):
            self.SKIP(100, 'KW_RES_logic')
        elif (self.entrada == 'KW_RES_number'):
            self.SKIP(101, 'KW_RES_number')
        elif (self.entrada == 'STRING'):
            self.SKIP(102, 'STRING')
        elif (self.entrada == 'KW_RES_null'):
            self.SKIP(103, 'KW_RES_null')
    def estado_98(self):
        """
        + Param : ListaID Tipo •ListaParam : ")"
        + ListaParam: •"," Param : ")"
        + ListaParam: •Ɛ : ")"
        """
        if (self.entrada == 'ListaParam'):
            self.SKIP(105, 'ListaParam')
        elif (self.entrada == 'OP_VIR'):
            self.SKIP(99, 'OP_VIR')
        else:
            self.SKIP(104, 'Ɛ')
    def estado_99(self):
        """
        + ListaParam: "," •Param : ")"
        + Param : •ListaID Tipo ListaParam : ")"
        + ListaID: •ID ListaAdd: Tipo
        """
        if (self.entrada == 'Param'):
            self.SKIP(991, 'OP_PV')
        elif (self.entrada == 'ListaID'):
            self.SKIP(97, 'ListaID')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(5, 'KW_RES_ID')
    def estado_991(self):
        """
        + ListaParam: "," Param• : ")"
        """
        self.REDUCE(2, 'ListaParam')
    def estado_100(self):
        """
        + Tipo: "logico"• : ListaParam
        """
        self.REDUCE(1, 'Tipo')
    def estado_101(self):
        """
        + Tipo: "numerico"• : ListaParam
        """
        self.REDUCE(1, 'Tipo')
    def estado_102(self):
        """
        + Tipo: "literal"• : ListaParam
        """
        self.REDUCE(1, 'Tipo')
    def estado_103(self):
        """
        + Tipo: "nulo"• : ListaParam
        """
        self.REDUCE(1, 'Tipo')
    def estado_104(self):
        """
        + ListaParam: Ɛ• : ")"
        """
        self.REDUCE(1, 'ListaParam')
    def estado_105(self):
        """
        + Param : ListaID Tipo ListaParam• : ")"
        """
        self.REDUCE(3, 'Param')
    def estado_106(self):
        """
        + Rotina: "subrotina" ID "(" Param •")" DeclaraVar ListaCmd Retorno "fim" "subrotina" : ListaRotina
        """
        if (self.entrada == 'OP_FP'):
            self.SKIP(107, 'OP_FP')
    def estado_107(self):
        """
        + Rotina: "subrotina" ID "(" Param ")" •DeclaraVar ListaCmd Retorno "fim" "subrotina" : ListaRotina
        + DeclaraVar: •"declare" Tipo ListaID ";" ListaDeclaraVar: ListaCmd
        + DeclaraVar: •Ɛ ListaCmd
        """
        if (self.entrada == 'DeclaraVar'):
            self.SKIP(108, 'DeclaraVar')
        elif (self.entrada == 'KW_RES_var'):
            self.SKIP(11, 'KW_RES_var')
        else:
            self.SKIP(311, 'Ɛ')
    def estado_108(self):
        """
        + Rotina: "subrotina" ID "(" Param ")" DeclaraVar •ListaCmd Retorno "fim" "subrotina" : ListaRotina
        + ListaCmd: •Cmd ListaCmd : Retorno
        + ListaCmd: •Ɛ: Retorno
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(112, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(109, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(110, 'Ɛ')
    def estado_109(self):
        """
        + ListaCmd: Cmd •ListaCmd : Retorno
        + ListaCmd: •Cmd ListaCmd : Retorno
        + ListaCmd: •Ɛ: Retorno
        + Cmd: •CmdSe : ListaCmd
        + Cmd: •CmdEnquanto : ListaCmd
        + Cmd: •CmdPara : ListaCmd
        + Cmd: •CmdRepita : ListaCmd
        + Cmd: •CmdAtrib : ListaCmd
        + Cmd: •CmdChamaRotina : ListaCmd
        + Cmd: •CmdEscreva : ListaCmd
        + Cmd: •CmdLeia : ListaCmd
        + CmdSe: •"se" "(" Expressao ")" "inicio" ListaCmd "fim" CmdSN : ListaCmd
        + CmdEnquanto: •"enquanto" "(" Expressao ")" "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdPara: •"para" CmdAtrib "ate" Expressao "faca" "inicio" ListaCmd "fim" : ListaCmd
        + CmdRepita: •"repita" ListaCmd "ate" Expressao : ListaCmd
        + CmdAtrib: •ID "<--" Expressao ";": ListaCmd
        + CmdChamaRotina: •ID Parametros Expressao ";": ListaCmd
        + CmdEscreva: •"escreva" "(" Expressao ")" ";": ListaCmd
        + CmdLeia: •"leia" "(" ID ")" ";": ListaCmd
        """
        if(self.entrada == 'ListaCmd'):
            self.SKIP(111, 'ListaCmd')
        elif(self.entrada == 'Cmd'):
            self.SKIP(109, 'Cmd')
        elif (self.entrada == 'CmdSe'):
            self.SKIP(29, 'CmdSe')
        elif (self.entrada == 'CmdEnquanto'):
            self.SKIP(360, 'CmdEnquanto')
        elif (self.entrada == 'CmdPara'):
            self.SKIP(30, 'CmdPara')
        elif (self.entrada == 'CmdRepita'):
            self.SKIP(31, 'CmdRepita')
        elif (self.entrada == 'CmdAtrib'):
            self.SKIP(33, 'CmdAtrib')
        elif (self.entrada == 'CmdChamaRotina'):
            self.SKIP(34, 'CmdChamaRotina')
        elif (self.entrada == 'CmdEscreva'):
            self.SKIP(35, 'CmdEscreva')
        elif (self.entrada == 'CmdLeia'):
            self.SKIP(32, 'CmdLeia')
        elif (self.entrada == 'KW_RES_if'):
            self.SKIP(36, 'KW_RES_if')
        elif (self.entrada == 'KW_RES_while'):
            self.SKIP(48, 'KW_RES_while')
        elif (self.entrada == 'KW_RES_for'):
            self.SKIP(56, 'KW_RES_for')
        elif (self.entrada == 'KW_RES_do'):
            self.SKIP(68, 'KW_RES_do')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(75, 'KW_RES_ID')
        elif (self.entrada == 'KW_RES_read'):
            self.SKIP(84, 'KW_RES_read')
        elif (self.entrada == 'KW_RES_write'):
            self.SKIP(79, 'KW_RES_write')
        else:
            self.SKIP(110, 'Ɛ')
    def estado_110(self):
        """
        + ListaCmd: Ɛ• : Retorno
        """
        self.REDUCE(1, 'ListaCmd')
    def estado_111(self):
        """
        + ListaCmd: Cmd ListaCmd• : Retorno
        """
        self.REDUCE(2, 'ListaCmd')
    def estado_112(self):
        """
        + Rotina: "subrotina" ID "(" Param ")" DeclaraVar ListaCmd •Retorno "fim" "subrotina" : ListaRotina
        + Retorno: •"retorne" Expressao: "fim"
        + Retorno: •Ɛ : "fim"
        """
        if (self.entrada == 'Retorno'):
            self.SKIP(113, 'Retorno')
        elif (self.entrada == 'KW_RES_return'):
            self.SKIP(116, 'OP_PV')
        else:
            self.SKIP(1121, 'Ɛ')
    def estado_1121(self):
        """
         Retorno: Ɛ• : "fim"
        """
        self.REDUCE(1, 'Retorno')
    def estado_113(self):
        """
        + Rotina: "subrotina" ID "(" Param ")" DeclaraVar ListaCmd Retorno •"fim" "subrotina" : ListaRotina
        """
        if (self.entrada == 'KW_RES_end'):
            self.SKIP(114, 'KW_RES_end')
    def estado_114(self):
        """
        + Rotina: "subrotina" ID "(" Param ")" DeclaraVar ListaCmd Retorno "fim" •"subrotina" : ListaRotina
        """
        if (self.entrada == 'KW_RES_met'):
            self.SKIP(115, 'KW_RES_met')
    def estado_115(self):
        """
        + Rotina: "subrotina" ID "(" Param ")" DeclaraVar ListaCmd Retorno "fim" "subrotina"• : ListaRotina
        """
        self.REDUCE(10, 'Rotina')
    def estado_116(self):
        """
        + Retorno: "retorne" •Expressao: "fim"
        + Expressao: •Expressao1 ListaExpressao : ")"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(117,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(134,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_117(self):
        """
        + Retorno: "retorne" Expressao•: "fim"
        """
        self.REDUCE(2, 'Retorno')
    def estado_118(self):
        """
        + Parametros: Ɛ•: ";"
        """
        self.REDUCE(1, 'Parametros')
    def estado_119(self):
        """
        + CmdChamaRotina: ID Parametros •";": ListaCmd
        """
        if (self.entrada == 'OP_PV'):
            self.SKIP(120, 'OP_PV')
    def estado_120(self):
        """
        + CmdChamaRotina: ID Parametros ";"•: ListaCmd
        """
        self.REDUCE(3, 'CmdChamaRotina')
######################################################################################
    def estado_121(self):
        """
        + Parametros: "(" •ListaParametros ")": ListaCmd
        + ListaParametros: •Expressao AddParametros : ")"
        + Expressao: •Expressao1 ListaExpressao : ")"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if (self.entrada == 'ListaParametros'):
            self.SKIP(122, 'ListaParametros')
        elif(self.entrada == 'Expressao'):
            self.SKIP(1221,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(187,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_122(self):
        """
        + Parametros: "(" ListaParametros •")": ListaCmd
        """
        if (self.entrada == 'OP_FP'):
            self.SKIP(123, 'OP_FP')
    def estado_1221(self):
        """
        + ListaParametros: Expressao •AddParametros : ")"
        + AddParametros: •"," ListaParametros: ")"
        + AddParametros: •Ɛ: ")"
        """
        if (self.entrada == 'AddParametros'):
            self.SKIP(1222, 'AddParametros')
        elif (self.entrada == 'OP_VIR'):
            self.SKIP(1224, 'OP_VIR')
        else:
            self.SKIP(1223, 'Ɛ')

    def estado_1222(self):
        """
        + ListaParametros: Expressao AddParametros• : ")"
        """
        self.REDUCE(2, 'ListaParametros')

    def estado_1223(self):
        """
        + AddParametros: Ɛ•: ")"
        """
        self.REDUCE(1, 'AddParametros')
    def estado_1224(self):
        """
        + AddParametros: "," •ListaParametros: ")"
        + ListaParametros: •Expressao AddParametros : ")"
        + Expressao: •Expressao1 ListaExpressao : AddParametros
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if (self.entrada == 'ListaParametros'):
            self.SKIP(1225, 'ListaParametros')
        elif(self.entrada == 'Expressao'):
            self.SKIP(1221,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(187,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')

    def estado_1225(self):
        """
        + AddParametros: "," ListaParametros•: ")"
        """
        self.REDUCE(2, 'AddParametros')

    def estado_123(self):
        """
        + Parametros: "(" ListaParametros ")"•: ListaCmd
        """
        self.REDUCE(3, 'Parametros')
    def estado_124(self):
        """
        + Expressao: Expressao1 •ListaExpressao : ";"
        + ListaExpressao: •OperadorRelacional Expressao: ";"
        + ListaExpressao: •Ɛ : ";"
        + OperadorRelacional: •"<": Expressao
        + OperadorRelacional: •"<=": Expressao
        + OperadorRelacional: •">": Expressao
        + OperadorRelacional: •">=": Expressao
        + OperadorRelacional: •"=": Expressao
        + OperadorRelacional: •"<>": Expressao
        """
        if (self.entrada == 'ListaExpressao'):
            self.SKIP(126, 'ListaParametros')
        elif (self.entrada == 'OperadorRelacional'):
            self.SKIP(127, 'OperadorRelaconal')
        elif (self.entrada == 'OP_MA'):
            self.SKIP(183, 'OP_MA')
        elif (self.entrada == 'OP_MAEQ'):
            self.SKIP(184, 'OP_MAEQ')
        elif (self.entrada == 'OP_ME'):
            self.SKIP(181, 'OP_ME')
        elif (self.entrada == 'OP_MEEQ'):
            self.SKIP(182, 'OP_MEEQ')
        elif (self.entrada == 'OP_EQ'):
            self.SKIP(186, 'OP_EQ')
        elif (self.entrada == 'OP_DIF'):
            self.SKIP(185, 'OP_DIF')
        else:
            self.SKIP(125, 'Ɛ')
    def estado_125(self):
        """
        + ListaExpressao: Ɛ• : ";"
        """
        self.REDUCE(1, 'ListaExpressao')
    def estado_126(self):
        """
        + Expressao: Expressao1 ListaExpressao• : ";"
        """
        self.REDUCE(2, 'Expressao')
    def estado_127(self):
        """

        + ListaExpressao: OperadorRelacional •Expressao : ";"
        + Expressao: •Expressao1 ListaExpressao : ";"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if (self.entrada == 'Expressao'):
            self.SKIP(128, 'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(124, 'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_128(self):
        """
        + ListaExpressao: OperadorRelacional Expressao• : ";"
        """
        self.REDUCE(2, 'ListaExpresao')

    def estado_145(self):
        """
        + Expressao1: Expressao2 •ListaExpressao1 : ListaExpressao
        + ListaExpressao1: •OperadorLogico Expressao1 : ListaExpresssao
        + ListaExpressao1: •Ɛ : ListaExpressao
        + OperadorLogico: •"e" : Expressao1
        + OperadorLogico: •"ou" : Expressao1
        """

        if (self.entrada == 'ListaExpressao1'):
            self.SKIP(147, 'ListaExpressao1')
        elif (self.entrada == 'OperadorLogico'):
            self.SKIP(146, 'OperadorLogico')
        elif (self.entrada == 'KW_RES_and'):
            self.SKIP(149, 'KW_RES_and')
        elif (self.entrada == 'KW_RES_or'):
            self.SKIP(150, 'KW_RES_or')
        else:
            self.SKIP(148, 'Ɛ')

    def estado_146(self):
        """
        + ListaExpressao1: OperadorLogico •Expressao1 : ListaExpresssao
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao1'):
            self.SKIP(151,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')

    def estado_147(self):
        """
        + Expressao1: Expressao2 ListaExpressao1• : ListaExpressao
        """
        self.REDUCE(2, 'Expressao1')

    def estado_148(self):
        """
         + ListaExpressao1: Ɛ• : ListaExpresssao
        """
        self.REDUCE(1, 'ListaExpressao1')

    def estado_149(self):
        """
         + OperadorLogico: "e"• : Expressao1
        """
        self.REDUCE(1, 'OperadorLogico')

    def estado_150(self):
        """
         + OperadorLogico: "ou"• : Expressao1
        """
        self.REDUCE(1, 'OperadorLogico')

    def estado_151(self):
        """
        + ListaExpressao1: OperadorLogico Expressao1• : ListaExpresssao
        """
        self.REDUCE(2, 'ListaExpressao1')

    def estado_152(self):
        """
        + Expressao2: Valor •ListaExpressao2 : ListaExpressao1
        + ListaExpressao2: •OperadorMatematico Expressao2 : ListaExpresssao1
        + ListaExpressao2: •Ɛ : ListaExpressao1
        + OperadorMatematico: •"+" : Expressao2
        + OperadorMatematico: •"-" : Expressao2
        + OperadorMatematico: •OperadorMatematicoNivel2 : Expressao2
        + OperadorMatematicoNivel2: •"*" : Expressao2
        + OperadorMatematicoNivel2: •"/" : Expressao2
        """
        if (self.entrada == 'ListaExpressao2'):
            self.SKIP(153, 'ListaExpressao2')
        elif (self.entrada == 'OperadorMatematico'):
            self.SKIP(154, 'OperadorMatematico')
        elif (self.entrada == 'OperadorMatematicoNivel2'):
            self.SKIP(156, 'OperadorMatematicoNivel2')
        elif (self.entrada == 'OP_SUB'):
            self.SKIP(160, 'OP_SUB')
        elif (self.entrada == 'OP_SUM'):
            self.SKIP(161, 'OP_SUM')
        elif (self.entrada == 'OP_SUB'):
            self.SKIP(160, 'OP_SUB')
        elif (self.entrada == 'OP_MULT'):
            self.SKIP(159, 'OP_MULT')
        elif (self.entrada == 'OP_DIV'):
            self.SKIP(157, 'OP_DIV')
        else:
            self.SKIP(158, 'Ɛ')
    def estado_153(self):
        """
        + Expressao2: Valor ListaExpressao2• : ListaExpressao1
        """
        self.REDUCE(2, 'Expressao2')

    def estado_154(self):
        """
        + ListaExpressao2: OperadorMatematico •Expressao2 : ListaExpresssao1
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if (self.entrada == 'Expressao2'):
            self.SKIP(155, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')
    def estado_155(self):
        """
        + ListaExpressao2: OperadorMatematico Expressao2• : ListaExpresssao1
        """
        self.REDUCE(2, 'ListaExpressao2')
    def estado_156(self):
        """
        + OperadorMatematico: OperadorMatematicoNivel2• : Expressao2
        """
        self.REDUCE(1, 'OperadorMatematico')
    def estado_157(self):
        """
        + OperadorMatematicoNivel2: "/"• : Expressao2
        """
        self.REDUCE(1, 'OperadorMatematicoNivel2')
    def estado_158(self):
        """
        + ListaExpressao2: Ɛ• : ListaExpressao1
        """
        self.REDUCE(1, 'ListaExpressao2')
    def estado_159(self):
        """
        + OperadorMatematicoNivel2: "*"• : Expressao2
        """
        self.REDUCE(1, 'OperadorMatematiconivel2')
    def estado_160(self):
        """
        + OperadorMatematico: "-"• : Expressao2
        """
        self.REDUCE(1, 'OperadorMatematico')
    def estado_161(self):
        """
        + OperadorMatematico: "+"• : Expressao2
        """
        self.REDUCE(1, 'OperadorMatematico')

    def estado_162(self):
        """
        + Valor: Negacao •Expressao : ListaExpressao2
        + Expressao: •Expressao1 ListaExpressao : ListaExpressao2
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(1621,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(124,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')

    def estado_1621(self):
        """
        + Valor: Negacao Expressao• : ListaExpressao2
        """
        self.REDUCE(2, 'Valor')
    def estado_163(self):
        """
        + Valor: "verdadeiro"• : ListaExpressao2
        """
        self.REDUCE(1, 'Valor')
    def estado_164(self):
        """
        + Valor: "falso"• : ListaExpressao2
        """
        self.REDUCE(1, 'Valor')
    def estado_165(self):
        """
        + Valor: literal• : ListaExpressao2
        """
        self.REDUCE(1, 'Valor')
    def estado_166(self):
        """
        + Negacao: Ɛ• : Expressao
        """
        self.REDUCE(1, 'Negacao')
    def estado_1661(self):
        """
        + Negacao: "nao"• : Expressao
        """
        self.REDUCE(1, 'Negacao')
    def estado_167(self):
        """
        + Valor: numerico• : ListaExpressao2
        """
        self.REDUCE(1, 'Valor')
    def estado_168(self):
        """
        + Valor: "(" •Expressao ")" : ListaExpressao2
        + Expressao: •Expressao1 ListaExpressao : ")"
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if(self.entrada == 'Expressao'):
            self.SKIP(169,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(140,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')

    def estado_169(self):
        """
        + Valor: "(" Expressao •")" : ListaExpressao2
        """
        if (self.entrada == 'OP_FP'):
            self.SKIP(170, 'OP_FP')

    def estado_170(self):
        """
        + Valor: "(" Expressao ")"• : ListaExpressao2
        """
        self.REDUCE(3, 'Valor')
    def estado_171(self):
        """
        + Valor: ID •Parametros : ListaExpressao2
        + Parametros: •"(" ListaParametros ")" : ListaExpressao2
        + Parametros: •Ɛ : ListaExpressao2
        """
        if (self.entrada == 'Parametros'):
            self.SKIP(1711, 'Parametros')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(173, 'OP_AP')
        else:
            self.SKIP(172, 'Ɛ')
    def estado_1711(self):
        """
        + Valor: ID Parametros• : ListaExpressao2
        """
        self.REDUCE(2, 'Valor')
    def estado_172(self):
        """
        + Parametros: Ɛ• : ListaExpressao2
        """
        self.REDUCE(1, 'Parametros')
    def estado_173(self):
        """
        + Parametros: "(" •ListaParametros ")" : ListaExpressao2
        + ListaParametros: •Expressao AddParametros : ")"
        + Expressao: •Expressao1 ListaExpressao : AddParamatros
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if (self.entrada == 'ListaParametros'):
            self.SKIP(174, 'ListaParametros')
        elif(self.entrada == 'Expressao'):
            self.SKIP(176,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(187,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')

    def estado_174(self):
        """
        + Parametros: "(" ListaParametros •")" : ListaExpressao2
        """
        if (self.entrada == 'OP_FP'):
            self.SKIP(175, 'OP_FP')

    def estado_175(self):
        """
        + Parametros: "(" ListaParametros ")"• : ListaExpressao2
        """
        self.REDUCE(3, 'Parametros')
    def estado_176(self):
        """
        + ListaParametros: Expressao •AddParametros : ListaExpressao2
        + AddParametros: •"," ListaParametros : ListaExpressao2
        + AddParametros: •Ɛ : ListaExpressao2
        """
        if (self.entrada == 'AddParametros'):
            self.SKIP(177, 'AddParametros')
        elif (self.entrada == 'OP_VIR'):
            self.SKIP(179, 'OP_VIR')
        else:
            self.SKIP(178, 'Ɛ')
    def estado_177(self):
        """
        + ListaParametros: Expressao AddParametros• : ListaExpressao2
        """
        self.REDUCE(2, 'ListaParametros')
    def estado_178(self):
        """
        + AddParametros: Ɛ• : ListaExpressao2
        """
        self.REDUCE(1, 'AddParametros')
    def estado_179(self):
        """
        + AddParametros: "," •ListaParametros : ListaExpressao2
        + ListaParametros: •Expressao AddParametros : ListaExpressao2
        + Expressao: •Expressao1 ListaExpressao : AddParamatros
        + Expressao1: •Expressao2 ListaExpressao1 : ListaExpressao
        + Expressao2: •Valor ListaExpressao2 : ListaExpressao1
        + Valor: •"verdadeiro" : ListaExpressao2
        + Valor: •"falso" : ListaExpressao2
        + Valor: •literal : ListaExpressao2
        + Valor: •"(" Expressao ")" : ListaExpressao2
        + Valor: •numerico : ListaExpressao2
        + Valor: •ID Parametros : ListaExpressao2
        + Valor: •Negacao Expressao : ListaExpressao2
        + Negacao: •"nao" : ListaExpressao2
        + Negacao: •Ɛ : ListaExpressao2
        """
        if (self.entrada == 'ListaParametros'):
            self.SKIP(180, 'ListaParametros')
        elif(self.entrada == 'Expressao'):
            self.SKIP(176,'Expressao')
        elif(self.entrada == 'Expressao1'):
            self.SKIP(187,'Expressao1')
        elif (self.entrada == 'Expressao2'):
            self.SKIP(145, 'Expressao2')
        elif (self.entrada == 'Valor'):
            self.SKIP(152, 'Valor')
        elif (self.entrada == 'KW_RES_true'):
            self.SKIP(163, 'KW_RES_true')
        elif (self.entrada == 'KW_RES_false'):
            self.SKIP(164, 'KW_RES_false')
        elif (self.entrada == 'STRING'):
            self.SKIP(165, 'STRING')
        elif (self.entrada == 'INT' or self.entrada == 'FLOAT'):
            self.SKIP(167, 'KW_RES_number')
        elif (self.entrada == 'Negacao'):
            self.SKIP(162, 'Negacao')
        elif (self.entrada == 'KW_RES_neg'):
            self.SKIP(1661, 'KW_RES_neg')
        elif (self.entrada == 'OP_AP'):
            self.SKIP(168, 'OP_AP')
        elif (self.entrada == 'KW_RES_ID'):
            self.SKIP(171, 'KW_RES_ID')
        else:
            self.SKIP(166, 'Ɛ')

    def estado_180(self):
        """
        + AddParametros: "," ListaParametros• : ListaExpressao2
        """
        self.REDUCE(2, 'AddParametros')
    def estado_181(self):
        """
        + OperadorRelacional: "<"• : Expressao
        """
        self.REDUCE(1, 'OperadorRelacional')
    def estado_182(self):
        """
        + OperadorRelacional: "<="• : Expressao
        """
        self.REDUCE(1, 'OperadorRelacional')
    def estado_183(self):
        """
        + OperadorRelacional: ">"• : Expressao
        """
        self.REDUCE(1, 'OperadorRelacional')
    def estado_184(self):
        """
        + OperadorRelacional: ">="• : Expressao
        """
        self.REDUCE(1, 'OperadorRelacional')
    def estado_185(self):
        """
        + OperadorRelacional: "<>"• : Expressao
        """
        self.REDUCE(1, 'OperadorRelacional')
    def estado_186(self):
        """
        + OperadorRelacional: "="• : Expressao
        """
        self.REDUCE(1, 'OperadorRelacional')
    def estado_192(self):
        """
        + Programa: "algoritmo" DeclaraVar ListaCmd "fim" "algoritmo" ListaRotina• : EOF
        """
        self.REDUCE(6, 'Programa')
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
