from pytube import YouTube

# Asking the link from user:
link = input("Enter the link of youtube video you want to download:   ")
yt = YouTube(link)

# Showing details
print("Title: ", yt.title)
print("Number of videos: ", yt.views)
print("Lenght of videos: ", yt.length)
print("Ratingn of the videos: ",yt.rating)

# Getting the highest resolution possilble:
ys = yt.streams.get_lowest_resolution()

# starting to download:
print("Downloading...")
ys.download("/Users/alibiouki/Downloads/YT")
print("Download completed...")