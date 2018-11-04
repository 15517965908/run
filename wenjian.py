from txt2 import load_txt3,is_chu
import os
import sys
from prettytable import PrettyTable 

x=[]
y=[]
def is_chu(x,y):
	if y==0:
		return 0
	else:
		return round(x/y,5)



for flie_name in os.listdir('1'):
	if flie_name[-4:]=='.txt':
		x.append(flie_name)
for flie_name in os.listdir('2'):
	if flie_name[-4:]=='.txt':
		y.append(flie_name)
z11=0
z22=0
z33=0
z44=0
z55=0
z66=0
z88=0
z77=[0,0,0,0]
z=[]
output=sys.stdout
outputfile=open('resoult.txt','w')
sys.stdout=outputfile
for _ in x:
	if _ in y:
		print('文件：',_)
		z=load_txt3('1/'+_,'2/'+_)

		z11=z11+z[0]
		z22=z22+z[1]

		z88=z88+z[3]
		z44=z44+z[4]
		z55=z55+z[5]
		z66=z66+z[6]


		z77[0]=z77[0]+z[7][0]
		z77[1]=z77[1]+z[7][1]
		z77[2]=z77[2]+z[7][2]
		z77[3]=z77[3]+z[7][3]

z33=is_chu(z22,z11)
print('总结：')
p=PrettyTable(['总结','中文','英文','数字','符号','综合'])
p.add_row(['总字数',z88,z44,z55,z66,z11])
p.add_row(['正确字数',z77[0],z77[1],z77[2],z77[3],z22])
p.add_row(['正确率',is_chu(z77[0],z88),is_chu(z77[1],z44),is_chu(z77[2],z55),is_chu(z77[3],z66),z33])

print(p)
outputfile.close()