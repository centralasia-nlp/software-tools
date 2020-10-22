import os
import sys
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import threading

global files
global words
global unique_words
global number_of_sentences

files = 0
words = []
unique_words = set()
number_of_sentences = 0
threads = []

clear = lambda: os.system('clear')

def read_file(filename):
    global files
    global words
    global unique_words
    global number_of_sentences
    f = open(filename, 'r')
    if files % 100 == 0:
        print(f"Files processed: {files}")
    files += 1
    text = f.read()
    if text == "":
        f.close()
        return
    text = text.replace('\n', "")
    words += text.split()
    #unique_words |= set(words)
    number_of_sentences += len(sent_tokenize(text))
    f.close()

def stats(foldername, is_file=False):
    for folder_or_filename in os.listdir(foldername):
        if os.path.isdir(f'{foldername}/{folder_or_filename}'):
            #t = threading.Thread(target=stats, args=(f'{foldername}/{folder_or_filename}', is_file))  # <- note extra ','
            #threads.append(t)
            #t.start()
            stats(f'{foldername}/{folder_or_filename}', is_file)
        elif folder_or_filename.endswith(".txt"):
            read_file(f'{foldername}/{folder_or_filename}')
    
    


if len(sys.argv) < 2:
    print("Please provide the folder name as a command line parameter. Ex: python stats.py ziyonet/")
    quit()
else:
    stats(sys.argv[1])
    print(f"Stats for {sys.argv[1]}:\n")
    print(f"        Number of .txt files: {files}")
    print(f"        Number of words: {len(words)}")
   # print(f"        Number of unique words: {len(unique_words)}")
    print(f"        Number of sentences: {number_of_sentences}")
                

                

            
    
        
