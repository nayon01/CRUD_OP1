from django.shortcuts import render, redirect
from .models import *
import os

# HomePage Creates a new Profile and saves it to the database.


def HomePage(request):
    if request.method == 'POST':
        name = request.POST['name']
        photo = request.FILES.get('photo')
        mobile = request.POST['mobile']
        email = request.POST['email']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        prof = UserProfile.objects.create(
            name=name, photo=photo, mobile=mobile, email=email, address1=address1, address2=address2)
        prof.save()
        return redirect('homepage')

    return render(request, "index.html")


# All Profiles Data passed to Profile Page & Search works.
def AllProfile(request):
    search = request.GET.get('search')
    if search:
        pro = UserProfile.objects.filter(name__icontains=search)
    else:
        pro = UserProfile.objects.all()
    return render(request, 'allProfile.html', locals())


# Update Profile  Edit and Save.
def Update(request, id):
    pro = UserProfile.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        photo = request.FILES.get('photo')
        mobile = request.POST['mobile']
        email = request.POST['email']
        address1 = request.POST['address1']
        address2 = request.POST['address2']

        if len(request.FILES) != 0:
            if len(pro.photo) > 0:
                os.remove(pro.photo.path)
            pro.photo = photo
        pro.name = name
        pro.email = email
        pro.mobile = mobile
        pro.address1 = address1
        pro.address2 = address2
        pro.save()
        return redirect('allProfile')

    return render(request, 'update.html', locals())


# Delete a profile.
def Delete(request, id):
    name = UserProfile.objects.get(id=id)
    name.delete()
    return redirect('allProfile')
