from flask import Flask, render_template, redirect, request
from Aulo import start_aulo
import os

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def letsgo():
    if request.method == "POST":
       songname = request.form.get("songname")
       sharelink = request.form.get("sharelink")
       starttime = request.form.get("starttime")
       endtime = request.form.get("endtime")

       try:
           length = int(endtime) - int(starttime)
       except:
           length = "u bloody bastard"

       output = start_aulo(songname, sharelink, starttime, endtime)

       return render_template("aulo_running.html", length=length, url=sharelink, songname=songname, output=output)

    return render_template("index.html")

@app.route("/audiofiles")
def show_files():
    path = os.getcwd()+"/home/pi/Desktop/door/audio_files"

    list_of_files = ""
    for filename in os.listdir(path):
        list_of_files += filename + " <br> "
    return render_template("files.html", value=list_of_files)

@app.route("/manual")
def show_manual():
    return render_template("manual.html")

@app.route("/restart")
def restart_door():
    command = "just restarted door script, see the output:"
    output = "output of script"
    result = command + "<br>" + output
    return render_template("restart.html", value= result)

@app.route("/surprise")
def surprise():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)


app.run(host="0.0.0.0", port=5123, debug=True)
