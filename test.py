
import random

r = [random.randint(0, 255) for i in range(0, 4)]	#rand part of IP address
mask = random.randint(7, 30) 				#partof network MASK
							#just skip this
print(*r, sep='.', end='/', )				#display address
print(mask)						#and mask, and that all
print("hello, world")
print("lalala")