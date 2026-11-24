# Aperçu local du site : py serve.py, puis http://localhost:8001
# Sert /faq depuis faq.html, comme GitHub Pages (le simple « py -m http.server » ne le fait pas).
import functools
import http.server
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8001


class Handler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        bare = self.path.split("?")[0].split("#")[0]
        local = self.translate_path(bare)
        if not os.path.exists(local) and os.path.exists(local + ".html"):
            self.path = bare + ".html"
        elif not os.path.exists(local):
            self.path = "/404.html"
        return super().send_head()


if __name__ == "__main__":
    server = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Handler, directory=str(ROOT)))
    print(f"Aperçu : http://localhost:{PORT}  (Ctrl+C pour arrêter)")
    server.serve_forever()
