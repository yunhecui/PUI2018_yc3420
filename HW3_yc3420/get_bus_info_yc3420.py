from __future__ import print_function
import os
import json
import sys
import pandas as pd
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

key = sys.argv[1]
bus_line = sys.argv[2]
stop_name = []
stop_status = []
stop_info = []
locations = []

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. please use \
    get_bus_info_yc3420.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv")
    
else:
    #request the json file
    api_url =  'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='+ key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line 

    #print (api_url)
    response = urllib.urlopen(api_url)
    data = response.read().decode("utf-8")
    dataDict = json.loads(data)


   #parameter prep
    schedule = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    

    for i in range(len(schedule)):    
        locations.append(schedule[i]['MonitoredVehicleJourney']['VehicleLocation'])
        #bus_number= len(locations)
        stop_info.append(schedule[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'])
        
        if stop_info == {}:
            stop_name.append('N/A')
            stop_status.append('N/A')
        
        else:
            stop_status.append(stop_info[i]['Extensions']['Distances']['PresentableDistance'])
            stop_name.append(stop_info[i]['StopPointName'])
        
        
        #make the csv file
        result_csv = pd.DataFrame({'Latitude':locations[i]["Latitude"],'Longitude':locations[i]["Longitude"],'Stop_Name':stop_name[i],'Status':stop_status[i]})
        result_csv.to_csv('%s.csv'%(sys.argv[2]),sep = ',')

