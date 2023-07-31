import re
# # Lesson 1
# text = "The agent's phone number is 408-555-1234. Call soon!"
# # text = "my phone once, my phone twice"

# pattern = 'phone'
# match = re.search(pattern,text)

# matches = re.findall('phone', text)
# print(matches)
# print(match)

# for match in re.finditer("phone",text):
#     print(match.group())

# Lesson 2
# text = "The agent's phone number is 408-555-1234. Call soon!"
# phone =  re.search(r"\d\d\d-\d\d\d-\d\d\d\d",text)
# # print(phone.group())

# phone =  re.search(r"\d{3}-\d{3}-\d{4}",text)
# print(phone)

# phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
# results = re.search(phone_pattern,text)
# print(results.group())
# print(results.group(1)) # starts from index 1, not 0

# Lesson 3
print(re.search(r"cat|dog","The cat is here"))
print(re.findall(r"...at","The cat in the hat sat there.")) # . adds a wild card to the beginning
print(re.findall(r"^\d","1 is a number")) # starts with
print(re.findall(r"\d$","1 is a number")) # ends with
phrase = "there are 3 numbers 34 inside 5 this sentence"

pattern = r'[^\d]+'
print(re.findall(pattern,phrase))

test_phrase = 'This is a string! But it has punctuaion. How can we remove it?'
print(re.findall(r'[^!.? ]+',test_phrase))
clean = re.findall(r'[^!.? ]+',test_phrase)
' '.join(clean)

text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern,text))

text = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like to take a catnap?'
textthree = 'Hello, have you seen this caterpillar?'

re.search(r'cat(fish|nap|claw)',text)



fake_variable = []