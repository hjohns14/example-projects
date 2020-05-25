'''
Good morning! Here's your coding interview problem for today.
	This problem was asked by Facebook:
		
		Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
		count the number of ways it can be decoded.
			
			For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
			You can assume that the messages are decodable. For example, '001' is not allowed.
'''


code_dict =  {
	1: 'a',  2: 'b', 3: 'c', 4: 'd', 5: 'e',
	6: 'f', 7: 'g',	8: 'h', 9: 'i', 10: 'j',
	11: 'k', 12: 'l', 13: 'm', 14: 'n',	15: 'o' ,
	16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
	21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}

win = 23914
prob = 111





class Book():
	def __init__(self, key):
		self.id = "dhfaohufneklahfsiohfsd"
		self.purpose = "To get this daily coding problem"
		self.key = key
		self.options = []


	def split_int(self):
		self.split_key = [int(i) for i in str(self.key)]
		return self.split_key

	def append_code(self, op, i):
		op.append(code_dict[i])


	def group_nums(self):
		self.option = []
		self.split_int()
		for i in range(len(self.split_key)):
			# the key is split just execut boi
			if i < len(self.split_key) - 1:
				check_sum = int(str(self.split_key[i]) + str(self.split_key[i+1]))
			print(code_dict[self.split_key[i]])
			if check_sum < 27 and check_sum:
				self.append_code(self.option, check_sum)
			elif i == len(self.split_key):
				self.append_code(self.option, self.split_key[i])
		print(self.option)



	def run(self):
		self.group_nums()





book = Book(win)


book.run()

















'''

def de_code(key):
	key_list = [int(i) for i in str(key)]
	options = []
	option_1 = []
	option_2 = []
	print(key_list)


 ## So close yet so far away

	for i in key_list:
		option_1.append(code_dict[int(i)])
	options.append(option_1)

	i= 0
	while i <= len(key_list)-2:
		check_sum = int(str(key_list[i]) + str(key_list[i+1]))
		if check_sum < 27:
			print(check_sum)
			option_2.append(code_dict[check_sum])
			i += 2
		elif i == len(key_list)- 1:
			option_2.append(code_dict[int(key_list[i])])
			
		else:
			option_2.append(code_dict[int(key_list[i])])
			i+=1

	options.append(option_2)

		



	print(options)
	print("number of combinations: ", len(options))
'''