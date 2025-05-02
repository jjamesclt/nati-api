from flask import Flask
from app.routes import register_blueprints

app = Flask(__name__)
register_blueprints(app)

@app.route("/")
def index():
    return {"message": "Welcome to the NATI API"}, 200


if __name__ == "__main__":
    '''
    TEST
    cert_path = "/certs/server.crt"
    key_path = "/certs/server.key"

    os.system("/app/generate-csr.sh")

    context = (cert_path, key_path)
    app.run(host="0.0.0.0", port=5000, ssl_context=context)
    '''
    #DEV
    app.run(host="0.0.0.0", port=5000)
