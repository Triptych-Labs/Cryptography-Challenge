import typing
from Crypto.Cipher import ChaCha20, AES, Salsa20
from Crypto.Hash import SHA256
import numpy
import sys
import json
import collections

key = "triptychlabs.io                 "  # 32 bytes key


def decrypt_salsa20(suite: typing.List):
    cipher = Salsa20.new(key=key.encode("utf-8"), nonce=suite[1][:8])
    codex = cipher.decrypt(suite[1][8:])

    return codex


def encrypt_salsa20(message: bytes) -> typing.List:
    cipher = Salsa20.new(key.encode("utf-8"))
    nonce = cipher.nonce  # type: ignore
    codex = nonce + cipher.encrypt(message)  # type: ignore

    return [decrypt_salsa20, [nonce], codex, "Salsa20"]


def decrypt_aes(suite: typing.List):
    cipher = AES.new(key.encode("utf-8"), AES.MODE_EAX, nonce=suite[0][0])
    codex = cipher.decrypt(suite[1])

    return codex


def encrypt_aes(message: bytes) -> typing.List:
    cipher = AES.new(key.encode("utf-8"), AES.MODE_EAX)
    nonce = cipher.nonce  # type: ignore
    codex, tag = cipher.encrypt_and_digest(message)  # type: ignore

    return [decrypt_aes, [nonce, tag], codex, "AES"]


def decrypt_chacha20(suite: typing.List):
    message_hash = ChaCha20.new(key=key.encode("utf-8"), nonce=suite[0][0])
    codex = message_hash.decrypt(suite[1])

    return codex


def encrypt_chacha20(message: bytes) -> typing.List:
    message_hash = ChaCha20.new(key=key.encode("utf-8"))
    codex = message_hash.encrypt(message)

    return [decrypt_chacha20, [message_hash.nonce], codex, "ChaCha20"]


def hash_message(message: bytes):
    return SHA256.new(message).hexdigest()


def encode(message: str, encodings: typing.List):
    message_cipher = message.encode("utf-8")

    history = []

    for encoding in encodings:
        suite = encoding(message_cipher)
        history.append([*suite[:]])
        message_cipher = suite[2]

    history.reverse()
    ciphers = []
    message_deciphered = bytes()
    for encoding in history:
        message_deciphered = encoding[0](encoding[1:])
        ciphers.append(encoding[len(encoding) - 1])

    cipher_suite = collections.Counter(ciphers)

    obj = {
        "cipherOrder": " -> ".join(ciphers),
        "cipherSuite": dict(cipher_suite),
        "messageCipher": list(bytearray(message_cipher)),
        "message": str(message_deciphered),
        "messageHash": str(hash_message(message_cipher)),
    }

    obj_json = json.dumps(obj, indent=2)
    print(obj_json)


if __name__ == "__main__":
    encrypt_ops = [
        encrypt_aes,
        encrypt_chacha20,
        encrypt_salsa20,
    ]
    entropy = 3
    encrypt_ops_indices = numpy.random.randint(len(encrypt_ops), size=entropy * entropy)
    encrypt_ops = [encrypt_ops[i] for i in encrypt_ops_indices]

    messages: typing.List[typing.List] = [
        [
            sys.argv[1],
            encrypt_ops,
        ]
    ]

    for message in messages:
        encode(message[0], message[1])

