#start
# -*- coding: cp936 -*-
import Image,ImageDraw
import ImageFilter,random,sys
img = Image.open("1.jpg")

##图像处理##
#转换为RGB图像
img = img.convert("RGB")              

#经过PIL自带filter处理
imgfilted_b = img.filter(ImageFilter.BLUR)
imgfilted_c = img.filter(ImageFilter.CONTOUR)
imgfilted_ee = img.filter(ImageFilter.EDGE_ENHANCE)
imgfilted_ee_m = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
imgfilted_em = img.filter(ImageFilter.EMBOSS)                    
imgfilted_fe = img.filter(ImageFilter.FIND_EDGES)                                                
imgfilted_sm = img.filter(ImageFilter.SMOOTH)
imgfilted_sm_m = img.filter(ImageFilter.SMOOTH_MORE)
imgfilted_sh = img.filter(ImageFilter.SHARPEN)
imgfilted_d = img.filter(ImageFilter.DETAIL)

##组合使用filter
group_imgfilted = img.filter(ImageFilter.CONTOUR)
group_imgfilted = group_imgfilted.filter(ImageFilter.SMOOTH_MORE)

##图像保存##
imgfilted_b.save("1b.jpg")
imgfilted_c.save("1c.jpg")
imgfilted_ee.save("1ee.jpg")
imgfilted_ee_m.save("1eem.jpg")
imgfilted_em.save("1em.jpg")
imgfilted_fe.save("1fe.jpg")                                
imgfilted_sm.save("1sm.jpg")
imgfilted_sm_m.save("1smm.jpg")
imgfilted_sh.save("1sh.jpg")
imgfilted_d.save("1d.jpg")
group_imgfilted.save("1group.jpg")

##图像显示##
imgfilted_b.show()
imgfilted_c.show()
imgfilted_ee.show()
imgfilted_ee_m.show()
imgfilted_em.show()
imgfilted_fe.show()                                
imgfilted_sm.show()
imgfilted_sm_m.show()
imgfilted_sh.show()
imgfilted_d.show()
group_imgfilted.show()
#end
