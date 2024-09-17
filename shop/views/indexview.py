from django.views.generic import ListView
from shop.models import Category, Product

class IndexView(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        categories = Category.objects.order_by("name")
        
        filter = self.request.GET.get("q", "")
        
        if filter:
            title = f"Search results for '{filter}'"
            products = Product.objects.filter(name__icontains=filter).order_by("name")
        else:
            title = "All Products"
            products = Product.objects.all().order_by("name")
        
        context['categories'] = [{'id': c.id, 'name': c.name} for c in categories]
        context['title'] = title
        context['products'] = products
        
        category_id = self.kwargs.get('id')  
        if category_id:
            context['title'] = next((c.name for c in categories if c.id == int(category_id)), "No Category")
            context['products'] = Product.objects.filter(category_id=category_id).order_by("name")
        
        return context


