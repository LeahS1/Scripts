'''
Using Google Map API to find a location's coordinates
'''

import urllib
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse({'key':'{Replace with Key}','sensor':'false', 'address': address})
    print (1)
    print (urllib.parse({'key':'{Replace with Key}','sensor':'false', 'address': address}))
    

    print ('Retrieving', url)
    uh = urllib.urlopen(url)
    data = uh.read()
    print ('Retrieved',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    print (json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print ('lat',lat,'lng',lng)
    try:
       location = js['results'][0]['address_components'][3]['short_name']
       print(location)
    except: 
        print ('Country code could not be found for this location')
