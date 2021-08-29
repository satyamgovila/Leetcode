
import collections
result = []

word_dict = collections.Counter(word)
for patt in patterns:
    print(patt)
    if patt in word:
        flag = True
    else:
        flag = False
    result.append(flag)
        
print(sum(result))
