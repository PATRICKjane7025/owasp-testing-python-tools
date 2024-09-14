import ssl
import socket

# Target server (replace with actual .in site)
target_server = 'https://sales.life9.io'  # Ensure this domain is correct and reachable
port = 443

# Set up SSL context for TLS 1.2
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# Connect to the target server over HTTPS
try:
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=target_server)
    conn.connect((target_server, port))
except socket.gaierror as e:
    print(f"Failed to connect to {target_server}: {e}")
    exit()

# Send crafted HTTP GET request over HTTPS
http_request = f"GET / HTTP/1.1\r\nHost: {target_server}\r\n\r\n".encode()
conn.send(http_request)

# Receive and analyze the response from the server
response = conn.recv(4096)
print(response.decode())

# Close the connection
conn.close()
