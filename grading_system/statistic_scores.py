import numpy as np

def statistic_scores(lst_of_scores, skip_questions, wrong_questions):
    print("Total students with high scores:", sum(score > 80 for score in lst_of_scores))
    print("Mean (average) score:", np.mean(lst_of_scores))
    print("Highest score:", max(lst_of_scores))
    print("Lowest score:", min(lst_of_scores))
    print("Range of scores:", max(lst_of_scores) - min(lst_of_scores))
    print("Median score:", np.median(lst_of_scores))

    most_skip_values = max(skip_questions.values())
    most_wrong_values = max(wrong_questions.values())

    most_skip_keys = [key for key, value in skip_questions.items() if value == most_skip_values]
    print("Question that most people skip:")
    for question in sorted(most_skip_keys):
        print(f"{question} - {most_skip_values} - {most_skip_values / 25}")

    most_wrong_keys = [key for key, value in wrong_questions.items() if value == most_wrong_values]
    print("Question that most people answer incorrectly:")
    for question in sorted(most_wrong_keys):
        print(f"{question} - {most_wrong_values} - {most_wrong_values / 25}")