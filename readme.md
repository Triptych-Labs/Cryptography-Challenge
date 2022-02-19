# Intention:
Generate encrypted text from input message with psuedorandom sequencing of encryption.

# How to use:

`python3 main.py <message>`

## Outputs
```
{
  "cipherOrder": "Salsa20 -> AES -> AES -> Salsa20 -> ChaCha20 -> Salsa20 -> AES -> ChaCha20 -> Salsa20",
  "cipherSuite": {
    "Salsa20": 4,
    "AES": 3,
    "ChaCha20": 2
  },
  "messageCipher": [
    22,
    94,
    179,
    98,
    205,
    225,
    23,
    159,
    151,
    238,
    192,
    192,
    99,
    44,
    60,
    147,
    65,
    171,
    141,
    157,
    254,
    43,
    102,
    213,
    57,
    129,
    77,
    151,
    121,
    244,
    52,
    77,
    176,
    42,
    206,
    16,
    44,
    174,
    137,
    221,
    250,
    75,
    140,
    109,
    45,
    109,
    234,
    39,
    211,
    208,
    198,
    3,
    184,
    51,
    109,
    214,
    16,
    190
  ],
  "message": "b'andrew gower likes geepees'",
  "messageHash": "f60ca7f20c495184320d3d66906bccc30c8693f1f1e65ca11eaa1ace3859d9fb"
}
```

