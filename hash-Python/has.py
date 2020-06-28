import sys
import time
start = time.time()
print(sys.argv)
if len(sys.argv) != 3:
    raise ValueError('Please provide two file names.')
sys.argv[0] = sys.argv[0][0:len(sys.argv[0]) - sys.argv[0][::-1].find('/')]
inputFile1 = sys.argv[0]+sys.argv[1]
inputFile2 = sys.argv[0]+sys.argv[2]
print("The files that will be used for input are {0} and {1}".format(sys.argv[1],
                                                                     sys.argv[2]))
filename, filename2 = str(sys.argv[1]), str(sys.argv[2])
f = open(filename, "r")
j = ' '
for i in f:
    j = j+i
k = j.split()
sort_dict = {}
total_str = "".join(k)
count = 0
key = 0
for i in k:
    if len(i) > 1:
        key = total_str.count(i[0])+total_str.count(i[-1])
    else:
        key = total_str.count(i[0])
    sort_dict[i] = key
    key = 0

final_dict = {}
f2 = open(filename2, 'r')
second_text = f2.readlines()
second_text = ''.join(second_text)
nlines = second_text.count('\n')
second_text = second_text.strip()
k1 = 0
second_text = second_text.split()
for k in sort_dict.keys():
    count += 1
    final_dict[k] = second_text.count(k)
sort_final = sorted(final_dict.items(), key=lambda x: x[0])
end = time.time()
print('''
*********************
***** STATSTICS *****
*********************''')
print("Total Lines Read: {}".format(nlines))
print("Total Words Read: {}".format(len(second_text)), end="\n\n")
print("Break Down by Key Word ")
for s in sort_final:
    print("{} : {}".format(s[1], s[0]))
print("Total Key Words: {}".format(count))
print("Total Time of  Program: {}".format(end-start))
