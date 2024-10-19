# Better Optimized Jaccard Similarity Algorithm
# This is the fastest i could get the algorithm to be, avg time of algorithm2 was (0.0349)seconds, but this algorithm(3) avg time is (0.0309)seconds.
# Indecating approximately 11.49% improvement
import time  # To measure the execution time of the algorithm
def optimized_jaccard_similarity2(text1, text2):

    # Tokenize the texts and convert to lowercase for case insensitivity
    # Use sets to only store unique words
    word_set1 = set(text1.lower().split())  # set of words in text1
    word_set2 = set(text2.lower().split())  # set for words in text2
    
    # calaculate intersection
    intersection_count = len(word_set1.intersection(word_set2))  # To store the number of common words between both texts

    # Uinion count is (sum of unique words from both texts) - intersection_count    
    union_count = len(word_set1) + len(word_set2) - intersection_count 

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
    similarity_optimized = optimized_jaccard_similarity2(text_a, text_b) * 100  # Calculate similarity percentage
    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate execution time
    # Output similarity percentage and execution time
    print(f"Optimized Jaccard Similarity for {type} samples: %{similarity_optimized:.2f}")
    print(f"Execution Time : {execution_time:.4f} seconds")

# Testing for large samples
testJaccard('Implementation/largeSample_a.txt', 'Implementation/largeSample_b.txt', "large")

# Testing for medium samples
testJaccard('Implementation/mediumSample_a.txt', 'Implementation/mediumSample_b.txt', "medium")

# Testing for small samples
testJaccard('Implementation/smallSample_a.txt', 'Implementation/smallSample_b.txt', "small")
