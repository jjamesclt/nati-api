#!/bin/bash

CERT_DIR="/certs"
KEY_FILE="$CERT_DIR/server.key"
CERT_FILE="$CERT_DIR/server.crt"

if [ ! -f "$KEY_FILE" ] || [ ! -f "$CERT_FILE" ]; then
  echo "Generating self-signed TLS certificate..."
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout "$KEY_FILE" \
    -out "$CERT_FILE" \
    -subj "/CN=localhost"
else
  echo "TLS cert already exists at $CERT_FILE"
fi
