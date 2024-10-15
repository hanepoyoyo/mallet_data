import os
import subprocess

# set pass
root_dir = "C:\\Users\\tsuba\\mallet_data\\"
corpus_dir = root_dir + "corpus"
model_dir = root_dir + "model"
os.makedirs(corpus_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

# create topic model
corpus_path = os.path.join(corpus_dir, "corpus.mallet")
state_path = os.path.join(model_dir, "state.gz")
keys_path = os.path.join(model_dir, "keys.txt")
topics_path = os.path.join(model_dir, "topics.txt")

mallet_modeling = f'mallet train-topics --input "{corpus_path}" --num-topics 10 --output-state "{state_path}" --output-topic-keys "{keys_path}" --output-doc-topics "{topics_path}"'
subprocess.call(mallet_modeling, shell=True)

print("トピックモデルを作成しました。")