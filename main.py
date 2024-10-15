import os
import subprocess

from method import install_mecab
from method import cleanse_source
from method import create_corpus
from method import create_model

# set mallet home
mallet_home = os.path.join(os.getcwd(), 'mallet')
os.environ['MALLET_HOME'] = mallet_home

# set dir pass
source_dir = 'txt_source'
cleansed_dir = 'txt_cleansed'
corpus_dir = 'txt_corpus'
model_dir = 'txt_model'
os.makedirs(source_dir, exist_ok=True)
os.makedirs(cleansed_dir, exist_ok=True)
os.makedirs(corpus_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

# set console encoding
os.system('chcp 65001')
subprocess.call('cls', shell=True)

# please comment out if you don't need install mecab
# install_mecab.install_mecab()

cleanse_source.cleanse_source(source_dir, cleansed_dir)
create_corpus.create_corpus(cleansed_dir, corpus_dir)
create_model.create_model(corpus_dir, model_dir)