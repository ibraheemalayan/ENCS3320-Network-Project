
from http_codes import HTTPStatus
from utils import generate_response, send_binary_file, send_text_file
from os  import path


def not_found():
    
    return generate_response(code=HTTPStatus.NOT_FOUND, body_and_length=send_text_file(path.join("templates" ,"not_found.html")))
    

def redirect_to_google():
    
    headers = {
        "Location": "https://www.google.com/"
    }
    
    return generate_response(code=HTTPStatus.TEMPORARY_REDIRECT, added_headers=headers)


def redirect_to_cnn():
    
    headers = {
        "Location": "https://edition.cnn.com/"
    }
    
    return generate_response(code=HTTPStatus.TEMPORARY_REDIRECT, added_headers=headers)

def redirect_to_birzeit():
    
    headers = {
        "Location": "https://www.birzeit.edu/ar"
    }
    
    return generate_response(code=HTTPStatus.TEMPORARY_REDIRECT, added_headers=headers)


def index_en():
    
    return generate_response(code=HTTPStatus.OK, body_and_length=send_text_file(path.join("templates" ,"index_en.html")))

def index_ar():
    
    return generate_response(code=HTTPStatus.OK, body_and_length=send_text_file(path.join("templates" ,"index_ar.html")))

def return_static_file(file_path: str):
    
    # Secure File Path To Prevent Directory Traversal
    
    file_path = path.normpath(file_path)
    
    if not file_path.startswith("/statics/") and not file_path.startswith("/images/"):
        
        return not_found()
    
    file_path = path.basename(file_path)
    
    # determine content type
    
    content_type = None
    
    binary=False
    
    if file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
        content_type = "image/jpeg"
        binary=True
        
    elif file_path.endswith(".svg"):
        content_type = "image/svg+xml"
        
    elif file_path.endswith(".png"):
        content_type = "image/png"
        binary=True
        
    elif file_path.endswith(".js"):
        content_type = "text/javascript"
        
    elif file_path.endswith(".css"):
        content_type = "text/css"
        
    elif file_path.endswith(".woff2"):
        content_type = "font/woff2"
        binary=True
        
    else:
        return not_found() # unsupported content type
    
    file_body = None
    size = None
    
    try:
        if binary:
            file_body, size = send_binary_file(path.join("statics", file_path))
        else:
            file_body, size = send_text_file(path.join("statics", file_path))
    except FileNotFoundError:
        return not_found()

    return generate_response(code=HTTPStatus.OK, content_type=content_type,  body_and_length=(file_body, size))

endpoints = {
    "/": index_en,
    "/en": index_en,
    "/ar": index_ar,
    "/go": redirect_to_google,
    "/cn": redirect_to_cnn,
    "/bzu": redirect_to_birzeit
}
