from django.shortcuts import render, redirect

# Create your views here.

from main.models import Product, Category

def main(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html",{
        'products': products,
        'categories': categories,
        
        
    })
    

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html',{
        'product': product
    })


def about(request):
    return render(request,"about.html",{
        "first_name": "ilnur",
        'age': 16,
        'skills': ['html', 'css', "python", "js"]
    })
    
    
def contacts(request):
    return render(request,'contacts.html',{
        "email": "house 14, street alymbek danta 127",
        "phone": "999402300",   
        "gmail": "randomgmail@gmail.com",
        'social_media': ['timur','kamilla','madina']
    })
    
def list1(request):
    return render(request,"list.html",{
        'groups': ['one','two','three'],
        "contacts": ['madina','dawud','Ernis']
        
    })


def students(request):
    return render(request,'students.html',{
        "students": ['ilnur','dawud','dior','abror']
    })


def page(request):
    products = Product.objects.all()
    return render(request, "index.html",{
        'products': products,
        
    })
    
    
Product.objects.filter(price__gte=600)
Product.objects.filter(price__lte=600)
Product.objects.filter(price__gt=600)
Product.objects.filter(price__lt=600)
Product.objects.filter(price__range=(100, 1000))
Product.objects.filter(price__in=[600, 200, 400])
Product.objects.filter(name__contains="pro")
Product.objects.filter(name__icontains="Pro")
Product.objects.filter(image__isnull=True)

    
def product_create(request):
    print(request.POST)
    categories = Category.objects.all()
    
    print(request.method)
    
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        color = request.POST.get("color")
        info = request.POST.get("info")
        category_id = int(request.POST.get("category"))
        
        image = None
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            
        product = Product.objects.create(
            name=name,
            price=price,
            color=color,
            info=info,
            image=image,    
            category_id=category_id,
        )
        
        return redirect("main")
    
    return render(request,"product_create.html",{
        "categories": categories
    })
    
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)  
    product.delete()                          
    return redirect("main")    


def product_update(request,id):
    print(request.POST)
    categories = Category.objects.all()
    product = Product.objects.get(id=id) 
     
    print(request.method)
    
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        color = request.POST.get("color")
        info = request.POST.get("info")
        category_id = int(request.POST.get("category"))
        
        image = None
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            
        product.name = name
        product.price = price
        product.color = color
        product.info = info
        product.category = category_id
        product.save()
        return redirect("main")

    
    return render(request,"product_update.html",{
        "categories": categories
    })