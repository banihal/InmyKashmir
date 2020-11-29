from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from home.models import Products, Sample, Logo
from reportlab.pdfgen import canvas  
from django.http import HttpResponse  
# Create your views here.

def home(request):
	context = {
		'products' : Products.objects.all(),
		'logos': Logo.objects.all(),
		'sample':Sample.objects.all()
	}
	return render(request, 'home/home.html',context)


def product(request):
	context = {
		'products' : Products.objects.all()
	}
	return render(request, 'home/product.html',context)


def about(request):
	context = {
		'samples' : Sample.objects.all()
	}
	return render(request, 'home/about.html',context)

  
# def getpdf(request):  
#     response = HttpResponse(content_type='application/pdf')  
#     response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
#     p = canvas.Canvas(response)  
#     p.setFont("Times-Roman", 55)  
#     p.drawString(100,700, "Hello, Javatpoint.")  
#     p.showPage()  
#     p.save()  
#     return response  