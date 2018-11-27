# CLASSE DE TAGS HASH

class TAGs:

    def __init__(self):

        self.simbolos = ['programa', 'algoritmo', 'fim', 'subrotina', 'declare', 'logico', 'numerico', 'literal', 'se', 'enquanto',
                     'senao', 'leia', 'repita', 'ate', 'verdadeira', 'falso', 'ou', 'e', 'nao']

        self.tags = {
                     ##----------------------##
                     'programa': 'KW_RES_program',
                     'algoritmo': 'KW_RES_algorithm',
                     'fim': 'KW_RES_end',
                     'subrotina': 'KW_RES_met',
                     'declare': 'KW_RES_var',
                     'logico': 'KW_RES_logic',
                     'numerico': 'KW_RES_number',
                     'literal': 'KW_RES_string',
                     'se': 'KW_RES_id',
                     'enquanto': 'KW_RES_for',
                     'senao': 'KW_RES_else',
                     'leia': 'KW_RES_read',
                     'repita': 'KW_RES_do',
                     'ate': 'KW_RES_dwhile',
                     'verdadeira': 'KW_RES_true',
                     'falso': 'KW_RES_false',
                     'ou': 'KW_RES_or',
                     'e': 'KW_RES_and',
                     'nao': 'KW_RES_Neg'}
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
                     '<=': 'OP_EQME',
                     '<--': 'OP_AT',
                     '<>': 'OP_DIF',
                     '(': 'OP_AP',
                     ')': 'OP_FP',
                     ',': 'OP_VIR',
                     ';': 'OP_PV'
"""