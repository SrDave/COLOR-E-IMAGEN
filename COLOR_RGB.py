import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen y convertirla a formato de punto flotante
img = plt.imread("imagen_practica.JPG")
img2 = img.astype(np.float32)

# Separar los canales de color
rojo = img2[:,:,0]
verde = img2[:,:,1]
azul = img2[:,:,2]

# Crear una imagen en escala de grises sumando los canales de color
im_gris = rojo + verde + azul

# Mostrar la imagen original y los canales de color individuales
plt.figure(figsize=(8,8))  # Cambiar tamaño de figura para mejor visualización
plt.subplot(2,2,1)
plt.title("Imagen original")
plt.imshow(img)
plt.subplot(2,2,2)
plt.title("Rojo")
plt.imshow(rojo, cmap="gray")
plt.subplot(2,2,3)
plt.title("Verde")
plt.imshow(verde, cmap="gray")
plt.subplot(2,2,4)
plt.title("Azul")
plt.imshow(azul, cmap="gray")

# Definir los umbrales para cada canal de color
umbral_rojo = 100
umbral_verde = 50
umbral_azul = 25

# Crear máscaras para cada color basado en las diferencias entre los canales
img_dif_rojo = rojo - verde - azul
masc_rojo = img_dif_rojo > umbral_rojo

img_dif_verde = verde - azul - rojo
masc_verde = img_dif_verde > umbral_verde

img_dif_azul = azul - rojo - verde
masc_azul = img_dif_azul > umbral_azul

# Crear una imagen en escala de grises a partir de los canales de color
I_I = (rojo + verde + azul) / 3
II = (I_I * 255 / np.max(I_I)).astype(np.uint8)

# Inicializar las nuevas imágenes R, G, B a partir de la imagen en escala de grises
R = II.copy()
G = II.copy()
B = II.copy()

# Aplicar la máscara para reemplazar los valores en las imágenes R, G y B
R[masc_rojo] = rojo[masc_rojo]
G[masc_rojo] = verde[masc_rojo]
B[masc_rojo] = azul[masc_rojo]

# Reemplazar los valores en las imágenes R, G y B para los píxeles donde la máscara verde es verdadera
# (Estas líneas están comentadas porque solo se procesan los píxeles rojos en este ejemplo)
# R[masc_verde] = rojo[masc_verde]
# G[masc_verde] = verde[masc_verde]
# B[masc_verde] = azul[masc_verde]

# Reemplazar los valores en las imágenes R, G y B para los píxeles donde la máscara azul es verdadera
R[masc_azul] = rojo[masc_azul]
G[masc_azul] = verde[masc_azul]
B[masc_azul] = azul[masc_azul]

# Crear y mostrar la nueva imagen combinando los canales R, G y B modificados
nueva = np.stack([R, G, B], axis=2)
plt.figure()
plt.imshow(nueva)
plt.title("Imagen Procesada")
plt.show()
