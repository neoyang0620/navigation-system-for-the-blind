import json
import os
import cv2

data_path = '/Users/apple/darkflow/ZED1/left/4selecting/json' #原始json文件位置
img_path = '/Users/apple/darkflow/ZED1/depth' #对应原始图片位置

jsonlabels =os.listdir(data_path) #读取json列表
jsonlabels = filter(lambda x: x.endswith('json'), jsonlabels)#文件夹里筛选出json文件
img_output = img_path + '/' + 'output'
#os.mkdir(img_path + '/outputs')

for jsonlabel in jsonlabels:#循环处理每一个json
    print(jsonlabel)
    file_name, _ = jsonlabel.split('.') #删除‘.’之后的信息，只保留名字
    f = open(data_path + '/' + jsonlabel,'r')  #读取json文件
    setting = json.load(f)
    length = len(setting)#每一个json中列表长度，有几个目标
    count = 0
    deletenum = 0
    print(length)
    img = cv2.imread(img_path + '/' + file_name + '.png')#读取原始图片
    h, w, _ = img.shape #获得原始图片的宽与高
    thick = int((h + w) // 300)#用h与w来定义框和字体的粗细
    while (count < length):#处理每一个目标
        label = setting[deletenum]['label'] #5个数据读出来
        distance = setting[deletenum]['testpoint']['distance']
        distance = float(distance)
        if ( label == 'car') and (distance < 6.0) and (distance > 0.0):#根据类别信息选择筛选条件
            xmin = setting[deletenum]['topleft'] ['x']
            ymax = setting[deletenum]['topleft'] ['y']
            xmax = setting[deletenum]['bottomright'] ['x']
            ymin = setting[deletenum]['bottomright'] ['y']
          
            print (label,xmax,xmin,ymax,ymin,distance)
            cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255),thick) #画框
            cv2.line(img,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(255,0,0),thick//3)#对角线
            cv2.line(img,(int(xmin),int(ymax)),(int(xmax),int(ymin)),(255,0,0),thick//3)#对角线
            cv2.putText(img, label+str(distance), (int(xmin), int(ymax)-12), 0, 1e-3 * h , (0, 0, 255),thick//3) #文字1，1分别是字体字号
            deletenum+=1
        else:
            del setting[deletenum]
        count += 1
    cv2.imwrite(img_path + '/outputs_selecting/'+file_name +'.png',img)#输出



'''
f = open(data_path + '/' + 'WechatIMG123.json')  #读取json文件
setting = json.load(f)
length = len(setting)
count = 0
print(length)
img = cv2.imread(img_path + '/' + 'WechatIMG123' + '.jpeg')
while (count < length):
    label = setting[count]['label'] #5个数据读出来
    xmin = setting[count]['topleft'] ['x']
    ymax = setting[count]['topleft'] ['y']
    xmax = setting[count]['bottomright'] ['x']
    ymin = setting[count]['bottomright'] ['y']
    print (label,xmax,xmin,ymax,ymin)
    cv2.rectangle(img, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255),10) #画框
    cv2.putText(img, label, (int(xmin), int(ymax)-10), 1,5 , (0, 0, 255),10) #文字1，1分别是字体字号
    count+=1
cv2.imwrite('output.jpg',img)#输出
'''





