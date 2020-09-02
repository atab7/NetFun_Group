from socket import *
import time
import os
import sys

default_headers = {
    'Server' : 'MyServer',
    'Content-Type': 'text/html',
    'Connection' : 'close',
    }      

def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


serverPort   = 6789 #If possible, get this dynamically as well
ipAddress    = get_ip()

try:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #For testing, delete this line during deployment
    serverSocket.bind((ipAddress, serverPort)) #Prepare a sever socket #This is MQU IP idk why i'm here
    serverSocket.listen(5)
except Exception as err:
    print(err)
    sys.exit()

#Establish the connection
print('Ready to serve...')

connectionSocket, addr =  serverSocket.accept()
try:
    message = connectionSocket.recv(1024).decode()          

    filename = message.split()[1]
    file_path = os.path.join(sys.path[0], filename[1:])
    file_content = ''
    with open(file_path, 'r') as f:
        file_content = f.read()        
                                
    outputdata = [
        f'Date: {time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())}\n',
        f'Server: {default_headers["Server"]}\n',
        f'Content-Length: {len(file_content.encode("utf-8"))}\n', 
        f'Content-Type: {default_headers["Content-Type"]}\n\n',
        file_content, 
        '\n'
    ]               
    #Send one HTTP header line into socket
    connectionSocket.send('HTTP/1.1 200 OK\n'.encode('utf-8'))
    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):           
        connectionSocket.send(outputdata[i].encode('utf-8'))
    connectionSocket.send("\r\n".encode('utf-8'))
    connectionSocket.close()
        
except IOError:
    #Send response message for file not found
    not_found = [
        'HTTP/1.1 404 Not Found\n',
        'Content-Type: text/html\n\n',
        '<html><head></head><body><h1>404 Page Not Found!</h1></body></html>\n',
        '\r\n'
    ]
    [connectionSocket.send(item.encode('utf-8')) for item in not_found]
    #Close client socket
    connectionSocket.close()       

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data                                    
