#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('10.126.190.205', serverPort)) #Prepare a sever socket #This is MQU IP idk why i'm here
#Fill in start
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =   #Fill in start              #Fill in end          
    try:
        message = "generic message"  #Fill in start          #Fill in end               
        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = #Fill in start       #Fill in end                   
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end                
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            	connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start        
        #Fill in end
        #Close client socket
        #Fill in start
        #Fill in end            
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data                                    
