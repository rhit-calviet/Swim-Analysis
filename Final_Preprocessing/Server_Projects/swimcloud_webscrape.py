from zenrows import ZenRowsClient

client = ZenRowsClient("6cedce8cd36ea79dd85419706bd2f34e599ce26b")
url = "https://www.swimcloud.com/country/usa/college/division/1/records/F/Y/UNOV/"

response = client.get(url)

print(response.text)