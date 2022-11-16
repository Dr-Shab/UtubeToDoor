#!/bin/bash

if [ "$1" == "-h" ]; then
  echo -e "Usage: \n
1st variable: name of output file\n
2nd variable: URL - favourably share link\n
3rd variable: start time in seconds\n
4th: end time in seconds\n
example: ./songloader.sh meme_sound https://youtu.be/GPXkjtpGCFI 5 13"
  exit 1
else
  youtube-dl -x --audio-format "mp3" -o "/home/pi/Desktop/door/audio_files/$1_uncutted.%(ext)s" "$2"

  ffmpeg -i /home/pi/Desktop/door/audio_files/$1_uncutted.mp3 -ss $3 -to $4 -c copy $1.mp3

  rm /home/pi/Desktop/door/audio_files/$1_uncutted.mp3

  if [ -e $1.mp3 ]
  then
    exit 0
  else
    exit 2
  fi
fi


