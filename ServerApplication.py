import http.server
import socketserver
import os

print("Noah's Local Server Program\n")
print("Enter directory of folder your html file is located in:\n")
location = input()

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler


directory = location
os.chdir(directory)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("/n")
    print("Address: http://localhost:", PORT, "/name-of-file.html")
    httpd.serve_forever()
