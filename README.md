![A gif for a ship](https://i.pinimg.com/originals/bf/fe/eb/bffeeb6e56305a13708c87d3df45a178.gif)
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

![Jaccard Similarity Rule](https://user-images.githubusercontent.com/4745789/98461673-302d7180-21d4-11eb-9722-41f473c1fe84.png)

Where:
- \( A \) and \( B \) are two sets of words (i.e., tokens) extracted from the texts.

### Algorithms
1. **Naive Algorithm**:  
   - This algorithm directly computes the union and intersection of two sets of words.
   - Time complexity: \(O(n^2)\).

2. **Optimized Algorithm**:  
   - The optimized approach uses more efficient data structures (hashes) to reduce the time complexity.
   - Time complexity: \(O(n)\).

### Inputs
- Two texts (represented as strings or lists of words) for which the similarity is to be calculated.

### Outputs
- A numeric value representing the Jaccard similarity between the two texts.

### Goals and Learning Objectives
- **Compare the time complexity** and **performance** of both algorithms.
- **Analyze the trade-offs** between simplicity (naive approach) and efficiency (optimized approach).
- **Gain practical experience** in implementing and analyzing algorithms in Python.

### Files Included:
- `algorithm1.py`: Contains the naive implementation of Jaccard Similarity.
- `algorithm2.py`: Contains the optimized implementation of Jaccard Similarity.
- Sample Text Files:
  - `smallSample_a.txt`, `smallSample_b.txt`
  - `mediumSample_a.txt`, `mediumSample_b.txt`
  - `largeSample_a.txt`, `largeSample_b.txt`

### How to Run:
1. Clone the repository.
2. Run `algorithm1.py` to execute the naive Jaccard Similarity algorithm on the text files.
3. Run `algorithm2.py` to execute the optimized Jaccard Similarity algorithm on the text files.
4. Compare the results and performance using the provided sample data.

Both scripts will read the input text files and output the Jaccard Similarity score for each pair of text samples.

---

### Handling File Path Issues:

If the script encounters a `FileNotFoundError` or path issue, follow these steps to resolve the problem:

1. **Modify the `base_path` Variable**:

   Open the Python file (`algorithm1.py` or `algorithm2.py`) and locate the variable `base_path`. This variable should hold the directory path where your text files are stored.

   Example:
   base_path = "C:\\\path\\\to\\\CS315_Project\\\\"  # Insert your actual path here

2. **Leave `base_path` Empty If Not Needed**:

   If your script and the text files are in the same folder, you can leave the `base_path` variable as an empty string:

   base_path = ""


### Contributors
- **Muhannad Majed Alfwazan**
- **Mohammad Mansour Albulaihy**
- **Eyad Fahad Alarfaj**
- **Mohammed Saleh Alsaif**
