# Intention:
Generate encrypted text from input message with psuedorandom sequencing of encryption.

# How to use:

`python3 main.py <message>`

## Outputs
```
{
  "cipherOrder": "Salsa20 -> AES -> ChaCha20 -> AES -> Salsa20 -> ChaCha20 -> Salsa20 -> AES -> ChaCha20",
  "cipherSuite": {
    "Salsa20": 3,
    "AES": 3,
    "ChaCha20": 3
  },
  "messageCipher": [
    62,
    153,
    66,
    122,
    131,
    190,
    183,
    195,
    10,
    169,
    110,
    92,
    188,
    79,
    167,
    37,
    123,
    242,
    75,
    108,
    83,
    226,
    80,
    158,
    234,
    247,
    254,
    88,
    194,
    212,
    210,
    217,
    54,
    22,
    15,
    233,
    113,
    65,
    40,
    225,
    34,
    227,
    186,
    150,
    127,
    255,
    41,
    215,
    6,
    150
  ],
  "message": "andrew gower likes geepees",
  "messageHash": "380d180f847f1afcef9fed001576cac97535b35266dcbef6a2d943f76cbd68e5"
}
```

