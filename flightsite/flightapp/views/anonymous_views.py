from django.shortcuts import render

from ..models import Country

def anonymous_index(request):
    """
    Anonymous home page.
    This is what the un-logged-in user can see/do
    """
    return render(request, 'flightapp/anonymous_index.html')


def countries_list(request):
    """
    List of all countries- maybe ill delete it
    """
    countries = Country.objects.all()

    context = {'countries': countries}
    return render(request, 'flightapp/countries_list.html', context)