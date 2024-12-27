string = input("Enter a word: ")
print(str)
vowels = "aeiouAEIOU"
vowel_count=0
consonant_count=0
for i in str:
    if i.isalpha():
        if i in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")           
