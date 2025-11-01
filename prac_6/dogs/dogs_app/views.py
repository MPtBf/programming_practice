from django.shortcuts import render
import requests


def getBreedsList() -> list[str]:
    """
    Запрос на все породы собак
    :return: список из названий пород
    """
    j = requests.get("https://dog.ceo/api/breeds/list/all").json()
    breedsList = list(j['message'].keys())

    return breedsList


def getBreedRandImgUrl(breed) -> str:
    """
    Запрашивает случайную картинку собаки заданной породы
    :param breed: название породы
    :return: url картинки
    """

    randImgUrl = f"https://dog.ceo/api/breed/{breed}/images/random"
    j = requests.get(randImgUrl).json()
    url = j['message']

    return url


def main_page(request):
    """
    Задание контекста главной страницы, обработка ввода пользователя
    :param request: какой-то параметр запроса от django
    :return: какой-то httpResponse от django
    """

    breedsList = getBreedsList()

    feedback = ''
    breeds = []
    imgsUrls = []
    if request.method == 'POST':
        inp = request.POST.get('breeds', '').strip()
        breeds, imgsUrls, feedback = handleUserInput(inp, breedsList)

    context = {
        'feedback': feedback,
        'breedsData': [{'num': i+1, 'breed': breed}
                       for i, breed in enumerate(breedsList)],
        'imgsData': [{'breed': breed, 'url': url}
                     for breed, url in zip(breeds, imgsUrls)],
    }
    return render(request, 'main_page.html', context)


def handleUserInput(inp, breedsList) -> tuple:
    """
    Обработка ввода пользователя
    :param inp: сырая строка ввода
    :param breedsList: список всех пород
    :return: (breedsNames, imgsUrls, feedbackMessage).
    breedsNames - названия введённых пород;
    imgsUrls - url картинок к каждой породе;
    feedbackMessage - обратная связь (в случае ошибки)
    """

    try:
        breedsNames = inp.split(', ')
        breedsNames = [bn.lower() for bn in breedsNames]
        breedsNames = list(set(breedsNames))

        for bn in breedsNames:
            if bn not in breedsList:
                return [], [], f'Породы "{bn}" нет в списке доступных'

        imgsUrls = []
        for bn in breedsNames:
            url = getBreedRandImgUrl(bn)
            imgsUrls += [url]

    except Exception as e:
        return [], [], f'Ошибка при обработке ввода: {e}'

    return breedsNames, imgsUrls, ''
