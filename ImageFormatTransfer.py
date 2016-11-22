# -*- coding: utf-8 -*-
__author__ = 'oukohou'
__time__ = '2016/11/21 22:40'
# If this runs wrong, don't ask me, I don't know why;
# If this runs right, thank god, and I don't know why.
# Maybe the answer, my friend, is blowing in the wind.

from PIL import Image
import os

# 将原始jpeg图片改为jpg，以避免可能出现的格式读取问题；
def formatTransfer(imgPath):
    for path, subdirs, files in os.walk(imgPath):
        for filename in files:
            current_file = os.path.join(path, filename)
            # 修改输出扩展名为.jpg
            lower4 = os.path.splitext(current_file)[1]
            if lower4 == ".jpg":
                continue
            else :
                outfile = os.path.splitext(current_file)[0] + ".jpg"
                # 捕获异常，以使得异常之后能继续处理：
                try:
                    # 打开原始图像并存入新文件
                    Image.open(current_file).save(outfile)
                    os.remove(current_file)
                except IOError:
                # 错误处理
                # do nothing...
                    continue

if __name__ == "__main__":
    Dir = "I:\kaggle-diabetic/sample/sample"
    formatTransfer(Dir)
