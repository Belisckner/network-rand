
import random

r = [random.randint(0, 255) for i in range(0, 4)]	#rand part of IP address
mask = random.randint(7, 30) 				#part of network MASK
print(*r, sep='.', end='/', )				#display address
print(mask)						#and mask, and that all