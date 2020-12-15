myDict = {
    "fast": "In a quick manner",
    "abdullah" : "A Coder",
    "marks": [1, 3, 7, 11],
    "anotherdict": {'harry': 'player'},
    1: 2
}

# Dictionary methods
print(list(myDict.keys())) # Prints keys of the dictionary
print(list(myDict.values())) # Prints value of the dictionary
print(myDict.items()) # Prints the key/value pairs of the dictionary
print(myDict)
updateDict = {
    "Wisal": "Friend",
    "Yasin": "Friend",
    "Senir": "Friend"
}
myDict.update(updateDict) # Adds key value pairs from updateDict to myDict
# Update overwrites value if key is same
print(myDict)
# print(myDict.get["Abdullah2"])  # Returns none as key not present
# print(myDict["Abdullah2"]) # Gives error as key not present