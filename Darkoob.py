"""
Welcome to Darkoob Framework by AFRA IOT.
Darkoob is a Python backend framework.
This framework is designed to simplify web development and provide
developers with powerful tools for building robust web applications.
Feel free to explore the code and contribute to its development!
If you have any questions, contact us at afraiot.org.
Happy coding! 🚀
"""


from http.server import SimpleHTTPRequestHandler,HTTPServer
from jinja2 import Environment, FileSystemLoader
import  json
template_dir = "templates"
template_env = Environment(loader=FileSystemLoader(template_dir))

class MyRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render_template(self, template_name, **context):
        template = template_env.get_template(template_name)
        rendered_template = template.render(**context)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(rendered_template.encode())

    def do_GET(self):
        http_method = self.command
        if self.headers.get('Content-Length'):
            content_length = int(self.headers.get('Content-Length'))
            data = json.loads(self.rfile.read(content_length).decode('utf-8'))
        else:
            data={}
        # Find the handler for the requested path
        handler = routes.get((self.path, http_method), None)
        if handler:
            handler(self,data,http_method)
        else:
            # Handle 404 error
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('404 - Page not found.'.encode())

    def do_POST(self):
        http_method = self.command
        if self.headers.get('Content-Length'):
            content_length = int(self.headers.get('Content-Length'))
            data = json.loads(self.rfile.read(content_length).decode('utf-8'))
        else:
            data = {}
        # Now, post_data contains the body of the POST request

        # Find the handler for the requested path and method
        handler = routes.get((self.path, http_method), None)
        if handler:
            handler(self,data,http_method)
        else:
            # Handle 404 error
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('405 - Method Not Allowed'.encode())
    def do_PUT(self):
        http_method = self.command
        if self.headers.get('Content-Length'):
            content_length = int(self.headers.get('Content-Length'))
            data = json.loads(self.rfile.read(content_length).decode('utf-8'))
        else:
            data = {}
        # Now, post_data contains the body of the POST request

        # Find the handler for the requested path and method
        handler = routes.get((self.path, http_method), None)
        if handler:
            handler(self,data,http_method)
        else:
            # Handle 404 error
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('405 - Method Not Allowed'.encode())

    def do_DELETE(self):
        http_method = self.command
        if self.headers.get('Content-Length'):
            content_length = int(self.headers.get('Content-Length'))
            data = json.loads(self.rfile.read(content_length).decode('utf-8'))
        else:
            data = {}
        # Now, post_data contains the body of the POST request

        # Find the handler for the requested path and method
        handler = routes.get((self.path, http_method), None)
        if handler:
            handler(self,data,http_method)
        else:
            # Handle 404 error
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('405 - Method Not Allowed'.encode())

# Routes dictionary
routes = {}

# Function to add routes
def add_route(path, handler, methods=['GET']):
    for method in methods:
        routes[(path, method)] = handler

def send_response(request_handler, status_code, response_data):
    response = json.dumps(response_data)
    request_handler.send_response(status_code)
    request_handler.send_header('Content-type', 'application/json')
    request_handler.end_headers()
    request_handler.wfile.write(response.encode('utf-8'))

# Function to start the server
def run_server(host='localhost', port=8000):
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"Server started on {server_address[0]}:{server_address[1]}")
    httpd.serve_forever()