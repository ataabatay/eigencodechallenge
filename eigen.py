import sys
import pathlib
import string


def main():
  check_file_extensions(sys.argv[1:-1])
  lines = read_files(sys.argv[1:-1])  
  print(count_lines(lines))
  words = find_unique_words(lines)
  interest_level = 100
  print(count_occurences(words, interest_level))
  
  
  
def count_occurences(words, interest_level):
  occurences = {}
  for word in words:
    if word in occurences:
      occurences[word] += 1
    else:
      occurences[word] = 1
  return sorted(occurences.items(), key= lambda word: word[1], reverse=True)[:interest_level]
  
def find_unique_words(lines):
  all_words = []
  punctuation = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '}', '|', '~', '\n', ' -']

  for line in lines:
    # lowercase the entire sentence
    lower_case_line = line['sentence'].lower()
    # remove punctuation ()
    for punc in punctuation:
      if punc in lower_case_line:
        lower_case_line = lower_case_line.replace(punc,'')
    # split the words into a list
    split_words = lower_case_line.split(' ')
    # add the words to all_words list
    all_words.extend(split_words)
  return all_words
      
def count_lines(lines):
  documents_and_line_count = {}
  for line in lines:
    if line['document'] not in documents_and_line_count:
      documents_and_line_count[line['document']] = 1
    else:
      documents_and_line_count[line['document']] += 1
  return documents_and_line_count
  
def read_files(args):
  lines = []
  for filename in args:
    try:
      with open(filename) as file:
        print(f'✅ Good for you {filename} exists!')
        for index, line in enumerate(file):
          lines.append({'sentence': line, 'document': filename, 'index': index})
    except FileNotFoundError:
      sys.exit(f'❌ HEEEJJJJJ {filename} does not exist!')
  return lines

def check_file_extensions(args):
  for file in args:
    if pathlib.Path(file).suffix != '.txt':
      sys.exit(f'❌ HEEEJJJJ {file} is a non .txt file donno what to do with that!')

if __name__ == '__main__':
  main()