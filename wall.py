import numpy as np
np.set_printoptions(threshold=np.inf)
from PIL import Image


class Wall:
    def __init__(self, path):
        self.path = path




    def getValue(self):
        img = Image.open(self.path)
        imgConverted = img.convert('L')
        imgConverted.save('final.jpg','jpeg')
        imgArrayed = np.array(imgConverted)
        out = np.zeros([imgArrayed.shape[0],imgArrayed.shape[1]])
        for i in range(imgArrayed.shape[0]):  # 转化为二值矩阵
            for j in range(imgArrayed.shape[1]):
                if imgArrayed[i][j] == 255:
                    out[i][j] = 0
                if imgArrayed[i][j] == 59:
                    out[i][j] = 0.6
                if imgArrayed[i][j] == 0:
                    out[i][j] = 1
        return out
