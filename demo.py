import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
d = os.path.dirname(__file__)  # 根目录
font = os.path.join(d, "msyhl.ttc")
text = open("遥远的救世主.txt", "r", encoding='utf-8', errors="ignore").read()
text = text.replace("芮小丹说", "芮小丹")
text = text.replace("芮小丹问", "芮小丹")
text = text.replace("丁元英说", "丁元英")
text = text.replace("丁元英问", "丁元英")
text = text.replace("肖亚文说", "肖亚文")
text = text.replace("韩楚风说", "韩楚风")
text = text.replace("刘冰说", "刘冰")
text = text.replace("欧阳雪说", "欧阳雪")
text = text.replace("冯世杰说", "冯世杰")
text = text.replace("叶晓明说", "叶晓明")


# 下面两种都可以读取图片 因为图片本质上就是一个二维数组
# mask = np.array(Image.open(os.path.join(d,'timg.jpg')))
mask = imread(os.path.join(d, 'timg.jpg')) # 设置背景图片

# 生成我们的一个word云印象
# max_font_size=40 设置最大字体是40
# random_state=2 配色方案
# mask=mask 图片关联
# stopwords 屏蔽某些词
wc = WordCloud(font_path=font, max_words=200, mask=mask, stopwords=STOPWORDS.add("强奸"), background_color='green')
wc.generate(text) # generate（）根据我们的文本生成词云
image_colors = ImageColorGenerator(mask) # 从背景图片生成颜色值
plt.imshow(wc.recolor(color_func=image_colors)) # 显示我们生成图片 根据背景颜色设置词云文字颜色
# plt.imshow() # 显示我们生成图片
plt.axis("off")
plt.show() # 生成可视化图片
wc.to_file("text2.png")



# """
# wordcloud的所有参数
#
# font_path : string //字体路径，需要展现什么字体就把该字体路径+后缀名写上，如：font_path = '黑体.ttf'
# width : int (default=400) //输出的画布宽度，默认为400像素
# height : int (default=200) //输出的画布高度，默认为200像素
# prefer_horizontal : float (default=0.90) //词语水平方向排版出现的频率，默认 0.9 （所以词语垂直方向排版出现频率为 0.1 ）
# mask : nd-array or None (default=None) //如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将被忽略，遮罩形状被 mask 取代。除全白（#FFFFFF）的部分将不会绘制，其余部分会用于绘制词云。如：bg_pic = imread('读取一张图片.png')，背景图片的画布一定要设置为白色（#FFFFFF），然后显示的形状为不是白色的其他颜色。可以用ps工具将自己要显示的形状复制到一个纯白色的画布上再保存，就ok了。
# scale : float (default=1) //按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍。
# min_font_size : int (default=4) //显示的最小的字体大小
# font_step : int (default=1) //字体步长，如果步长大于1，会加快运算但是可能导致结果出现较大的误差。
# max_words : number (default=200) //要显示的词的最大个数
# stopwords : set of strings or None //设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS
# background_color : color value (default=”black”) //背景颜色，如background_color='white',背景颜色为白色。
# max_font_size : int or None (default=None) //显示的最大的字体大小
# mode : string (default=”RGB”) //当参数为“RGBA”并且background_color不为空时，背景为透明。
# relative_scaling : float (default=.5) //词频和字体大小的关联性
# color_func : callable, default=None //生成新颜色的函数，如果为空，则使用 self.color_func
# regexp : string or None (optional) //使用正则表达式分隔输入的文本
# collocations : bool, default=True //是否包括两个词的搭配
# colormap : string or matplotlib colormap, default=”viridis” //给每个单词随机分配颜色，若指定color_func，则忽略该方法。
# fit_words(frequencies)  //根据词频生成词云
# generate(text)  //根据文本生成词云
# generate_from_frequencies(frequencies[, ...])   //根据词频生成词云
# generate_from_text(text)    //根据文本生成词云
# process_text(text)  //将长文本分词并去除屏蔽词（此处指英语，中文分词还是需要自己用别的库先行实现，使用上面的 fit_words(frequencies) ）
# recolor([random_state, color_func, colormap])   //对现有输出重新着色。重新上色会比重新生成整个词云快很多。
# to_array()  //转化为 numpy array
# to_file(filename)   //输出到文件
#
# """


"""
worldcloud 生成词云有两种方式
文本 频率
"""

"""
mode RGBA
color_func 生成新颜色的函数
regexp 使用正则表达式
collocation 是否两个词是否匹配
recolor([random_state,color_func,colormap])
to_array() 装换numpy_array
to_file(filename)

"""