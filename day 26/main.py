import pandas

df = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
dict_alpha = {row.letter: row.code for (index, row) in df.iterrows()}

not_finished = True
while not_finished:
    word = list(input("Please enter your word: ").upper())
    try:
        out = [dict_alpha[key] for key in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(out)
        not_finished = False
