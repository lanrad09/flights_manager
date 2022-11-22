from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id): 
    try:
        #First get the object(flight)
        flight = Flight.objects.get(id=flight_id)
        # flight = Flight.objects.get(pk=flight_id)#check the difference with test?
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
    return render(request, "flights/flight.html", { 
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all() 
        # passengers is the related name
        # we need both passenger, passengers already on the flight and those who are not already on the flight
    })

def book(request, flight_id):
    #check if rquest is POST
    if request.method =="POST":
        try:
         #Get the flight whose pry id is that flight id
            passenger = Passenger.objects.get(id=int(request.POST["passenger"]))
            flight = Flight.objects.get(pk=flight_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no flight chosen")
        except Flight.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        except Passenger.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: passenger does not exist")
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse, "flights:flight", args=(flight_id))

        #associate the flight with a passenger id, a passenger to book on the flight
        #assume the information is going to be in request.POST["passenger"] , this means is that the data about which passenger id
        # will want to register on this flight, is gonna be passsed in a by a form with an input field whose name is passenger. The name on a particular input field dictate
        #passenger = Passenger.objects.get(id=int(request.POST["passenger"]))# make sure its converted to int if its string
        #add the passenger to the flight
        #passenger.flights.add(flight)
        #return HttpResponseRedirect(reverse, "flight", args=(flight_id)) # the flight route take an argument of flight id args structure is a turple




