import requests
from openpyxl import Workbook
import random

def random_sample():
    return random.choices(range(100_000, 1_000_001), k=1)

# Write the data to an Excel file
workbook = Workbook()
sheet = workbook.active
sheet.title = "Swimming Times"
 
headers_written = 0

url = "https://usaswimming.sisense.com/api/datasources/USA%20Swimming%20Times%20Elasticube/jaql?trc=sdk-ui-1.23.0"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNjRhZjE4MGY5Nzg1MmIwMDJkZTU1ZDhkIiwiYXBpU2VjcmV0IjoiZDBhYTNhYTItYmQxZS1mNmY2LTNmN2ItZjhmY2Y1MGIzN2ZlIiwiYWxsb3dlZFRlbmFudHMiOlsiNjRhYzE5ZTEwZTkxNzgwMDFiYzM5YmVhIl0sInRlbmFudElkIjoiNjRhYzE5ZTEwZTkxNzgwMDFiYzM5YmVhIn0.h8Mts3Y9ekmCKiUB_4bspnWOHGaOTuSjItm7qd7st6I",
    "Content-Type": "application/json",
}

# Tomasso: 628907
# Vineet: 370891
# Blaise: 156314
# person_keys = [62807, 370891, 156314]

person_keys = random_sample()

# for person_key in range(0, 5_000_000):

# random sample of 10,000 people
# for person_key in person_keys:
person_count = 0
while person_count < 10:

    person_key = random_sample()[0]

    payload = {
        "metadata": [
            {
                "jaql": {
                    "title": "Event",
                    "dim": "[SwimEvent.EventCode]",
                    "datatype": "text"
                }
            },
            {
                "jaql": {
                    "title": "Swim Time",
                    "dim": "[UsasSwimTime.SwimTimeFormatted]",
                    "datatype": "text"
                }
            },
            {
                "jaql": {
                    "title": "Age",
                    "dim": "[UsasSwimTime.AgeAtMeetKey]",
                    "datatype": "numeric"
                }
            },
            {
                "jaql": {
                    "title": "Points",
                    "dim": "[UsasSwimTime.PowerPoints]",
                    "datatype": "numeric"
                }
            },
            {
                "jaql": {
                    "title": "Time Standard",
                    "dim": "[TimeStandard.TimeStandardName]",
                    "datatype": "text"
                }
            },
            {
                "jaql": {
                    "title": "Meet",
                    "dim": "[Meet.MeetName]",
                    "datatype": "text"
                }
            },
            {
                "jaql": {
                    "title": "LSC",
                    "dim": "[OrgUnit.Level3Code]",
                    "datatype": "text"
                }
            },
            {
                "jaql": {
                    "title": "Team",
                    "dim": "[OrgUnit.Level4Name]",
                    "datatype": "text"
                }
            },
            {
                "jaql": {
                    "title": "Swim Date",
                    "dim": "[SeasonCalendar.CalendarDate (Calendar)]",
                    "datatype": "datetime",
                    "level": "days"
                },
                "format": {
                    "mask": {
                        "days": "MM/dd/yyyy"
                    }
                }
            },
            {
                "jaql": {
                    "title": "PersonKey",
                    "dim": "[UsasSwimTime.PersonKey]",
                    "datatype": "numeric"
                }
            },
            {
                "jaql": {
                    "title": "SwimEventKey",
                    "dim": "[UsasSwimTime.SwimEventKey]",
                    "datatype": "numeric"
                }
            },
            {
                "jaql": {
                    "title": "MeetKey",
                    "dim": "[UsasSwimTime.MeetKey]",
                    "datatype": "numeric"
                }
            },
            {
                "jaql": {
                    "title": "SortKey",
                    "dim": "[UsasSwimTime.SortKey]",
                    "datatype": "text",
                    "sort": "asc"
                }
            },
            {
                "jaql": {
                    "title": "UsasSwimTimeKey",
                    "dim": "[UsasSwimTime.UsasSwimTimeKey]",
                    "datatype": "numeric"
                }
            },
            {
                "jaql": {
                    "title": "PersonKey",
                    "dim": "[UsasSwimTime.PersonKey]",
                    "datatype": "numeric",
                    "filter": {
                        "equals": person_key
                    }
                },
                "panel": "scope"
            },
            {
                "jaql": {
                    "title": "AgeKey",
                    "dim": "[Age.AgeKey]",
                    "datatype": "numeric",
                    "filter": {
                        "from": 13,
                        "to": 24
                    }
                },
                "panel": "scope"
            }
        ],
        "datasource": {
            "title": "USA Swimming Times Elasticube",
            "live": False
        },
        "by": "ComposeSDK",
        "queryGuid": "fffd8b61-4d21-4f1c-a07a-b6e56c014c3f",
        "count": 500
    }

    response = requests.post(url, json=payload, headers=headers)

    # Check the response
    # print(response.json())

    # file_path = 'swimming_times.json'

    # Write the response to a JSON file
    # with open(file_path, 'w') as json_file:
    #     json.dump(response.json(), json_file, indent=4)

    # Extract response data
    data = response.json()
    headers_list = data.get("headers", [])
    values = data.get("values", [])

    print(values)
    # Append headers only once
    if headers_written == 0:
        sheet.append(headers_list)
        headers_written = 1

    if values:
        person_count += 1
        # Write rows
        for row in values:
            sheet.append([cell.get("text") for cell in row])
    
# Save the workbook    
excel_file_path = "swimming_times.xlsx"
workbook.save(excel_file_path)
print(f"Data written to {excel_file_path}")
