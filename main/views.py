from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Birkenstock Boston Taupe Suede',
        'price': 2599000,
        'description': 'Birkenstock Boston Taupe Suede adalah sandal yang nyaman digunakan sehari-hari. Dengan bahan kulit suede yang lembut dan nyaman saat digunakan.'
    }

    return render(request, 'main.html', context)