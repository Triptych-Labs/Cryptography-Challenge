# Intention:
Generate encrypted metadata from input message.

# How to use:

`python3 main.py <message>`

## Outputs
```
{
  "cipherSuite": {
    "AES": 4,
    "ChaCha20": 3,
    "Salsa20": 2
  },
  "messageCipher": [
    66,
    206,
    94,
    68,
    244,
    196,
    65,
    178,
    70,
    45,
    107,
    93,
    31,
    29,
    112,
    144,
    37,
    67,
    78,
    240,
    22,
    116,
    139,
    91,
    249,
    240,
    91,
    80,
    189,
    184,
    250,
    253,
    220,
    252,
    191,
    87,
    59,
    66,
    230,
    40,
    101,
    77
  ],
  "message": "b'andrew gower likes geepees'",
  "messageHash": "c1dba28da599d7b699dbdca2347ac0c320caf9b28ed6d73d2662a69e77ea2e30"
}
```

