Text Similarity Project - CS315

## Group Members:
1. Muhannad Majed AlFwazan 
2. Mohammad Mansour Albulaihy 
3. Eyad Fahad Alarfaj 
3. Mohammed Saleh AlSaif 

---

## Project Overview:
This project implements two algorithms for calculating the Jaccard Similarity between two sets of text:
1. Algorithm 1 (Naive Approach): Implemented in `algorithm1.py`.
2. Algorithm 2 (Optimized Approach): Implemented in `algorithm2.py`.

## Input Files:
The following sample text files are used to test both algorithms:
- `smallSample_a.txt` and `smallSample_b.txt`
- `mediumSample_a.txt` and `mediumSample_b.txt`
- `largeSample_a.txt` and `largeSample_b.txt`

## Files Included:
- `algorithm1.py`: Contains the naive implementation of Jaccard Similarity.
- `algorithm2.py`: Contains the optimized implementation of Jaccard Similarity.
- `FinalReport.pdf`: The final report detailing the problem, algorithm descriptions, analyses, and results.
- Sample Text Files:
  - `smallSample_a.txt`, `smallSample_b.txt`
  - `mediumSample_a.txt`, `mediumSample_b.txt`
  - `largeSample_a.txt`, `largeSample_b.txt`

## Instructions to Run:
1. Run `algorithm1.py` to execute the naive Jaccard Similarity algorithm on the text files.
2. Run `algorithm2.py` to execute the optimized Jaccard Similarity algorithm on the text files.

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
