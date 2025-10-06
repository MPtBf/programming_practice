

def print_pack_report(cakes_count) -> None:
    """
    Если число пирожных делится и на 5, и на 3, выводит в консоль
    f"{cakes_count} - расфасуем по 3" или f"{cakes_count} - расфасуем по 5"
    в зависимости от того, делится количество на 3 или на 5
    :param cakes_count: кол-во пирожных, целое положительное число
    больше единицы
    :return: None, выводит строку в консоль
    """

    is_divisible_by_3 = cakes_count % 3 == 0
    is_divisible_by_5 = cakes_count % 5 == 0

    if is_divisible_by_3 and is_divisible_by_5:
        print(f"{cakes_count} - расфасуем по 3 или по 5")
    elif is_divisible_by_3:
        print(f"{cakes_count} - расфасуем по 3")
    elif is_divisible_by_5:
        print(f"{cakes_count} - расфасуем по 5")
    else:
        print(f"{cakes_count} - не заказываем!")


print_pack_report(14)
