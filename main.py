from http.client import responses

import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import requests
from cloudinary.api import transformation
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Configurar credenciales de Cloudinary desde .env
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# Obtener el directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Definir las carpetas
input_folder = os.path.join(current_dir, "imagenes")  # Carpeta de imágenes originales
output_folder = os.path.join(current_dir, "imagenes_procesadas")  # Carpeta de imágenes procesadas

# Crear carpetas si no existen
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"Carpeta creada: {input_folder}. Por favor coloca las imágenes ahí y vuelve a ejecutar.")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Carpeta creada: {output_folder}. Aquí se guardarán las imágenes procesadas.")

def process_images():
    # Dimensiones deseadas
    target_width, target_height = 1000, 460

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):  # Filtrar formatos válidos
            input_path = os.path.join(input_folder, filename)
            print(f"Procesando: {filename}")

            try:
                # Subir la imagen a Cloudinary con transformación
                response = cloudinary.uploader.upload(
                    input_path,
                    transformation=[
                        {
                            "width": target_width,
                            "height": target_height,
                            "crop": "fill",  # Recorta y ajusta manteniendo proporciones
                            "gravity": "auto",  # Centra el sujeto automáticamente
                            "quality": "100"  # Mantiene la calidad al 100%
                        }
                    ]
                )

                # Obtener la URL de la imagen procesada
                processed_url = response['secure_url']

                # Descargar y guardar localmente
                output_path = os.path.join(output_folder, filename)
                img_data = requests.get(processed_url).content
                with open(output_path, "wb") as f:
                    f.write(img_data)

                print(f"Guardado exitoso en: {output_path}")

                # Eliminar la imagen de Cloudinary para evitar consumir créditos
                public_id = response['public_id']
                cloudinary.api.delete_resources([public_id])
                print(f"Imagen eliminada de Cloudinary: {public_id}")

            except Exception as e:
                print(f"Error procesando {filename}: {e}")

# Ejecutar el procesamiento
if __name__ == "__main__":
    process_images()
    print("Proceso completado. Revisa la carpeta de imágenes procesadas.")

