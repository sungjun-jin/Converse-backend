import json

from django.http    import JsonResponse,HttpResponse
from django.views   import View

from product.models import Product,Media
from .models        import (
    Instagram,
    Store,
    StoreType
)

class MainPageView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            size = int(data['one'])
            products = Product.objects.prefetch_related('media_set').filter(name__contains = data['category'], is_main_page = 1)[:size]
            cards = [{

                'name'  : product.name,
                'code'  : product.code,
                'price' : product.price,
                'url'   : product.media_set.values('media_url').first()['media_url'],
                'hover' : product.media_set.values('media_url')[1]['media_url'],

            } for product in products]

            return JsonResponse({'cards' : cards}, status = 200)

        except KeyError:
            return JsonResponse({'Message' : 'INVALID_KEY'}, status = 400)

class StoreView(View):
    def get(self, request):
        stores = Store.objects.select_related('store_type').values()

        return JsonResponse({'stores' : list(stores)}, status = 200)

def get_instagram_data():
    data = Instagram.objects.values()
    return list(data)
