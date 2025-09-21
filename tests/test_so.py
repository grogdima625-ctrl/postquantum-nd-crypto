import numpy as np
from src.so_generator import random_so

def test_orthogonality():
    n = 5
    M = random_so(n)
    should_be_identity = M.T @ M
    assert np.allclose(should_be_identity, np.eye(n)), "Matrix is not orthogonal"

def test_determinant():
    n = 5
    M = random_so(n)
    det = np.linalg.det(M)
    assert np.isclose(det, 1.0), f"Determinant is not +1, got {det}"

if __name__ == "__main__":
    test_orthogonality()
    test_determinant()
    print("All tests passed.")
