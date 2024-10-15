import os
import subprocess
import MeCab

def create_corpus(cleansed_dir, corpus_dir):
    # create mecab tokens
    mecab = MeCab.Tagger("-Owakati")
    tokens = []

    for filename in os.listdir(cleansed_dir):
        cleansed_path = os.path.join(cleansed_dir, filename)
        
        if filename.endswith(".txt"):
            # create token
            with open(cleansed_path, 'r', encoding='shift_jis') as f:
                cleansed = f.read()
                token = mecab.parse(cleansed).strip()
                tokens.append(token)

    # output mecab tokens
    token_path = os.path.join(corpus_dir, "tokens.mecab")
    with open(token_path, 'w', encoding='utf-8') as f:
        for token in tokens:
            f.write(token + '\n')


    # create mallet corpus
    corpus_path = os.path.join(corpus_dir, "corpus.mallet")
    mallet_conversion = f'mallet\\bin\\mallet import-file --input "{token_path}" --output "{corpus_path}" --keep-sequence --remove-stopwords'
    subprocess.call(mallet_conversion, shell=True)

    print("コーパスを作成しました。")