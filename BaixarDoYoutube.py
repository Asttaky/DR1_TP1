#pip install moviepy
#pip install yt_dlp
import yt_dlp
from moviepy.editor import *
import os

def download_youtube_video(video_url, output_path='./'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(video_url, download=True)
            video_title = info_dict.get('title', None)
            video_ext = info_dict.get('ext', None)
            video_filename = f"{output_path}/{video_title}.{video_ext}"
            
            print("Download concluído!")
            
            # Após o download, converter para MP3
            convert_to_mp3(video_filename, output_path)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def convert_to_mp3(video_filename, output_path):
    try:
        video = VideoFileClip(video_filename)
        audio_filename = os.path.join(output_path, os.path.splitext(os.path.basename(video_filename))[0] + ".mp3")
        video.audio.write_audiofile(audio_filename, codec='mp3')
        print(f"Áudio extraído e salvo como {audio_filename}")
    except Exception as e:
        print(f"Ocorreu um erro durante a conversão: {e}")

if __name__ == "__main__":
    video_url = input("Digite a URL do vídeo do YouTube: ")
    output_path = input("Digite o diretório para salvar o vídeo (deixe em branco para o diretório atual): ") or './'
    download_youtube_video(video_url, output_path)
