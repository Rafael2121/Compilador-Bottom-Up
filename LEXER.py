# Programa destinado a ser o LEXER do portugolo

from Compiladores import tag,token,Tokens,TabSimb

# INTERFACE PRINCIPAL


class LEXER:


	def __init__(self):
		self.n_linha = 0
		self.m_coluna = 0
		self.tabelaSimbolos = null		
		self.ultimoChar = 0
		self.ref_arquivo = abre_arquivo()
		self.lista_Tokens = Tokens()


	def abre_arquivo(self):
		# Armazena o arquivo PortuGolo
		if ref_arquivo == null:
			ref_arquivo = open("arquivoTeste.txt", 'r')
		return arquivo
		# return


	def lexermain(self):
		#classe que percorre o arquivo
		ref_arquivo = open("arquivoTeste.txt", 'r')

		for linha in ref_arquivo:
			#Acréscimo de linha a cada leitura
			n_linha += 1
			reconheceToken(linha)

		pass

	def reconheceToken(self, linha):
		# metodo que irá ler o texto do arquivo, por token
		estado = 1
		m_coluna = 1

		lexema = ""
		caractere = null

		for letra in linha:

			#na leitura do proximo char, é incrementado a coluna
			caractere = letra.lower()
			m_coluna += 1

			if estado == 1:
				if caractere == ";":
					lista_Tokens.add(Token(null, ";", n_linha, m_coluna))
					# return 
					pass
				elif caractere == "(":
					lista_Tokens.add(Token(null, "(", n_linha, m_coluna))
					# return 
					pass
				elif caractere == ")":
					lista_Tokens.add(Token(null, ")", n_linha, m_coluna))
					# return 
					pass
				elif caractere == ",":
					lista_Tokens.add(Token(null, ",", n_linha, m_coluna))
					# return 
					pass
				elif caractere == "<":
					lexema += (str)caractere
					estado = 5
					# muda de estado
					pass
				elif caractere == ">":
					lexema += (str)caractere
					estado = 11
					# muda de estado
					pass
				elif caractere == "+":
					lista_Tokens.add(Token(null, "+", n_linha, m_coluna))
					pass
				elif caractere == "-":
					lista_Tokens.add(Token(null, "-", n_linha, m_coluna))
					pass
				elif caractere == "*":
					lista_Tokens.add(Token(null, "*", n_linha, m_coluna))
					# return
					pass
				elif caractere == "/":
					lexema += (str)caractere
					estado = 23
					#muda de estado
					pass
				elif caractere.isalpha():
					lexema += caractere
					estado = 18
					#muda de estado
				elif caractere.isdigit():
					lexema += caractere
					estado = 14
					#muda de estado
				elif caractere == '"':
					lexema += caractere
					estado = 28
					#muda de estado

			# Estado "<"
			elif estado == 5:
				if caractere == "=":
					lista_Tokens.add(Token(null, "<=", n_linha, m_coluna))
					#return
					pass
				elif caractere == "-":
					estado = 7
					#muda de estado
					pass
				elif caractere == ">":
					lista_Tokens.add(Token(null, "<>", n_linha, m_coluna))
					#return
				else:
					# Volta 1 caractere
					lista_Tokens.add(Token(null, "<", n_linha, m_coluna))
					#return
					pass

			# Estado ">"
			elif estado == 7:
				if caractere == "-":
					lista_Tokens.add(Token(null, "<--", n_linha, m_coluna))
					pass
				else:
					#retorna um erro
					pass

			elif estado == 11:
				if caractere == "=":
					lista_Tokens.add(Token(null, ">=", n_linha, m_coluna))
					#return
					pass
				else:
					# Volta 1 caractere
					lista_Tokens.add(Token(null, ">", n_linha, m_coluna))
					#return
					pass

			# Estado /
			elif estado == 23:
				if caractere == "*":
					estado = 26
					# Muda de estado
					pass
				elif caractere == "/":
					estado = 25
					# Muda de estado
					pass
				else:
					# Volta 1 caractere
					lista_Tokens.add(Token(null, "/", n_linha, m_coluna))
					# return
					pass

			elif estado == 26:
				if caractere == "*":
					estado = 27
					#muda de estado

			elif estado == 25:
				if caractere == "/n":
					estado = 1

			elif estado == 27:
				if caractere == "*":
					pass
				elif caractere == "/":
					estado = 1
				else:
					estado = 26

			# Estado de letra
			elif estado == 18:
				if caractere.isalpha() or caractere.isdigit():
					# enquanto encontrar 
					lexema += caractere

				else:					
					# caractere é uma palavra
					# Será feita uma consulta na tabela se esta palavra é reservada
					# volta 1 caractera
					lista_Tokens.add(Token(null,lexema,n_linha,m_coluna))
					lexema = ""

			# Estado de numero
			elif estado == 14:
				if caractere.isdigit():
					lexema += caractere
				elif caractere == ".":
					# muda  de estado
					estado = 16
					lexema += caractere					
				else:
					# volta 1 estado
					lista_Tokens.add(Token(null,lexema,n_linha,m_coluna))
					lexema = ""

			elif estado == 16:
				if caractere.isdigit():
					lexema += caractere
				else:
					# volta 1 caractere
					lista_Tokens.add(Token(null,lexema,n_linha,m_coluna))
					lexema = ""

			# Estado de "
			elif estado == 28:
				if caractere == '"':
					lista_Tokens.add(Token(null,lexema,n_linha,m_coluna))
					lexema = ""
				else:
					lexema += caractere

			else:

		# Fim do While
			














