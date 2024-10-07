
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
\[
J(A, B) = \frac{|A \cap B|}{|A \cup B|}
\]
Where:
- \( A \) and \( B \) are two sets of words (i.e., tokens) extracted from the texts.

### Algorithms
1. **Naive Algorithm**:  
   - This algorithm directly computes the union and intersection of two sets of words.
   - Time complexity: \(O(n^2)\), where \(n\) is the total number of unique words in both texts.

2. **Optimized Algorithm**:  
   - The optimized approach uses more efficient data structures (e.g., hash sets) to reduce the time complexity.
   - Time complexity: \(O(n)\), where \(n\) is the number of words.

### Inputs
- Two texts (represented as strings or lists of words) for which the similarity is to be calculated.

### Outputs
- A numeric value representing the Jaccard similarity between the two texts.

### Goals and Learning Objectives
- **Compare the time complexity** and **performance** of both algorithms.
- **Analyze the trade-offs** between simplicity (naive approach) and efficiency (optimized approach).
- **Gain practical experience** in implementing and analyzing algorithms in Python (or a similar programming language).

### How to Run
1. Clone the repository.
2. Run `naive_jaccard.py` for the naive algorithm and `optimized_jaccard.py` for the optimized algorithm.
3. Provide the input texts in the appropriate format.
4. Compare the results and performance using sample data.

### Contributors
- **Muhannad Majed Alfwazan**
- **Eyad Fahad Alarfaj**
- **Mohammad Mansour Albulaihy**
- **Mohammed Saleh Alsaif**