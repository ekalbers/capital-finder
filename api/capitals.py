from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

# https://restcountries.com/v3.1/name/{name}


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        country = dic.get('country')
        capital = dic.get('capital')

        if country:
            url = f'https://restcountries.com/v3.1/name/{country}'
            r = requests.get(url)
            data = r.json()
            country = data[0]['name']['common']
            capital = data[0]['capital'][0]
            message = f'The capital of {country} is {capital}.'

        if capital:
            url = f'https://restcountries.com/v3.1/capital/{capital}'
            r = requests.get(url)
            data = r.json()
            country = data[0]['name']['common']
            capital = data[0]['capital'][0]
            message = f'{capital} is the capital of {country}.'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return


