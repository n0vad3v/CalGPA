from functools import reduce
import re
import sys

with open(sys.argv[1],'r',encoding = 'utf-8') as src:
    data = src.read().replace('\n','').replace('\t','').replace('中','75').replace('优','95').replace('良','85').replace('<font color="red">','').replace('</font>','')

total = re.findall('<td align="center"><b>(.*?)</b></td>',data)[1]

datastr = ''
findtr = re.findall('<tr>(.*?)</tr>',data)

# For cleaning the chaos data
newtr = []
for i in findtr:
    if 'color' not in i and 'align' not in i and '<td>&nbsp;</td><td>&nbsp;</td>' not in i and 'Nsb_r_list_thb' not in i:
        newtr.append(i)
# Now we have clean data
credit = []
score = []
for i in newtr:
    data = re.findall(r"<td>(.*?)</td>",i)
    credit.append(data[2])
    score.append(data[5])

score = list(map(int,score))
credit = list(map(float,credit))
sumup = reduce(lambda x,y:x+y,credit)
floatscore = map(lambda x:(x-50)/10,score)
floatscore = [0 if i<0 else i for i in list(floatscore)]

addup = map(lambda x,y:x*y,credit,floatscore)
div = reduce(lambda x,y:x+y,addup)

gpa = div/sumup

print("Your GPA is {:.2f},with system credit:{},sumup credit:{}".format(gpa,float(total),sumup))
