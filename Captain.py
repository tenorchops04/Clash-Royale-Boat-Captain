import json 
import requests

# Prompt user for clan tag, which is used in the API request.
clanTag = raw_input("Enter clan tag: ")
print('')

# API token must be passed in every request in Authorization HTTP header using Bearer authentication scheme.
headers = {
    "authorization": "Bearer "
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9."
    "eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFhN2UxOWRhLTU2ODItNDYzOC04N"
    "zU0LTBhYzQwMzFmMmQ0YyIsImlhdCI6MTYwMDExNzI1Mywic3ViIjoiZGV2ZWxvcGVyLzMxZTIxNTNmLWYyNzQtODg2My01ZjU"
    "3LTVmNGJhNDRmNWRiYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsIn"
    "R5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3NS4xNDIuMjE3LjEwMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.V5I49akr7m"
    "DoWHPhIWeheoQolxBrR5UqMKS-GcMrEED4ZlVxWKJIF6IgfJEpXpjU3hx_MT5sY4WO1aPL4ymKng"
}

base = "https://api.clashroyale.com/v1/clans/%23" # The url for making the API request.
end = "/riverracelog"                             # The ending portion of the url. This one retrieves the clan's river race log.

urlClan = base + clanTag + end                    # Build the completed url to make the request.

# Get the requested data from the API.
responseClan = requests.get(urlClan, headers=headers) # Stores the data from the API
clanData = json.loads(responseClan.text)              # Converts the data to appropriate python variable types

# Get the names of each player in each clan, along with their fame and repair points. Print them out to console.
for item in clanData['items']:
    for standing in item['standings']:
        print(standing['clan']['name'])
        for participant in standing['clan']['participants']:
            print(participant['name'])
            print('\tFame: %s' % participant['fame'])
            print('\tRepair Points: %s' % participant['repairPoints'])
            print('')
        print('')

