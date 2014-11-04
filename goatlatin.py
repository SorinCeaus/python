# file: goatlatin.py
# desc: facebook telephone interview task, 7/4/2014
#
# Goat Latin is a made-up language based off of English, sort of like Pig Latin. The rules of Goat Latin are as follows:
# 1. If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add 'ma'.
# For example, the word 'goat' becomes 'oatgma'.
# 2. If a word begins with a vowel, append 'ma' to the end of the word.
# For example, the word 'I' becomes 'Ima'.
# 3. Add one letter "a" to the end of each word per its word index in
# the sentence, starting with 1.  That is, the first word gets "a" added
# to the end, the second word gets "aa" added to the end, the third word
# in the sentence gets "aaa" added to the end, and so on.
#
sentence = ['This','is','goat','latin']
n=0
for word in sentence:
	n=n+1
	aaa=[n*'a']
	fl=word[:1].lower()
	if fl not in ("a", "e", "i", "o", "u"):
		# begins with consonant
		print 'word begins with consonant: ', word
		print 'lets change it, first letter is'
		cword=word[1:] + fl + 'ma'
		cword=cword+aaa[0]
		print 'word becomes:', cword
	if fl in ("a", "e", "i", "o", "u"):
		print 'word begins with a vowel: ', word
		# begins with vowel
		cword=word + 'ma'
		cword=cword+aaa[0]
		print 'word becomes:', cword
