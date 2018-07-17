from django.shortcuts import render, redirect
from .models import Photo
from .forms import ClientContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    active_tab = "Home"
    home_photos = Photo.objects.all()
    carousel_id = 0
    return render(request, 'home.html',{"active_tab":active_tab, "home_photos":home_photos, "carousel_id":carousel_id})

def index(request):
    active_tab = "Photos"
    storage = messages.get_messages(request)
    concert_photos = Photo.objects.filter(tag="concerts")
    event_photos = Photo.objects.filter(tag="events")
    family_photos = Photo.objects.filter(tag="family")
    food_photos = Photo.objects.filter(tag="food")
    people_photos = Photo.objects.filter(tag="people")
    sports_photos = Photo.objects.filter(tag="sports")
    travel_photos = Photo.objects.filter(tag="travel")
    wedding_photos = Photo.objects.filter(tag="wedding")
    context = {"concert_photos":concert_photos,"event_photos":event_photos, "family_photos":family_photos, "food_photos": food_photos, "people_photos":people_photos, "sports_photos":sports_photos, "travel_photos":travel_photos, "wedding_photos":wedding_photos, 'message':storage, 'active_tab':active_tab}
    return render(request, 'index.html', context)

def detail(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'detail.html', {"photo":photo})

def about(request):
    active_tab = "About"
    return render(request, 'about.html', {"active_tab":active_tab})

def contact(request):
    active_tab = "Contact"
    form = ClientContactForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save(commit=True)
        messages.success(request, "Thanks for contacting me. I'll get back to you as soon as possible")
        return redirect("index")
    return render(request, 'contact.html', {'form':form, "active_tab":active_tab})

def videos(request):
    active_tab = "Videos"
    return render(request, 'videos.html',{"active_tab":active_tab})

def singleCategory(request):
    tag = request.GET.get(["category"][0])
    photos = Photo.objects.filter(tag=tag)
    active_tab = "Photos"
    return render(request, 'singlecategory.html',{"tag":tag, "photos":photos, "active_tab":active_tab})
    
