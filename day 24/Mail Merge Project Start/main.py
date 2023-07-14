import shutil

curr_file = "./Input/Letters/starting_letter.txt"
with open("Input/Names/invited_names.txt", 'r') as names:
    for name in names:
        name = name.split('\n')
        new_file = f"./Output/ReadyToSend/invite_{name[0]}.txt"
        shutil.copy(curr_file, new_file)
        with open(new_file, 'r+') as new:
            content = new.read()
            new.seek(0)
            new.truncate()
            new.write(content.replace('[name]', name[0]))



