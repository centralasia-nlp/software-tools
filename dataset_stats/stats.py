import os
import sys
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
global files
global words
global unique_words
global number_of_sentences

files = 0
words = []
unique_words = set()
number_of_sentences = 0

def stats(foldername, is_file=False):
    global files
    global words
    global unique_words
    global number_of_sentences
    clear = lambda: os.system('clear')
    for folder_or_filename in os.listdir(foldername):
        if os.path.isdir(f'{foldername}/{folder_or_filename}'):
            stats(f'{foldername}/{folder_or_filename}', is_file)

        elif folder_or_filename.endswith(".txt"):
            with open(f'{foldername}/{folder_or_filename}', 'r') as f:
               
                print(f"Files processed: {files}")
                clear()
                
                files += 1
                text = f.read()
                if text == "":
                    continue
                text = text.replace('\n', "")
                words += text.split()
                unique_words |= set(words)
                number_of_sentences += len(sent_tokenize(text))
        
    
    print(f"Stats for {foldername}:\n")
    print(f"        Number of .txt files: {files}")
    print(f"        Number of words: {len(words)}")
    print(f"        Number of unique words: {len(unique_words)}")
    print(f"        Number of sentences: {number_of_sentences}")


if len(sys.argv) < 2:
    print("Please provide the folder name as a command line parameter. Ex: python stats.py ziyonet/")
    quit()
else:
    stats(sys.argv[1])
                

                

            
    
        
