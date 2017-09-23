import random

def get_random_state():
    """ Returns a random state's dictionary from the data list """
    return random.choice(data)

def search_for_dict_entry(value):
    """ Searches for the input dictionary's value in the data list """
    for i in data:
        if value in i.values():
            return i
    return None

# State data is sorted by state name
data = [
        {
            "StateName": "Alabama",
            "abbreviation": "AL",
            "capital": "Montgomery",
            "image": "https://i.imgur.com/lmxzMAp.png"
        },
        # {
        #     "StateName": "Alaska",
        #     "abbreviation": "AK",
        #     "capital": "Juneau"
        # },
        {
            "StateName": "Arizona",
            "abbreviation": "AZ",
            "capital": "Phoenix",
            "image": "https://i.imgur.com/CfNVqcJ.png"
        },
        {
            "StateName": "Arkansas",
            "abbreviation": "AR",
            "capital": "Little Rock",
            "image": "https://i.imgur.com/GkEwX8H.png"
        },
        {
            "StateName": "California",
            "abbreviation": "CA",
            "capital": "Sacramento",
            "image": "https://i.imgur.com/NvnAAng.png"
        },
        {
            "StateName": "Colorado",
            "abbreviation": "CO",
            "capital": "Denver",
            "image": "https://i.imgur.com/bqQMLrg.png"
        },
        {
            "StateName": "Connecticut",
            "abbreviation": "CT",
            "capital": "Hartford",
            "image": "https://i.imgur.com/dN2yHft.png"
        },
        {
            "StateName": "Delaware",
            "abbreviation": "DE",
            "capital": "Dover",
            "image": 'https://i.imgur.com/rV7Bs9t.png'
        },
        {
            "StateName": "Florida",
            "abbreviation": "FL",
            "capital": "Tallahassee",
            "image": "https://i.imgur.com/iOvB0V7.png"
        },
        {
            "StateName": "Georgia",
            "abbreviation": "GA",
            "capital": "Atlanta",
            "image": "https://i.imgur.com/ozDxkye.png"
        },
        # {
        #     "StateName": "Hawaii",
        #     "abbreviation": "HI",
        #     "capital": "Honolulu"
        # },
        {
            "StateName": "Idaho",
            "abbreviation": "ID",
            "capital": "Boise",
            "image": "https://i.imgur.com/xVhL6KF.png"
        },
        {
            "StateName": "Illinois",
            "abbreviation": "IL",
            "capital": "Springfield",
            "image": "https://i.imgur.com/DQ0dOrE.png"
        },
        {
            "StateName": "Indiana",
            "abbreviation": "IN",
            "capital": "Boise",
            "image": "https://i.imgur.com/NHr5Kty.png"
        },
        {
            "StateName": "Iowa",
            "abbreviation": "IA",
            "capital": "Des Moines",
            "image": "https://i.imgur.com/EM1yhmj.png"
        },
        {
            "StateName": "Kansas",
            "abbreviation": "KS",
            "capital": "Topeka",
            "image": "https://i.imgur.com/LlyjHGd.png"
        },
        {
            "StateName": "Kentucky",
            "abbreviation": "KY",
            "capital": "Frankfort",
            "image": "https://i.imgur.com/W4uJxHF.png"
        },
        {
            "StateName": "Louisiana",
            "abbreviation": "LA",
            "capital": "Baton Rouge",
            "image": "https://i.imgur.com/0hsaM9j.png"
        },
        {
            "StateName": "Maine",
            "abbreviation": "ME",
            "capital": "Augusta",
            "image": "https://i.imgur.com/gy7tgnQ.png"
        },
        {
            "StateName": "Maryland",
            "abbreviation": "MD",
            "capital": "Annapolis",
            "image": "https://i.imgur.com/J8hyzjf.png"
        },
        {
            "StateName": "Massachusetts",
            "abbreviation": "MA",
            "capital": "Boston",
            "image": "https://i.imgur.com/6AHh9mw.png"
        },
        {
            "StateName": "Michigan",
            "abbreviation": "MI",
            "capital": "Lansing",
            "image": "https://i.imgur.com/0uLOYwC.png"
        },
        {
            "StateName": "Minnesota",
            "abbreviation": "MN",
            "capital": "Saint Paul",
            "image": "https://i.imgur.com/4q2S6no.png"
        },
        {
            "StateName": "Mississippi",
            "abbreviation": "MS",
            "capital": "Jackson",
            "image": "https://i.imgur.com/jIQHaVW.png"
        },
        {
            "StateName": "Missouri",
            "abbreviation": "MO",
            "capital": "Jefferson City",
            "image": "https://i.imgur.com/Aht1vE0.png"
        },
        {
            "StateName": "Montana",
            "abbreviation": "MT",
            "capital": "Helena",
            "image": "https://i.imgur.com/oMkMWHn.png"
        },
        {
            "StateName": "Nebraska",
            "abbreviation": "NE",
            "capital": "Lincoln",
            "image": "https://i.imgur.com/vbH9U8o.png"
        },
        {
            "StateName": "Nevada",
            "abbreviation": "NV",
            "capital": "Carson City",
            "image": "https://i.imgur.com/1kDsRAx.png"
        },
        {
            "StateName": "New Hampshire",
            "abbreviation": "NH",
            "capital": "Concord",
            "image": "https://i.imgur.com/J5fA7MD.png"
        },
        {
            "StateName": "New Jersey",
            "abbreviation": "NJ",
            "capital": "Trenton",
            "image": "https://i.imgur.com/t2W1bXt.png"
        },
        {
            "StateName": "New Mexico",
            "abbreviation": "NM",
            "capital": "Santa Fe",
            "image": "https://i.imgur.com/FX02qkp.png"
        },
        {
            "StateName": "New York",
            "abbreviation": "NY",
            "capital": "Albany",
            "image": "https://i.imgur.com/tSclKIw.png"
        },
        {
            "StateName": "North Carolina",
            "abbreviation": "NC",
            "capital": "Raleigh",
            "image": "https://i.imgur.com/dLiAnC1.png"
        },
        {
            "StateName": "North Dakota",
            "abbreviation": "ND",
            "capital": "Bismarck",
            "image": "https://i.imgur.com/wrhLYgt.png"
        },
        {
            "StateName": "Ohio",
            "abbreviation": "OH",
            "capital": "Columbus",
            "image": "https://i.imgur.com/EKzR9XX.png"
        },
        {
            "StateName": "Oklahoma",
            "abbreviation": "OK",
            "capital": "Oklahoma City",
            "image": "https://i.imgur.com/d0beWf6.png"
        },
        {
            "StateName": "Oregon",
            "abbreviation": "OR",
            "capital": "Salem",
            "image": "https://i.imgur.com/oXrEI0l.png"
        },
        {
            "StateName": "Pennsylvania",
            "abbreviation": "PA",
            "capital": "Harrisburg",
            "image": "https://i.imgur.com/CODKbXU.png"
        },
        {
            "StateName": "Rhode Island",
            "abbreviation": "RI",
            "capital": "Providence",
            "image": "https://i.imgur.com/A22BcsB.png"
        },
        {
            "StateName": "South Carolina",
            "abbreviation": "SC",
            "capital": "Columbia",
            "image": "https://i.imgur.com/V4gqpee.png"
        },
        {
            "StateName": "South Dakota",
            "abbreviation": "SD",
            "capital": "Pierre",
            "image": "https://i.imgur.com/ehvQmsG.png"
        },
        {
            "StateName": "Tennessee",
            "abbreviation": "TN",
            "capital": "Nashville",
            "image": "https://i.imgur.com/JsNP28k.png"
        },
        {
            "StateName": "Texas",
            "abbreviation": "TX",
            "capital": "Austin",
            "image": "https://i.imgur.com/I75z6zr.png"
        },
        {
            "StateName": "Utah",
            "abbreviation": "UT",
            "capital": "Salt Lake City",
            "image": "https://i.imgur.com/TRgwJNS.png"
        },
        {
            "StateName": "Vermont",
            "abbreviation": "VT",
            "capital": "Montpelier",
            "image": "https://i.imgur.com/DDMUTbD.png"
        },
        {
            "StateName": "Virginia",
            "abbreviation": "VA",
            "capital": "Richmond",
            "image": "https://i.imgur.com/x1ejsrV.png"
        },
        {
            "StateName": "Washington",
            "abbreviation": "WA",
            "capital": "Olympia",
            "image": "https://i.imgur.com/iElVW5K.png"
        },
        {
            "StateName": "West Virginia",
            "abbreviation": "WV",
            "capital": "Charleston",
            "image": "https://i.imgur.com/vILB497.png"
        },
        {
            "StateName": "Wisconsin",
            "abbreviation": "WI",
            "capital": "Madison",
            "image": "https://i.imgur.com/VEdsvEz.png"
        },
        {
            "StateName": "Wyoming",
            "abbreviation": "WY",
            "capital": "Cheyenne",
            "image": "https://i.imgur.com/cHtctJe.png"
        }
    ]
