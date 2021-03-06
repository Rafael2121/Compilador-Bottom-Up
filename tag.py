# CLASSE DE TAGS HASH

class TAGs:

    def __init__(self):
        self.simbolos = ['programa', 'algoritmo', 'fim', 'subrotina', 'declare', 'logico', 'numerico', 'literal',
                         'nulo', 'se', 'enquanto', 'inicio', 'faca', 'repita', 'para', 'escreva', 'senao', 'leia',
                         'repita', 'ate', 'verdadeira', 'falso', 'ou', 'e', 'nao']
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
            'faca': 'KW_RES_DoIt',
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
        # --------

        self.FRISTS = {
            'Compilador': ['KW_RES_algorithm'],
            'Programa': ['KW_RES_algorithm'],
            'DeclaraVar': ['KW_RES_var', 'Ɛ'],
            'ListaDeclaraVar' : ['KW_RES_logic', 'KW_RES_number', 'KW_RES_string', 'KW_RES_null', 'Ɛ'],
            'ListaID': ['KW_RES_ID'],
            'ListaAdd': ['OP_VIR', 'Ɛ'],
            'Tipo': ['KW_RES_logic', 'KW_RES_number', 'KW_RES_string', 'KW_RES_null'],
            'ListaRotina': ['KW_RES_met', 'Ɛ'],
            'Rotina': ['KW_RES_met'],
            'ListaParam': ['OP_VIR', 'Ɛ'],
            'Param': ['KW_RES_ID'],
            'Retorno': ['KW_RES_return', 'Ɛ'],
            'ListaCmd': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                         'KW_RES_write', 'KW_RES_read', 'Ɛ'],
            'Cmd': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                    'KW_RES_write', 'KW_RES_read'],
            'CmdSe': ['KW_RES_if'],
            'CmdSN': ['KW_RES_else', 'Ɛ'],
            'CmdEnquanto': ['KW_RES_while'],
            'CmdPara': ['KW_RES_for'],
            'CmdRepita': ['KW_RES_do'],
            'CmdAtrib': ['KW_RES_ID'],
            'CmdChamaRotina': ['KW_RES_ID'],
            'CmdEscreva': ['KW_RES_write'],
            'CmdLeia': ['KW_RES_read'],
            'Expressao': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP',
                          'KW_RES_ID', 'KW_RES_neg'],
            'ListaExpressao': ['OP_EQ', 'OP_MEEQ', 'OP_MAEQ', 'OP_MA', 'OP_ME', 'OP_DIF', 'Ɛ'],
            'OperadorRelacional': ['OP_EQ', 'OP_MEEQ', 'OP_MAEQ', 'OP_MA', 'OP_ME', 'OP_DIF'],
            'Expressao1': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP',
                           'KW_RES_ID', 'KW_RES_neg'],
            'ListaExpressao1': ['KW_RES_or', 'KW_RES_and', 'Ɛ'],
            'OperadorLogico': ['KW_RES_or', 'KW_RES_and'],
            'Expressao2': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP',
                           'KW_RES_ID', 'KW_RES_neg'],
            'ListaExpressao2': ['OP_SUM', 'OP_SUB', 'OP_MULT', 'OP_DIV', 'Ɛ'],
            'OperadorMatematico': ['OP_SUM', 'OP_SUB', 'OP_MULT', 'OP_DIV'],
            'OperadorMatematicoNivel2': ['OP_MULT', 'OP_DIV'],
            'Valor': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP', 'KW_RES_ID',
                      'KW_RES_neg'],
            'Negacao': ['KW_RES_neg', 'Ɛ'],
            'Parametros': ['OP_AP', 'Ɛ'],
            'ListaParametros': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP',
                                'KW_RES_ID', 'KW_RES_neg'],
            'AddParametros': ['OP_VIR']
        }
        self.FOLLOW = {
            'Compilador': ['KW_RES_EOF'],
            'Programa': ['KW_RES_EOF'],
            'DeclaraVar': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                           'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'ListaID': ['KW_RES_ID'],
            'ListaAdd': ['OP_FP   '],
            'Tipo': ['KW_RES_ID', 'OP_VIR', 'OP_FP'],
            'ListaRotina': ['KW_RES_EOF'],
            'Rotina': ['KW_RES_EOF', 'KW_RES_met'],
            'ListaParam': ['OP_FP'],
            'Param': ['OP_FP', 'OP_VIR'],
            'Retorno': ['KW_RES_end'],
            'ListaCmd': ['KW_RES_dwhile', 'KW_RES_return', 'KW_RES_end'],
            'Cmd': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                    'KW_RES_write', 'KW_RES_read'],
            'CmdSe': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                      'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'CmdSN': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                      'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'CmdEnquanto': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                            'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'CmdPara': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                        'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'CmdRepita': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                          'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'CmdAtrib': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                         'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'CmdChamaRotina': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                               'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'CmdEscreva': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                           'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'CmdLeia': ['KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                        'KW_RES_write', 'KW_RES_read', 'KW_RES_return'],
            'Expressao': ['KW_RES_end', 'OP_FP','KW_RES_DoIt', 'KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do',
                          'KW_RES_ID', 'KW_RES_write', 'KW_RES_read', 'KW_RES_return', 'OP_FP', 'OP_VIR'],
            'ListaExpressao': ['KW_RES_end', 'OP_FP', 'KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for',
                               'KW_RES_do','KW_RES_DoIt',
                               'KW_RES_ID', 'KW_RES_write', 'KW_RES_read', 'KW_RES_return', 'OP_FP', 'OP_VIR', 'OP_PV'],
            'OperadorRelacional': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP',
                                   'KW_RES_ID', 'KW_RES_neg'],
            'Expressao1': ['OP_EQ', 'OP_MEEQ', 'OP_MAEQ', 'OP_MA', 'OP_ME', 'OP_DIF', 'KW_RES_end', 'OP_FP',
                           'KW_RES_if', 'KW_RES_else', 'KW_RES_while','KW_RES_DoIt', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                           'KW_RES_write', 'KW_RES_read', 'KW_RES_return', 'OP_FP', 'OP_VIR'],
            'ListaExpressao1': ['OP_EQ', 'OP_MEEQ', 'OP_MAEQ', 'OP_MA', 'OP_ME', 'OP_DIF', 'KW_RES_end', 'OP_FP',
                                'KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                                'KW_RES_write', 'KW_RES_read','KW_RES_DoIt', 'KW_RES_return', 'OP_FP', 'OP_VIR', 'OP_PV'],
            'OperadorLogico': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP',
                               'KW_RES_ID', 'KW_RES_neg'],
            'Expressao2': ['KW_RES_or', 'KW_RES_and', 'OP_EQ', 'OP_MEEQ', 'OP_MAEQ', 'OP_MA', 'OP_ME', 'OP_DIF',
                           'KW_RES_end', 'OP_FP', 'KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do',
                           'KW_RES_ID', 'KW_RES_write', 'KW_RES_read','KW_RES_DoIt', 'KW_RES_return', 'OP_FP', 'OP_VIR', 'OP_PV'],
            'ListaExpressao2': ['KW_RES_or', 'KW_RES_and', 'OP_EQ', 'OP_MEEQ', 'OP_MAEQ', 'OP_MA', 'OP_ME', 'OP_DIF',
                                'KW_RES_end', 'OP_FP', 'KW_RES_if','KW_RES_DoIt', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for',
                                'KW_RES_do', 'KW_RES_ID', 'KW_RES_write', 'KW_RES_read', 'KW_RES_return', 'OP_FP', 'OP_VIR', 'OP_PV'],
            'OperadorMatematico': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP',
                                   'KW_RES_ID', 'KW_RES_neg'],
            'OperadorMatematicoNivel2': ['KW_RES_true', 'KW_RES_false','INT', 'FLOAT', 'STRING', 'OP_AP',
                                         'KW_RES_ID', 'KW_RES_neg'],
            'Valor': ['OP_SUM', 'OP_SUB', 'OP_MULT', 'OP_DIV', 'KW_RES_or', 'KW_RES_and',
                      'OP_EQ', 'OP_MEEQ', 'OP_MAEQ', 'OP_MA', 'OP_ME', 'OP_DIF', 'KW_RES_end', 'OP_FP',
                      'KW_RES_if', 'KW_RES_else', 'KW_RES_while','KW_RES_DoIt', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                      'KW_RES_write', 'KW_RES_read', 'KW_RES_return', 'OP_FP', 'OP_VIR', 'OP_PV'],
            'Negacao': ['KW_RES_true', 'KW_RES_false', 'INT', 'FLOAT', 'STRING', 'OP_AP',
                        'KW_RES_ID', 'KW_RES_neg'],
            'Parametros': ['OP_SUM', 'OP_SUB', 'OP_MULT', 'OP_DIV', 'KW_RES_or', 'KW_RES_and',
                           'OP_EQ', 'OP_MEEQ', 'OP_MAEQ', 'OP_MA', 'OP_ME', 'OP_DIF', 'KW_RES_end', 'OP_FP',
                           'KW_RES_if', 'KW_RES_else', 'KW_RES_while', 'KW_RES_for', 'KW_RES_do', 'KW_RES_ID',
                           'KW_RES_write', 'KW_RES_read', 'KW_RES_return', 'OP_FP', 'OP_VIR', 'OP_PV'],
            'ListaParametros': ['OP_FP'],
            'AddParametros': ['OP_FP']
        }


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
