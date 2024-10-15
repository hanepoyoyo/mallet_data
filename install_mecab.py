import subprocess

def install_mecab():
    subprocess.call("pip install mecab-python3", shell=True)
    subprocess.call("pip install unidic-lite", shell=True)