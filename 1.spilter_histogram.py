# -*- coding: cp936 -*-
#阿瓦图像村出品，转载请注明出处 QQ：576916092
import Image,ImageDraw,ImageFilter,random,sys
im1 = Image.open("1.jpg")
 
##图像处理##
 
#转换为RGB图像
im1_sp = im1.convert("RGB")              

#将RGB三个通道分开
r,g,b=im1_sp.split()             
 
#将RGB分通道图像上色
imd = Image.new("L",im1.size,0)
r_color= Image.merge("RGB",(r,imd,imd))
g_color= Image.merge("RGB",(imd,g,imd))
b_color= Image.merge("RGB",(imd,imd,b))
 
#R通道histogram
width, height = r.size
pix = r.load()
a = [0]*256
for w in xrange(width):
    for h in xrange(height):
        p = pix[w,h]
        a[p] = a[p] + 1
s = max(a)
print a,len(a),s     #长度256,a保存的分别是颜色范围0-255出现的次数
r_hist = Image.new('RGB',(512,512),(255,255,255))  
draw = ImageDraw.Draw(r_hist)  
 
for k in range(256):
   #print k,a[k],a[k]*200/s
    a[k] = a[k]*400/s        #映射范围0-200
    source = (2*k,511)           #起点坐标y=255, x=[0,1,2....]
    target = (2*k,511-a[k])    #终点坐标y=255-a[x],a[x]的最大数值是200,x=[0,1,2....]
    draw.line([source, target], (255,0,0))
 
#G通道histogram
width, height = g.size
pix = g.load()
a = [0]*256
for w in xrange(width):
    for h in xrange(height):
        p = pix[w,h]
        a[p] = a[p] + 1
s = max(a)
print a,len(a),s     #长度256,a保存的分别是颜色范围0-255出现的次数
g_hist = Image.new('RGB',(512,512),(255,255,255))  
draw = ImageDraw.Draw(g_hist)  

for k in range(256):
    #print k,a[k],a[k]*200/s
    a[k] = a[k]*400/s        #映射范围0-200
    source = (2*k,511)           #起点坐标y=255, x=[0,1,2....]
    target = (2*k,511-a[k])    #终点坐标y=255-a[x],a[x]的最大数值是200,x=[0,1,2....]
    draw.line([source, target], (0,255,0))

#B通道histogram
width, height = b.size
pix = b.load()
a = [0]*256
for w in xrange(width):
    for h in xrange(height):
        p = pix[w,h]
        a[p] = a[p] + 1
s = max(a)
print a,len(a),s     #长度256,a保存的分别是颜色范围0-255出现的次数
b_hist = Image.new('RGB',(512,512),(255,255,255))  
draw = ImageDraw.Draw(b_hist)  

for k in range(256):
    #print k,a[k],a[k]*200/s
    a[k] = a[k]*400/s        #映射范围0-200
    source = (2*k,511)           #起点坐标y=255, x=[0,1,2....]
    target = (2*k,511-a[k])    #终点坐标y=255-a[x],a[x]的最大数值是200,x=[0,1,2....]
    draw.line([source, target], (0,0,255))

im1_mer= Image.merge("RGB",(r,g,b))

##图像保存##

#单通道图保存
r.save("1r.jpg")
g.save("1g.jpg")
b.save("1b.jpg")

#上色图保存
r_color.save("1rr.jpg")
g_color.save("1gg.jpg")
b_color.save("1bb.jpg")

#直方图保存
r_hist.save("1r_hist.jpg")
g_hist.save("1g_hist.jpg")
b_hist.save("1b_hist.jpg")

##图像显示##

#单通道图显示
r.show()
g.show()
b.show()
 
#上色图显示
r_color.show()
g_color.show()
b_color.show()

#直方图显示
r_hist.show()
g_hist.show()
b_hist.show()
