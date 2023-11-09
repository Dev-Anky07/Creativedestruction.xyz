from pytube import YouTube

# Define Function ...
def download_Audio(yt):
    # Filter all the audio files
    my_streams = yt.streams.filter(only_audio=True)
    for streams in my_streams:
        # print audio quality/itag/codec 
        print(f"Audio itag : {streams.itag} Quality : {streams.abr} ACodec : {streams.codecs[0]}")
        

    input_itag = input("Enter itag Value : ")
    audio = yt.streams.get_by_itag(input_itag)
    
    # download the Video inn audio format..
    audio.download() # audio.download(r"New path where you want to save the file")
    print("Audio is Downloading as ",yt.title+".mp3")
    
link = "https://www.youtube.com/watch?v=XKD9UxvdbVU"
# create Object ..
yt = YouTube(link)

# call the function
download_Audio(yt)