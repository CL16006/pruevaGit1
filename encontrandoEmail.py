fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count = 0
lst=list()
fh = open(fname)
for line in fh:
    line=line.rstrip()
    if line.startswith('From') and line.endswith('2008'):
        n=line.split()
        print(n[1])
        count+=1
    else:
        continue

print("There were", count, "lines in the file with From as the first word")
