import SimpleHTTPServer
import SocketServer

port = 8000
handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("",port), handler)

print "Server started at port 8000"

httpd.serve_forever()

