from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Restaurant, Book, Mess, Book1
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal

def home(request):
    return render(request, 'myapp/home.html')



@login_required(login_url='signin')
def findrestaurant(request):
    context = {}
    if request.method == 'POST':
        city_name_r = request.POST.get('city_name')


        date_r = request.POST.get('date')
        restaurant_list = Restaurant.objects.filter(city_name=city_name_r, date=date_r)
        if restaurant_list:
            return render(request, 'myapp/list.html', locals())
        else:
            context["error"] = "Sorry no restaurants available"
            return render(request, 'myapp/findrestaurant.html', context)
    else:
        return render(request, 'myapp/findrestaurant.html')


@login_required(login_url='signin')
def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('restaurant_id')
        seats_r = int(request.POST.get('no_seats'))
        restaurant = Restaurant.objects.get(id=id_r)
        if restaurant:
            if restaurant.rem > int(seats_r):
                name_r = restaurant.restaurant_name
                cost = int(seats_r) * restaurant.price
                city_name_r = restaurant.city_name

                nos_r = Decimal(restaurant.nos)
                price_r = restaurant.price
                date_r = restaurant.date
                time_r = restaurant.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = restaurant.rem - seats_r
                Restaurant.objects.filter(id=id_r).update(rem=rem_r)
                book = Book.objects.create(name=username_r, email=email_r, userid=userid_r, restaurant_name=name_r,
                                           city_name=city_name_r, restaurantid=id_r,
                                          price=price_r, nos=seats_r, date=date_r, time=time_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'myapp/bookings.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'myapp/findrestaurant.html', context)

    else:
        return render(request, 'myapp/findrestaurant.html')



@login_required(login_url='signin')
def cancellings(request, restaurant=None):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('restaurant_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            restaurant = Restaurant.objects.get(id=book.restaurantid)
            rem_r = restaurant.rem + book.nos
            Restaurant.objects.filter(id=book.restaurantid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that restaurant"
            return render(request, 'myapp/error.html', context)
    else:
        return render(request, 'myapp/findrestaurant.html')


@login_required(login_url='signin')
def seebookings(request,new={}):
    context = {}
    id_r = request.user.id
    book_list = Book.objects.filter(userid=id_r)
    if book_list:
        return render(request, 'myapp/booklist.html', locals())
    else:
        context["error"] = "Sorry no restaurants booked"
        return render(request, 'myapp/findrestaurant.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r)
        if user:
            login(request, user)
            return render(request, 'myapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signup.html', context)
    else:
        return render(request, 'myapp/signup.html', context)
def adminapp(request):
    return render(request, 'myapp/adminapp.html')

def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user and user.is_superuser == True:
            login(request,user)
            return adminapp(request)
        elif user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'myapp/success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'myapp/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'myapp/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'myapp/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'myapp/success.html', context)

@login_required(login_url='signin')
def findmess(request):
    context = {}
    if request.method == 'POST':
        city_name_r = request.POST.get('city_name')
        food_type_r = request.POST.get('food_type')


        date_r = request.POST.get('date')
        mess_list = Mess.objects.filter(city_name=city_name_r, date=date_r,food_type=food_type_r)
        if mess_list:
            return render(request, 'myapp/list1.html', locals())
        else:
            context["error"] = "Sorry no mess available"
            return render(request, 'myapp/findmess.html', context)
    else:
        return render(request, 'myapp/findmess.html')
@login_required(login_url='signin')
def bookingsmess(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('mess_id')
        seats_r = int(request.POST.get('no_seats'))
        doc_r = request.FILES.get('user_doc',False)

        mess = Mess.objects.get(id=id_r)
        if mess:
            if mess.rem > int(seats_r):
                name_r = mess.mess_name
                cost = int(seats_r) * mess.price
                city_name_r = mess.city_name
                food_type_r = mess.food_type

                nos_r = Decimal(mess.nos)
                price_r = mess.price
                date_r = mess.date
                time_r = mess.time
                username_r = request.user.username
                email_r = request.user.email
                userid_r = request.user.id
                rem_r = mess.rem - seats_r
                Mess.objects.filter(id=id_r).update(rem=rem_r)
                book1 = Book1.objects.create(name=username_r, email=email_r, userid=userid_r, mess_name=name_r,
                                               city_name=city_name_r,food_type=food_type_r,messid=id_r,user_doc=doc_r,
                                               price=price_r, nos=seats_r, date=date_r, time=time_r,
                                               status='BOOKED')
                print('------------book id-----------', book1.id)
                    # book.save()
                return render(request, 'myapp/bookingsmess.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'myapp/findmess.html', context)

    else:
        return render(request, 'myapp/findmess.html')

@login_required(login_url='signin')
def cancellingsmess(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('mess_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book1 = Book1.objects.get(id=id_r)
            mess = Mess.objects.get(id=book1.messid)
            rem_r = mess.rem + book1.nos
            Mess.objects.filter(id=book1.messid).update(rem=rem_r)
            #nos_r = book.nos - seats_r
            Book1.objects.filter(id=id_r).update(status='CANCELLED')
            Book1.objects.filter(id=id_r).update(nos=0)
            return redirect(seebookingsmess)
        except Book1.DoesNotExist:
            context["error"] = "Sorry You have not booked that mess"
            return render(request, 'myapp/error.html', context)
    else:
        return render(request, 'myapp/mess.html')

@login_required(login_url='signin')
def seebookingsmess(request,new={}):
    context = {}
    id_r = request.user.id
    book1_list = Book1.objects.filter(userid=id_r)
    if book1_list:
        return render(request, 'myapp/booklistmess.html', locals())
    else:
        context["error"] = "Sorry no mess booked"
        return render(request, 'myapp/findmess.html', context)

def restaurantadmin(request):
    if(request.method=="POST"):
        restaurant_name=request.POST['restaurant_name']
        city_name=request.POST['city_name']

        nos = request.POST['nos']
        rem = request.POST['rem']
        date = request.POST['date']
        time = request.POST['time']
        price = request.POST['price']

        s=Restaurant.objects.create(restaurant_name=restaurant_name,city_name=city_name,nos=nos,rem=rem, date=date, time=time,price=price)
        s.save()
        return viewrestaurantsdetails(request)

    return render(request,'myapp/restaurantadmin.html')
def viewrestaurantsdetails(request):
    k=Restaurant.objects.all()
    return render(request,'myapp/list_of_restaurants.html',{'s':k})










