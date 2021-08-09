import pandas

url = 'https://data.sfgov.org/api/views/rqzj-sfat/rows.csv'
foodtruckdata = pandas.read_csv(url)
foodtruckdatanohead = foodtruckdata.drop('locationid')
print(foodtruckdatanohead)
#print(type(foodtruckdata))
#print(foodtruckdata.loc[1])