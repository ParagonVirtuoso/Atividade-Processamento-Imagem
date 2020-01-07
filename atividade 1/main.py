import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('ImageQuestion3.jpg')
img = cv2.flip(img,1)
col = len(img[0])
lin = len(img)

#gabriel barbosa
topoE = (270, 385)
baixoD = (320, 450)
x, y = topoE[0], topoE[1]
w, h = baixoD[0] - topoE[0], baixoD[1] - topoE[1]

# Recorte para aplicar o filtro
GB = img[y:y+h, x:x+w]

#aplicando o filtro
recorteGB = cv2.GaussianBlur(GB, (51,51), 0)

#mesclando a imagem original novamente
img[y:y+h, x:x+w] = recorteGB

#Éverton Ribeiro
topoE = (370, 410)
baixoD = (425, 480)
x, y = topoE[0], topoE[1]
w, h = baixoD[0] - topoE[0], baixoD[1] - topoE[1]

# Recorte para aplicar o filtro
ER = img[y:y+h, x:x+w]

#aplicando o filtro
recorteER = cv2.GaussianBlur(ER, (51,51), 0)

#mesclando a imagem original novamente
img[y:y+h, x:x+w] = recorteER

##################

#converte para escala de cinza para equalizar
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalizar a imagem em somente uma escala
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# converte a imagem novamente para colorido mesclando
img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

##################
#apos a equalização a imagem piorou pois ficou muito clara, ainda mais nas faixas onde acabou com algus pontos brancos
#preferivel sem a equalização, mais ainda quando esta colorido!
##################

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')


cv2.imshow("Imagem Equalizada",img)
plt.show()
cv2.waitKey(0)


