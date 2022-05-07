# ENCS3320 Computer Networks First Project

a simple HTTP 1.0 web server built with python 3

![Sample Run 14](https://i.ibb.co/cwjJKJG/ENCS3320-webp-14-comppressed.webp)

# Setup

* install python **>= 3.9** and git
* clone this repository, and move to it

    ```bash
    git clone https://github.com/ibraheemalayan/ENCS3320-Network-Project.git    
    cd ENCS3320-Network-Project    
    ```
* run the server    

    ```bash    
    python3 server.py    
    ```

* use a browser ( or any http client ) to visit the following endpoints 

    | endpoint     | code | path | link                      |
    |--------------|------|------|---------------------------|
    | index        | 200  | /    | http://localhost:9090/    |
    | arabic index | 200  | /ar  | http://localhost:9090/ar  |
    | Google       | 307  | /go  | http://localhost:9090/go  |
    | CNN          | 307  | /cnn | http://localhost:9090/cnn |
    | Birzeit      | 307  | /bzu | http://localhost:9090/bzu |

    > there are other endpoints like **/statics/** for static files (fonts, images, stylesheets ...)    
    > and for non existing paths, **404**, try http://localhost:9090/nothing_is_here


# Author

Ibraheem Alyan, visit [my resume](https://www.ibraheemalyan.dev/)