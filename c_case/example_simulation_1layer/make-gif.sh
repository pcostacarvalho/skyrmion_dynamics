in='j01-p1-teste'

#ffmpeg -i snap%05d.png ${in}.mp4
#ffmpeg -i ${in}.mp4 -filter:v "setpts=PTS/4" ${in}.fast.mp4
ffmpeg -i ${in}.fast.mp4 ${in}.gif 
