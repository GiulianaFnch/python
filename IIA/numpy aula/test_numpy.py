import sys

def main():
    print('python exe:', sys.executable)
    try:
        import numpy as np
    except Exception as e:
        print('failed to import numpy:', e)
        return

    print('numpy version:', np.__version__)
    a = np.array([1, 2, 3, 4, 5])
    print('array:', a)
    print('sum:', np.sum(a))
    print('mean:', np.mean(a))

if __name__ == '__main__':
    main()
