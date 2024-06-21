inp = "I am Sipra das"
#op= count number of vowels 
vowel = 0
cons = 0
str = inp.strip()
for i in str.lower():
    if i != " ":
        if i in ('a','e','i','o','u'):
            vowel=vowel+1
        else:
            cons = cons+1

print("count of vowel is {} and count of consonants is {}"  .format(vowel,cons))

