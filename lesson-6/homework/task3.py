import os
with open('word_count_report.txt','w+') as file:
     content=file.read()
     file.write("")
filename='sample.txt'
if not os.path.exists(filename):
    print(f"The file '{filename}' does not exist.")
    paragraph=input("Type a paragraph to create the file: ")
    with open(filename, "w") as file:
        file.write(paragraph)
    print(f"The file '{filename}' has been created successfully.")
# else:
#     with open(filename, 'r') as file:
#         content = file.read()
#         print(f"Contents of '{filename}':\n")
#         print(content)
with open(filename, 'r') as file:
        content = file.read()
cleaned=content.lower().replace('.','').replace(',','').replace('\n',' ').split()
# print(cleaned)
total=len(cleaned)
num=[]
s=set()
words_without_dublicate=set(cleaned)
for i in words_without_dublicate:
    num.append(cleaned.count(i))
    s.add(cleaned.count(i))
# print(num)
most_common=[]
for i in s:
    while(i in num):
        most_common.append(i)
        num.remove(i)
# print(s)
print(f"Total words: {total}")
print("Top 5 most common words: ")
# print(most_common)
# print(words_without_dublicate)
def most():
     processed_words = set()
     for i in range(-1, -6,-1):
          for j in words_without_dublicate:
               if j not in processed_words and (most_common[i]==cleaned.count(j)):
                    print(f"{j} - {most_common[i]} times")
                    processed_words.add(j)
                    break
most()
with open('word_count_report.txt', 'a') as file:
     file.write("Word Count Report\n")
     file.write(f"Total words: {total}\n")
     file.write("Top 5 Words: \n")
     processed_words = set()
     for i in range(-1, -6,-1):
          for j in words_without_dublicate:
               if j not in processed_words and (most_common[i]==cleaned.count(j)):
                    file.write(f"{j} - {most_common[i]}\n")
                    processed_words.add(j)
                    break

     



        