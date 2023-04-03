import matplotlib.pyplot as plt
import os
def distance(xy1,xy0):

    x1,y1=float(xy1.split(',')[0]),float(xy1.split(',')[1])
    x0,y0=float(xy0.split(',')[0]),float(xy0.split(',')[1])
    return (x1-x0)*(x1-x0)+(y1-y0)*(y1-y0)
#计算两点之间的距离
def buff_count(file_name):
    with open(file_name, 'rb') as f:
        count = 0
        buf_size = 1024 * 1024
        buf = f.read(buf_size)
        while buf:
            count += buf.count(b'\n')
            #b" "前缀表示：后面字符串是bytes 类型。
            buf = f.read(buf_size)
        return count


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)

dd = open('not satisfied.name','w')

dicn={}
fl=os.listdir()
##这里应该加地址吧
namedic= {}
for n in fl:
    if not n.endswith('.txt') :continue
    if 'o' in n:continue
    size1=0
    #if '20210730' not in n: continue
    ##筛选出需要处理的文件
    print(n)
    if n[:-4]+'-order.txt' in fl:
        ##如果把名字里多加了-order(也就是目标文件),且size很大，就跳过
        size1 = get_FileSize(n[:-4]+'-order.txt')
        if size1 > 12: continue

    fls = open(n, 'r').readlines()
    dicn[n] = fls[1].rstrip().split('\t')[-1]
    # if int(dicn[n]) != 5:
    #     dd.write(n + '\t' + dicn[n] + '\n')
    if '_'.join(n.split('_')[:-1])+'_' in namedic:
        namedic['_'.join(n.split('_')[:-1])+'_'] = namedic['_'.join(n.split('_')[:-1])+'_']+[n.split('_')[-1][:-4]]
    else:
        namedic['_'.join(n.split('_')[:-1])+'_'] = [n.split('_')[-1][:-4]]
    #就是_前的名字为键，其后的标号是键对应的值
    #if namedic.__len__()>20:break
print(namedic.__len__(),namedic)
print(dicn)
dd.write('\n'+'\n'+'\n'+"dicn:")
for i in dicn:
    dd.write(i+'\t'+dicn[i]+'\n')
dd.close()
for name2 in namedic:
  for nn in namedic[name2]:
    name = name2+str(nn)
    f = open(name+'.txt','r')
    w = open(name+'-order.txt','w')
    #开始读文件和生成新文件
    l0 = f.readline()
    print(nn,name, l0)
    dth = (490/float(l0.split('\t')[1]))*(490/float(l0.split('\t')[1]))
    ##7.196599276143151
    ##68.08771493285145的平方=4635.936924777243
    w.write(l0)
    l = f.readline().rstrip()
    sp0 = l.split('\t')[:-2]
    ##sp0是第二排所示坐标的列表
    w.write('\t'.join(sp0+l.split('\t')[-2:])+'\n')
    #写下第二行信息
    for l1 in f:
        l1 = l1.rstrip()
        sp1 = l1.split('\t')[:-2]
        sp3 = [0 for n in range(len(sp0))]
        for i0,xy0 in enumerate(sp0):
            dis0 = dth
            for i1,xy1 in enumerate(sp1):
                if xy1=='':continue
                if xy1 in sp3:continue
                dis = distance(xy1,xy0)
                #print(dis,dis0,xy0,xy1,i0,i1,l1.split('\t')[-2:])
                if dis<dis0 and dis<dth:
                    dis0=dis
                    sp3[i0]=xy1
            if sp3[i0]==0:sp3[i0]=xy0
        #print(sp3+l1.split('\t')[-2:])
        w.write('\t'.join(sp3+l1.split('\t')[-2:])+'\n')
        sp0 = sp3
