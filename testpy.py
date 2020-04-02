import urllib.request, json
github_link = "https://gauravghati.github.io/apis/home.json"
with urllib.request.urlopen(github_link) as url: 
   json_data = json.loads(url.read().decode())
print(json_data)