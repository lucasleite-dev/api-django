from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^produtos$', ProdutoList.as_view()),
    url(r'^produtos/(?P<pk>[0-9]+)$', ProdutoDetalhes.as_view()),
]
