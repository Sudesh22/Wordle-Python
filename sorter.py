import time

words = []

with open("abc.txt") as f:
    for x in f:
        words.append(str(x).strip("\n"))
        words = set(words)
        words = sorted(list(words))
print(len(words))

with open(r'words.txt', 'w') as fp:
    for item in words:
        # write each item on a new line
        fp.write(str("%s," % item).lower())
    print('Done')
