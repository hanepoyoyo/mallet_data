# mallet_data操作手順
## インストール
- 任意の場所に`mallet_data`をインストールする。

## 実行
- コマンドプロンプトを開く。
- `mallet_data`を置いた場所に移動(`cd`)する。
- `python main.py`とターミナルに入力し、実行する。

## 説明
### main.py
- メインファイル。

### method
- 各処理を記述する。
  - `install_mecab.py`では、mecabに必要なパッケージをインストールする。
  - `create_corpus.py`では、コーパスを作成する。
  - `create_model.py`では、トピックモデルを作成する。


### txt_...
- テキストやコーパス、モデル等を格納する。
  - `txt_source`では、青空文庫にあるShift_JIS形式のテキストを格納する。
  - `txt_corpus`では、mecabで処理したテキストとmallet形式のテキストを格納する。
  - `txt_model`では、トピックモデルを格納する。