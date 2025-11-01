import requests
import json

beautyPrint = lambda data: print(json.dumps(data, indent=2))




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
 j = requests.get("https://dog.ceo/api/breed/affenpinscher/images/random").json()
 url = j['message']

 return url



