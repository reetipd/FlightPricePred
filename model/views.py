from django.shortcuts import render
import pandas as pd
import sklearn
import pickle
# Create your views here.

model = pickle.load(open('flight_model1.pkl','rb'))

def index(request):
    return render(request,"index.html")
    
def predict(request):

    if request.method == 'POST':
        Departure_date = request.POST.get('Departure_date')
        Date = int(pd.to_datetime(Departure_date,format = "%Y-%m-%d %H:%M").day)
        Month = int(pd.to_datetime(Departure_date, format ="%Y-%m-%d %H:%M").month)
        print(Date,Month)
        Dep_Hour = int(pd.to_datetime(Departure_date,format = "%Y-%m-%d %H:%M").hour)
        Dep_Minute = int(pd.to_datetime(Departure_date,format = "%Y-%m-%dT%H:%M").minute)
        print(Dep_Hour,Dep_Minute)
        Arrival_date = request.POST.get('Arrival_date')
        Arrival_Hour = int(pd.to_datetime(Departure_date,format = "%Y-%m-%d %H:%M").hour)
        Arrival_Minute = int(pd.to_datetime(Departure_date,format = "%Y-%m-%d %H:%M").minute)

        Duration_Hr = abs(Arrival_Hour-Dep_Hour)

        Total_Stops = request.POST.get('Stops')

        airline=request.POST.get('airline')
        if(airline=='Jet Airways'):
            Airline_Jet_Airways = 1
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='IndiGo'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 1
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Air India'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 1
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='SpiceJet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Vistara'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        elif (airline=='GoAir'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif (airline=='Jet Airways Business'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 1
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0

        elif (airline=='Vistara Premium economy'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 1
            Airline_Trujet = 0
            
        elif (airline=='Trujet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 1

        else:
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0
        

        Source = request.POST.get("Source")
        if (Source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0

        elif (Source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1

        else:
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        Source = request.POST.get("Destination")
        if (Source == 'Cochin'):
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
        
        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'New_Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Source == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0

        elif (Source == 'Kolkata'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1

        else:
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
        
    prediction = model.predict([[
     Total_Stops,
     Date, 
     Month, 
     Dep_Hour, 
     Dep_Minute,
     Arrival_Hour,
     Arrival_Minute,
     Duration_Hr,
     Airline_Air_India,
     Airline_GoAir,
     Airline_IndiGo,
     Airline_Jet_Airways,
     Airline_Jet_Airways_Business,
     Airline_Multiple_carriers,
     Airline_Multiple_carriers_Premium_economy,
     Airline_SpiceJet,
      Airline_Trujet,
      Airline_Vistara,
      Airline_Vistara_Premium_economy,
       Source_Chennai,
       Source_Delhi,
       Source_Kolkata,
       Source_Mumbai,
       Destination_Cochin,
       Destination_Delhi,
       Destination_Hyderabad,
       Destination_Kolkata,
       Destination_New_Delhi]])
    output = round(prediction[0],2)
    return render(request,"index.html",context={'price':output})

