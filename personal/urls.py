from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('<slug:slug>', views.post_detail, name='detail'),
]


urlpatterns += [
                   # ... the rest of your URLconf goes here ...
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
