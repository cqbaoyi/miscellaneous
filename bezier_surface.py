from scipy import interpolate
import numpy as np

# m >= (kx + 1)(ky + 1) = 4 * 4 = 16
x = np.array([1, 3, 7, 11, 12, 17, 20, 25, 30, 40, 50, 67, 78, 90, 100, 120])
y = np.array([2, 7, 9, 14, 16, 20, 21, 40, 50, 61, 72, 82, 99, 109, 120, 135])
z = np.array([0.1, 0.4, 0.9, 1.7, 1.9, 4.0, 5.0, 7.0, 9.2, 11.0, 13.0, 16.0, 20.0, 25.0, 31.0, 39.0])

surface= interpolate.bisplrep(x, y, z)
print(interpolate.bisplev(4, 17, surface))

