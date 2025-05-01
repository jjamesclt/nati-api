import os
from app import app

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
