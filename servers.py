
import socket, sys, scriptlog

call_logs_servidor = scriptlog.logs

class Servers:

	@staticmethod
	def serverTCP(port):

		# A interface de rede foi definida como "0.0.0.0", ou seja, qualquer interface ativa no momento.
		# Alterar para sua preferência.
		sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket TCP sobre IPv4.
		sock_tcp.bind(("0.0.0.0", port)) # IP e Porta de conexão.
		sock_tcp.listen(1) # Quantas conexões seram aceitas.
		call_logs_servidor.logs_servidor(f"Aguardando conexão 0.0.0.0 {port}.") # Armazenar as logs de quantos vezes o servidor foi aberto na variável 'servidor_iniciado'.

		con, client = sock_tcp.accept() # Segurar até que alguem se conect no servidor.
		call_logs_servidor.logs_clientes(f"Conexão recebida: {client}") # Armazenar as logs de conexão.

		con.send("Digite a senha: ".encode()) # Solicitar a senha todas as vezes que o usuário se conectar.
		senha = con.recv(1024) # Armazenar a senha digitada pelo usuário.
		senha_correta = "teste"

		if senha.decode() == senha_correta: # Comprar valores

			while True:

				# Área do servidor.
				msg = input("> ") # Entrada de dados do servidor.
				if msg == "sair": # Encerrar a conexão se o servidor digitar 'sair'.
					print ("Você encerro a conexão.")
					con.send("O servidor encerro a conexão.".encode())
					sock_tcp.close() # Encerrar o socket
					break
				con.send(f"\nServidor: {msg}".encode()) # Enviar os dados do servidor para o cliente.

				# Área do cliente.
				dado_cliente = con.recv(1024).decode() # Receber os dados do cliente.

				if not dado_cliente: # Essa função verifica se o cliente saiu da sessão, com base na falta de respostas.
					print ("O cliente saiu da sessão.")
					break
				print (f"\nCliente: {dado_cliente}")

		else:

			print ("O cliente errou a senha e foi desconectado da sessão.")
			con.send("Senha incorreta.".encode())
			sock_tcp.close() # 'Matar' socket

		sock_tcp.close() # 'Matar' socket

	@staticmethod
	def serverUDP(port):

		sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Criar um socket UDP sobre IPv4.
		sock_udp.bind(("0.0.0.0", port)) # Função 'bind', aguarda conexão no IP e porta passada.
		print (f"Aguardando Dados 0.0.0.0 {port}")

		while True:
			dados, cliente = sock_udp.recvfrom(1024)  # Essa função retorna dois valores, o primeiro valor é os dados que o cliente enviou e o segundo e as informações do cliente(IP e Porta, por exemplo).
							  						 # Função 'recvfrom', recebe os dados enviado pelo cliente.
			print (f"{cliente} - {dados.decode()}") # Imprimir os dados enviado pelo cliente.

			msg = input("> ")
			msg += "\n"
			sock_udp.sendto(msg.encode(), cliente) # Função 'sendto', envia os dados do servidor para o cliente.
		sock_udp.close() # 'Matar' Socket.

	@staticmethod
	def clientTCP(port, ip):

		# Criar socket para conexão do cliente
		sock_client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket TCP sobre IPv4.
		sock_client_tcp.connect((ip, port)) # Tupla para conectar no IP e Porta do servidor.

		# Receber a autênticação do servidor.
		dados_servidor = sock_client_tcp.recv(1024).decode() # Receber a caixa de senha do servidor.
		senha_servidor = input(dados_servidor) # Digitar a senha.
		sock_client_tcp.send(senha_servidor.encode()) # Enviar a senha.

		while True:

			# Receber as mensagens do servidor.
			msg_servidor = sock_client_tcp.recv(1024).decode() # Receber as mensagens do servidor.

			# Verificar se o servidor saiu da conexão.
			if not msg_servidor or msg_servidor == "sair":
				print ("Servidor encerro a conexão.")
				sock_client_tcp.close() # 'Matar' Socket.
				break
			print (f"{msg_servidor}")


			# Caixa de dados do cliente.
			msg_cliente = input("> ")
			sock_client_tcp.send(msg_cliente.encode())

		sock_client_tcp.close() # 'Matar' Socket.

	@staticmethod
	def clientUDP(ip, port):

		# Socket UDP cliente
		sock_client_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		servidor = (ip, port)

		while True:
			# Mensagens do cliente
			msg_client = input("> ")
			sock_client_udp.sendto(msg_client.encode(), servidor)

			# Receber Mensagens do servidor.
			msg_servidor, srv = sock_client_udp.recvfrom(1024)
			print (f"{srv} - {msg_servidor.decode()}")
