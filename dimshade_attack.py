import numpy as np
from dimshade_core import generate_SO5_key, derive_scalar_secret

# Истинные ключи
A = generate_SO5_key()
B = generate_SO5_key()

# Истинный вектор
v_true = np.random.randn(5)
v_true /= np.linalg.norm(v_true)

# Истинный скалярный секрет
s_true = derive_scalar_secret(A, B, v_true)
print(f"🎯 Истинный скалярный секрет: {s_true:.10f}")

# Эмуляция атаки: перебор случайных векторов
attempts = 100_000
closest = None
min_diff = float('inf')

for _ in range(attempts):
    v_guess = np.random.randn(5)
    v_guess /= np.linalg.norm(v_guess)
    s_guess = derive_scalar_secret(A, B, v_guess)
    diff = abs(s_guess - s_true)
    if diff < min_diff:
        min_diff = diff
        closest = s_guess

print(f"\n🧪 Лучшая попытка восстановления: {closest:.10f}")
print(f"📉 Минимальная разница: {min_diff:.10f}")
print(f"🔐 Успешность атаки: {'НЕВОЗМОЖНА' if min_diff > 1e-6 else 'ВОЗМОЖНА'}")
