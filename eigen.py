import sys
import csv
import pathlib

def main():
    # check to see all the command line arguments are valid
    check_clas(sys.argv[1:-1])
    # try to read the input files into a lines variable
    lines = read_files(sys.argv[1:-1])
    # how many words you'd like to see in the csv output
    interest_level = 30
    # how many example sentence you'd like to see in the csv output for each word
    number_of_samples = 1
    # all the common words in English
    common_words = fetch_most_common_words()
    # all the words found in the files
    all_words = fetch_all_words(lines)
    # all the interesting words found in the files after filtering the common words out
    all_interesting_words = filter_common_words(all_words, common_words)
    # finding the number of occurences for each word
    interesting_unique_words_and_their_count = count_occurences(all_interesting_words, interest_level)
    # finding inside which documents and sentences we find the unique and interesting words
    final_output_list = find_and_add_parent_docs_and_samples(interesting_unique_words_and_their_count, lines, number_of_samples)
    # create the output csv file and write final output into it with the words, occurences, documents and samples
    create_output_file(sys.argv[len(sys.argv) - 1] ,final_output_list)
    
def create_output_file(filename: str, data: list):
  '''
  Take a filename and data and writes the data into a csv output file
  '''
  try:
    with open(filename, 'w') as file:
      fieldnames = ['word', 'occurence', 'documents', 'samples']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      for word in data:
        writer.writerow({'word': word['word'], 'occurence': word['occurence'], 'documents': word['documents'], 'samples': word['samples']})
  except FileExistsError:
    sys.exit('Output file already exists, overwriting not possible')

def find_and_add_parent_docs_and_samples(words: dict, lines: list, number_of_samples: int) -> list:
  '''
  Takes a list of word dicts, lines read from the input file and the number of sample sentences you'd like to see and returns a list of all the words, their occurences, the documents they're found in and sample senteces they were found in
  '''
  doc_and_sample_added_words = []
  for word in words:
    doc_list = []
    sample_list = []
    for line in lines:
      if word in line['sentence']:
        doc_list.append(line['document'])
        sample_list.append(line['sentence'])
    doc_and_sample_added_words.append({'word': word, 'occurence': words[word], 'documents': list(set(doc_list)), 'samples': sample_list[:number_of_samples]})
  return doc_and_sample_added_words


def filter_common_words(words: dict, common_words: list) -> list:
    '''
    Takes a list of words and iterates through them one by one checking if they are found in the common_words list or not, returns all the non-common words in a list
    '''
    interesting_unique_words = []
    for word in words:
      if word not in common_words:
        interesting_unique_words.append(word)
    return interesting_unique_words


def fetch_most_common_words() -> list:
    '''
    Opens the mostcommonwords.txt file, reads all the words and returns them in a list
    '''
    common_words = []
    try:
      with open('mostcommonwords.txt') as file:
        common_words = file.read().splitlines()
        for i, word in enumerate(common_words):
          common_words[i] = word.lower()
      return common_words
    except FileNotFoundError:
      sys.exit('Cannot find the file for most common words.')

def count_occurences(words: list, interest_level: int) -> dict:
    '''
    Takes a list of words and how many words you would like the output to be and returns a dictionary of unique words and their count in the provided list
    '''
    occurences = {}
    for word in words:
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1
    return dict(sorted(occurences.items(), key=lambda word: word[1], reverse=True)[:interest_level])



def fetch_all_words(lines: list) -> list:
    '''
    Accepts a list of lines read from a file cleans the list and returns a list of all the words
    '''
    all_words = []
    punctuation = ["!",'"',"#","$","%","&","(",")","*","+",",",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","{","}","|","~","\n"," -",]
    for line in lines:
        # remove punctuation ()
        for punc in punctuation:
            if punc in line['sentence']:
                line['sentence'] = line['sentence'].replace(punc, "")
        # split the words into a list
        split_words = line['sentence'].split(" ")
        # add the words to all_words list
        all_words.extend(split_words)
    return all_words



def read_files(filenames: list) -> list:
    '''
    Takes a list of files, tries to open and read the files and if it can, returns a list of all the lines read   
    '''
    lines = []
    for filename in filenames:
        try:
            with open(filename) as file:
                print(f"✅ Good for you {filename} exists!")
                for index, line in enumerate(file):
                    lines.append(
                        {"sentence": line.lower(), "document": filename, "index": index}
                    )
        except FileNotFoundError:
            sys.exit(f"❌ HEEEJJJJJ {filename} does not exist!")
    return lines


def check_clas(args: list):
    '''
    Takes in a list of command line arguments and checks if the input files end with .txt and checks if there are at least one input and one output file
    '''
    for file in args:
        if pathlib.Path(file).suffix != ".txt":
            sys.exit(
                f"❌ HEEEJJJJ {file} is a non .txt file donno what to do with that!"
            )
    if len(args) < 1:
      sys.exit('Usage: eigen.py input.txt input2.txt ... output.csv')      

if __name__ == "__main__":
    main()