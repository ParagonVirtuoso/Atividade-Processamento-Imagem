import cv2
import numpy as np
from matplotlib import pyplot as plt
ddepth = cv2.CV_16UC3
kernel_size = 3

img = cv2.imread('atividade8.jpg',0)

topoE = (456, 380)
baixoD = (535, 410)
x, y = topoE[0], topoE[1]
w, h = baixoD[0] - topoE[0], baixoD[1] - topoE[1]

# Recorte para aplicar o filtro
GB = img[y:y+h, x:x+w]
largura = GB.shape[1]
altura = GB.shape[0]
proporcao = float(altura/largura)
largura_nova = 240 #em pixels
altura_nova = int(largura_nova*proporcao)
17
tamanho_novo = (largura_nova, altura_nova)
img_redimensionada = cv2.resize(GB,
tamanho_novo, interpolation = cv2.INTER_AREA)

(alt, lar) = img_redimensionada.shape[:2] #captura altura e largura
centro = (lar // 2, alt // 2) #acha o centro
M = cv2.getRotationMatrix2D(centro, 3, 1.0) #30 graus
img_rotacionada = cv2.warpAffine(img_redimensionada, M, (lar, alt))

gau = cv2.GaussianBlur(img_redimensionada, (7, 7), 0)
canny1 = cv2.Canny(gau, 20, 120)
resultado = np.uint8(np.absolute(canny1))

ret, thresh1 = cv2.threshold(resultado,120, 255, cv2.THRESH_BINARY_INV)

largura_nova = 720 #em pixels
altura_nova = int(largura_nova*proporcao)
17
tamanho_novo = (largura_nova, altura_nova)
final = cv2.resize(thresh1,
tamanho_novo, interpolation = cv2.INTER_AREA)

cv2.imshow("Imagem Equalizada", final)
cv2.imwrite("imagem_final.jpg", final)
plt.show()
cv2.waitKey(0)


