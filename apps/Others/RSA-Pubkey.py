#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import ssl
import OpenSSL

def main(doamin):
    cert = ssl.get_server_certificate((doamin, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

    pub = '{:X}'.format(x509.get_pubkey().to_cryptography_key().public_numbers().n)

    format = {

        "Public Key": '{}'.format(':'.join(pub[i:i + 2] for i in range(0, len(pub), 2))),
        "Public Key Bits": '{}'.format(x509.get_pubkey().bits()),

    }
    print(json.dumps(format))
    return json.dumps(format)

if __name__ == '__main__':
    main('google.com')