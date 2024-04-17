def calculate_scores(correct_exams, answer_key):
    lst_of_scores = []
    skip_questions = {}
    wrong_questions = {}

    keys = answer_key.split(",")
    for exam in correct_exams:
        result = exam.split(",")
        score = 0
        for idx, answer in enumerate(result[1:], start=1):
            if answer == '':
                skip_questions[idx] = skip_questions.get(idx, 0) + 1
            else:
                if answer == keys[idx - 1]:
                    score += 4
                else:
                    score -= 1
                    wrong_questions[idx] = wrong_questions.get(idx, 0) + 1
        lst_of_scores.append(score)

    return lst_of_scores, skip_questions, wrong_questions