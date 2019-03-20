# Compiladores
Projeto do 6to semestre - compilador PORTUGOLO

Projeto de compilador Bottom up, a ser entregue no final do 6º Semestre como atividade prática final. O código foi feito em python, e engloa as funções de Lexer e Parser de um compilador.

v1.0
"""
A primeira versão do Compiler-Brain Portugolo, um trabalho do curso de Ciência da Computação da UniBH, mais especificamente da matéria compiladores.
O objetivo é que até o final do semestre tenha um compilador de Portugolo funcional em Python.

-----------------------------
"""

Portugolo:
|--_init_
|--compiler-brain
|--LEXER
|--ob_token
|--tag # Será aonde concentrará as tags do programa, inicialmente estão na classe Lexer
"""
Abaixo estão as classes relevantes para esta versão inicial do programa, que mais pra frente serão otimizadas
LEXER:
|--lexermain:
|	Obtem o arquivo; controla por linhas o arquivo txt que 
|	será enviado para extrator_token
|--extrator_tokens:
|	Recebe a linha e lê token por token buscando sempre seguir o
|	fluxo determinado no diagrama
X
"""
v2.0
"""
A versão final do compilador recebe adição de algumas classes

|--_init_
|--compiler-brain
|--LEXER # Análise lexica
|--ob_token # Classe objeto token
|--tag # Classe que concentrará as tags reservadas do programa
|--Stack # Classe pilha para controle de objetos para o parser do compilerBrain
|--PARSER # Análise Sintática

Na classe LEXER você encontra na linha 36 o comando que requisita o texto que será compilado.

"""
...
