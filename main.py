import pymongo

DEFAULT_CONNECTION_URL = "mongodb://localhost:27017"
DB_NAME = "Assignment1"
client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)

database = client['Assignment1']

sri=[
    {
    "Product": 'tv',
    "Name": 'Jidesh C',
    "Rating": '4',
    "Comment": 'Initial impression was very good, nice 4k tv, picture clarity is very good in this price range, sound also good loud and clearWill write detailed review after some days of use'
    },
 {
    "Product": 'tv',
    "Name": 'Jayaraman Desingou',
    "Rating": "5",
    "Comment": 'Very good TV. Decent picture quality and sound effect. Value for money. I am just expecting this TV to work for 4 years.'
}
]
collection_name = "AssignmentMongo"
collection = database[collection_name]

collection.insert_many(sri)