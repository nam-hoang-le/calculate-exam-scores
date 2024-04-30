# Exam Grading System

## Overview

This is a Python program for grading exam papers and generating statistical analysis reports. It includes functionalities to read student answers from input files, grade the exams, calculate scores, and update the grades in an output file.

## Features

- File Handling: Easily read student answers from input files and save graded results to output files.
- Grading System: Automatically grade exams based on an answer key and calculate scores for each student.
- Statistical Analysis: Generate reports on exam scores, including mean, median, highest, and lowest scores, as well as the number of students with high scores.
- Error Handling: Identify and handle invalid input data, such as missing or incorrect answers.

## Usage

1. Reading Exam Data:

- Run read_file() to input the file containing student answers. The program will handle file opening errors and provide feedback.

2. Grading Exams:

- Use calculate_scores() to grade the exams based on an answer key. It calculates scores for each student and identifies skipped or incorrectly answered questions.
3. Generating Reports:

- Generate statistical analysis reports using statistic_scores(). This function provides insights into the distribution of scores, identifies the highest and lowest scores, and highlights questions that students commonly skip or answer incorrectly.
4. Updating Grades:

- Update the grades in an output file using update_scores(). This function appends student names and their corresponding scores to an output file for record-keeping.

5. Updated Version: 

- A version with complete usability is available in the updated_version folder with the addition of NumPy and Pandas.

## File Structure

```
|___ Data_Files
|
|___ grading_system
|
|___ running_example
|   
|___ updated_version
|
|___ LICENSE
|
|___ README.md
```

## Example

```python
import numpy as np 
import re
from grading_system import read_file, calculate_scores, statistic_scores, update_scores

# Step 1: Read exam data
correct_exams, name_file = read_file()

# Step 2: Grade exams
lst_of_scores, skip_questions, wrong_questions = calculate_scores(correct_exams, answer_key)

# Step 3: Generate statistical analysis reports
statistic_scores(lst_of_scores, skip_questions, wrong_questions)

# Step 4: Update grades in output file
update_scores(correct_exams, lst_of_scores, name_file)

```

## Requirements
- Python 3.x
- NumPy (for statistical analysis)

## License
This project is licensed under the MIT License.

Please read the LICENSE file for more details. 

## Contact

If you have any question, please contact me at lenam1072004@gmail.com.