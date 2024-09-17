# import stat
# from django.urls import path  # Correct import for path
# from OnlineShop import settings
# from shop.views.indexview import IndexView
# from shop.views.productdetailsview import ProductDetailsView

# urlpatterns = [
#     # path("products", ProductDetailsView.as_view(), name="products"),   
#     path("products/<int:id>/", ProductDetailsView.as_view(), name="product-details"),
#     path("", IndexView.as_view(), name="index"),  # Correct usage of IndexView
# ]

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop.views.productdetailsview import ProductDetailsView
from shop.views.indexview import IndexView

urlpatterns = [
    path('categories/<int:id>/', IndexView.as_view(), name='category-details'),
    path('', IndexView.as_view(), name='index'),
    path('product/<int:id>/', ProductDetailsView.as_view(), name='product-details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
