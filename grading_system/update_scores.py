def update_scores(correct_exams, lst_of_scores, name_file):
    res = []
    for exam, score in zip(correct_exams, lst_of_scores):
        res.append([exam.split(",")[0], score])

    with open(f"Data_Files/output/{name_file}_grades.txt", 'a') as f:
        for element in res:
            f.write(",".join(map(str, element)) + "\n")
