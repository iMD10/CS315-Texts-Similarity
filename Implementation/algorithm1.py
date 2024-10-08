# Naive algorithm
# First Implementation
import time
def naive_jaccard_similarity(text1, text2):
    
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    
    union_list = []
    union_count = 0
    for word in words1:
        flag_comp = True
        for unique_word in union_list:
            if word == unique_word:
                flag_comp = False
                break;
        if flag_comp == True:
            union_list.append(word)
            union_count += 1

    intersection_count = 0
    for word in union_list:             
        for compare_word in words2:      
            if word == compare_word:   
                intersection_count += 1
                break

    for word in words2:
        flag_comp = True
        for unique_word in union_list:
            if word == unique_word:
                flag_comp = False
                break;
        if flag_comp == True:
            union_list.append(word)
            union_count += 1
                

    
    
    if union_count == 0:               
        return 0.0
    return intersection_count / union_count  

# naive function Finish here -----------

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


text_a = read_file('Implementation/sample_a.txt')
text_b = read_file('Implementation/sample_b.txt')
start_time = time.time()
similarity_naive = naive_jaccard_similarity(text_a, text_b)
end_time = time.time()
execution_time = end_time - start_time
print(f"Naive Jaccard Similarity: {similarity_naive:.2f}")
print(f"Execution Time : {execution_time:.3f}")