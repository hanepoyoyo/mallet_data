import re
import os


# remove header
def remove_header(source):
    removed = source.split('-------------------------------------------------------', 2)[-1]
    removed = removed.strip()
    
    return removed


# remove footer
def remove_footer(source):
    patterns = ['［＃本文終わり］', '底本：']
    
    # find footer position
    footer_position = len(source)
    for pattern in patterns:
        match = re.search(pattern, source)
        if match:
            footer_position = min(footer_position, match.start())
    removed = source[:footer_position].strip()
    
    return removed


# remove bracketed text
def remove_bracketed_text(source):
    removed = re.sub(r'［＃.*?］', '', source)
    removed = removed.strip()
    
    return removed


# cleanse source files
def cleanse_source(source_dir, cleansed_dir):
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        cleansed_path = os.path.join(cleansed_dir, filename)
        
        if filename.endswith(".txt"):
            # cleanse source file
            with open(source_path, 'r', encoding='shift_jis') as f:
                source = f.read()

                removed_header = remove_header(source)
                removed_footer = remove_footer(removed_header)
                cleansed = remove_bracketed_text(removed_footer)
            
            # output source file
            with open(cleansed_path, 'w', encoding='shift_jis') as f:
                f.write(cleansed)