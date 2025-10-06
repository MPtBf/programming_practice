

def check_winners(scores: list, student_score: int | float) -> None:
    """
    Проверяет, входит ли student_score в тройку лидеров в списке scores,
    если да, то выводит в консоль "Вы в тройке победителей!",
    иначе - "Вы не попали в тройку победителей."
    :param scores: список, который содержит количество баллов каждого
    участника олимпиады
    :param student_score: количество баллов, которое заработал Стас
    :return: None, выводит строку в консоль
    """

    if student_score not in scores:
        raise ValueError('Балла Стаса нет в списке')

    # сортируем, получаем баллы по позрастанию
    sorted_scores = sorted(scores)
    three_top_scores = sorted_scores[-3:]

    if student_score in three_top_scores:
        print('Вы в тройке победителей!')
    else:
        print('Вы не попали в тройку победителей.')


unsorted_list = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
student_score = 20

check_winners(unsorted_list, student_score)
