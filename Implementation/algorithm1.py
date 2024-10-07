# Naive algorithm
# First Implementation
def naive_jaccard_similarity(text1, text2):
    
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    
    set1 = set(words1)
    set2 = set(words2)

     
    intersection_count = 0
    for word in set1:                  
        for compare_word in set2:      
            if word == compare_word:   
                intersection_count += 1
                
    
    union_count = len(set1) + len(set2)  
    for word in set1:                  
        if word in set2:              
            union_count -= 1           
    
    
    if union_count == 0:               
        return 0.0
    return intersection_count / union_count  

# naive function Finish here -----------

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


text_a = read_file('sample_a.txt')
text_b = read_file('sample_b.txt')
similarity_naive = naive_jaccard_similarity(text_a, text_b)
print(f"Naive Jaccard Similarity: {similarity_naive:.2f}")