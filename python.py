import simpleHTTPServer
import SocketServer

PORT = 8000

Handler = simpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("",PORT),Handler)
print 'sirviendo en el puerto {0}'.format(PORT)
httpd.serrve_forever