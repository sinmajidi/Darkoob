"""
Welcome to Darkoob Framework by AFRA IOT.
Darkoob is a Python backend framework.
This framework is designed to simplify web development and provide
developers with powerful tools for building robust web applications.
Feel free to explore the code and contribute to its development!
If you have any questions, contact us at afraiot.org.
Happy coding! 🚀
"""
from http.cookies import SimpleCookie

from http.server import SimpleHTTPRequestHandler,HTTPServer

from jinja2 import Environment, FileSystemLoader
import  json
from datetime import datetime, timedelta
template_dir = "templates"
template_env = Environment(loader=FileSystemLoader(template_dir))

# Routes dictionary
routes = {}
allowed_methods={}

class MyRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def redirect(self, location, status_code=302):
        self.send_response(status_code)
        self.send_header('Location', location)
        self.end_headers()

    def method_not_allowed(self):
        send_response(self,405,{"message":"method not allowed"})

    def not_found(self):
        send_response(self,404,{"message":" not found"})

    def render_template(self, template_name, **context):
        template = template_env.get_template(template_name)
        rendered_template = template.render(**context)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(rendered_template.encode())

    def do_GET(self):
        http_method = self.command
        if self.path not in allowed_methods:
            self.not_found()
            return
        if self.path in allowed_methods and http_method in allowed_methods[self.path]:
            # The DELETE method is allowed for this path
            if self.headers.get('Content-Length'):
                content_length = int(self.headers.get('Content-Length'))
                data = json.loads(self.rfile.read(content_length).decode('utf-8'))
            else:
                data = {}
            # Find the handler for the requested path and method
            handler = routes.get((self.path, http_method), None)
            if handler:
                handler(self, data, http_method)
            else:
                # Handle 404 error
                self.not_found()
        else:
            # Handle 405 error (Method Not Allowed)
            self.method_not_allowed()

    def do_POST(self):
        http_method = self.command
        if self.path not in allowed_methods:
            self.not_found()
            return
        if self.path in allowed_methods and http_method in allowed_methods[self.path]:
            # The DELETE method is allowed for this path
            if self.headers.get('Content-Length'):
                content_length = int(self.headers.get('Content-Length'))
                data = json.loads(self.rfile.read(content_length).decode('utf-8'))
            else:
                data = {}
            # Find the handler for the requested path and method
            handler = routes.get((self.path, http_method), None)
            if handler:
                handler(self, data, http_method)
            else:
                # Handle 404 error
                self.not_found()
        else:
            # Handle 405 error (Method Not Allowed)
            self.method_not_allowed()
    def do_PUT(self):
        http_method = self.command
        if self.path not in allowed_methods:
            self.not_found()
            return
        if self.path in allowed_methods and http_method in allowed_methods[self.path]:
            # The DELETE method is allowed for this path
            if self.headers.get('Content-Length'):
                content_length = int(self.headers.get('Content-Length'))
                data = json.loads(self.rfile.read(content_length).decode('utf-8'))
            else:
                data = {}
            # Find the handler for the requested path and method
            handler = routes.get((self.path, http_method), None)
            if handler:
                handler(self, data, http_method)
            else:
                # Handle 404 error
                self.not_found()
        else:
            # Handle 405 error (Method Not Allowed)
            self.method_not_allowed()

    def do_DELETE(self):
        http_method = self.command
        if self.path not in allowed_methods:
            self.not_found()
            return
        if self.path in allowed_methods and http_method in allowed_methods[self.path]:
            # The DELETE method is allowed for this path
            if self.headers.get('Content-Length'):
                content_length = int(self.headers.get('Content-Length'))
                data = json.loads(self.rfile.read(content_length).decode('utf-8'))
            else:
                data = {}
            # Find the handler for the requested path and method
            handler = routes.get((self.path, http_method), None)
            if handler:
                handler(self, data, http_method)
            else:
                # Handle 404 error
                self.not_found()
        else:
            # Handle 405 error (Method Not Allowed)
            self.method_not_allowed()




# Function to add routes
def add_route(path, handler, methods=['GET']):
    if not isinstance(methods, list):
        methods = [methods]
    for method in methods:
        routes[(path, method)] = handler
        # Store the allowed methods for the route
        if path in allowed_methods:
            allowed_methods[path].append(method)
        else:
            allowed_methods[path] = [method]

def send_response(request_handler, status_code, response_data, headers=None):
    response = json.dumps(response_data)
    request_handler.send_response(status_code)
    request_handler.send_header('Content-type', 'application/json')
    if headers:
        for header, value in headers.items():
            request_handler.send_header(header, value)
    request_handler.end_headers()
    request_handler.wfile.write(response.encode('utf-8'))

# Function to start the server
def run_server(host='localhost', port=8000):
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"Server started on {server_address[0]}:{server_address[1]}")
    httpd.serve_forever()


#cookies function
def cookie_set(request_handler, key, value,age=None):
    headers = {}
    cookie = SimpleCookie(request_handler.headers.get('Cookie'))
    cookie[key] = value
    if age is not None:
        expiration_time = datetime.utcnow() + timedelta(seconds=age)
        cookie[key]['expires'] = expiration_time.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
    cookie[key]['path'] =request_handler.path
    headers['Set-Cookie'] = cookie[key].OutputString()
    return headers

def cookie_get(request_handler, key):
    user_name_cookie = request_handler.headers.get('Cookie')
    if user_name_cookie:
        cookie = SimpleCookie(user_name_cookie)
        if key in cookie:
            return cookie[key].value
    return None

def cookie_delete(request_handler, key):
    headers={}
    user_name_cookie = request_handler.headers.get('Cookie')
    if user_name_cookie:
        cookie = SimpleCookie(user_name_cookie)
        if key in cookie:
            expiration_time = datetime.utcnow()
            cookie[key]['expires'] = expiration_time.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
            headers['Set-Cookie'] = cookie[key].OutputString()
            return headers
    return None



#query_parameter
