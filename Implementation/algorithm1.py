# Naive algorithm
# First Implementation
import time # To test the execution time of algorithm
def naive_jaccard_similarity(text1, text2):
    
    # This to split the text into list of words
    words1 = text1.lower().split() 
    words2 = text2.lower().split()

    # Union list will contain the union of both texts
    union_list = []
    # To count the number of words in union
    union_count = 0

    # This to remove dublicated words and making union set
    for word in words1:
        flag_comp = True
        for unique_word in union_list:
            if word == unique_word: # If it is already in union then don't put it in the list
                flag_comp = False
                break;
        if flag_comp == True: # If it's not in union list then put it and increase the counter
            union_list.append(word)
            union_count += 1

    # To count the common words in text1 and text2 ignoring the duplicated words 
    intersection_count = 0
    for word in union_list:             
        for compare_word in words2:      
            if word == compare_word:   
                intersection_count += 1
                break

    # To count the complete union by finding only words that unique from text2
    for word in words2:
        flag_comp = True
        for unique_word in union_list: 
            if word == unique_word: # If it's already in union then skip it
                flag_comp = False
                break;
        if flag_comp == True: # If it's not found in union list then put it in union list and increase counter
            union_list.append(word)
            union_count += 1
                

    
    
    if union_count == 0:   # To handel run time error in case of union set is empty           
        return 0.0
    return intersection_count / union_count  # This is the Jaccar Similirity law

# naive function Finish here -----------

def read_file(file_path): # To read from input from txt files
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def testJaccard(address1, address2, type):
    text_a = read_file(address1) # This is text1
    text_b = read_file(address2) # This is text2
    start_time = time.time() # Just to save the starting time of algorithm execution
    similarity_naive = naive_jaccard_similarity(text_a, text_b) * 100
    end_time = time.time()
    execution_time = end_time - start_time # Calculate the execution time
    print(f"Naive Jaccard Similarity for {type} samples: %{similarity_naive:.2f}")
    print(f"Execution Time : {execution_time:.3f}")

# Testing for large samples
testJaccard('Implementation/largeSample_a.txt', 'Implementation/largeSample_b.txt', "large")

# Testing for medium samples
testJaccard('Implementation/mediumSample_a.txt', 'Implementation/mediumSample_b.txt', "medium")

# Testing for small samples
testJaccard('Implementation/smallSample_a.txt', 'Implementation/smallSample_b.txt', "small")



