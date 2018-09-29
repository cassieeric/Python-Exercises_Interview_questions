# 请输入3个英文单词
word1 = input('请输入第一个英文单词：') # hello
word2 = input('请输入第二个英文单词：') # world
word3 = input('请输入第三个英文单词：') # python

c = [word1[0], word2[0], word3[0]]
# print(c) 结果是：['h', 'w', 'p']
d = sorted(c)
# print(d) 结果是：['h', 'p', 'w']
e = [word1, word2, word3]
print(sorted(e))
