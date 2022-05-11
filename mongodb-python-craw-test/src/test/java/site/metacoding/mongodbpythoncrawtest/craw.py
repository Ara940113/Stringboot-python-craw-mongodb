# 크롤링

# python -m pip install beautifulsoup4

from datetime import datetime
import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.cursor import CursorType

def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result

# Mongo 연결
mongo = MongoClient("localhost", 20000)

#크롤링
list = []
aid =["0000000001","0000000002","0000000003","0000000004","0000000005","0000000006","0000000007","0000000008","0000000009","0000000010","0000000011","0000000012","0000000013","0000000014","0000000015","0000000016","0000000017","0000000018","0000000019","0000000020"] 

for a in aid:
    try:
        html = requests.get(
         f"https://n.news.naver.com/mnews/article/005/{a}?sid=100")
        soup = BeautifulSoup(html.text, 'html.parser')

        company_el = soup.select_one(".media_end_linked_more_point")
        title_el = soup.select_one(".media_end_head_headline")
        createdAt_el = datetime.datetime.now()

        # print(company_el.get_text())
        # print(title_el.get_text())
        # print(createdAt_el.string)
         # print(html.status_code)
        if(html.status_code == 200):
            dict = {"company":company_el.get_text(),"title":title_el.get_text(),"createdAt": createdAt_el}
            list.append(dict)
    except Exception as e:
        pass
print(len(list))
a= mongo_save(mongo,list, "greendb", "navers")  # List안에 dict을 넣어야 함






