#start
# -*- coding: cp936 -*-
#����ͼ����Ʒ��ת����ע������
#QQ��576916092
import Image,ImageDraw
import ImageFilter,random,sys
import ImageEnhance
img = Image.open("1.jpg")

##ͼ����##

#ת��ΪRGBͼ��
img = img.convert("RGB")              


#PILͼ����ǿlambda
imgbri=img.point(lambda i : i*1.4) #��ÿһ�����ص������ǿ
imgbri.save("1bri.jpg")
imgbri.show()

#PILͼ����ǿImageEnhance
istep=4
irange=4.0

imgenhancer_Color=ImageEnhance.Color(img)
for i in range(istep):
        factor=i/irange
        img_enhance_color=imgenhancer_Color.enhance(factor)
        img_enhance_color.show("Color %f" %factor)
        img_enhance_color.save("Color_%.2f.jpg" %factor) 
        
imgenhancer_Brightness=ImageEnhance.Brightness(img)
for i in range(istep):
        factor=i/irange
        img_enhance_Brightness=imgenhancer_Brightness.enhance(factor)
        img_enhance_Brightness.show("Brightness %f" %factor)
        img_enhance_Brightness.save("Brightness_%.2f.jpg" %factor) 
        
imgenhancer_Contrast=ImageEnhance.Contrast(img)
for i in range(istep):
        factor=i/irange
        img_enhance_Contrast=imgenhancer_Contrast.enhance(factor)
        img_enhance_Contrast.show("Contrast %f" %factor)
        img_enhance_Contrast.save("Contrast_%.2f.jpg" %factor) 
        
imgenhancer_Sharpness=ImageEnhance.Sharpness(img)
for i in range(istep):
        factor=i/irange
        img_enhance_Sharpness=imgenhancer_Sharpness.enhance(factor)
        img_enhance_Sharpness.show("Sharpness %f" %factor)
        img_enhance_Sharpness.save("Sharpness_%.2f.jpg" %factor) 
#end
