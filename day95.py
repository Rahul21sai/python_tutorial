import re

pattern = r"expression"
text = "the cat is in the hat"

match = re.search(pattern,text)
print(match)


# matches = re.finditer(pattern,text)
# for match in matches:
#     print(match.span())
#     print(text[match.span()[0]]:match.span()[1]])