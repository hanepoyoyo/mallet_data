import os
import subprocess
import MeCab

# if you install mecab, please uncomment.
'''
subprocess.call("pip install mecab-python3", shell=True)
subprocess.call("pip install unidic-lite", shell=True)
'''


# set pass
root_dir = "C:\\Users\\tsuba\\mallet_data\\"
source_dir = root_dir + "source"
corpus_dir = root_dir + "corpus"
os.makedirs(source_dir, exist_ok=True)
os.makedirs(corpus_dir, exist_ok=True)


# create mecab tokens
mecab = MeCab.Tagger("-Owakati")
tokens = []

for filename in os.listdir(source_dir):
    source_path = os.path.join(source_dir, filename)
    
    if filename.endswith(".txt"):
        # create token
        with open(source_path, 'r', encoding='shift_jis') as f:
            source = f.read()
            token = mecab.parse(source).strip()
            tokens.append(token)

# output mecab tokens
token_path = os.path.join(corpus_dir, "tokens.mecab")
with open(token_path, 'w', encoding='utf-8') as f:
    for token in tokens:
        f.write(token + '\n')


# create mallet corpus
corpus_path = os.path.join(corpus_dir, "corpus.mallet")
mallet_conversion = f'mallet import-file --input "{token_path}" --output "{corpus_path}" --keep-sequence --remove-stopwords'
subprocess.call(mallet_conversion, shell=True)

print("コーパスを作成しました。")