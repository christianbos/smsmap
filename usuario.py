import requests

dicc = {}

headers = {'content-type':'application/json; charset=UTF-8'}
elId = '&trailId=4503921934467072'
url = "https://mapaton-public.appspot.com/_ah/api/dashboardAPI/v1/getTrailRawPoints?fields=points"+elId
# payload = {"trailId": "4503921934467072" , "numberOfElements":30, "cursor":""}
data = requests.post(url, headers=headers)
data = data.json()
puntos = data
points = puntos["points"]
i = 0

for item in points:

    lon = item['location']['longitude']
    lat = item['location']['latitude']
    dicc[i] = [lon,lat]
    i = i+1

print(dicc)
