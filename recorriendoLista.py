fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    #convirtiendo la linea a una lista
    n = line.split()
    for i in range(len(n)):
        if len(lst) <= 0: lst.append(n[i])
        else:
            lst.append(n[i])

new_list=list()
#eliminando elementos duplicados en la lista
for i in lst:
    if i not in new_list:
        new_list.append(i)
new_list.sort()
print(new_list)