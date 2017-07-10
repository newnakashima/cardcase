from http.server import HTTPServer, BaseHTTPRequestHandler
from randomPass import PassGenerator
import re

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    prop = {}
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        filename = 'index.html'
        filecontent = self.readFile(filename)
        self.wfile.write(bytes(filecontent, "utf-8"))
        return 

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        gen = PassGenerator()
        self.prop["password"] = gen.genpass()

        filename = 'index.html'
        filecontent = self.readFile(filename)
        self.wfile.write(bytes(filecontent, "utf-8"))
        return

    def readFile(self, filename):
        filecontent = ''
        with open(filename, 'r') as f:
            for line in f:
                line = self.checkTemplate(line)
                filecontent += line
        return filecontent

    def checkTemplate(self, line):
        res = re.match(r'.*\{\{(.*)\}\}.*', line)
        if res is not None and res.lastindex > 0:
            repl = "" if res.group(1) not in self.prop else self.prop[res.group(1)]
            print("repl is " + repl)
            line = re.sub(r'\{\{(.*)\}\}', repl, line)
        return line

def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler):
    try:
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
        httpd.socket.close()

run()
