f = open("README.md")
print(f.read())

# returns cursor to start of file
f.seek(0)
print(f.read())

f.seek(0)
print(f.readline())

f.close()

# same as the above but auto-closes file
with open("README.md") as file:
    file.read()


# to write file
with open("text.txt", "w") as file:
    file.write("HI!\n")
    file.write("HI HI!\n")


def copy(file1, file2):
    with open(file1) as file1:
        with open(file2, "w") as file2:
            file2.write(file1.read())

copy("text.txt", "text2.txt")

def copy_and_reverse(file1, file2):
    with open(file1) as file1:
        with open(file2, "w") as file2:
            file2.write(file1.read()[::-1])

copy_and_reverse("text.txt", "reverse_text.txt")

def statistics(file):
    with open(file) as f:
        lines = f.readlines()
    
    word_count = 0
    character_count = 0

    for line in lines:
        character_count += len(line)
        word_count += len(line.split(" "))
    
    stats = {
        "lines": len(lines),
        "words": word_count,
        "characters": character_count
    }
    
    return stats
    
print(statistics("text.txt"))


def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()