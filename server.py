"""
 Implements a simple HTTP/1.0 Server

"""

from os import path
import socket

from utils import Req
from handlers import endpoints, not_found, return_static_file, not_found

debug = False

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 9090


if __name__ == "__main__":
    
    
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # deepcode ignore BindToAllNetworkInterfaces: < listen to all interfaces >
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    
    server_socket.listen(1)
    
    print('Development server is listening on port %s ...' % SERVER_PORT)
    
    while True:    
        # Wait for client connections
        client_connection, client_address = server_socket.accept()
    
        # Get the client request
        request: Req = Req(client_connection.recv(1024).decode())
        
        if not request.valid:
            request.log_invalid()
            continue
            
        
        request.log()
        
        requested_path = path.normpath(request.path)
        
        response = None
        
        if requested_path in endpoints:
            response = endpoints[requested_path]()
        
        elif requested_path.startswith("/statics/") or requested_path.startswith("/images/"):
            response = return_static_file(requested_path)
            
        else:
            response = not_found()

    
        # Send HTTP response
        client_connection.sendall(response if isinstance(response, bytes) else response.encode())
        client_connection.close()
    
    # Close socket
    server_socket.close()