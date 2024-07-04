from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from os import listdir
from os.path import isfile
from threading import Thread
from config import mpd_music_dir as base_path


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            path = json.loads(self.rfile.read(content_length).decode())
            if type(path) != str:
                raise Exception('path is not a string')
            if '..' in path.split('/'):
                raise Exception('Fuck you and your path traversals')
            abs_path = f'{base_path}/{path}'

            allfiles = sorted(listdir(abs_path))
            dirs, files = [], []

            for f in allfiles:
                relpath = f'{path}/{f}'.removeprefix('/')
                if isfile(f'{base_path}/{relpath}'):
                    files.append (relpath)
                else:
                    dirs.append(relpath)
            resp = {'dirs': dirs, 'files': files}
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode())


        except Exception as e:
            self.send_response(500, f'Error: {e}')
            self.end_headers()

def run():
    httpd = HTTPServer(('0.0.0.0', 80), Handler)
    try:
        httpd.serve_forever()
    except Exception as e:
        print('Server crashed:', e)
        exit(1)

def start_server():
    Thread(target=run, daemon=True).start()