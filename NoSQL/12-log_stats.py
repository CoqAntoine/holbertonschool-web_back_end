#!/usr/bin/env python3
""" 12-log_stats.py """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Nombre total de logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Nombre de documents par méthode
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Nombre de documents avec method=GET et path=/status
    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
