in='3l-c-case-j10'

ffmpeg -i snap%05d.png ${in}.mp4
#ffmpeg -i ${in}.mp4 -filter:v "setpts=PTS/4" ${in}.fast.mp4
ffmpeg -i ${in}.mp4 ${in}.gif 
