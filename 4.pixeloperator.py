#start

# -*- coding: cp936 -*-

import Image



img = Image.open("1.jpg")



def Img2bin_arr(img, threshold):

    '''

    @将位图流转化为二维二值数组

    @param img: instance of Image

    @param threshold: 大小范围[0, 255]

    '''

    threshold = max(0, threshold)

    threshold = min(255, threshold)

    

    if img.mode != 'L':

        img = img.convert('L')

        

    width, height = img.size

    pix = img.load()

    

    get_val = lambda p: 255 if p >= threshold else 0

        

    return [[get_val(pix[w, h]) for w in xrange(width)] for h in xrange(height)]



def bin_arr2Img(matrix, bg_color, fg_color):

    '''

    @将二维二值数组转化为位图流

    @param img: instance of Image

    @param bg_color: 背景色，元组类型，格式：(L)（灰度）,(R, G, B)，或者(R, G, B, A)

    @param fg_color: 前景色

    '''

    def ensure_color(color):

        if len(color) == 1:

            return (color, color, color, 255)

        elif len(color) == 3:

            color = list(color)

            color.append(255)

            return tuple(color)

        elif len(color) == 4:

            return color

        else:

            raise ValueError, 'len(color) cannot be %d' % len(color)

        

    bg_color = ensure_color(bg_color)

    fg_color = ensure_color(fg_color)

    

    height, width = len(matrix), len(matrix[0])

    dst_img = Image.new("RGBA", (width, height))

    dst_pix = dst_img.load()

    

    for w in xrange(width):

        for h in xrange(height):

            if matrix[h][w] < 128:

                dst_pix[w, h] = fg_color

            else:

                dst_pix[w, h] = bg_color

                

    return dst_img



def paper_cut(img, threshold, bg_color, fg_color):

    '''

    @效果：剪纸

    @param img: instance of Image

    @param threshold: 大小范围[0, 255]

    @param bg_color: 背景色，元组类型，格式：(L)（灰度）,(R, G, B)，或者(R, G, B, A)

    @param fg_color: 前景色

    @return: instance of Image

    '''

    matrix = Img2bin_arr(img, threshold) # 位图转化为二维二值数组

    return bin_arr2Img(matrix, bg_color, fg_color) # 二维二值数组转化为位图



if __name__ == "__main__":

    import sys, os, time



    path = os.path.dirname(__file__) + os.sep.join(['', '1.jpg'])

    threshold = 150

    bg_color = (255, 255, 255, 0)

    fg_color = (255, 0, 0, 255)

    

    if len(sys.argv) >= 2:

        path  = sys.argv[1]

    if len(sys.argv) == 3:

        threshold = int(sys.argv[2])

    if len(sys.argv) == 5:

        bg_color = tuple(sys.argv[3])

        fg_color = tuple(sys.argv[4])



    start = time.time()

    

    img = Image.open(path)

    img = paper_cut(img, threshold, bg_color, fg_color)

    img.save(os.path.splitext(path)[0]+'.papercut_'+str(threshold)+'.png', 'PNG')



    end = time.time()

    print 'It all spends %f seconds time' % (end-start) 



#end
