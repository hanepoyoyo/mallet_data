import os
import zipfile
import shutil

# set dir pass
raw_dir = '..\\txt_raw'
source_dir = '..\\txt_source'
os.makedirs(raw_dir, exist_ok=True)
os.makedirs(source_dir, exist_ok=True)

# unzip zip files
for filename in os.listdir(raw_dir):
    zip_file = os.path.join(raw_dir, filename)

    if filename.endswith('.zip'):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            for file in zip_ref.namelist():
                if file.endswith('.txt'):
                    zip_ref.extract(file, source_dir)

        os.remove(zip_file)

print("解凍が完了しました。")