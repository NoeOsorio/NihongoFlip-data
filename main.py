from firebase import db
from tqdm import tqdm
import json

# Abre el archivo JSON para leerlo
with open('datos.json', 'r') as archivo:
    data = json.load(archivo)
# Obtener datos

nombre_leccion = input("Introduzca el nombre de la lección: ")
# Subir documento a la colección "lessons"
print("Buscando documento en la base de datos...")
doc_ref = db.collection("lessons").document(nombre_leccion)
if (doc_ref.get().exists):
    print("La lección ya existe en la base de datos")
else:
    # Solicitar nombre de la lección
    title = input("Introduzca el titulo de la lección: ")
    level = input("Introduzca el nivel de la lección: ")
    # Datos únicos para el documento
    documento = {
        "language": "japones",
        "lesson": nombre_leccion,
        "level": level,
        "title": title
    }
    doc_ref.set(documento)


# Subcolección para términos
subcoleccion_ref = doc_ref.collection("vocabulary")
# Subir términos sin repetir atributos
with tqdm(total=len(data)) as pbar:
    for item in data:
        termino = {
            "frontTitle": item[0],
            "frontSubtitle": item[1],
            "backTitle": item[2],
            "example": item[3],
            "category": item[4],
            "exampleTranslation": item[5]
        }
        subcoleccion_ref.add(termino)
        pbar.update(1)

# Contar el número de términos en la subcolección "vocabulary"
numero_de_terminos = len(list(subcoleccion_ref.list_documents()))

# Actualizar el documento de la lección con el número de términos
doc_ref.update({"cardNumber": numero_de_terminos})
print("¡Datos subidos a Firebase exitosamente!")
