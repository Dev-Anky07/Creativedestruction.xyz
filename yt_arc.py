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
    audio.download(r"Archive/Youtube/Songs")
    print("Audio is Downloading as ",yt.title+".mp3")
    
link = "https://www.youtube.com/watch?v=XKD9UxvdbVU"
# create Object ..
yt = YouTube(link)

# call the function
download_Audio(yt)

## This is currently archiving the file in an mp4 format, 

''' 

The path would be like archive/yt/{tag of user}

Tag would act as a unique identifier for a certain user of the code

Name of the archived audio/video file should resemble the unique code identifier (maybe !?)

'''