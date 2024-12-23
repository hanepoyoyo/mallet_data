# mallet_data操作手順
**コマンドプロンプトで実行する。その他ターミナルでは動作保証外。**


## インストール
- 任意の場所に`mallet_data`をインストールする。


## 実行
- コマンドプロンプトを開く。
- `mallet_data`に移動(`cd`)する。
- `python main.py`とターミナルに入力し、実行する。


## 説明
### main.py
- メインファイル。

### mallet
- [mallet-2.0.8](https://mallet.cs.umass.edu/download.php)の本体。

### method
- 各処理を記述する。
  - `raw_to_source.py`では、青空文庫からダウンロードしたzipファイルを解凍し、sourceを作成する。(単独で動作する。`method`内で実行すること。)
  - `install_mecab.py`では、mecabに必要なパッケージをインストールする。(初回のみ必要。不必要であれば`main.py`内の呼び出しをコメントアウトすること。)
  - `cleanse_source.py`では、sourceをクレンジングする。
  - `create_corpus.py`では、コーパスを作成する。
  - `create_model.py`では、トピックモデルを作成する。
  - `txt_to_utf-8.py`では、utf-8に直して文字化けを解決する。

### txt_...
- テキストやコーパス、モデル等を格納する。
  - `txt_raw`では、青空文庫にあるzip形式のテキストを格納する。ただしダウンロード不良のため、以下の作品IDを含まない。
    - [535, 3392, 3393, 3394, 3395]
  - `txt_source`では、解凍したShift_JIS形式のテキストを格納する。
  - `txt_cleansed`では、クレンジングしたテキストを格納する。
  - `txt_corpus`では、mecabで処理したテキストとmallet形式のテキストを格納する。
  - `txt_model`では、トピックモデルを格納する。
  - `txt_utf-8`では、utf-8に変換したテキストを格納する。