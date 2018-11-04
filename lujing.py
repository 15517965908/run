import re
def bijiao(t1,t2):
    def edit(str1, str2):
        matrix = [[i+j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    d = 0
                else:
                    d = 1
                matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+d)
                
        return matrix[len(str1)][len(str2)],matrix,str1,str2

    cor_len=len(t1)
    len_t1=len(t1)
    len_t2=len(t2)
    x=edit(t1,t2)
    #打印矩阵    
    #for _ in range(len(x[1])):
       #print(x[1][_])

    #打印最短路径
    def print_lujing(t):
        i=len_t1
        j=len_t2
        s=[[len_t1,len_t2]]
        while i>0 and j>0:
            ss12=min(t[i-1][j-1],t[i][j-1],t[i-1][j])
            if ss12==t[i-1][j-1]:
                s.append([i-1,j-1])
                i=i-1
                j=j-1
            elif t[i-1][j]==ss12:
                s.append([i-1,j])
                i=i-1
            elif t[i][j-1]==ss12:
                s.append([i,j-1])
                j=j-1
        while i!=0:
            s.append([i-1,j])
            i=i-1
        while j!=0:
            s.append([i,j-1])
            j=j-1
        return s


    y=print_lujing(x[1])
    #print(y)
    ss1=[]
    for sss in range(len(y)-1):
        s1=abs(y[sss+1][0]-y[sss][0])
        s2=abs(y[sss+1][1]-y[sss][1])
        ss1.append([s1,s2])
    #print(ss1)
    si=len(ss1)

    for _ in range(si):
        if ss1[_][0]==0 and ss1[_][1]==0:
            pass
        elif ss1[_][0]==1 and ss1[_][1]==1:
            pass
        elif ss1[_][0]==1 and ss1[_][1]==0:
            t2=t2[:len_t2-_]+'@'+t2[len_t2-_:]
            len_t2=len_t2+1
        elif ss1[_][0]==0 and ss1[_][1]==1:
            t1=t1[:len_t1-_]+'@'+t1[len_t1-_:]
            len_t1=len_t1+1
    x=list(t1)
    y=list(t2)
    return x,y,cor_len

def tongji(t3,t4):
    if len(t3)!=0 and t3[len(t3)-1]=='\n':t3=t3[:-1]
    if len(t4)!=0 and t4[len(t4)-1]=='\n':t4=t4[:-1]
    x1,x2,x3=bijiao(t3,t4)
    #print(x1)
    #print(x2)
    #识别正确
    ii1=0
    #识别错误
    ii2=0
    #多识别
    ii3=0
    #未能识别
    ii4=0
    #总字数，识别正确率
    zz3=[]
    #分类统计
    #zz4【0】中文
    #zz4[1]英文
    #zz4[2]数字
    #zz4[3]符号
    zz4=[0,0,0,0]
    for _ in range(len(x1)):
        z1=x1[_]
        z2=x2[_]
        if z1==z2:
            #print(z1,'相同')
            ii1=ii1+1
            zz3.append('√')
            if re.match(u'[\u4e00-\u9fa5]',z1):
                zz4[0]=zz4[0]+1
            elif re.match('[a-zA-Z]',z1):
                zz4[1]=zz4[1]+1
            elif re.match('[0-9]',z1):
                zz4[2]=zz4[2]+1
            else:
                zz4[3]=zz4[3]+1
            
        elif z1=="@":
            #print(z2,'多识别')
            ii2=ii2+1
            zz3.append(' ')
        elif z2=='@':
            #print(z1,'未能识别')
            ii3=ii3+1
            zz3.append(' ')
        else:
            #print(z1,z2,'识别错误')
            zz3.append('×')
        
            ii4=ii4+1
    #print('识别正确字数：',ii1,'未能识别字数：',ii3,'识别错误字数：',ii4,'识别正确率：',ii1/x3)
    #print(zz3)
    return ii1/(x3+0.000001),ii1,ii2,ii3,ii4,x1,x2,x3,zz3,zz4
if __name__=='__main__':
    print(tongji('你好a123456.','你好a34565.'))
