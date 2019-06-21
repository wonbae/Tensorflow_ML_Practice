#-*- coding: utf-8 -*-

# function to split syllables to characters
def split_syllables(word):
	top_list = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']
	mid_list = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']
	bot_list = [u'', u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']
	result = u""
	for syllable in word:
		if ord(syllable) < 44032 or ord(syllable) > 55203:
			result += syllable
		else:
			base = ord(syllable)-44032
			top_idx = base//588
			mid_idx = (base%588)//28
			bot_idx = (base%588)%28
			result += top_list[top_idx] + mid_list[mid_idx] + bot_list[bot_idx]
	return result

# function to build syllable by joining characters
def combine_to_syllables(chars):
	top_idx = [0, 1, -1, 2, -1, -1, 3, 4, 5, -1, -1, -1, -1, -1, -1, -1, 6, 7, 8, -1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
	bot_idx = [1, 2, 3, 4, 5, 6, 7, -1, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, -1, 18, 19, 20, 21, 22, -1, 23, 24, 25, 26, 27]
	idx = 0
	types = [0]*len(chars)
	for char in chars:
		if ord(char) > 12643 or ord(char) < 12593:
			types[idx] = -1
		elif ord(char) >= 12623:
			types[idx] = 2
		idx+=1
	for i in range(1, len(types)):
		if types[i] == 2 and types[i-1]==0:
			types[i-1]=1
	for i in range(0, len(types)-1):
		if types[i] == 2 and types[i+1]==0:
			types[i+1]=3
	syllables = []
	character = []
	idx = 0
	for i in types:
		if i<2 and len(character)>0:
			syllables.append(character)
			character = []
		character.append(chars[idx])
		if i==-1:
			syllables.append(character)
			character = []
		idx+=1
	if len(character)>0:
		syllables.append(character)
	result = u""
	for syllable in syllables:
		if len(syllable)==3:
			tmp = 44032 + top_idx[ord(syllable[0])-12593]*588 + (ord(syllable[1])-12623)*28 + bot_idx[ord(syllable[2])-12593]
			result += chr(tmp)
		elif len(syllable)==2:
			if ord(syllable[0])>=12623:
				result += syllable[0] + syllable[1]
				continue
			tmp = 44032 + top_idx[ord(syllable[0])-12593]*588 + (ord(syllable[1])-12623)*28
			result += chr(tmp)
		elif len(syllable)==1:
			result += syllable[0]
		else:
			for character in syllable:
				result+=character	
	return result

# function to print list
def print_list(arg):
	for i in range(len(arg)):
		print(arg[i])
	print("")

# function to print dictionary
def print_dict(arg):
	for key in arg.keys():
		print (key, ":", arg[key])
	print("")


# step1: load requried resources

# load dictionary
dictionary={}
	# to do
f = open("dictionary", "r", encoding="utf-8")
# for line in f:
# 	line = line.split()
# 	# print(line)
# 	# print(line[0])
# 	dictionary[line[0]] = line[1]
for line in f:
	morph = line.strip().split('\t')
	if morph[0] not in dictionary:
		dictionary[morph[0]] = [morph[1]]
	else:
		dictionary[morph[0]] += [morph[1]]
f.close()


print('dictionary:')
print_dict(dictionary)


# load connectivity
connectivity=[]
	# to do
f = open("connectivity", "r", encoding="utf-8")
for line in f:
	connectivity.append(line.strip())
f.close()


print('connectivity:')
print_list(connectivity)

# step2: split word into character
# read user input & syllables->characters
	# to do
word = input('input your word: ')
chars = split_syllables(word)
print('chars: ', chars)

# step3: build CYK table
# construct empty table with word length
table = []
	# to do
for i in range(len(chars)):
	table.append([])
	for j in range(i + 1):
		table[-1].append([])
	# table.append([[]] * (i+1))


print ("cyk table initialized:")
print_list(table)

# step4: morpheme segmentation
	# to do

tmp = []

# for row in range(len):
# 	for col in range(len):
# 		idx_prime = len + col - row
# 		tmp += table[row][col]
# 		print(tmp)
# 		if combine_to_syllables(tmp) == dictionary[0]:
# 			table.append()

for i in range(len(chars))[::-1]:
	for j in range(i+1)[::-1]:
		subword = combine_to_syllables(chars[j:j + len(chars) - i])
		if subword in dictionary:
			for morph in dictionary[subword]:
				table[i][j].append(subword + ":" + morph)



print ("cyk table after morpheme segmentation:")
print_list(table)

# step5: connectivity check
	# to do
for j in range(len(chars))[::-1]:
	for i in range(j + 1, len(chars)):
		idx_prime = len(chars) + j - i

		for left_morph in table[i][j]:
			for right_morph in table[idx_prime][idx_prime]:
				left_category = left_morph.split('+')[-1].split(':')[1]
				right_category = right_morph.split('+')[0].split(':')[1]

				if(left_category + '\t' + right_category) in connectivity:
					table[j][j].append(left_morph + '+' + right_morph)
		# print(i,j)

print ("cyk table after connectivity checking:")
print_list(table)
				
# step6: print result
print ("result:")
	# to do
print(table[0][0])
