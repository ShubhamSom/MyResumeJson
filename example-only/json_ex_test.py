import json
from pprint import pprint

json_data = """
[
  {
    "_id": "6182b56d82f544009fdfe7b9",
    "index": 0,
    "guid": "ecc46f86-eedf-423c-b1c1-d8887085b86e",
    "isActive": false,
    "balance": "$2,365.27",
    "picture": "http://placehold.it/32x32",
    "age": 25,
    "eyeColor": "blue",
    "name": "Pacheco Harvey",
    "gender": "male",
    "company": "SLAMBDA",
    "email": "pachecoharvey@slambda.com",
    "phone": "+1 (967) 542-3584",
    "address": "112 Gunnison Court, Kaka, Puerto Rico, 7487",
    "about": "Aliqua excepteur ex sunt aliquip. Commodo consequat cillum cillum dolore consequat eiusmod officia. Fugiat minim consectetur ipsum culpa fugiat consequat sunt sit. Ullamco laboris qui excepteur commodo cupidatat cillum velit aliquip cillum. Tempor sit ut consequat dolore anim amet enim commodo ex ut nulla incididunt aliquip.\r\n",
    "registered": "2020-02-04T09:35:01 -06:-30",
    "latitude": -86.26695,
    "longitude": 117.783998,
    "tags": [
      "Lorem",
      "eiusmod",
      "sit",
      "est",
      "reprehenderit",
      "eu",
      "eiusmod"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Eleanor Douglas"
      },
      {
        "id": 1,
        "name": "Virgie Olson"
      },
      {
        "id": 2,
        "name": "Thomas Phillips"
      }
    ],
    "greeting": "Hello, Pacheco Harvey! You have 9 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": "6182b56d3341d6354046bc5b",
    "index": 1,
    "guid": "15b79198-368a-4d9c-8265-1cc92e57918f",
    "isActive": true,
    "balance": "$1,882.51",
    "picture": "http://placehold.it/32x32",
    "age": 30,
    "eyeColor": "brown",
    "name": "Goodwin Newman",
    "gender": "male",
    "company": "POSHOME",
    "email": "goodwinnewman@poshome.com",
    "phone": "+1 (983) 406-2743",
    "address": "991 Kenmore Court, Wheaton, Ohio, 6133",
    "about": "Sint Lorem proident ea pariatur est excepteur enim commodo. Occaecat minim officia sunt tempor sunt nostrud anim aliqua ut enim reprehenderit. Aute exercitation enim nulla Lorem culpa deserunt. Minim sint fugiat proident id quis veniam laboris irure ut. Amet nisi et fugiat dolore proident nisi consequat ullamco enim. Velit id aliqua culpa ea tempor ut mollit quis enim.\r\n",
    "registered": "2015-08-14T12:55:30 -06:-30",
    "latitude": 41.623095,
    "longitude": 57.249161,
    "tags": [
      "irure",
      "nulla",
      "cillum",
      "consequat",
      "id",
      "qui",
      "eiusmod"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Wilson Hamilton"
      },
      {
        "id": 1,
        "name": "Virginia Maxwell"
      },
      {
        "id": 2,
        "name": "Allison Heath"
      }
    ],
    "greeting": "Hello, Goodwin Newman! You have 7 unread messages.",
    "favoriteFruit": "banana"
  },
  {
    "_id": "6182b56da99fb46ee80f7245",
    "index": 2,
    "guid": "341e6cd5-49d0-427d-b080-2ffec5698ffa",
    "isActive": true,
    "balance": "$3,737.65",
    "picture": "http://placehold.it/32x32",
    "age": 20,
    "eyeColor": "brown",
    "name": "Earnestine Kline",
    "gender": "female",
    "company": "VIOCULAR",
    "email": "earnestinekline@viocular.com",
    "phone": "+1 (828) 546-3103",
    "address": "415 Lott Street, Carlton, Mississippi, 6193",
    "about": "Consequat non velit mollit eiusmod et eiusmod cupidatat. Nisi velit occaecat ad labore nostrud ad dolore. Deserunt aliqua adipisicing consectetur elit nisi ullamco eu. Quis ex Lorem cillum reprehenderit.\r\n",
    "registered": "2016-10-31T02:02:23 -06:-30",
    "latitude": -82.68876,
    "longitude": 0.964558,
    "tags": [
      "laboris",
      "veniam",
      "aute",
      "commodo",
      "mollit",
      "incididunt",
      "id"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Hobbs Sanchez"
      },
      {
        "id": 1,
        "name": "Effie Hubbard"
      },
      {
        "id": 2,
        "name": "Wyatt Chaney"
      }
    ],
    "greeting": "Hello, Earnestine Kline! You have 4 unread messages.",
    "favoriteFruit": "banana"
  },
  {
    "_id": "6182b56de2b74ac23887797b",
    "index": 3,
    "guid": "7abcbeae-6701-45a7-8a33-1fea9117d6f7",
    "isActive": false,
    "balance": "$2,921.12",
    "picture": "http://placehold.it/32x32",
    "age": 37,
    "eyeColor": "brown",
    "name": "Singleton Rich",
    "gender": "male",
    "company": "QUILTIGEN",
    "email": "singletonrich@quiltigen.com",
    "phone": "+1 (875) 587-3238",
    "address": "649 Sullivan Place, Nord, Virginia, 5828",
    "about": "Ex veniam dolor est veniam id. Ut et sint dolor sint. Do adipisicing anim consectetur aliquip officia reprehenderit. Amet nisi aute laboris nostrud minim officia mollit consequat cupidatat esse occaecat sint. Irure sunt sit esse commodo laborum consectetur. Excepteur consectetur in magna aliqua dolore consectetur esse est labore excepteur cupidatat aliqua eiusmod.\r\n",
    "registered": "2018-04-12T09:27:57 -06:-30",
    "latitude": -34.810899,
    "longitude": -18.698872,
    "tags": [
      "deserunt",
      "dolor",
      "aliquip",
      "velit",
      "eu",
      "reprehenderit",
      "excepteur"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Muriel Beach"
      },
      {
        "id": 1,
        "name": "Nadine Fitzgerald"
      },
      {
        "id": 2,
        "name": "Wiggins Griffith"
      }
    ],
    "greeting": "Hello, Singleton Rich! You have 2 unread messages.",
    "favoriteFruit": "banana"
  },
  {
    "_id": "6182b56d50e1066dc65fcfc1",
    "index": 4,
    "guid": "c679d4c8-3285-4bdc-b202-195a3c7c9494",
    "isActive": true,
    "balance": "$1,650.84",
    "picture": "http://placehold.it/32x32",
    "age": 40,
    "eyeColor": "brown",
    "name": "Blackwell Mann",
    "gender": "male",
    "company": "KINDALOO",
    "email": "blackwellmann@kindaloo.com",
    "phone": "+1 (979) 505-3051",
    "address": "932 Dupont Street, Bellamy, New Mexico, 227",
    "about": "Magna cupidatat esse quis enim exercitation adipisicing proident est et magna. Ullamco cupidatat anim nostrud est occaecat consequat anim Lorem quis. Mollit aliquip excepteur nostrud nulla exercitation ad voluptate laboris occaecat pariatur ad aute. Nostrud magna ullamco proident occaecat commodo fugiat nisi esse ea fugiat. Eiusmod ex est voluptate qui est nostrud occaecat occaecat. Nisi minim occaecat qui id tempor commodo eiusmod proident mollit consequat.\r\n",
    "registered": "2014-09-19T04:50:13 -06:-30",
    "latitude": -77.723613,
    "longitude": -140.852834,
    "tags": [
      "sit",
      "pariatur",
      "exercitation",
      "minim",
      "cillum",
      "aute",
      "tempor"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Cooper Cortez"
      },
      {
        "id": 1,
        "name": "Fowler Gay"
      },
      {
        "id": 2,
        "name": "Guerra Gutierrez"
      }
    ],
    "greeting": "Hello, Blackwell Mann! You have 8 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": "6182b56dd0f5339347dcc754",
    "index": 5,
    "guid": "2ced47d9-1cb8-4c9f-84d6-260eb4086703",
    "isActive": false,
    "balance": "$2,708.81",
    "picture": "http://placehold.it/32x32",
    "age": 38,
    "eyeColor": "blue",
    "name": "Rosemarie Fox",
    "gender": "female",
    "company": "ONTALITY",
    "email": "rosemariefox@ontality.com",
    "phone": "+1 (806) 536-3774",
    "address": "785 Overbaugh Place, Rote, Kansas, 6630",
    "about": "Consequat laborum reprehenderit dolor aliquip est mollit. Do proident do ex mollit eiusmod cupidatat officia consequat anim cupidatat ut ex. Ullamco sunt nulla officia cillum reprehenderit deserunt eiusmod fugiat anim non eiusmod.\r\n",
    "registered": "2020-07-19T12:24:29 -06:-30",
    "latitude": 83.379138,
    "longitude": -176.912795,
    "tags": [
      "deserunt",
      "sint",
      "nostrud",
      "do",
      "ut",
      "nostrud",
      "elit"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Irwin Ramsey"
      },
      {
        "id": 1,
        "name": "Rachael Gillespie"
      },
      {
        "id": 2,
        "name": "Mcdaniel Mathis"
      }
    ],
    "greeting": "Hello, Rosemarie Fox! You have 8 unread messages.",
    "favoriteFruit": "strawberry"
  },
  {
    "_id": "6182b56d1f8ca8d4ad1b1bf8",
    "index": 6,
    "guid": "7c0ca8f1-8010-4184-916c-2853f92af752",
    "isActive": true,
    "balance": "$3,491.46",
    "picture": "http://placehold.it/32x32",
    "age": 23,
    "eyeColor": "brown",
    "name": "Marquita Britt",
    "gender": "female",
    "company": "ZANILLA",
    "email": "marquitabritt@zanilla.com",
    "phone": "+1 (972) 493-2670",
    "address": "196 Losee Terrace, Blodgett, Minnesota, 2507",
    "about": "Tempor ullamco sit labore adipisicing eiusmod magna mollit occaecat culpa labore. Minim adipisicing sunt id incididunt anim esse ullamco quis. Sint sunt aliqua anim id laboris qui aliqua laborum Lorem velit.\r\n",
    "registered": "2016-07-04T01:51:53 -06:-30",
    "latitude": -46.642509,
    "longitude": -69.901194,
    "tags": [
      "esse",
      "excepteur",
      "quis",
      "veniam",
      "ut",
      "ea",
      "occaecat"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Madeleine Sullivan"
      },
      {
        "id": 1,
        "name": "Mccarthy Ashley"
      },
      {
        "id": 2,
        "name": "Ebony Wilcox"
      }
    ],
    "greeting": "Hello, Marquita Britt! You have 4 unread messages.",
    "favoriteFruit": "apple"
  }
]
"""
print(type(json_data))
pprint(json_data)

json_obj=json.loads(json_data)
print(json_obj)