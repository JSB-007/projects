from pymongo import MongoClient

# MongoDB connection settings
host = 'localhost'  # MongoDB server host
port = 27017  # MongoDB server port
database_name = 'your_database_name'  # Name of your database

# Create a MongoDB client
client = MongoClient(host, port)

# Access your database
db = client[database_name]

# Access a collection within the database
collection = db['your_collection_name']

# Now you can perform database operations
# For example, you can insert a document into the collection
data = {'name': 'John Doe', 'age': 25}
result = collection.insert_one(data)
print(f"Inserted document ID: {result.inserted_id}")

# You can also query the collection
query = {'name': 'John Doe'}
result = collection.find(query)
for document in result:
    print(document)

# Close the connection
client.close()

