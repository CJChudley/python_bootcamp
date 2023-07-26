# Lesson 1
text = "The agent's phone number is 408-555-1234. Call soon!"
text = "my phone once, my phone twice"
import re
pattern = 'phone'
match = re.search(pattern,text)

matches = re.findall('phone', text)
print(matches)
print(match)

for match in re.finditer("phone",text):
    print(match.group())

# Lesson 2
