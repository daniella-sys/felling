from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Завантаження завершено!")
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    video_url = input("Введіть URL відео з YouTube: ")
    download_video(video_url)

