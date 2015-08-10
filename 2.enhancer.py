#start
# -*- coding: cp936 -*-
#阿瓦图像村出品，转载请注明出处
#QQ：576916092
import Image,ImageDraw
import ImageFilter,random,sys
import ImageEnhance
img = Image.open("1.jpg")

##图像处理##

#转换为RGB图像
img = img.convert("RGB")              


#PIL图像增强lambda
imgbri=img.point(lambda i : i*1.4) #对每一个像素点进行增强
imgbri.save("1bri.jpg")
imgbri.show()

#PIL图像增强ImageEnhance
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
