import pymongo
client=pymongo.MongoClient()
mydb=client["mydb"]
mycol=mydb["SendtoMessage"]
data={'name':"Arya", 'eposta':"arya@gmail.com", 'message':"Web site is so great. Thx"}
mycol.insert_one(data)