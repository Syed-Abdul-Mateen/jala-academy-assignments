# Matching a String Against a Regular Expression With matches()

import re

text = "hello123"
pattern = "^[a-z0-9]+$"

result = re.match(pattern, text)

print(result is not None)
