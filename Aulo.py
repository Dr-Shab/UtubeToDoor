import subprocess

def start_aulo(name, url, start, end):
    audio_name = name
    if audio_name == "exit":
        exit(0)
    audio_url = url
    audio_start = start
    audio_end = end

    song_loader_p = subprocess.run(['./song_loader.sh', audio_name, audio_url, audio_start, audio_end], stdout=subprocess.PIPE)
    output = song_loader_p.stdout.decode()
    if song_loader_p.returncode == 0:
        print('audio successfully downloaded and cutted with status code:', song_loader_p.returncode)
    elif song_loader_p.returncode == 1:
        print('U wanted some help, u got it!')
        raise Exception(f'Invalid result: {song_loader_p.returncode}')
    else:
        print(f'Download not successfull, Invalid result: {song_loader_p.returncode}')
        raise Exception(f'Invalid result: {song_loader_p.returncode}')

    return output

