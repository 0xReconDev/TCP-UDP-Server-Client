# 🛰️ TCP/UDP Server & Client em Python

Este projeto contém um conjunto de scripts em Python que permitem iniciar servidores e clientes TCP ou UDP, com logs automáticos de conexões e sessões iniciadas. Ideal para estudo de redes, protocolos e comunicação via socket.

## 📁 Estrutura do Projeto

- `tcp.py` — Script principal para iniciar servidores ou clientes com base em argumentos.
- `servers.py` — Classe `Servers` com métodos para cada tipo de conexão (TCP/UDP, servidor/cliente).
- `scriptlog.py` — Módulo auxiliar para registro de logs em arquivos `.log`.

## 🚀 Funcionalidades

- 🌐 Servidor TCP com autenticação por senha
- 📡 Servidor UDP com troca contínua de mensagens
- 🤝 Cliente TCP interativo
- 🛰️ Cliente UDP com suporte a múltiplas mensagens
- 📝 Logs automáticos:
  - `servidor.log`: servidores iniciados
  - `conexoes.log`: conexões de clientes

## 🧪 Como Usar

### 🔧 Execução

```bash
python3 tcp.py <PORTA> <ARGUMENTO>
```
### 🖥️ Modo Servidor

"-t" → Inicia servidor TCP

"-u" → Inicia servidor UDP

```bash
python3 tcp.py 8080 -t
```

### 💻 Modo Cliente

"-ct" → Cliente TCP

"-uc" → Cliente UDP

```bash
python3 tcp.py 8080 -ct
```
| Será solicitado o IP do servidor.

## 📄 Logs

° Todas as conexões e execuções são salvas automaticamente:

    ° servidor.log → quando o servidor é iniciado.
    
    ° conexoes.log → quando um cliente se conecta.


## 🧠 Conceitos Envolvidos

° Sockets TCP e UDP.

° Bind e listen (TCP).

° Comunicação bidirecional.

° Validação de senha simples.

° Registro de logs.

° Programação orientada a objetos.


## 📌 Observações

° A senha esperada pelo servidor TCP é "teste" (padrão atual).

° O IP padrão de escuta é "0.0.0.0" — ou seja, aceita conexões em todas as interfaces.

° O código é didático e pode ser facilmente expandido com threads ou autenticação real.

## ✅ Requisitos
° Python 3.x

## 🛠️ Autor
° Projeto criado por **0xReconDev** como prática de conceitos de redes e segurança ofensiva.
