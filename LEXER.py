# Programa destinado a ser o LEXER do portugolo

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
					# muda de estado
					pass
				elif caractere == ">":
					lexema += (str)caractere
					# muda de estado
					pass
				elif caractere == "+":
					lexema += (str)caractere
					# muda de estado
					pass
				elif caractere == "-":
					lexema += (str)caractere
					# muda de estado
					pass
				elif caractere == "*":
					lista_Tokens.add(Token(null, "*", n_linha, m_coluna))
					# return
					pass
				elif caractere == "/":
					lexema += (str)caractere
					#muda de estado
					pass
				elif caractere.isalpha():
					lexema += caractere
					#muda de estado
				elif caractere.isdigit():
					lexema += caractere
					#muda de estado
				elif caractere == '"':
					lexema += caractere
					#muda de estado
			# Estado "<"
			elif estado = :
				if caractere == "=":
					lista_Tokens.add(Token(null, "<=", n_linha, m_coluna))
					#return
					pass
				elif caractere == "-":

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
			elif estado = :
				if caractere == "=":
					lista_Tokens.add(Token(null, ">=", n_linha, m_coluna))
					#return
					pass
				else:
					# Volta 1 caractere
					lista_Tokens.add(Token(null, ">", n_linha, m_coluna))
					#return
					pass
			# Estado +
			elif estado = :
				# Letra ou Digito
				if caractere:
					#return
					pass
				# Outro
				else:
					#return
					pass
			# Estado -
			elif estado = :
				# Letra ou Digito
				if caractere:
					#return
					pass
				# Outro
				else:
					#return
					pass
			# Estado /
			elif estado = :
				if caractere == "*":
					# Muda de estado
					pass
				elif caractere == "/":
					# Muda de estado
					pass
				else:
					# Volta 1 caractere

					lista_Tokens.add(Token(null, "/", n_linha, m_coluna))
					# return
					pass
			pass
			# Estado de letra
			elif estado = :
				if caractere.isalpha() or caractere.isdigit():
					# enquanto encontrar 
					lexema += caractere
				else:					
					# caractere é uma palavra
					# Será feita uma consulta na tabela se esta palavra é reservada
					lista_Tokens.add(Token(null,lexema,n_linha,m_coluna))
					lexema = ""					
			# Estado de numero
			elif estado = :
				if caractere.isdigit():
					lexema += caractere
					
				elif caractere == "."::
					# muda  de estado
					lexema += caractere					
				else:
					lista_Tokens.add(Token(null,lexema,n_linha,m_coluna))
					lexema = ""

			elif estado = :
				if caractere.isdigit():
					lexema += caractere
				else:
					lista_Tokens.add(Token(null,lexema,n_linha,m_coluna))
					lexema = ""

			# Estado de "
			elif estado = :
				if caractere == '"':
					lista_Tokens.add(Token(null,lexema,n_linha,m_coluna))
					lexema = ""
				else:
					lexema += caractere
			




			# Estado de comentário //
			elif estado = :				
				if caractere == "\n" or caractere == "\r":
					# Pula de linha
					estado = 1				
			elif estado = :
				# estado de comentário
				if caractere == "*":

					# Muda de estado
					pass
			
			elif estado = :
				if caractere == "*":

					pass
				elif caractere == "/"
					# Fim do comentário
					estado = 1
					pass
				else:
					#Volta de estado

					pass

			else:

		# Fim do While
			














