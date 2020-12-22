import json

data = '''
 { 
  "name" : "Felix",
  "phone" : {
     "type" : "intl",
     "number" : "+254796854357"
  },
   "email" : {
      "hide" : "yes"
  }
}'''

info = json.loads(data)
print('Name: ', info["name"])
print('Phone: ', info["phone"]["number"])
print('Hide: ', info["email"] ["hide"])