from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TCP and IP Address Table</title>
</head>
<body>

  <h2>TCP and IP Address Example</h2>

  <table border="1" cellpadding="8" cellspacing="0">
    <tr>
      <th>Host</th>
      <th>IP Address</th>
      <th>TCP Port</th>
      <th>Service</th>
    </tr>
    <tr>
      <td>Client PC</td>
      <td>10.0.0.15</td>
      <td>49152</td>
      <td>HTTP Request</td>
    </tr>
    <tr>
      <td>Web Server</td>
      <td>10.0.0.50</td>
      <td>80</td>
      <td>HTTP Response</td>
    </tr>
    <tr>
      <td>Database Server</td>
      <td>10.0.0.100</td>
      <td>3306</td>
      <td>MySQL</td>
    </tr>
    <tr>
      <td>Email Server</td>
      <td>10.0.0.200</td>
      <td>25</td>
      <td>SMTP</td>
    </tr>
  </table>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()