from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Library.apps.lib import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_author/', views.AuthorCreate.as_view(), name='add_author'),
    path('add_debtor/', views.DebtorCreate.as_view(), name='add_debtor'),
    path('add_book/', views.BookCreate.as_view(), name='add_book'),
    path('add_pub_house/', views.PublishingHouseCreate.as_view(), name='add_pub_house'),
    path('list_author', views.AuthorRead.as_view(), name='list_author'),
    path('list_book', views.BookRead.as_view(), name='list_books'),
    path('list_debtor', views.DebtorRead.as_view(), name='list_debtor'),
    path('list_pub_house', views.PublishingHouseRead.as_view(), name='list_pub_house'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
