import numpy as np

def random_so(n):
    """Generate a random SO(n) matrix via QR decomposition."""
    A = np.random.randn(n, n)
    Q, R = np.linalg.qr(A)
    # Ensure determinant = +1 (special orthogonal)
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1
    return Q

# Example: generate SO(4)
so4 = random_so(4)
print("Random SO(4) matrix:\n", np.round(so4, 3))
print("Determinant:", round(np.linalg.det(so4), 3))
