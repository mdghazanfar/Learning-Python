
text = """
a b a c b a A B
"""
print(text.split())

print(text.lower().split())

for word in text.split():
    print(word)
    
    
word_count = {}

# for word in text.split():
#    word_count[word] = 1
# print(word_count )
    
    

for word in text.lower().split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
print(word_count )