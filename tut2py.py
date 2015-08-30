
largest = -1
print "Before", largest
for value in [3,41,12,9,74,15] :
    if value > largest :
        largest = value
print largest,value

max = -1
min= 10000
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    if len(num)<1 : break
    try:
        num = float(num)
    except :
        print "Invalid input"
        continue
    if num > max :
        max= num
    if num < min :
        min = num
print "Maximum is", max
print "Minimum is", min


colon=":"
count=0
total=0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(colon)
    pos=int(pos)
    num=line[pos+1:40]
    num=float(num)
    count=count+1
    total=total+num
print "Average spam confidence:", total/count
