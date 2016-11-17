#creating a list of various banned words across multiple websites
banned = []
with open('banned.txt', 'r') as banned_words:
    for word in banned_words:
        if word not in banned:
            banned.append(word.strip('\n'))
with open('banned2.txt', 'r') as banned_words:
    for word in banned_words:
        if word not in banned:
            banned.append(word.strip('\n'))
with open('banned3.txt', 'r') as banned_words:
    for word in banned_words:
        if word not in banned:
            banned.append(word.strip('\n'))

years = {}
count = 0
total = 0
i = 0

with open('song-data.json') as lyrics:
    for line in lyrics:
        if line[0] == '>':
                i = int(line[1:5])
                years[i] = 0
        elif line[0] == '(':
            pass
        else:
            line = line[:-76]
            for part in line.split():
                part = part.lower()
                part = ''.join(c for c in part if  c not in '.,;:-_?!*""''\'()/\[]')
                if part in banned:
                    years[i] += 1
                    total += 1

print(years)
print('total = ' + str(total))
