<div align="center">

# Gestor de Lecciones de Idiomas con Firebase 📚

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)

Una herramienta de Python para subir y organizar lecciones de idiomas en Firebase Firestore, facilitando la gestión eficiente del vocabulario y el seguimiento de los términos por lección.

</div>

## 🚀 Descripción

Esta herramienta de Python permite a los educadores y gestores de contenido cargar lecciones de idiomas a Firebase Firestore de manera estructurada y automática. Integra funciones para la creación de lecciones y la subida de términos de vocabulario, así como para el conteo y la actualización automática del número de términos en cada lección.

## 🌟 Características Principales

- **Gestión Automatizada de Lecciones**: Creación de documentos de lecciones en Firestore con detalles como el nombre, nivel y título de la lección.
- **Subida de Vocabulario**: Carga de términos de vocabulario a subcolecciones específicas de Firestore con soporte para múltiples atributos, como traducciones y ejemplos.
- **Conteo Automático de Términos**: Conteo del número de términos de vocabulario por lección y actualización automática del documento de la lección con este dato.

## 💻 Tecnologías Utilizadas

- Python
- Firebase Firestore
- TQDM para barras de progreso

## 📚 Retos y Soluciones

- **Integración con Firebase**: Configurar la autenticación y conexión con Firebase desde Python.
- **Optimización de la Subida de Datos**: Manejo eficiente de la subida de grandes volúmenes de términos de vocabulario a Firebase, utilizando barras de progreso para mejorar la experiencia del usuario.

## 🛠 Ejemplo de Ejecución

Para utilizar esta herramienta, sigue estos pasos:

1. Prepara tu archivo `datos.json` con el vocabulario a cargar, siguiendo el formato:
```json
[
  ["FrontTitle1", "FrontSubtitle1", "BackTitle1", "Example1", "Category1", "ExampleTranslation1"],
  ["FrontTitle2", "FrontSubtitle2", "BackTitle2", "Example2", "Category2", "ExampleTranslation2"],
  ["ここ", "", "aquí", "ここにすわってください。", "Pronombre de lugar", "Por favor, siéntate aquí."],
]
```

2. Ejecuta el script en tu terminal o consola de comandos.

3. Ingresa el nombre, título y nivel de la lección cuando se soliciten.

La herramienta automáticamente verificará si la lección ya existe, creará el documento de la lección si es necesario, subirá los términos de vocabulario y actualizará el número de tarjetas en la lección.

## ⚙️ Configuración del Proyecto

Para configurar y ejecutar este proyecto en tu entorno de desarrollo, necesitarás Python y acceso a un proyecto Firebase. Sigue estos pasos:

1. Clona el repositorio.
2. Instala las dependencias necesarias, como `firebase-admin` y `tqdm`, usando `pip install firebase-admin tqdm`.
3. Configura tu autenticación de Firebase en tu entorno de desarrollo, siguiendo la documentación de Firebase para Python. Esto debe de estar en `firebase/cred.json`
4. Asegúrate de tener un archivo `datos.json` válido con los términos de vocabulario que deseas subir.
5. Ejecuta el script con `python main.py`.

## 🤝 Contribuir

Si estás interesado en contribuir a este proyecto o tienes sugerencias para mejorarlo, por favor, siente libre de abrir un issue o una pull request en GitHub.

## 📝 Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).