story = '''Once upon a time there was a youtuber named Harry who uploaded Python course with notes'''

# Length
print(len(story))

# String checking
# This outputs true as story ends with notes
print(story.endswith("notes"))

# Counting occurances 
print(story.count("H"))
print(story.count("Python"))

# Capitalize first letter of String
print(story.capitalize())

# Returning index of an occurance
# Tells index of first occurance
print(story.find("Once"))

# Replace words
# Replaces all occurances of old to new
print(story.replace("Harry", "Abdullah"))