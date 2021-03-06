# Sockets
# São interfaces programaveis de comunicação entre softwares
# que podem estar rodando em computadores distintos
# na rede . Permite a transferencia de strigs em bytes
# de um processo para o outro.
# A comunicação é feita através do endereço 
#de ip e o port number ( n de identificação da conversa)

"""
Lado do Servidor: Abre um TCP/IP numa port, espera por uma menssagem
de um cliente, e manda essa mensagem de volta como resposta. Esse 
é uma simples ouve/responde conversação por cliente, mas percorre um loop
infinito para ouvir por mais clientes enquanto o script do servidor
estiver rodando. O cliente pode rodar em outra máquina ou no mesmo
computador se usar o 'localhost' como servidor
"""

from socket import *
import time

# Cria o nome do host
meuHost = ''

# Utiliza este número de porto
minhaPort = 50007

# Cria um objeto socket. As duas constantes referem-se a:
# Familia do endereço (padrão é socket.AF_INET)
# Se é stream (socket.SOCK_STREAM, o padrão) ou datagram (socket.SOCK_DGRAM)
# E o protocolo (padrão é 0)
# Da maneira como configuramos:
# AF_INIT == Protocolo de endereço de IP
# SOCK_STREAM == Protocolo de transferência TCP
# Combinação = Server TCP/IP
sockobj = socket(AF_INET, SOCK_STREAM)

# Vincula o servidor ao número de porto
sockobj.bind((meuHost, minhaPort))

# O socket começa a esperar por clientes limitando a 
# 5 conexões por vez
sockobj.listen(5)


while True:
    # Aceita uma conexão quando encontrada e devolve a
    # um novo socket conexão e o endereço do cliente
    # conectado
    conexão, endereço = sockobj.accept()
    print('Server conectado por', endereço)
    
    while True:
        # Recebe data enviada pelo cliente
        data = conexão.recv(1024)
        # time.sleep(3)
        
        # Se não receber nada paramos o loop
        if not data: break

        # O servidor manda de volta uma resposta
        conexão.send(b'Eco=&gt;' + data)
    
    # Fecha a conexão criada depois de responder o
    # cliente
    conexão.close()