# Optimized Jaccard Similarity Algorithm
import time  # To measure the execution time of the algorithm

def optimized_jaccard_similarity(text1, text2):
    
    # Tokenize the texts and convert to lowercase for case insensitivity
    words1 = text1.lower().split()  
    words2 = text2.lower().split()

    # Use dictionaries to count occurrences of each word in both texts
    word_count1 = {}  # Dictionary for word counts in text1
    word_count2 = {}  # Dictionary for word counts in text2

    # Appends only unique words of text1 into word_count1 {}
    for word in words1:                  
        if word not in word_count1:
            # Word has not been appended yet, so append it
            word_count1[word] = None

    # Appends only unique words of text2 into word_count2 {}
    for word in words2:                  
        if word not in word_count2:
            # Word has not been appended yet, so append it
            word_count2[word] = None

    # Initialize intersection and union sizes
    intersection_count = 0  # To store the number of common words between both texts
    union_count = len(word_count1) + len(word_count2)  # Initialize union with sum of unique words from both texts

    # Calculate the intersection then calculating union
    for word in word_count1:  # Loop through words in text1's word counts
        if word in word_count2:  # If word is common between both texts
            intersection_count += 1  # Increase intersection count

    # Uinion count is (sum of unique words from both texts) - intersection_count    
    union_count -= intersection_count 

    # Handle case where both sets are empty, preventing division by zero
    if union_count == 0:  
        return 0.0
    
    # Calculate and return the Jaccard similarity
    return intersection_count / union_count  

# Function to read text from a file
def read_file(file_path):  
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Testing function for Jaccard similarity on different sample sizes
def testJaccard(address1, address2, type):
    text_a = read_file(address1)  # Read text from the first file
    text_b = read_file(address2)  # Read text from the second file
    start_time = time.time()  # Record the start time of the algorithm execution
    similarity_optimized = optimized_jaccard_similarity(text_a, text_b) * 100  # Calculate similarity percentage
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate execution time
    # Output similarity percentage and execution time
    print(f"Optimized Jaccard Similarity for {type} samples: %{similarity_optimized:.2f}")
    print(f"Execution Time : {execution_time:.4f} seconds")

# The path_address variable should contain the full path to the folder where the text files are stored.
# If the script is in the same folder as the text files, you can leave it empty (path_address = "").
# Example of setting the path: path_address = "C:\\Users\\YourName\\Documents\\CS315_Project\\"
base_path = "Implementation/"

# Testing for large samples
testJaccard(base_path + 'largeSample_a.txt',base_path + 'largeSample_b.txt', "large")

# Testing for medium samples
testJaccard(base_path + 'mediumSample_a.txt',base_path + 'mediumSample_b.txt', "medium")

# Testing for small samples
testJaccard(base_path + 'smallSample_a.txt',base_path + 'smallSample_b.txt', "small")
