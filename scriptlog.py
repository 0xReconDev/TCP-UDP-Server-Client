class logs:
	# Salvar todas as vezes que o servidor for iniciado.
	def logs_servidor(server_init):
		log_server = open("servidor.log", "a")
		log_server.write(server_init + "\n")
		log_server.close()
		print (server_init)

	# Salvar todas as vezes que o cliente se conectar.
	def logs_clientes(cliente_conect):
		log_cliente = open("conexoes.log", "a")
		log_cliente.write(cliente_conect + "\n")
		log_cliente.close()
		print (cliente_conect)
