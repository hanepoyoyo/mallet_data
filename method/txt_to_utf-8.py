import os

source_dir = '..\\txt_cleansed'
utf_8_dir = '..\\txt_utf-8'
os.makedirs(utf_8_dir, exist_ok=True)

# cleanse source files
def cleanse_source(source_dir, utf_8_dir):
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        utf_8_path = os.path.join(utf_8_dir, filename)
        
        if filename.endswith(".txt"):
            # cleanse source file
            with open(source_path, 'r', encoding='shift_jis') as f:
                source = f.read()
            
            # output source file
            with open(utf_8_path, 'w', encoding='utf-8') as f:
                f.write(source)


cleanse_source(source_dir, utf_8_dir)