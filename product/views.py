import json

from django.http      import JsonResponse,HttpResponse
from django.views     import View

from foundation.views import get_instagram_data
from .models          import (
    Product,
    Detail,
    Series,
    Media,
    Size,
    Description
)

class DetailView(View):
    def get(self,request,product_code):
        try:
            selected_product = Product.objects.select_related('detail').prefetch_related('media_set', 'series_set','description_set','productsize_set').get(code = product_code)

            data = [{
                'code'         : selected_product.code,
                'name'         : selected_product.name,
                'price'        : selected_product.price,
                'gender'       : selected_product.gender,
                'summary'      : selected_product.detail.summary,
                'color_name'   : selected_product.color_name,
                'size_list'    : [size.size.size for size in selected_product.productsize_set.all()],
                'size_img'     : selected_product.detail.size_img,
                'series_code'  : [series.code for series in selected_product.series_set.all()],
                'series_image' : [series.image for series in selected_product.series_set.all()],
                'media_url'    : [media.media_url for media in selected_product.media_set.all()],
                'description'  : [description.string for description in selected_product.description_set.all()],
                'desc_img'     : selected_product.detail.desc_img,
                'information'  : selected_product.detail.information,
            }]

            return JsonResponse({'product_detail' : data, 'instagram' : get_instagram_data()}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({'Message' : 'PRODUCT_DOES_NOT_EXIST'}, status = 400)
