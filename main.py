import os
import subprocess

import install_mecab
import create_corpus
import create_model

# set mallet home
mallet_home = os.path.join(os.getcwd(), 'mallet')
os.environ['MALLET_HOME'] = mallet_home

# set dir pass
source_dir = 'source'
corpus_dir = 'corpus'
model_dir = 'model'
os.makedirs(source_dir, exist_ok=True)
os.makedirs(corpus_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

# set console encoding
os.system('chcp 65001')
subprocess.call('cls', shell=True)

# please comment out if you don't need install mecab
# install_mecab.install_mecab()

create_corpus.create_corpus(source_dir, corpus_dir)
create_model.create_model(corpus_dir, model_dir)