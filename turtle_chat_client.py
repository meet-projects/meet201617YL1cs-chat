# turtle_chat_client.py

import sys
import socket
import select

class Client:
    '''
    Class to manage client-side socket input/output (i.e. communication) for
    chat tool.
    '''
    _BUFFER_SIZE=4096 #Size of buffers for socket input/output
    _TIME_OUT=0.2 #Time to wait, in seconds, before timing out server
    _END_MSG='<\chat>' #Special message indicating end of session.
    _DEFAULT_PORT=9009 #Default port number
    _DEFAULT_HOST='localhost' #Default host (for communicating between sessions on one machine)

    def __init__(self,username='Me',partner_name='Partner',hostname=None,port=None):
        '''
        Initialize a new client object.

        :param username: string, name of chat participant.  Default value='Me'
        :param partner_name: string, name of partner that you are chatting with.
                            Default='Partner'
        :param hostname: string, as name suggests;
                        default value='localhost' (for single-computer connection)
        :param port: integer, port number over which connection is made to server
                    (Hint: use four-digit integers for a test run of your code). 
                    Default value=9009
        '''
        if hostname is None:
            self.hostname=Client._DEFAULT_HOST
        else :
            self.hostname=hostname

        if port is None:
            self.port=Client._DEFAULT_PORT
        else :
            self.port=port
        
        self.username=username
        self.partner_name=partner_name
        #Create a new socket
        self.server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.settimeout(Client._TIME_OUT) #Wait _TIME_OUT seconds before deciding server has timed out

        #Try to connect to host
        try :
            self.server.connect((self.hostname,self.port))
            print('Connected to '+self.hostname+' at port, '+str(self.port) +'. You can start sending messages.')
        except Exception as err:
            print('Unable to connect to '+self.hostname+' at port '+str(self.port))
            raise(err) #Give error to user for debugging purposes
            #sys.exit() #When debugging is done, you can do this, instead of raising error.

    def send(self, msg):
        '''
        Send string through socket.  Encode to bytes-like object.

        :param msg: string to encode and send through socket belonging to this client.
        '''
        self.server.send(msg.encode())

    def receive(self):
        '''
        Call to check whether the chat partner has sent a message.

        :return: String received from partner, or None when chat session has terminated.
        '''
        ready_to_read,ready_to_write,in_error = select.select([self.server] , [], [],Client._TIME_OUT)
        
        if len(ready_to_read) != 0 :
            # incoming message from remote server
            # Wait to receive a message up to BUFFER_SIZE in size,
            #but at least one byte, or until remote end is closed.
            #If remote end is closed, return empty string.
            data = self.server.recv(Client._BUFFER_SIZE)
            if len(data)==0 : #If empty string, remote end has closed.
                print('\nDisconnected from chat server - session ending.')
                return Client._END_MSG
            else :
                #Input comes in as bytes - decode.
                return data.decode()
        else :
            return None

    def get_server(self):
        '''
        :return: socket connection to server of this client instance
        '''
        return self.server

if __name__ == "__main__":
    my_client=Client()
    server_socket=my_client.get_server()
    while True :
        ready_to_read,ready_to_write,in_error=select.select([sys.stdin, server_socket],[],[])
        for my_socket in ready_to_read :
            if my_socket == server_socket :
                new_msg=my_client.receive()
                if new_msg == Client._END_MSG :
                    sys.exit()
                elif not (new_msg is None) :
                    print(new_msg)
            else : #Get input to send
                msg=input()
                my_client.send(msg)