# Programa destinado a análise dos objetos recuperados pelo LEXER

# aqui o filho chora e a mae nao ve
# v1 -> top down

class PARSER:

    def __init__(self):
        pass

    def parsermain(self, listaTokens):
        """
        Módulo que compara os tokens reconhecidos pelo PARSER com a gramatica portugolo
        No final desta classe está em comentário TODA a gramática, que será retirada nas versões que aceitarão qualquer uma
        O objetivo final é um parser bottom up com um módulo que entenda um padrão de escrita de gramática, que se estiver minimamente
        boa, poderá ser reconhecida e aplicada
        """




        pass

    def parser_analisys(self):

        pass

    """
    Compilador → Programa EOF
    Programa → algoritmo DeclaraVar ListaCmd fim algoritmo ListaRotina
    DeclaraVar → declare ListaID Tipo ; | ε
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
    CmdSe → se ( Expressao ) faca inicio ListaCmd fim
    ComandoPara → para CmdAtrib ate Expressao faca inicio ListaCmd fim
    ComandoRepita → repita ListaCmd ate Expressao
    CmdAtrib → ID <-- Expressao ;
    CmdChamaRotina → ID X ;
    CmdEscreva → escreva ( Expressao );
    CmdLeia → leia ( ID );
    Expressao → ExpressaoMatematica | literal
    ExpressaoMatematica → ExpressaNumerica | ExpressaoLogica | ( ExpressaoMatematica )
    ExpressaoLogica → ExpressaoLogicaN2 ListaExpressaoLogica
    ListaExpressaoLogica → OperadorLogico ExpressaoLogica | ε
    ExpressaoLogicaN2 → Negacao Logico ExpressaoLogicaN3
    ExpressaoLogicaN3 → operadorRelacional ExpressaoLogicaN2 | ε
    Negacao → nao Negacao | ε
    OperadorLogico → e | ou
    OperadorRelacional → <> | =
    Logico → verdadeiro | falso | ID X | ( ExpressaoLogica )
    ExpressaoNumerica → Equacao AddComparador
    AddComparador → OperadorRelacionalNumerico Equacao | ε
    Equacao → Numerico EquacaoN2
    EquacaoN2 → OperadorMatematico Equacao | ε
    OperadorRelaciomalNumerico → < | <= | > | >= | <> | =
    OperadorMatematico → * | / | OperadorMatematicoN2
    OperadorMatematico → + | -    
    Numerico → numero | ID X | ( Equacao )
    X → ( Parametros ) | ε
    Parametros → Valor AddParametros
    AddParametros → , Parametros | ε
    Valor → Logico | Numerico| literal
    """
