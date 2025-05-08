import servers, sys

port = int(sys.argv[1])
s = servers.Servers # Chamar a classe 'Servers' dentro de servers.

arg = sys.argv[2] # Parâmetros

if arg == "-t": # Parâmetro para iniciar servidor TCP.
	s.serverTCP(port) # Chamar a função da classe.

elif arg == "-u": # Parâmetro para iniciar servidor UDP.
	s.serverUDP(port) # Chamar a função da classe.

elif arg == "-ct": # Parâmetro para ser conectar a um servidor TCP.
	ip = input("IP: ")
	s.clientTCP(port, ip) # Chamar a função da classe.

elif arg == "-uc": # Parâmetro para ser conectar a um servidor UDP.
	ip = input("IP: ")
	s.clientUDP(ip, port) # Chamar a função da classe.

