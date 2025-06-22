import re

text = "abc123xyz"

m1 = re.match(r"\d+", text)
m2 = re.search(r"\d+", text)

print(m1)
print(m2.group())