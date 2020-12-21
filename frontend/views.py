from django.http import HttpResponse
from django.shortcuts import render
from .models import Metadatas, ContactDetails, ContactMessage, Footer, Work, Whoweare, Blog, About

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    Home = ContactDetails.objects.all()
    FooterData = Footer.objects.all()
    Sitedata = Metadatas.objects.all()
    Sitework = Work.objects.all()
    About = Whoweare.objects.all()
    IndexBlog = Blog.objects.all()
    
    #return render(request, template, context)
    return render(request, 'index.html', {'Homemessage':Home, 'Foot':FooterData, 'Metadat':Sitedata, 'Work':Sitework, 'Whoare':About, 'Blog':IndexBlog})

def work(request):
	MyHome = ContactDetails.objects.all()
	FooterValue = Footer.objects.all()
	Workdata = Metadatas.objects.all()
	Allwork = Work.objects.all()
	return render(request, 'work.html', {'Homemessage':MyHome, 'Foot':FooterValue, 'Metadat':Workdata, 'OurWork':Allwork})

def about(request):
	AboutHome = ContactDetails.objects.all()
	Footerabout = Footer.objects.all()
	Workabout = Metadatas.objects.all()
	Aboutus = About.objects.all()
	return render(request, 'about.html', {'Homemessage':AboutHome, 'Foot':Footerabout, 'Metadat':Workabout, 'About':Aboutus})


def service(request):
	ServiceHome = ContactDetails.objects.all()
	Footerservice = Footer.objects.all()
	Metaservice = Metadatas.objects.all()
	Servicework = Work.objects.all()
	return render(request, 'service.html', {'Homemessage':ServiceHome, 'Foot':Footerservice, 'Metadat':Metaservice, 'Serwork':Servicework})


def blog(request):
	BlogHome = ContactDetails.objects.all()
	FooterBlog = Footer.objects.all()
	MetaBlog = Metadatas.objects.all()
	MainBlog = Blog.objects.all()
	return render(request, 'blog.html', {'Homemessage':BlogHome, 'Foot':FooterBlog, 'Metadat':MetaBlog, 'Blog':MainBlog})



def contact(request):
	if request.method=="POST":
		if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
			ContactMessages =  ContactMessage()
			ContactMessages.name = request.POST.get('name')
			ContactMessages.email = request.POST.get('email')
			ContactMessages.phone = request.POST.get('phone')
			ContactMessages.message = request.POST.get('message')
			ContactMessages.save()
	ContactHome = ContactDetails.objects.all()
	FooterContact = Footer.objects.all()
	MetaContact = Metadatas.objects.all()
	return render(request, 'contact.html', {'Homemessage':ContactHome, 'Foot':FooterContact, 'Metadat':MetaContact})


def blogdetails(request, id):
	BlogHome = ContactDetails.objects.all()
	Blogabout = Footer.objects.all()
	Metablog = Metadatas.objects.all()
	Blogdetail = Blog.objects.filter(id=id)
	return render(request, 'blogdetail.html', {'Homemessage':BlogHome, 'Foot':Blogabout, 'Metadat':Metablog,'Blogs':Blogdetail})

