word = input().lower()
list = list(set(word))
cnt = []

for i in list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(list[(cnt.index(max(cnt)))].upper())