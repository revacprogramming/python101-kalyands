# Dictionaries

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for lin in handle:
    wds = lin.split()
    print(wds)