from django.template import loader
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from shop.models import Category, Product

class ProductDetailsView(TemplateView):
    template_name = "shop/productdetails.html"

    def get(self, request, id):
        categories = Category.objects.order_by("name")
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404("Product not found")
        
        context = {
            "categories": [{"id": c.id, "name": c.name} for c in categories],
            "title": product.name,
            "description": product.description,
            "price": product.price,
            "volume": product.volume,
            "image": product.image,
        }
        
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
