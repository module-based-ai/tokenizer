# mbaitok

A small and fast tokenizer that converts text into a list of numeric tokens.

## Installation

```
pip install mbaitok
```

## Usage

```python
from mbaitok import tokenize

tokens = tokenize("Hello!")
print(tokens)  # [34, 5, 12, 12, 15, 63]
```

Each character is mapped to its index in the tokenizer's alphabet. The same character will always produce the same number, so tokens can be decoded back to text.

## Supported characters

Supports letters (a–z, A–Z), digits (0–9), common punctuation, and a range of currency/special symbols (£, €, ¥, ₿, etc.).

## License

MIT
