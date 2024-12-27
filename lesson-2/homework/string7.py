sentence = input("Input a sentence: ")
replace = input("Replace: ")
With =input("With: ")
# first=sentence.split(replace[0])[0]
# third=sentence.split(replace[-1])[1]
# print(first)
# print(third)
# print(first+With+third)
replaced=sentence.replace(replace, With)
print(replaced)
