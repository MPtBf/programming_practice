from django.shortcuts import render

def book_detail(request):
    """
    отображение информации о книге
    """

    context = {
        'book_info': {
            'author': 'Дж Ханк Рейнвотер',
            'title': 'Как пасти котов',
        }
    }

    return render(request, 'book_detail.html', context)

