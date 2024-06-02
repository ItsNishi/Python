#################################################################
###
###            This is my first IP Scanner
###              Thanks to TCM Security
### 
###
#################################################################
#################################################################
###
###                     Notes
###            this is not the best script
###              more of proof of concept
###
#################################################################


import sys
import socket
from datetime import datetime as dt #can import parts of a module and can use an alias


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
    print("invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")


print('#' * 55)
print('Scanning target: ' +target)
print('Time Started: ' +str(dt.now()))    
print('#' * 55)

try:
    for port in range(50,85):#port range
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#gathering IPv4 Address and port
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #getting the result of the target and the port and connect_ex is an error indicator if open 0 if 1 closed
        if result == 0:
            print(f"port {port} is open")
            s.close()
                    
except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to host.")
    sys.exit()