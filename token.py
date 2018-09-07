# Objeto token

class Token:

	def __init__(self, tag, lexema, linha, coluna):
		self.tag = tag
		self.lexema = lexema
		self.linha = linha
		self.coluna = coluna

	def __str__(self):
		desc = "<" + tag + ",'" + lexema + "'> linha:" + linha + " coluna:" + coluna
		return desc



