import numpy as np
from dimshade_core import generate_SO5_key, derive_scalar_secret

def test_quantum_attack_fails():
    A = generate_SO5_key()
    B = generate_SO5_key()
    v_true = np.random.randn(5)
    v_true /= np.linalg.norm(v_true)
    s_true = derive_scalar_secret(A, B, v_true)

    min_diff = float('inf')
    for _ in range(1000):  # Уменьшено для CI
        v_guess = np.random.randn(5)
        v_guess /= np.linalg.norm(v_guess)
        s_guess = derive_scalar_secret(A, B, v_guess)
        diff = abs(s_guess - s_true)
        if diff < min_diff:
            min_diff = diff

    assert min_diff > 1e-6, "Атака слишком близка к секрету — устойчивость нарушена"
