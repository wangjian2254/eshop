#coding=utf-8
# Create your views here.
from shop.models import ProductInfo
from tool.eshopTools import EshopTemplateView


class Index(EshopTemplateView):
    template_name = 'index.dwt'

class Goods(EshopTemplateView):
    template_name = 'goods.dwt'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        goodsid=int(self.args[0])
        context['goods']=ProductInfo.objects.get(id=goodsid)



        return self.render_to_response(context)

class Search(EshopTemplateView):
    template_name = 'search.dwt'


