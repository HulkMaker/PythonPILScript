# -*- coding: cp936 -*-
#����ͼ����Ʒ��ת����ע������ QQ��576916092
import Image,ImageDraw,ImageFilter,random,sys
im1 = Image.open("1.jpg")
 
##ͼ����##
 
#ת��ΪRGBͼ��
im1_sp = im1.convert("RGB")              

#��RGB����ͨ���ֿ�
r,g,b=im1_sp.split()             
 
#��RGB��ͨ��ͼ����ɫ
imd = Image.new("L",im1.size,0)
r_color= Image.merge("RGB",(r,imd,imd))
g_color= Image.merge("RGB",(imd,g,imd))
b_color= Image.merge("RGB",(imd,imd,b))
 
#Rͨ��histogram
width, height = r.size
pix = r.load()
a = [0]*256
for w in xrange(width):
    for h in xrange(height):
        p = pix[w,h]
        a[p] = a[p] + 1
s = max(a)
print a,len(a),s     #����256,a����ķֱ�����ɫ��Χ0-255���ֵĴ���
r_hist = Image.new('RGB',(512,512),(255,255,255))  
draw = ImageDraw.Draw(r_hist)  
 
for k in range(256):
   #print k,a[k],a[k]*200/s
    a[k] = a[k]*400/s        #ӳ�䷶Χ0-200
    source = (2*k,511)           #�������y=255, x=[0,1,2....]
    target = (2*k,511-a[k])    #�յ�����y=255-a[x],a[x]�������ֵ��200,x=[0,1,2....]
    draw.line([source, target], (255,0,0))
 
#Gͨ��histogram
width, height = g.size
pix = g.load()
a = [0]*256
for w in xrange(width):
    for h in xrange(height):
        p = pix[w,h]
        a[p] = a[p] + 1
s = max(a)
print a,len(a),s     #����256,a����ķֱ�����ɫ��Χ0-255���ֵĴ���
g_hist = Image.new('RGB',(512,512),(255,255,255))  
draw = ImageDraw.Draw(g_hist)  

for k in range(256):
    #print k,a[k],a[k]*200/s
    a[k] = a[k]*400/s        #ӳ�䷶Χ0-200
    source = (2*k,511)           #�������y=255, x=[0,1,2....]
    target = (2*k,511-a[k])    #�յ�����y=255-a[x],a[x]�������ֵ��200,x=[0,1,2....]
    draw.line([source, target], (0,255,0))

#Bͨ��histogram
width, height = b.size
pix = b.load()
a = [0]*256
for w in xrange(width):
    for h in xrange(height):
        p = pix[w,h]
        a[p] = a[p] + 1
s = max(a)
print a,len(a),s     #����256,a����ķֱ�����ɫ��Χ0-255���ֵĴ���
b_hist = Image.new('RGB',(512,512),(255,255,255))  
draw = ImageDraw.Draw(b_hist)  

for k in range(256):
    #print k,a[k],a[k]*200/s
    a[k] = a[k]*400/s        #ӳ�䷶Χ0-200
    source = (2*k,511)           #�������y=255, x=[0,1,2....]
    target = (2*k,511-a[k])    #�յ�����y=255-a[x],a[x]�������ֵ��200,x=[0,1,2....]
    draw.line([source, target], (0,0,255))

im1_mer= Image.merge("RGB",(r,g,b))

##ͼ�񱣴�##

#��ͨ��ͼ����
r.save("1r.jpg")
g.save("1g.jpg")
b.save("1b.jpg")

#��ɫͼ����
r_color.save("1rr.jpg")
g_color.save("1gg.jpg")
b_color.save("1bb.jpg")

#ֱ��ͼ����
r_hist.save("1r_hist.jpg")
g_hist.save("1g_hist.jpg")
b_hist.save("1b_hist.jpg")

##ͼ����ʾ##

#��ͨ��ͼ��ʾ
r.show()
g.show()
b.show()
 
#��ɫͼ��ʾ
r_color.show()
g_color.show()
b_color.show()

#ֱ��ͼ��ʾ
r_hist.show()
g_hist.show()
b_hist.show()
