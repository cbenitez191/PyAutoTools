from pytube import YouTube

def download_video_in_mp4(url, output_path="downloads"):
    try:
        # Crear instancia de YouTube con la URL del video
        yt = YouTube(url)
        
        # Seleccionar el stream de video en MP4 de la mejor calidad
        video_stream = yt.streams.filter(file_extension="mp4", progressive=True).get_highest_resolution()
        
        # Descargar el video
        print("Descargando video en MP4...")
        video_stream.download(output_path)
        
        print(f"Descarga completada. Archivo guardado en {output_path}")
    except Exception as e:
        print(f"Error al descargar: {e}")

# Uso
youtube_url = "https://www.youtube.com/watch?v=VIDEO_ID"
download_video_in_mp4(youtube_url)
