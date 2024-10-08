import time
def optimized_jaccard_similarity(text1, text2):
    # Tokenize the texts and convert to lowercase for case insensitivity
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    # Use dictionaries to count occurrences
    word_count1 = {}
    word_count2 = {}

    # Count occurrences of words in text1
    for word in words1:                 # O(n)
        word_count1[word] = word_count1.get(word, 0) + 1  # O(1)

    # Count occurrences of words in text2
    for word in words2:                 # O(m)
        word_count2[word] = word_count2.get(word, 0) + 1  # O(1)

    # Calculate intersection and union sizes
    intersection_count = 0               # O(1)
    union_count = len(word_count1) + len(word_count2)  # O(1)

    # Calculate intersection count
    for word in word_count1:             # O(n)
        if word in word_count2:          # O(1)
            intersection_count += 1      # O(1)
            union_count -= 1             # O(1)

    # Return the Jaccard similarity
    if union_count == 0:                 # O(1)
        return 0.0
    return intersection_count / union_count  # O(1)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()



def testJaccard(address1, address2, type):
    text_a = read_file(address1) # This is text1
    text_b = read_file(address2) # This is text2
    start_time = time.time() # Just to save the starting time of algorithm execution
    similarity_optimized = optimized_jaccard_similarity(text_a, text_b) * 100
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Optimized Jaccard Similarity for {type} samples: %{similarity_optimized:.1f}")
    print(f"Execution Time : {execution_time:.3f}")

# Testing for large samples
testJaccard('Implementation/largeSample_a.txt', 'Implementation/largeSample_b.txt', "large")

# Testing for medium samples
testJaccard('Implementation/mediumSample_a.txt', 'Implementation/mediumSample_b.txt', "medium")

# Testing for small samples
testJaccard('Implementation/smallSample_a.txt', 'Implementation/smallSample_b.txt', "small")