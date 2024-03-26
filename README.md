# Eigen Code Challenge

## Description
- Eigen code challenge was a code challenge I completed as part of prepping for technical interviews,
- This was solo project and I spent a total of roughly 10-15 hours on completing the challenge using Python, 
- The challenge was to find the most frequent interesting words in one or multiple text files along with outputting a summary table.

## Getting Started / Installation
- Access the source code via the 'Clone or download' button,
- Once the directory is pulled, navigate into it, you will see the eigen.py file and the text_files folder where sample text files were created
'''
python eigen.py <inputfilename> <inputfilename> <outputfilename>
'''
Example
'''
python eigen.py text_files/doc1.txt text_files/doc2.txt text_files/doc3.txt output.csv
'''

## Plan notes
- 


## Build notes
- Set up the environment on github,
- Created the check_clas (command line arguments) function to:
  - check the command line arguments provided to ensure input files end with .txt
  - check user input at least 1 input file
- Created read_files function to:
  - check all the input files exist
  - read all the lines into a lines variable to later utilise
- Created fetch_all_words function to:
  - remove all punctuation from each line and split lines into separate words
- Create count_occurences function to:
  - count how many times each word has been used in all the files provided
- Introduced mostcommonwords.txt and fetch_most_common_words functions to:
  - fetch all the most commonly used words in English (later on I added some words that I felt was missing from this list)
- Created filter_common_words function to:
  - remove the common words we found with fetch_all_words to get rid of uninteresting words (i.e 'to', 'as', 'I')
- Created find_and_add_parent_docs_and_samples function to:
  - add which documents each words was found in and sample sentences were each most popular interesting word was in
- Created create_output_file function to:
  - write the output .csv file with the data we have prepared 
- Wrote unit tests for each function
