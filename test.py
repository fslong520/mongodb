#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' mongodb学习 '

__author__ = 'fslong'
import pymongo
client=pymongo.MongoClient(host='localhost',port=27017)
db=client['test']
collection=db['students']
student={
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
result=collection.insert_one(student)
print(result)
print(result.inserted_id)
student1={
    'id':'20170102',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
student2={
    'id':'20170103',
    'name':'Jordan',
    'age':22,
    'gender':'male'
}
result=collection.insert_many([student1,student2])
print(result)
print(result.inserted_ids)
results=collection.find({'age':{'$lte':20}})
for i in results:
    print(i)