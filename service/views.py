import json

from django.http            import JsonResponse,HttpResponse
from django.views           import View

from account.models         import User
from account.utils          import login_required
from product.models         import Product, Size

from .models                import Cart

class CartView(View):
    @login_required
    def post(self,request):
        data = json.loads(request.body)
        try:
            selected_product = Product.objects.get(code = data['code'])
            selected_size = Size.objects.get(size = data['size'])
            Cart.objects.create(product = selected_product, size = selected_size, user = request.user, quantity = data['quantity'])

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({'Message' : 'INVALID_KEY'}, status = 400)

    @login_required
    def get(self,request):
        carts = Cart.objects.select_related('product', 'size').prefetch_related('product__media_set').filter(user = request.user)
        data = [
            {
            'name':cart.product.name,
            'url':cart.product.media_set.filter(media_url__contains='primary').first().media_url,
            'color_name' : cart.product.color_name,
            'size' : cart.size.size,
            'quantity' : cart.quantity,
            'price' : cart.product.price,
            } for cart in carts]

        return JsonResponse({'cart_list' : data}, status = 200)
