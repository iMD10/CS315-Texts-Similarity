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


text_a = read_file('sample_a.txt')
text_b = read_file('sample_b.txt')
similarity_optimized = optimized_jaccard_similarity(text_a, text_b)
print(f"Optimized Jaccard Similarity: {similarity_optimized:.2f}")