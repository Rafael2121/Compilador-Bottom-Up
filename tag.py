# CLASSE DE TAGS HASH

class TAGs:

    def __init__(self):

        self.simbolos = ['programa', 'algoritmo', 'fim', 'subrotina', 'declare', 'logico', 'numerico', 'literal', 'se', 'enquanto',
                     'senao', 'leia', 'repita', 'ate', 'verdadeira', 'falso', 'ou', 'e', 'nao']

        self.tags = {
                     ##----------------------##
                     'programa': 'KW_RES_program',
                     'algoritmo': 'KW_RES_algorithm',
                     'inicio': 'KW_RES_begin',
                     'fim': 'KW_RES_end',
                     'subrotina': 'KW_RES_met',
                     'retorne': 'KW_RES_return',
                     'declare': 'KW_RES_var',
                     'logico': 'KW_RES_logic',
                     'numerico': 'KW_RES_number',
                     'literal': 'KW_RES_string',
                     'nulo': 'KW_RES_null',
                     'se': 'KW_RES_if',
                     'enquanto': 'KW_RES_while',
                     'faca':'KW_RES_DoIt',
                     'senao': 'KW_RES_else',
                     'leia': 'KW_RES_read',
                     'escreva': 'KW_RES_write',
                     'repita': 'KW_RES_do',
                     'para': 'KW_RES_for',
                     'ate': 'KW_RES_dwhile',
                     'verdadeira': 'KW_RES_true',
                     'falso': 'KW_RES_false',
                     'ou': 'KW_RES_or',
                     'e': 'KW_RES_and',
                     'nao': 'KW_RES_neg'}
                     #--------
"""
                     '+': 'OP_SUM',
                     '-': 'OP_SUB',
                     '*': 'OP_MULT',
                     '/': 'OP_DIV',
                     '=': 'OP_EQ',
                     '>': 'OP_MA',
                     '>=': 'OP_MAEQ',
                     '<': 'OP_ME',
                     '<=': 'OP_MEEQ',
                     '<--': 'OP_AT',
                     '<>': 'OP_DIF',
                     '(': 'OP_AP',
                     ')': 'OP_FP',
                     ',': 'OP_VIR',
                     ';': 'OP_PV'
"""