import sys

print(' '.join(i[::-1].swapcase() for i in sys.argv[1:]))
