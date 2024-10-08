![A picture for library](https://thumb.ac-illust.com/f9/f9644141b1635fc76a55be05b982382b_t.jpeg)
# CS315 Algorithm Design and Analysis Project

## Project Title: Comparing Two Algorithms for Jaccard Similarity

### Course Information
- **Course**: CS315 Algorithm Design and Analysis
- **Project**: Implementing and analyzing two algorithms (naive and optimized) for calculating the Jaccard similarity between two texts.

### Project Overview
The objective of this project is to implement two approaches to calculate the **Jaccard Similarity** between two sets of words from different texts:
1. **Naive Algorithm**: A simple, brute-force approach to compute the Jaccard similarity.
2. **Optimized Algorithm**: A more efficient solution with improvements in time complexity.

### What is Jaccard Similarity?
Jaccard similarity is a measure used to compare the similarity between two sets. It is defined as the size of the intersection divided by the size of the union of the sets:

`
J(A, B) = |A ∩ B| / |A ∪ B|
`

Where:
- \( A \) and \( B \) are two sets of words (i.e., tokens) extracted from the texts.

### Algorithms
1. **Naive Algorithm**:  
   - This algorithm directly computes the union and intersection of two sets of words.
   - Time complexity: \(O(n*m)\), where \(n\) is the number of words in text A and \(m\) is the number of words in text B.

2. **Optimized Algorithm**:  
   - The optimized approach uses more efficient data structures (e.g., hash sets) to reduce the time complexity.
   - Time complexity: \(O(n+m)\), where \(n\) is the number of words in text A and \(m\) is the number of words in text B.

### Inputs
- Two texts (represented as strings or lists of words) for which the similarity is to be calculated.

### Outputs
- A numeric value representing the Jaccard similarity between the two texts.

### Goals and Learning Objectives
- **Compare the time complexity** and **performance** of both algorithms.
- **Analyze the trade-offs** between simplicity (naive approach) and efficiency (optimized approach).
- **Gain practical experience** in implementing and analyzing algorithms in Python.

### How to Run
1. Clone the repository.
2. Provide the input texts in `sample_a.txt` and `sample_b.txt`.
3. Run `algorithm1.py` for the naive algorithm and `algorithm2.py` for the optimized algorithm.
4. Compare the results and performance using the provided sample data.

### Contributors
- **Muhannad Majed Alfwazan**
- **Mohammad Mansour Albulaihy**
- **Eyad Fahad Alarfaj**
- **Mohammed Saleh Alsaif**