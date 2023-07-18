import pandas

df = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
dict_alpha = {row.letter: row.code for (index, row) in df.iterrows()}

word = list(input("Please enter your word: ").upper())
out = [dict_alpha[key] for key in word]
print(out)
