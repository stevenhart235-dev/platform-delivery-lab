"""Tiny dependency-free sample service for the delivery lab."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def health_response():
    return {"status": "ok", "application": "sample-api"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        body = json.dumps(health_response()).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print("Listening on http://localhost:8080/health")
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
