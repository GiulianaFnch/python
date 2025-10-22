"""NumPy hello-world demo

Run this with the project's virtualenv Python to verify numpy is available and see basic operations.
"""

import sys

def demo():
	print('Hello from NumPy demo')
	print('python exe:', sys.executable)
	try:
		import numpy as np
	except Exception as e:
		print('Failed to import numpy:', e)
		return

	print('numpy version:', np.__version__)

	# Create arrays
	a = np.array([1, 2, 3])
	b = np.array([4, 5, 6])
	print('a =', a)
	print('b =', b)

	# Arithmetic
	print('a + b =', a + b)
	print('a * 2 =', a * 2)

	# Broadcasting and reshape
	c = np.arange(6).reshape(2, 3)
	print('c =')
	print(c)
	print('c + 10 =')
	print(c + 10)

	# Simple statistics
	print('c.sum(axis=1) =', c.sum(axis=1))
	print('c.mean() =', c.mean())

	# Random numbers (seeded)
	rng = np.random.default_rng(0)
	r = rng.random((2, 2))
	print('random 2x2:')
	print(r)

if __name__ == '__main__':
	demo()

