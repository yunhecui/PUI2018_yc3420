from __future__ import print_function
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


key = sys.argv[1]
bus_line = sys.argv[2]

api_url =  'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' +\
    key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line 

print (api_url)
response = urllib.urlopen(api_url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

#print (dataDict)
schedule = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
locations =[]
for i in range(0, len(schedule)):    
    locations.append(schedule[i]['MonitoredVehicleJourney']['VehicleLocation'])
    bus_number= len(locations)

print ("BUS LINE: ",bus_line)
print ("Number of Active Buses:",len(schedule))
#print (bus_number)
#print (locations)
# output schedule
for i in range(0, len(schedule)):
    print ("Bus",i,"is at latitude",locations[i]["Latitude"],"and longitude",locations[i]["Longitude"])
    
















    
