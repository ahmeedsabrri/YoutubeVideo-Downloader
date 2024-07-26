from pytube import Youtube

if __name__ == "__main__":
    while (1) :
        print("Enter the link of the video you want to download")
        youtubeLink = input()
        ytObject = YouTube(youtubeLink);
        ytObject = ytObject.streams.filter(file_extension='mp4')
        print(ytObject.title)
        try:
            ytObject.download()
        except:
            print("Error")
         