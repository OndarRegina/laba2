# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from models import User, Request, Product

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        alluser = User.objects.all()
        allrequest = Request.objects.all()
        allproduct = Product.objects.all()
        context.update(
            {
                'users': alluser,
                'request': allrequest,
                'product': allproduct,
            }
        )
        return context