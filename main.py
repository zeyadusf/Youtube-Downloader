from pytube import YouTube
from pytube import Playlist

print("\n-------------------- Wellcome -------------\n")
vorl=int(input(" 1- Download Videos.\n 2- Download Playlist.\n >> "))

def finish():
    print("\t\t\tDownload Done\n")
print("---------------------------------------------------------------")

if vorl==1 :
    link = input(" Enter the video URL : ")
    video =YouTube(link)

    print("---------------------------------------------------------------")
    print(f">> video title :\n   {video.title}")
    print(f">> video duration : {int(video.length/60)} minutes or more. \n----------------------------------------------------")

    res=int(input(" Please Choose :\n 1- Higher Resolution .\n 2- Lower Resolution.\n >>  "))

    if res==1:
        path=input("Enter Video Path : ")
        print("Please wait a moment , Loading... ")
        video.streams.get_highest_resolution().download(output_path=path)
    else:
        path=input("Enter Video Path : ")
        print("Please wait a moment , Loading... ")
        video.streams.get_lowest_resolution().download(output_path=path)
    video.register_on_complete_callback(finish())


else:
    playlist_link=input(" Enter playlist URL : ")
    list= Playlist(playlist_link)
    path=input("Enter Video Path : ")
    print("Please wait a moment , Loading... ")
    for i in list.videos:
        i.streams.get_lowest_resolution().download(output_path=path)
        i.register_on_complete_callback(finish())

print("\n -------------------- By:Zeyad Elsayed Usf -------------------")
