from collections import OrderedDict

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
word_freq = {}
word_years = {}
temp = []
total = 0
i = 0

with open('song-data.json') as lyrics:
    for line in lyrics:
        if line[0] == '>':
                temp.clear()
                i = int(line[1:5])
                years[i] = 0
                word_years[i] = {}
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
                    if part not in word_freq:
                        word_freq[part] = 1
                    else:
                        word_freq[part] += 1
                    if part not in word_years[i]:
                        word_years[i][part] = 1
                    else:
                        word_years[i][part] += 1



with open('years-data.txt', 'w') as out_file:
    for x in sorted(years):
        out_file.write(str(x) + ": " + str(years[x]))
        out_file.write('\n')
    out_file.write("\tTotal: " + str(total))

with open('banned-data.txt', 'w') as out_file:
    for x in OrderedDict(sorted(word_freq.items(), key=lambda x: x[1])):
        out_file.write(str(x) + ": " + str(word_freq[x]))
        out_file.write('\n')

with open('years-banned-data.txt', 'w') as out_file:
    for x in sorted(word_years):
        out_file.write(str(x) + ": " + str(word_years[x]))
        out_file.write('\n')