import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8000))

terminado = False
print('Digite Fim para terminar o chat')

while not terminado:
    cliente.send(input('Mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'Fim':
        terminado = True
    else:
        print(msg)

cliente.close()