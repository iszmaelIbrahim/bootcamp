#Request

import requests

r = requests.get('https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49')
print(r)

body_ = r.content
print(f"AAAA {body_}")

state = {'key1': 'Melaka', 'key2': 'Selangor'}

r = requests.post("https://httpbin.org/post", data=state)
print(r.text)

#get request
# AAAA b'{\n  "id": "58611129-2dbc-4a81-a72f-77ddfc1b1b49",\n  "title": "My Neighbor Totoro",\n  "original_title": "\xe3\x81\xa8\xe3\x81\xaa\xe3\x82\x8a\xe3\x81\xae\xe3\x83\x88\xe3\x83\x88\xe3\x83\xad",\n  "original_title_romanised": "Tonari no Totoro",\n  "description": "Two sisters move to the country with their father in order to be closer to their hospitalized mother, and discover the surrounding trees are inhabited by Totoros, magical spirits of the forest. When the youngest runs away from home, the older sister seeks help from the spirits to find her.",\n  "director": "Hayao Miyazaki",\n  "producer": "Hayao Miyazaki",\n  "release_date": "1988",\n  "running_time": "86",\n  "rt_score": "93",\n  "people": [\n    "https://ghibliapi.herokuapp.com/people/986faac6-67e3-4fb8-a9ee-bad077c2e7fe",\n    "https://ghibliapi.herokuapp.com/people/d5df3c04-f355-4038-833c-83bd3502b6b9",\n    "https://ghibliapi.herokuapp.com/people/3031caa8-eb1a-41c6-ab93-dd091b541e11",\n    "https://ghibliapi.herokuapp.com/people/87b68b97-3774-495b-bf80-495a5f3e672d",\n    "https://ghibliapi.herokuapp.com/people/d39deecb-2bd0-4770-8b45-485f26e1381f",\n    "https://ghibliapi.herokuapp.com/people/591524bc-04fe-4e60-8d61-2425e42ffb2a",\n    "https://ghibliapi.herokuapp.com/people/c491755a-407d-4d6e-b58a-240ec78b5061",\n    "https://ghibliapi.herokuapp.com/people/f467e18e-3694-409f-bdb3-be891ade1106",\n    "https://ghibliapi.herokuapp.com/people/08ffbce4-7f94-476a-95bc-76d3c3969c19",\n    "https://ghibliapi.herokuapp.com/people/0f8ef701-b4c7-4f15-bd15-368c7fe38d0a"\n  ],\n  "species": [\n    "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",\n    "https://ghibliapi.herokuapp.com/species/603428ba-8a86-4b0b-a9f1-65df6abef3d3",\n    "https://ghibliapi.herokuapp.com/species/74b7f547-1577-4430-806c-c358c8b6bcf5"\n  ],\n  "locations": [\n    "https://ghibliapi.herokuapp.com/locations/"\n  ],\n  "vehicles": [\n    "https://ghibliapi.herokuapp.com/vehicles/"\n  ],\n  "url": "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49",\n  "length": null\n}'

#post request
# {
#   "args": {}, 
#   "data": "",
#   "files": {}, 
#   "form": {
#     "key1": "Melaka", 
#     "key2": "Selangor"
#   }, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Content-Length": "25", 
#     "Content-Type": "application/x-www-form-urlencoded", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.25.1", 
#     "X-Amzn-Trace-Id": "Root=1-60d44e89-4b946c152b538e2a66fc9f9e"
#   }, 
#   "json": null, 
#   "origin": "202.186.58.40", 
#   "url": "https://httpbin.org/post"
# }