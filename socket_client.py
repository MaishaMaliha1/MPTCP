import socket

def Main():

    host='10.194.9.141' #client ip
    port = 6000
    
    server = ('10.194.9.124', 5000)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    
    message = input("-> ")
    while message !='q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received FRom server: " + data)
        message = input("-> ")
    s.close()

if _name=='main_':
    Main()
