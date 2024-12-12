from PIL import Image  # pip install pillow
import os

downloads_folder = "C:/Users/WobistduTech/Downloads/"
pictures_folder = "C:/Users/WobistduTech/Pictures/"

def compress_image(source_path, dest_path, quality=60):
    try:
        with Image.open(source_path) as img:
            img.save(dest_path, optimize=True, quality=quality)
            print(f"Image {os.path.basename(source_path)} compressed successfully.")
    except Exception as e:
        print(f"Error compressing {os.path.basename(source_path)}: {e}")

if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(filename)
        
        # Normaliza la extensión a minúsculas para evitar problemas
        extension = extension.lower()
        
        # Verifica si el archivo es una imagen
        if extension in [".jpg", ".jpeg", ".png"]:
            source_path = os.path.join(downloads_folder, filename)
            dest_filename = f"compressed_{filename}"
            dest_path = os.path.join(pictures_folder, dest_filename)
            
            # Comprueba si ya existe un archivo comprimido con el mismo nombre
            if os.path.exists(dest_path):
                dest_path = os.path.join(pictures_folder, f"compressed_{name}_new{extension}")

            # Llama a la función de compresión
            compress_image(source_path, dest_path)

            # Elimina la imagen original
            try:
                os.remove(source_path)
                print(f"Original image {filename} deleted from Downloads.")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
