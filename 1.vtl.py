import os,shutil
import numpy as np
import cv2
import copy
from skimage import filters
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import matplotlib.pyplot as plt
from numba import jit
def outputImage(imgPath,img):
    if os.path.exists(imgPath):
        os.remove(imgPath)
    cv2.imwrite(imgPath,img)
import math,time

def gamma_trans(img,gamma):  # gamma函数处理
    gamma_table = [np.power(x / 255.0,gamma) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img,gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。

#@jit
def main():
    name0='2022-08-02_38'
    cap = cv2.VideoCapture('H:/'+name0+'.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    cou=cap.get(cv2.CAP_PROP_FRAME_COUNT)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(cou,fps,size,name0)
    #time.sleep(5000)
    i=1
    fnl=[1,2,3,4,5,6,7,8,9,10,11,12][:]
    #fnl=[6]
    show=0
    # dic1 = [[0,480,20,500,0,55,12],[0,480,525,1005,0,55,12],[10,480,1055,1525,0,55,12],[20,500,1550,2030,0,55,12],
    #      [510,990,10,490,0,55,12],[515,995,525,1005,0,55,12],[530,1000,1045,1515,0,55,12],[535,1015,1540,2020,0,55,12],
    #      [1010,1490,10,490,0,55,12],[1025,1515,510,1000,0,55,12],[1035,1515,1030,1510,0,55,12],[1040,1520,1530,2010,0,55,12]]
    dic1 =[[15, 495, 15, 495, 0, 55, 12], [15, 495, 515, 995, 0, 55, 12], [15, 495, 1020, 1500, 0, 55, 12], [15, 495, 1510, 1990, 0, 55, 12], [520, 1000, 15, 495, 0, 55, 12], [520, 1000, 515, 995, 0, 55, 12], [520, 1000, 1020, 1500, 0, 55, 12], [520, 1000, 1510, 1990, 0, 55, 12], [1015, 1495, 15, 495, 0, 55, 12], [1015, 1495, 515, 995, 0, 55, 12], [1015, 1495, 1020, 1500, 0, 55, 12], [1015, 1495, 1510, 1990, 0, 55, 12]]

    dic=dic1.copy()
    for fn in fnl:
        name=name0+'_'+str(fn)
        # if not os.path.exists(name):
        #     os.makedirs(name)
        fly=open(name+'.txt','w')
        fly.write(str(cou)+'\t'+str(fps)+'\t')
        fn=fn-1
        fly.write(str(dic1[fn][0])+':'+str(dic1[fn][1])+'\t'+str(dic1[fn][2])+':'+str(dic1[fn][3])+'\t'+str(dic1[fn][4])+'\t'+str(dic1[fn][5])+'\t'+str(dic1[fn][6])+'\n')
        dic[fn]=fly
    while(True):
        ret,frame0 = cap.read()
        i=i+1
        if i>630000:break
        for fn in fnl:
            pos,y,fn=[],[],fn-1
            if i > dic1[fn][4]:
                frame = cv2.resize(frame0[dic1[fn][0]:dic1[fn][1],dic1[fn][2]:dic1[fn][3],:],(430,430),interpolation=cv2.INTER_CUBIC)
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                if show == 2:
                    plt.imshow(gray,cmap=plt.cm.gray)
                    plt.show()
                mea=np.mean(gray)
                msk = gray>mea*1.05
                gray[msk] = mea*1.02
                if show == 2:
                    print(mea*1.05,gray)
                    plt.imshow(gray,cmap=plt.cm.gray)
                    plt.show()
                thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C ,cv2.THRESH_BINARY_INV,dic1[fn][5],dic1[fn][6]).astype(np.uint8)
                # if show == 2:
                #     plt.imshow(thresh,cmap=plt.cm.gray)
                #     plt.show()
                # thresh = cv2.erode(thresh, (3,3), iterations=3)
                # if show == 2:
                #     plt.imshow(thresh,cmap=plt.cm.gray)
                #     plt.show()
                cnts= cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[1]
                for j,c in enumerate(cnts):
                    rect = cv2.minAreaRect(c)
                    if rect[1][0]>=rect[1][1]:
                        if rect[1][0]<10 or  rect[1][1]<6 :continue
                        if rect[1][0]>50 or  rect[1][1]>26 :continue
                    if rect[1][0]<rect[1][1]:
                        if rect[1][1]<10 or  rect[1][0]<6 :continue
                        if rect[1][1]>50 or  rect[1][0]>26 :continue
                    if math.pow(rect[0][0]-215,2)+math.pow(rect[0][1]-215,2)>46225:continue
                    #print((int(rect[0][0]),int(rect[0][1])))
                    #if int(rect[0][0])>290 and int(rect[0][0])<310 and int(rect[0][1])>156 and int(rect[0][1])<176 and fn+1==7:continue
                    #if int(rect[0][0])>358 and int(rect[0][0])<384 and int(rect[0][1])>293 and int(rect[0][1])<317 and fn==11:continue
                    #if int(rect[0][0]) > 247 and int(rect[0][0]) < 267 and int(rect[0][1]) > 400 and int(rect[0][1]) < 420: continue
                    cv2.circle(frame,(int(rect[0][0]),int(rect[0][1])),2,(0,0,200),-1)
                    y.append([int(rect[0][0]),int(rect[0][1])])
                #cv2.rectangle(frame0,(dic1[fn][2],dic1[fn][0]),(dic1[fn][3],dic1[fn][1]),(0,0,255),2)

                if show>=1:
                    plt.imshow(frame,cmap=plt.cm.gray)
                    plt.show()
                #outputImage(name + '/' + str(i) + '.jpg',frame)
                if y.__len__()<1:
                    nn = y.__len__()
                    if nn != 1: print(nn, i, fn + 1)
                    dic[fn].write('\t'+str(i-dic1[fn][4])+'\t'+str(len(y))+'\n')
                    #fly.flush()
                    #outputImage(name+'/'+str(i)+'.jpg',frame)
                    continue
                arr=np.array(y)
                #print(arr,arr.shape)
                pos=list(arr[np.lexsort(arr[:,::-1].T)])
                nn=pos.__len__()
                if nn!=4:print(nn,i,fn+1)
                #pos=sorted(pos.items(),key=lambda abs:abs[0],reverse=False)
                    #y[j]=int(rect[0][1])
                # end4 = time.time()
                # print('Running time: %s Seconds'%(end4-start))
                for k in pos:
                    dic[fn].write(str(k[0])+','+str(k[1])+'\t')
                dic[fn].write(str(i-dic1[fn][4])+'\t'+str(nn)+'\n')
                dic[fn].flush()
                #end5 = time.time()
                #print('Running time: %s Seconds'%(end5-start))
                    #cv2.putText(frame,str(''),(int(rect[0][0]),int(rect[0][1])),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
                # cv2.imshow("Image",frame)
                # cv2.waitKey(0)
                #outputImage(name+'/'+str(i)+'.jpg',frame)

            # When everything done,release the capture
            #cap.release()
            #cv2.destroyAllWindows()
def unevenLightCompensate(gray,blockSize):

    average = np.mean(gray)

    rows_new = int(np.ceil(gray.shape[0] / blockSize))
    cols_new = int(np.ceil(gray.shape[1] / blockSize))

    blockImage = np.zeros((rows_new,cols_new),dtype=np.float32)
    for r in range(rows_new):
        for c in range(cols_new):
            rowmin = r * blockSize
            rowmax = (r + 1) * blockSize
            if (rowmax > gray.shape[0]):
                rowmax = gray.shape[0]
            colmin = c * blockSize
            colmax = (c + 1) * blockSize
            if (colmax > gray.shape[1]):
                colmax = gray.shape[1]

            imageROI = gray[rowmin:rowmax,colmin:colmax]
            temaver = np.mean(imageROI)
            blockImage[r,c] = temaver

    blockImage = blockImage - average
    blockImage2 = cv2.resize(blockImage,(gray.shape[1],gray.shape[0]),interpolation=cv2.INTER_CUBIC)
    gray2 = gray.astype(np.float32)
    dst = gray2 - blockImage2
    dst = dst.astype(np.uint8)
    dst = cv2.GaussianBlur(dst,(3,3),0)
    return dst


if __name__ == "__main__":
    # execute main
    main()
