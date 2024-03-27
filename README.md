# Eigen Code Challenge

## Description
- Eigen code challenge was a code challenge I completed as part of prepping for technical interviews,
- This was solo project and I spent a total of roughly 10-15 hours on completing the challenge using Python, 
- The challenge was to find the most frequent interesting words in one or multiple text files along with outputting a summary table.

## Getting Started / Installation
- Access the source code via the 'Clone or download' button,
- Once the directory is pulled, navigate into it, you will see the eigen.py file and the text_files folder where sample text files were created

```python
python eigen.py <inputfilename> <inputfilename> <outputfilename>
```

### Example
```python
python eigen.py text_files/doc1.txt text_files/doc2.txt text_files/doc3.txt output.csv
```

## Plan notes
- Upon reading the task, an immediate decision felt like it had to be made about the output. 
  - I was in between 2 options: tabulating the answer or create a csv file as an output. I entertained the idea of tabulating the answer in the terminal which I thought was a fun idea but in the end decided to go with creating a csv file as an output with the deliverables.
- One thing I noticed was the vague notion of 'most frequent **interesting** words'. This naturally tingled my spidey senses so I took note of this and moved on knowing that the most frequent words were most likely going to be common words (i.e 'I', 'to', 'as', etc.).
- Next thing to think about was how the program should be designed. Should the program just be designed so that it only runs for the given text files and create an output or should it be dynamic enough to accept as many or as little text files that the user passes.
  - I decided to go with designing the program so that it takes command line arguments in the form of text file names so that the user can pass as many or as little filenames to be analysed.
- Once these decisions were made, I proceded following the build notes below.

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
