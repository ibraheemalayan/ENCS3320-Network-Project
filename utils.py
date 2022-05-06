from typing import BinaryIO, Dict, List, Tuple
from datetime import datetime

from os import path
import cfg
        
from http_codes import HTTPStatus
    
    
class Req():
    ''' class to represent request '''
    
    def __init__(self, request_text:str, client_address) -> None:
        
        lines: List[str] = request_text.split('\n')
        
        splitted_line_1 = lines[0].split()
        
        if len(splitted_line_1) < 2:
            self.valid = False
            return
        
        self.method = splitted_line_1[0]
        self.path = splitted_line_1[1]
        
        self.client_address = client_address
        
        self.headers: Dict[str, str] = {}
        
        self.text = request_text
        
        for line in lines[1:]:
            if len(line.strip()) != 0:
                self.headers[line.split(":")[0]] = line.split(":")[1].strip()
                
        self.valid = True
        
    def log_invalid(self):
        
        print(f"{datetime.now()}    Invalid Request\t", end="")
            
    def log(self):
        ''' log request to standard output '''
        
        from server import debug
        
        if debug:
            
            print("\n\n---------------------------------\n")
            print(self.text)
            print("\n---------------------------------")
        
        else:
            
            print(f"{datetime.now()} [{cfg.request.client_address[0]}:{cfg.request.client_address[1]}]    {self.method}    {self.path:<45}\t", end="")


        
def generate_response(content_type="text/html", code=HTTPStatus.OK, body_and_length=None, added_headers={}) -> bytes:
    
    headers: Dict[str, str] = {
        "Content-Type": content_type,
        "Date": datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    }
    
    body = None
    
    if body_and_length is not None and body_and_length[0] is not None:
        if body_and_length[1] is None:
            headers["Content-Length"] = len(body_and_length[0])
        else:
            headers["Content-Length"] = body_and_length[1]
            
        if isinstance(body_and_length[0], str):
            body = body_and_length[0].encode()
        else:
            body = body_and_length[0]
    
    headers.update(added_headers)
    
    status = [str(c) for c in code.value]
    
    response_text = f"HTTP/1.0 {' '.join(status)}\n"
    
    for key in headers.keys():
        response_text += f"{key}: {headers[key]}\n"
        
    from server import debug
    print(code.value[0])
    
    full_response = bytes((response_text + "\n").encode())
    
    if body is not None:
        full_response += bytes(body)
    
    full_response += bytes("\n\n".encode())
    
    if debug:
        
        print(response_text)
    
    return full_response


def send_text_file(filename: str):
    
    file_size = path.getsize(filename)
    
    fptr = open(filename, "r")
    
    data = fptr.read()
    
    fptr.close()
    
    return data, file_size

def send_binary_file(filename: str):
    
    file_size = path.getsize(filename)
    
    fptr = open(filename, "rb")
    
    data = fptr.read()
    
    fptr.close()
    
    return data, file_size