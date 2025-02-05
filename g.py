import random
import sys
import string

class SimpleLCG:
	def	__init__(self, seed=None):
		self.m = 4294967296	 # 2^32
		self.a = 1664525
		self.c = 1013904223
		self.state = seed if seed is not None else int(random.random() * self.m)

	def	next(self):
		self.state = (self.a * self.state +	self.c)	% self.m
		return self.state /	self.m

def	main():
	# 默认字符集为小写和大写字母
	char_set = string.ascii_lowercase
	
	try:
		# 获取命令行参数
		seed = int(sys.argv[1])
		length = int(sys.argv[2])
		
		# 检查是否有第四个参数，如果有，则使用它作为字符集
		if len(sys.argv) ==	4:
			user_char_set =	sys.argv[3]
			if user_char_set !=	"":
				char_set = user_char_set
			
	except (IndexError,	ValueError):
		print("Usage: python script.py <seed> <length> [<character_set>]")
		sys.exit(1)

	random_string =	""
	rng	= SimpleLCG(seed)
	for	i in range(length):
		k =	int(rng.next() * len(char_set))
		random_string += char_set[k]

	print(random_string)

if __name__	== "__main__":
	main()