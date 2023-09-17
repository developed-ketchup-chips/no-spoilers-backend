import pymongo 

client = pymongo.MongoClient("mongodb+srv://saphia:saphia@cluster0.ey8zati.mongodb.net/")

information = mydb.table1

rec[{
    "EMPNO": 7934,
    "ENAME": "MILLER",
    "JOB": "CLERK",
    "MGR": 7782,
    "SAL": 1300,
    "DEPTNO": 10
}]
information.insert_many(rec)