print("""+=================+
+ the vowel eater +
+=================+""")

user_word = input('Enter a word:\n').upper()

for letter in user_word:
    if letter in ['A','E','I','O','U']:
        continue
    print(letter)
