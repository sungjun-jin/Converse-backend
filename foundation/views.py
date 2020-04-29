import json

from django.http       import JsonResponse,HttpResponse
from django.views      import View

from product.models    import Product,Media
from .models           import MainPage,Instagram

class MainPageView(View):
    def get(self,request):
        HAPPY_CAMPERS = '해피 캠퍼'
        PRO_LEATHERS  = '프로레더 선 블록'
        G4            = 'G4'
        JACK_PURCELL  = '잭퍼셀 시즈널'
        ARCHIVE_PRINT = '아카이브 프린트'

        happy_campers  = Product.objects.prefetch_related('media_set').filter(name__contains = HAPPY_CAMPERS)
        pro_leathers   = Product.objects.filter(name           = PRO_LEATHERS)
        g4s            = Product.objects.filter(name__contains = G4)
        jack_purcells  = Product.objects.filter(name__contains = JACK_PURCELL)
        archive_prints = Product.objects.filter(name__contains = ARCHIVE_PRINT)
        data = {
            'cards' : [
                    list(MainPage.objects.filter(id = 1).values()),
                    [{
                        'name'  : happy_camper.name,
                        'price' : happy_camper.price,
                        'url'   : happy_camper.media_set.values('media_url').first()['media_url'],
                        'hover' : happy_camper.media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    } for happy_camper in happy_campers],
                    list(MainPage.objects.filter(id = 2).values()),
                    list(MainPage.objects.filter(id = 3).values()),
                    [{
                        'name'  : pro_leather.name,
                        'price' : pro_leather.price,
                        'url'   : pro_leather.media_set.values('media_url').first()['media_url'],
                        'hover' : pro_leather.media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    } for pro_leather in pro_leathers],
                    list(MainPage.objects.filter(id = 4).values()),
                    list(MainPage.objects.filter(id = 5).values()),
                    list(MainPage.objects.filter(id = 6).values()),
                    list(MainPage.objects.filter(id = 7).values()),
                    list(MainPage.objects.filter(id = 8).values()),
                    list(MainPage.objects.filter(id = 9).values()),
                    [{
                        'name'  : g4s[1].name,
                        'price' : g4s[1].price,
                        'url'   : g4s[1].media_set.values('media_url').first()['media_url'],
                        'hover' : g4s[1].media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    },
                    {
                        'name'  : g4s[3].name,
                        'price' : g4s[3].price,
                        'url'   : g4s[3].media_set.values('media_url').first()['media_url'],
                        'hover' : g4s[3].media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    }],
                    list(MainPage.objects.filter(id= 10).values()),
                    [{
                        'name'  : jack_purcells[0].name,
                        'price' : jack_purcells[0].price,
                        'url'   : jack_purcells[0].media_set.values('media_url').first()['media_url'],
                        'hover' : jack_purcells[0].media_set.values('media_url')[1]['media_url'],
                        'size'  : 1
                    },
                    {
                        'name'  : jack_purcells[1].name,
                        'price' : jack_purcells[1].price,
                        'url'   : jack_purcells[1].media_set.values('media_url').first()['media_url'],
                        'hover' : jack_purcells[1].media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    }],
                    list(MainPage.objects.filter(id = 11).values()),
                    list(MainPage.objects.filter(id = 12).values()),
                    [{
                        'name'  : archive_prints[11].name,
                        'price' : archive_prints[11].price,
                        'url'   : archive_prints[11].media_set.values('media_url').first()['media_url'],
                        'hover' : archive_prints[11].media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    },
                    {
                        'name'  : archive_prints[5].name,
                        'price' : archive_prints[5].price,
                        'url'   : archive_prints[5].media_set.values('media_url').first()['media_url'],
                        'hover' : archive_prints[5].media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    },
                    {
                        'name'  : archive_prints[0].name,
                        'price' : archive_prints[0].price,
                        'url'   : archive_prints[0].media_set.values('media_url').first()['media_url'],
                        'hover' : archive_prints[0].media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    },
                    {
                        'name'  : archive_prints.last().name,
                        'price' : archive_prints.last().price,
                        'url'   : archive_prints.last().media_set.values('media_url').first()['media_url'],
                        'hover' : archive_prints.last().media_set.values('media_url')[1]['media_url'],
                        'size'  : 1,
                    }],
                    ]
                }

        return JsonResponse({'data' : data, 'instagrams' : getInstagramData()}, status = 200)

def getInstagramData():
    insta_dict = {}
    data = Instagram.objects.values()
    return list(data)

