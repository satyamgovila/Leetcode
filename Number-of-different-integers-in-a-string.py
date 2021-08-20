class Solution:
	def numDifferentIntegers(self, word: str) -> int:
		parsed = []

		for c in word: 
			if c.isalpha():
				parsed.append(" ")
			else:
				parsed.append(c)
		parsed = ("".join(parsed)).split(" ")
		parsed = [int(c) for c in parsed if c]
		return len(set(parsed))
