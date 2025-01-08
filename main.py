import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import requests
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

