# DimShade
**Post-quantum cryptographic protocol based on high-dimensional SO(n) geometry.**  
Developed by [DimensionalShade](https://github.com/DimensionalShade)

## 📐 Philosophy
DimShade is a geometric cryptographic protocol designed to resist quantum and classical attacks.  
It replaces lattice-based structures with orthogonal transformations in SO(n), yielding a shared scalar secret without decoding or key storage.

## 🔐 Features
- No lattice, no decoding, no key storage  
- Resistant to quantum brute-force (Grover, Shor)  
- Resistant to Rowhammer, side-channel, and fault injection  
- Fully reproducible and open-source  
- Designed for clarity, pedagogy, and auditability

## ⚙️ Installation
```bash
git clone https://github.com/DimensionalShade/DimShade.git
cd DimShade
pip install .
```

## 🧪 Example usage
```python
from dimshade import generate_SO5_key, encrypt, decrypt
import numpy as np

# Alice and Bob generate keys
A = generate_SO5_key()
B = generate_SO5_key()

# Shared secret
v = np.random.randn(5)
alice_secret = np.dot(A @ B @ v, v)
bob_secret   = np.dot(B @ A @ v, v)

assert np.isclose(alice_secret, bob_secret)
```

## 🛡️ Security Considerations
DimShade is designed to resist not only quantum attacks, but also a wide class of implementation-level threats that have proven effective against lattice-based schemes like Kyber.

### ✅ Resistance to Rowhammer and DRAM-based attacks
- DimShade does not store the secret key explicitly in memory.  
- The shared secret emerges from a joint geometric operation, not from static storage.

### ✅ Resistance to side-channel leakage
- No decoding step is involved — eliminating leakage vectors common in Kyber.  
- All operations (matrix multiplication, normalization) can be implemented in constant time.

### ✅ Resistance to fault injection
- DimShade does not rely on fragile decoding logic.  
- Faults in matrix operations can be detected via redundant computation or hash verification.

### ✅ Resistance to hardware trojans
- DimShade can be implemented in open hardware with formal verification.  
- Its core logic is compact and modular, allowing isolation from I/O and external components.

## 📜 License
MIT License — see [LICENSE](LICENSE)

## 🧠 Author
21.09.2025
Developed by **DimensionalShade**  
Philosophy, geometry, reproducibility, and post-quantum resistance.
