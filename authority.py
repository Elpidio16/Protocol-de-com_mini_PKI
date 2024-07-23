import hashlib

class Authority:
    def __init__(self):
        self.certificates = {}

    def sign_certificate(self, user_data):
        certificate = {
            'email': user_data['email'],
            'public_key': user_data['public_key']
        }
        certificate_signature = hashlib.sha256(str(certificate).encode('utf-8')).hexdigest()
        self.certificates[user_data['email']] = (certificate, certificate_signature)
        return certificate, certificate_signature

    def verify_certificate(self, email, certificate, signature):
        expected_signature = hashlib.sha256(str(certificate).encode('utf-8')).hexdigest()
        return expected_signature == signature

class CertificateRepository:
    def __init__(self):
        self.certificates = {}

    def add_certificate(self, email, certificate, signature):
        self.certificates[email] = (certificate, signature)

    def revoke_certificate(self, email):
        if email in self.certificates:
            del self.certificates[email]

    def get_certificate(self, email):
        return self.certificates.get(email, None)