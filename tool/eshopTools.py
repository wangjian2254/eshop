#coding=utf-8
import logging
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import Site
from shop.models import Eshop, Kind

__author__ = '王健'

from django.views.generic import TemplateView

TEMPLATE_CODE={}
KINDS={}
logger=logging.getLogger('eshop')

class EshopTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context=super(EshopTemplateView,self).get_context_data(**kwargs)
        current_site=Site.objects.get_current()
        eshop=Eshop.objects.filter(site=current_site)[0]
        if eshop:
            context['eshop']=eshop
        try:
            kinds=KINDS['kinds']
        except KeyError,e:
            kinds=Kind.objects.filter(father=None).all()
            for k in kinds:
                k.children=Kind.objects.filter(father=k.pk).all()
            if kinds:
                KINDS['kinds']=kinds
        if kinds:
            context['kinds']=kinds
        return context
    def get_template_names(self):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            try:
                template=TEMPLATE_CODE['style']
                logger.info('有样式缓存了！')
            except KeyError,e:
                logger.info('没有样式缓存了，加载缓存！')
                current_site=Site.objects.get_current()
                eshop=Eshop.objects.filter(site=current_site)[0]
                if eshop:
                    TEMPLATE_CODE['style']=eshop.templatecode+'/'
                else:
                    TEMPLATE_CODE['style']=''
            return [TEMPLATE_CODE['style']+self.template_name]
