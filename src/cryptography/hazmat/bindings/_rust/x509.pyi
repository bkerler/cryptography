# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

import typing

from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives._asymmetric import AsymmetricPadding
from cryptography.hazmat.primitives.asymmetric.types import PrivateKeyTypes

def load_pem_x509_certificate(data: bytes) -> x509.Certificate: ...
def load_pem_x509_certificates(
    data: bytes,
) -> typing.List[x509.Certificate]: ...
def load_der_x509_certificate(data: bytes) -> x509.Certificate: ...
def load_pem_x509_crl(data: bytes) -> x509.CertificateRevocationList: ...
def load_der_x509_crl(data: bytes) -> x509.CertificateRevocationList: ...
def load_pem_x509_csr(data: bytes) -> x509.CertificateSigningRequest: ...
def load_der_x509_csr(data: bytes) -> x509.CertificateSigningRequest: ...
def encode_name_bytes(name: x509.Name) -> bytes: ...
def encode_extension_value(extension: x509.ExtensionType) -> bytes: ...
def create_x509_certificate(
    builder: x509.CertificateBuilder,
    private_key: PrivateKeyTypes,
    padding: AsymmetricPadding,
    hash_algorithm: typing.Optional[hashes.HashAlgorithm],
) -> x509.Certificate: ...
def create_x509_csr(
    builder: x509.CertificateSigningRequestBuilder,
    private_key: PrivateKeyTypes,
    padding: AsymmetricPadding,
    hash_algorithm: typing.Optional[hashes.HashAlgorithm],
) -> x509.CertificateSigningRequest: ...
def create_x509_crl(
    builder: x509.CertificateRevocationListBuilder,
    private_key: PrivateKeyTypes,
    padding: AsymmetricPadding,
    hash_algorithm: typing.Optional[hashes.HashAlgorithm],
) -> x509.CertificateRevocationList: ...

class Sct: ...
class Certificate: ...
class RevokedCertificate: ...
class CertificateRevocationList: ...
class CertificateSigningRequest: ...
