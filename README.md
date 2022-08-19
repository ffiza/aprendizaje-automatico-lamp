<div align="center">
    <h1>Aprendizaje automático:
    Fundamentos y aplicaciones en meterología del espacio</h1>
</div>

Scripts y notebooks de Python desarrollados para el curso
"Aprendizaje automático: Fundamentos y aplicaciones en meterología del espacio",
dictado en agosto de 2022 en la Facultad de Ciencias Exactas y Naturales
de la Universidad de Buenos Aires.

Más información puede encontrarse en el [repositorio de la materia](https://github.com/Laboratorio-Computacion-Cientifica/TSWC-Aprendizaje-Automatico-Fundamentos-y-Aplicaciones-en-Meteorologia-del-Espacio).

* Coordinador: Dr. Sergio Dasso
* Docentes: Dra. María Graciela Molina, Lic. Jorge H. Namour

## Descripción

- ```code/utils/plot.py```: Este archivo contiene los parámetros de
configuración de los gráficos y una función que puede ejecutarse donde se
necesite que aplica la configuración.
- ```data/```: Contiene los archivos de datos usados en el curso (en
diversos formatos).
- ```docs/```: Contiene las clases y los enunciados de los trabajos.
- ```images/```: Contiene figuras producidas para cada trabajo.

### Trabajo práctico 0

El trabajo práctico 0 contiene análisis sencillos relacionados con el
entrenamiento de un modelo lineal; esto puede encontrarse en el notebook
```code/tp0.ipynb```.

### Trabajo práctico 1

El primer trabajo práctico consiste en la clasificación de señales de radar
(parte 1) y de eyecciones de masa coronal (CMEs, parte 2) haciendo uso de una red
neuronal (ANN). El código de la primera parte está contenido en el notebok
```code/tp1_radar.ipynb``` con la configuración en
```code/tp1_radar_settings.py```. La segunda parte está en el notebook 
```code/t1_cmes.ipynb``` con la configración en ```code/tp1_cmes_settings.py```.