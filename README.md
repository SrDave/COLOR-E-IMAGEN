## R-Red, G-Green, B-Blue

## Modelo aditivo en el que se combinan RGB

colores para formar a su vez una gran
variedad de colores.

### Podemos diferenciar:

– Intensidad: promedio de luz -> (R+G+B)/3

– Color: resultante de la proporción relativa de R, G y B.

Estos se suelen expresar en un rango de [0-255] (8-bits). 

Ejemplos:
- Gris -> R=G=B (color gris)
- Negro -> R=G=B=0 (gris, mínima intensidad)
 Blanco -> R=G=B=255 (gris, máxima
intensidad)
- Color que tiende a rojizo -> R>G, R>B

## Tema:

– Edición de imágenes (fotos) RGB con Python

 ## Objetivos:
 
– Experimentar con el modelo RGB

– Profundizar en métodos de procesado de imágenes con Python

## Tarea:

– Convertir una foto en color en una escala de grises pero
manteniendo los elementos rojos y azules propios de la
imagen orignal

## Pasos:

– Escoger una imagen en formato jpeg

– Leer las tres bandas con Python y representarlas (RGB y 3 colores por
separados en escala de grises). 

– Generar una máscara de rojo y de azul 

– Generar imagen de escala de grises (imagen de intensidad)

– Restituir los colores rojo y azul de la imagen original mediante las máscaras
sobre la imagen en escala de grises
