from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import json

# https://restcountries.com/v3.1/name/{name}

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # s = self.path
        # url_components = parse.urlsplit(s)
        # query_string_list = parse.parse_qsl(url_components.query)
        # dic = dict(query_string_list)
        # name = dic.get('name')

        url = 'https://restcountries.com/v3.1/name/america'
        r = requests.get(url)
        data = r.json()

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(data['name']['common'].encode())


