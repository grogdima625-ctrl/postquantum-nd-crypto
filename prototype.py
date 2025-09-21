import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def random_unit_quaternion():
    q = np.random.randn(4)
    return q / np.linalg.norm(q)

def quaternion_to_rotation_matrix(q):
    w, x, y, z = q
    return np.array([
        [1 - 2*(y**2 + z**2),     2*(x*y - z*w),     2*(x*z + y*w)],
        [    2*(x*y + z*w), 1 - 2*(x**2 + z**2),     2*(y*z - x*w)],
        [    2*(x*z - y*w),     2*(y*z + x*w), 1 - 2*(x**2 + y**2)]
    ])

v = np.array([1, 0, 0])
q = random_unit_quaternion()
R = quaternion_to_rotation_matrix(q)
v_rot = R @ v

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, *v, color='blue', label='Original')
ax.quiver(0, 0, 0, *v_rot, color='red', label='Rotated')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_title("SU(2) Rotation → SO(3) Action")
ax.legend()
plt.show()
