# This is written for PYTHON 2.7

import requests
import json
from pymongo import MongoClient

# client = MongoClient('54.210.240.10', 27010)


# def connect_to_mongo():
# Variable instantiation for EC2
ssh_address = "ubuntu@ec2-54-234-221-196.compute-1.amazonaws.com"
ssh_port = 27010
mongo_username = "nelsonyang"
mongo_password = "nelneltime"
private_key = "idiots.pem"
try:
    #client = MongoClient("mongodb://" + ssh_address + ":27017")
    client = MongoClient(ssh_address, 27017,
             ssl=True, ssl_keyfile='idiots.pem')

    db = client.test

    print "SUCCESS"

    client.database_names()

    #auth = client.test.authenticate(mongo_username,mongo_password)

    #print "SUCCESS"

    db.test.insert({test: "SUCCESS"})
    client.close()

except Exception as e:
    print "MongoDB connection failure: Please check the connection details"
    print e


# connect_to_mongo()

def lambda_handler(event, context):

    # print 'The click type is: ' + str(event.get('clickType'))

    # Variable Instantiation
    customerId = '57f1a3f0267ebde464c48a88'  # the customerId
    parentId = '57f1a4ca267ebde464c48a89'  # fake accountID for John Doe
    childId = '57f1a546267ebde464c48a8a'  # fake acountID for childOne
    apiKey = '?key=3163b60bbcdb2b1f90d9330fe46e45b6'  # Nessie API key for Julie

    amount = 3.14  # amount to be transferred
    description = 'Baby Got Cash'
    headers = {"content-type": "application/json"}

    baseUrl = 'http://api.reimaginebanking.com/'

    # Connect to MongoDB on EC2

    # Payload Setup
    transferPayload = {
        "medium": "balance",
        "payee_id": childId,
        "amount": amount,
        "description": description
    }

    # Make a Transfer
    transfer = requests.post(
        baseUrl + 'accounts/' + parentId + '/transfers' + apiKey,
        data=json.dumps(transferPayload),
        headers=headers
    )

    return 'Transfer status code: ' + str(transfer.status_code)
