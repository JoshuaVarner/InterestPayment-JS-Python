from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Set the response code to 200 (OK)
        self.send_response(200)
        # Set the content type to text/html
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Open the index.html file and read its contents
        with open('index.html', 'r') as f:
            html = f.read()
        # Write the contents of the file to the response as bytes
        self.wfile.write(bytes(html, "utf-8"))

# Create the web server
server = HTTPServer(('', 8000), RequestHandler)
# Start the web server
server.serve_forever()

