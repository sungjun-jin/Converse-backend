import json

from django.http      import JsonResponse,HttpResponse
from django.views     import View
from django.db.models import Q

from .models          import *

class FilterView(View):

    def get(self, request,category_name):

        product = Product.objects.filter(
            Q(category__name = category_name)| Q(group__name = category_name))

        return JsonResponse(
            {
                'filter' : {
                    'gender':list(
                        set([
                            gender['gender'] for gender in product.values('gender')]
                        ).difference(['남녀공용','유니섹스'])
                    ),
                    'color' : [
                        {'name':value[0], 'code':value[1]} for (key,value) in sorted(
                            {
                                color['id'] : (color['color_name'],color['color_code'])
                                for color in Color.objects.filter(product__in = product).values()
                            }.items())],
                    'size':[
                        size[1] for size in sorted(
                            {
                                size['id']:size['size']
                                for size in Size.objects.filter(product__in=product).values()
                            }.items())],
                    'silhouette':[
                        value for (key,value) in sorted(
                            {
                                silhouette['id']:silhouette['name']
                                for silhouette in Silhouette.objects.filter(product__in=product).values()
                            }.items())]
                }
            }, status=200)

class ProductView(View):

    def get(self, request,category_name):

        products  = Product.objects.filter(
            Q(category__name = category_name)| Q(group__name = category_name))

        filter_dict = {}

        if request.GET.getlist('gender', None):
            filter_dict['gender__in'] = request.GET.getlist('gender', None)+['남녀공용','유니섹스']
        if request.GET.getlist('color', None):
            filter_dict['product_color__color_code__in'] = request.GET.getlist('color', None)
        if request.GET.getlist('size', None):
            filter_dict['product_size__size'] = request.GET.getlist('size', None)
        if request.GET.getlist('silhouette', None):
            filter_dict['silhouette_id__name__in'] = request.GET.getlist('silhouette', None)

        sources      = products.prefetch_related('series_set','media_set','product_color')
        product_list = [product for product in products.filter(**filter_dict).values('id','code','name','price')][:20]

        for product in product_list:

            try:

                product['color_list'] = []

                for source in sources.get(code=product['code']).series_set.values('code'):

                    if '#' in source['code']:

                        source['code'] = source['code'].replace('#','')
                        image = sources.get(code=source['code']).media_set.values('media_url')[0]['media_url']

                    product['color_list'].append({
                        'color_code' : sources.get(code=source['code']
                                                  ).product_color.values('color_code')[0]['color_code'],
                        'image'      : image,
                        'hover'      : image.replace('primary','hover')
                    })

            except Product.DoesNotExist:

                image = sources.get(id=product['id']).media_set.values('media_url')[0]['media_url']

                product['color_list'] = {
                    'color_code' : sources.get(id=product['id']
                                              ).product_color.values('color_code')[0]['color_code'],
                    'image'      : image,
                    'hover'      : image.replace('primary','hover')}

        return JsonResponse({'product' : product_list},status=200)

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

            return JsonResponse({'product_detail' : data, 'recommendations' : get_recommendations(selected_product)}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({'Message' : 'PRODUCT_DOES_NOT_EXIST'}, status = 400)

def get_recommendations(selected_product):
    recommendations = Product.objects.select_related('group').prefetch_related('media_set').filter(group = selected_product.group)[:10]
    data = [{
            'code'  : recommendation.code,
            'url'   : recommendation.media_set.filter(media_url__contains = 'primary').first().media_url,
            'hover' : recommendation.media_set.filter()[2].media_url,
    } for recommendation in recommendations]

    return data

