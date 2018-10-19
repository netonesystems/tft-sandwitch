#Need to install requests package for python
#easy_install requests
import requests
import json

def rest(gamename, scoreapi):
    # Set the request parameters
    url = 'https://dev54622.service-now.com/api/now/table/u_game_score'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'RestClient'
    pwd = 'dev54622'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    sample = {'u_game_title': gamename, 'u_player': 'koseda', 'u_score': scoreapi}
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(sample))


    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
