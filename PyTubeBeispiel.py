import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=xNfLLx7Nwd0")

print("Titel: ", yt.title)
print("Aufrufe: ", yt.views)
print("Creator: ", yt.author)
