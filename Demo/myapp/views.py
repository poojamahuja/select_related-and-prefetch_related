from .models import Country, City, Person
from django.http import HttpResponse


def home(request):
    # city = City.objects.all()
    city = City.objects.all().select_related('country')
    print("------- Result of select_related -----------")
    for c in city:
        print("Country Name : ", c.country)

    # persons = Person.objects.all()
    persons = Person.objects.all().prefetch_related('city')
    print("------- Result of prefetch_related -----------")
    for person in persons:
        print("Person Name : ", person.firstname)
        for city in person.city.all():
            print("City Name : ", city)

    return HttpResponse('select_related and prefetch_related example')
