import pandas


url = 'https://data.sfgov.org/api/views/rqzj-sfat/rows.csv'
c = pandas.read_csv(url)
c = c.drop(["locationid", "FacilityType", "cnn", "LocationDescription", "blocklot", "block", "lot", "permit", "Status", "FoodItems", "X", "Y", "Schedule", "dayshours", "NOISent", "Approved", "Received", "PriorPermit", "ExpirationDate", "Location", "Fire Prevention Districts", "Police Districts", "Supervisor Districts", "Zip Codes", "Neighborhoods (old)"], axis = 1)
for index in c.index:
    latitude = float(c['Latitude'][index])
    longitude = float(c['Longitude'][index])
    if latitude or longitude == 0:
        latitude = 0
        longitude = 0
        c = c.drop([c.index[index]])
        #index -= 1


    print(latitude, 'latitude')
    print(longitude, 'longitude')

print(c)

    
    #print(row['Latitude'], row['Longitude'])
