from lujing import tongji
import sys
import re
from prettytable import PrettyTable 
#需要封装的函数
def is_chu(x,y):
	if y==0:
		return 0
	else:
		return round(x/y,5)
def edit_distance(s1, s2):
    t1=[]
    t2=[]
    if len(s1) > len(s2):
    	s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return (max(len(s1),len(s2))-distances[-1])/(max(len(s1),len(s2))+0.000001),t1,t2
#转换方式
def zhuanhuan(y):
	
	y=re.sub('line_(.*[0-9]),','',y)
	y=re.sub('(.*[0-9])_str,','',y)

	y=re.sub('_','',y)
	y=re.sub('“','\'',y,count=0)
	y=re.sub('”','\'',y,count=0)
	y=re.sub('‘','\'',y,count=0)
	y=re.sub('’','\'',y,count=0)
	y=re.sub('（','(',y,count=0)
	y=re.sub('）',')',y,count=0)
	y=re.sub('[\s]','',y,count=0)
	y=re.sub('：',':',y,count=0)
	y=re.sub('，',',',y,count=0)
	y=re.sub('；',';',y,count=0)
	return y

def load_txt3(dir_1,dir_2):
	h=[]
	z=[]
	z1=1
	num=0
	cor_num=0
	yingwen_num=0
	shuzi_num=0
	zhongwen_num=0
	cor_num_1=[0,0,0,0]

	num2=0
	yingwen_num2=0
	shuzi_num2=0
	zhongwen_num2=0
	f=open(dir_1,'r')
	#匹配到正确的行
	for x in f.readlines():
		#print('第',z1,'行开始匹配:')
		x=zhuanhuan(x)

		if len(x)==0:continue
		num=num+len(x)
		shuzi=len(re.sub('([^0-9])','',x,count=0))
		shuzi_num=shuzi+shuzi_num
		yingwen=len(re.sub('[^a-zA-z]','',x,count=0))
		yingwen_num=yingwen+yingwen_num
		zhongwen_num=zhongwen_num+len(re.sub(u'[^\u4e00-\u9fa5]','',x,count=0))
		#删除line_(.*[0-9])，
		#x=re.sub('line_(.*[0-9]),','',x)
		z1=z1+1
		with open(dir_2,'r') as f2:
			for y in f2.readlines():
				y=zhuanhuan(y)

				xz=edit_distance(x,y)
				z.append(xz[0])
			ssss=z.index(max(z))+1
			#print(z,'\n匹配度：',max(z),'\n匹配到的行：',ssss,'\n')
			#print('匹配到的行：',ssss)
			#统计匹配到的行的位置

			z=[]






		i=0
		#统计字数
		with open(dir_2,'r') as f2:
			for y in f2.readlines():
				
				if i==ssss-1:
					y=zhuanhuan(y)
					#print('匹配结果：')
					xss=tongji(x,y)
					#print('正确率',xss[0],'正确字数',xss[1],'总字数:',len(x))
					#总的正确字数
					cor_num=cor_num+xss[1]
					cor_num_1[0]=cor_num_1[0]+xss[9][0]
					cor_num_1[1]=cor_num_1[1]+xss[9][1]
					cor_num_1[2]=cor_num_1[2]+xss[9][2]
					cor_num_1[3]=cor_num_1[3]+xss[9][3]
					#总字数
					#找出最大的串
					i15='%s'*len(xss[6]) % tuple(xss[6])
					i16=re.search('@@@@',i15)
					if i16:
						i13=i16.span()
						i14=i13[1]
						while i14<len(i15)-1:
							if i15[i14+1]=='@':
								i14=i14+1
							else:
								break
						i16='%s'*len(xss[5]) % tuple(xss[5])
						h.append(i16[i13[0]:i14])
						#print(xss[5][:i13[0]]+xss[5][i14:])
						#print(xss[6][:i13[0]]+xss[6][i14:])
						#print(xss[8][:i13[0]]+xss[8][i14:])
					else:
						pass


						#print(xss[5])
						#print(xss[6])

						#print(xss[8])
					#print('----------------------分割线----------------------')
				i=i+1
	f.close()
	ssss=[]
#第二次匹配开始
	for i17 in h:
		#print('未匹配的行开始匹配：')
		with open(dir_2,'r') as f2:
			for y in f2.readlines():
				y=zhuanhuan(y)

				xz=edit_distance(i17,y)
				z.append(xz[0])
			ssss=z.index(max(z))+1
			#print(z,'\n匹配度：',max(z),'\n匹配到的行：',ssss,'\n')
			#print('匹配到的行：',ssss)
			#统计匹配到的行的位置

			z=[]
		i=0
		#统计字数
		with open(dir_2,'r') as f2:
			for y in f2.readlines():
				
				if i==ssss-1:
					y=zhuanhuan(y)
					#print('匹配结果：')
					xss=tongji(i17,y)
					#print('正确率',xss[0],'正确字数',xss[1],'总字数:',len(x))
					#总的正确字数
					cor_num=cor_num+xss[1]
					cor_num_1[0]=cor_num_1[0]+xss[9][0]
					cor_num_1[1]=cor_num_1[1]+xss[9][1]
					cor_num_1[2]=cor_num_1[2]+xss[9][2]
					cor_num_1[3]=cor_num_1[3]+xss[9][3]
					#总字数
					#
					#
					#

					#print(xss[5])
					#print(xss[6])
					#print(xss[8])


					

					
					#print('----------------------分割线----------------------')
				i=i+1


	





#统计文本2中的文本
	with open(dir_2,'r') as f3:
		for y11 in f3.readlines():
			y11=re.sub('line_(.*[0-9]),','',y11)
			y11=re.sub('\n','',y11,count=0)
			y11=re.sub('\s','',y11,count=0)
			#统计字数
			num2=num2+len(y11)
			shuzi2=len(re.sub('([^0-9])','',y11,count=0))
			shuzi_num2=shuzi2+shuzi_num2
			yingwen2=len(re.sub('[^a-zA-z]','',y11,count=0))
			yingwen_num2=yingwen2+yingwen_num2
			zhongwen_num2=zhongwen_num2+len(re.sub(u'[^\u4e00-\u9fa5]','',y11,count=0))
	
	

	#num=num+1
	#num2=num2+1
	#print('总字数、正确字数、正确率分别为：',num,cor_num,cor_num/num,'\n其中，中文为：',zhongwen_num,'英文为：',yingwen_num,'数字为：',shuzi_num,'符号为：',num-zhongwen_num-yingwen_num-shuzi_num,'\n正确的中文，英文，数字，字符分别为为：',cor_num_1)
	#print('中文、英文、数字、字符正确率统计',is_chu(cor_num_1[0],zhongwen_num),is_chu(cor_num_1[1],yingwen_num),is_chu(cor_num_1[2],shuzi_num),is_chu(cor_num_1[3],num-zhongwen_num-yingwen_num-shuzi_num))
	#print('总字数、正确字数、正确率分别为：',num2,cor_num,cor_num/num2,'\n其中，中文为：',zhongwen_num2,'英文为：',yingwen_num2,'数字为：',shuzi_num2,'符号为：',num2-zhongwen_num2-yingwen_num2-shuzi_num2)
	x = PrettyTable(['','中文','英文','数字','符号','综合'])
	xxx=num-zhongwen_num-yingwen_num-shuzi_num
	x.add_row(['总字数',zhongwen_num,yingwen_num,shuzi_num,num-zhongwen_num-yingwen_num-shuzi_num,num])
	x.add_row(['正确总字数',cor_num_1[0],cor_num_1[1],cor_num_1[2],cor_num_1[3],cor_num])
	x.add_row(['正确率',is_chu(cor_num_1[0],zhongwen_num),is_chu(cor_num_1[1],yingwen_num),is_chu(cor_num_1[2],shuzi_num),is_chu(cor_num_1[3],(num-zhongwen_num-yingwen_num-shuzi_num)),is_chu(cor_num,num)])
	print(x)
	return num,cor_num,is_chu(cor_num,num),zhongwen_num,yingwen_num,shuzi_num,xxx,cor_num_1
#输出函数

	# output=sys.stdout
	#outputfile=open(dir3,'w')
	# sys.stdout=outputfile
	
	# #print(y[6])
	# outputfile.close()
if __name__ == '__main__':
    load_txt3('221.txt','222.txt')
