import os
import subprocess

def create_model(corpus_dir, model_dir):
    # create topic model
    corpus_path = os.path.join(corpus_dir, "corpus.mallet")
    state_path = os.path.join(model_dir, "state.gz")
    keys_path = os.path.join(model_dir, "keys.txt")
    topics_path = os.path.join(model_dir, "topics.txt")

    mallet_modeling = f'mallet\\bin\\mallet train-topics --input "{corpus_path}" --num-topics 20 --num-top-words 50 --output-state "{state_path}" --output-topic-keys "{keys_path}" --output-doc-topics "{topics_path}" --optimize-interval 20'
    subprocess.call(mallet_modeling, shell=True)

    print("トピックモデルを作成しました。")