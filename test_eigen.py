from eigen import check_clas, read_files, fetch_all_words, count_occurences, fetch_most_common_words, filter_common_words, find_and_add_parent_docs_and_samples, create_output_file
import pytest
import csv

# ! Testing check_clas
def test_valid_clas():
  assert check_clas(['text_files/doc1.txt', 'text_files/doc2.txt', 'text_files/doc3.txt' ,'text_files/doc4.txt']) == True
  
def test_no_clas():
  with pytest.raises(SystemExit):
    check_clas([])
    
def test_invalid_clas():
  with pytest.raises(SystemExit):
    check_clas(['text_files/doc3.csv'])
    check_clas(['text_files/doc3.doc'])
    check_clas(['text_files/doc3.pdf'])
    
    
# ! Testing read_files
def test_read_files_nonexistent_file():
    # Test reading a nonexistent file
    with pytest.raises(SystemExit) as exc_info:
        read_files(["nonexistent_file.txt"])
    assert "does not exist" in str(exc_info.value)
    

@pytest.fixture
def create_files(tmp_path):
    # Create temporary files with content for testing
    file_contents = [
        "This is a test sentence.\n",
        "Another test sentence.\n",
        "Yet another test sentence.\n"
    ]
    file_paths = []
    for i, content in enumerate(file_contents):
        file_path = tmp_path / f"test_file_{i}.txt"
        file_path.write_text(content)
        file_paths.append(str(file_path))
    return file_paths

# Test cases
def test_read_files_existing_files(create_files):
    # Test reading existing files
    filenames = create_files
    lines = read_files(filenames)
    assert len(lines) == 3  # Assuming each file has one line
    for line in lines:
        assert isinstance(line, dict)
        assert "sentence" in line
        assert "document" in line
        assert "index" in line
    
# ! Testing fetch_all_words
@pytest.fixture
def create_lines():
  return [{'sentence': "let me begin by saying thanks to all you who've traveled, from far and wide, to brave the cold today.\n", 'document': 'text_files/doc1.txt', 'index': 0}]
  
def test_fetch_all_words(create_lines):
  # Get lines created by fixture
  lines = create_lines

  # Call the function to get the result
  all_words = fetch_all_words(lines)

  # Define the expected words after processing
  expected_words = ['let', 'me', 'begin', 'by', 'saying', 'thanks', 'to', 'all', 'you', "who've", 'traveled', 'from', 'far', 'and', 'wide', 'to', 'brave', 'the', 'cold', 'today']
  
  assert all_words == expected_words

# ! Testing count_occurences
@pytest.fixture
def create_words():
  return [
    "apple", "apple", "apple", "apple", "apple", "apple", "apple", "apple", "apple", "apple",
    "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana",
    "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange",
    "grape", "grape", "grape", "grape", "grape", "grape", "grape", "grape",
    "kiwi", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi", "kiwi",
    "mango", "mango", "mango", "mango", "mango", "mango",
    "pineapple", "pineapple", "pineapple", "pineapple", "pineapple", "pineapple",
    "watermelon", "watermelon", "watermelon", "watermelon", "watermelon", "watermelon",
    "strawberry", "strawberry", "strawberry", "strawberry",
    "blueberry", "blueberry", "blueberry", "blueberry",
    "raspberry", "raspberry", "raspberry", "raspberry",
    "blackberry", "blackberry", "blackberry",
    "cherry", "cherry", "cherry",
    "peach", "peach", "peach",
    "pear", "pear", "pear",
    "plum",
    "apricot",
    "fig",
    "papaya",
    "coconut"
]
  
def test_count_occurences(create_words):
  words = create_words
  interest_level = 5
  occurences = count_occurences(words, interest_level)
  expected_outcome = {
    "apple": 10,
    "banana": 10,
    "orange": 8,
    "grape": 8,
    "kiwi": 8
    }
  assert occurences == expected_outcome
  
# ! Testing fetch_most_common_words
@pytest.fixture
def create_common_words_file(tmp_path):
    file_path = tmp_path / "mostcommonwords.txt"
    words = ["apple", "banana", "orange", "grape", "kiwi"]
    with open(file_path, "w") as file:
        file.write("\n".join(words))
    return str(file_path)
    
def test_fetch_most_common_words_exists(create_common_words_file):
  common_words_file = create_common_words_file
  common_words = []
  with open(common_words_file) as file:
    common_words = file.read().splitlines()
  expected_words = ["apple", "banana", "orange", "grape", "kiwi"]
  assert common_words == expected_words
  
# ! Testing filter_common_words
@pytest.fixture
def all_words_examples():
  return [
    "apple",
    "orange", 
    "grape", 
    "kiwi",
    "mango",
    "pineapple",
    "watermelon", 
    "strawberry", 
    "blueberry",
    "raspberry", 
    "blackberry",
    "cherry", 
    "peach", 
    "pear",
    "plum",
    "apricot",
    "fig",
    "papaya",
    "coconut"
]
  
@pytest.fixture
def common_words_examples():
  return [
    "apple",
    "orange", 
    "grape", 
    "kiwi",
    "mango",
]

def test_filtering_correctly(all_words_examples, common_words_examples):
  all_words = all_words_examples
  common_words = common_words_examples
  
  assert filter_common_words(all_words, common_words) == [
    "pineapple",
    "watermelon", 
    "strawberry", 
    "blueberry",
    "raspberry", 
    "blackberry",
    "cherry", 
    "peach", 
    "pear",
    "plum",
    "apricot",
    "fig",
    "papaya",
    "coconut"
]
  
# ! Testing find_and_add_parent_docs_and_samples
# Fixture to create sample lines
@pytest.fixture
def create_lines_v2():
    return [
        {'sentence': "let me begin by saying thanks to all you who've traveled, from far and wide, to brave the cold today.", 'document': 'text_files/doc1.txt', 'index': 0},
        {'sentence': "we all made this journey for a reason. it's humbling, but in my heart i know you didn't come here just for me, you came here because you believe in what this country can be.", 'document': 'text_files/doc2.txt', 'index': 0},
        {'sentence': "in the face of war, you believe there can be peace. in the face of despair, you believe there can be hope. in the face of a politics that's shut you out, that's told you to settle, that's divided us for too long, you believe we can be one people, reaching for what's possible, building that more perfect union.", 'document': 'text_files/doc1.txt', 'index': 1},
        {'sentence': "that's the journey we're on today. but let me tell you how i came to be here. as most of you know, i am not a native of this great state. i moved to illinois over two decades ago. i was a young man then, just a year out of college; i knew no one in chicago, was without money or family connections. but a group of churches had offered me a job as a community organizer for $13,000 a year. and i accepted the job, sight unseen, motivated then by a single, simple, powerful idea - that i might play a small part in building a better america.", 'document': 'text_files/doc2.txt', 'index': 1}
    ]

# Test case: Words are found in sentences
def test_find_and_add_parent_docs_and_samples_words_found(create_lines_v2):
    words = {"thanks": 1, "brave": 1, "peace": 1}
    lines = create_lines_v2
    number_of_samples = 2
    result = find_and_add_parent_docs_and_samples(words, lines, number_of_samples)
    assert len(result) == 3  # 3 words
    assert result[0]['word'] == "thanks"
    assert result[0]['occurence'] == 1
    assert result[0]['documents'] == ['text_files/doc1.txt']
    assert len(result[0]['samples']) == 1  # 1 sample sentence
    assert result[1]['word'] == "brave"
    assert result[1]['occurence'] == 1
    assert result[1]['documents'] == ['text_files/doc1.txt']
    assert len(result[1]['samples']) == 1  # 1 sample sentence
    assert result[2]['word'] == "peace"
    assert result[2]['occurence'] == 1
    assert result[2]['documents'] == ['text_files/doc1.txt']
    assert len(result[2]['samples']) == 1  # 1 sample sentence

# Test case: Words are not found in any sentence
def test_find_and_add_parent_docs_and_samples_words_not_found(create_lines):
    words = {"banana": 1, "watermelon": 1}
    lines = create_lines
    number_of_samples = 2
    result = find_and_add_parent_docs_and_samples(words, lines, number_of_samples)
    assert len(result) == 2  # 2 words
    assert result[0]['word'] == "banana"
    assert result[0]['occurence'] == 1
    assert result[0]['documents'] == []
    assert result[0]['samples'] == []
    assert result[1]['word'] == "watermelon"
    assert result[1]['occurence'] == 1
    assert result[1]['documents'] == []
    assert result[1]['samples'] == []

# ! Testing create_output_file
# Test case: Successful creation of output file
def test_create_output_file_success(tmp_path):
    # Define test data
    data = [
        {'word': 'apple', 'occurence': 10, 'documents': ['doc1', 'doc2'], 'samples': ['sample1', 'sample2']},
        {'word': 'banana', 'occurence': 8, 'documents': ['doc1'], 'samples': ['sample3']},
        {'word': 'orange', 'occurence': 6, 'documents': ['doc2'], 'samples': ['sample4']}
    ]
    # Define output file path
    output_file = tmp_path / "output.csv"
    # Call the function to create the output file
    create_output_file(output_file, data)
    # Assert if the output file has been created
    assert output_file.is_file()