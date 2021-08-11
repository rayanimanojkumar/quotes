import mysql.connector as MYSQL
from bs4 import BeautifulSoup
import requests

URL = 'https://parade.com/937586/parade/life-quotes/'
SQL = 'INSERT INTO quoteslist (id, Quotes) VALUES (%s,%s)'

CONFIG = {
    'user': 'root',
    'password': 'Demon@',
    'host': '127.0.0.1',
    'database': 'my_quotes',
    'charset': 'utf8mb4'
}
SELECT = 'span[data-parade-type="promoarea"] .figure_block ~ p'
GT = {'strip': True, 'separator': ' '}
with requests.Session() as session:
    web_page = session.get(URL)
    web_page.raise_for_status()
    soup = BeautifulSoup(web_page.text, "html.parser")
    quote = [(x.get_text(**GT)) for x in soup.select(SELECT)]
    with MYSQL.Connect(**CONFIG) as db:
        mycursor = db.cursor()
        for q in quote:
            idx = q.split()[0]
            if idx[0].isdigit():
                text = q[len(idx):].strip()
                params = (idx.replace('.', ''), text)
                mycursor.execute(SQL, params)
        db.commit()


































# URL = "https://parade.com/937586/parade/life-quotes/"
# SQL = "INSERT INTO quoteslist (id, Quotes) VALUES (%S,%S)"
#
# with requests.Session() as session:
#     web_page = session.get(URL)
#     web_page.raise_for_status()
#     soup = BeautifulSoup(web_page.text, "html.parser")
#     quote = [(x.get_text(strip=True, separator=" ")) for x in soup.select(
#         'span[data-parade-type="promoarea"] .figure_block ~ p')]
#     db = None
#     try:
#         db = mysql.connector.Connect(
#                 host="127.0.0.1",
#                 user="root",
#                 password="Demon@",
#                 database="my_quotes",
#                 charset="utf8mb4"
#              )
#         mycursor = db.cursor()
#         for q in quote:
#             idx = q.split()[0]
#             if idx[0].isdigit():
#                 text = q[len(idx):].strip()
#                 params = (idx.replace('.', ''), text)
#                 mycursor.execute(SQL, params)
#
#     except Exception as e:
#             pass
#     finally:
#         db.commit()
#         db.close()
#
#



# URL = "https://parade.com/937586/parade/life-quotes/"
#
# web_page = requests.get(URL)
#
# soup = BeautifulSoup(web_page.text, "html.parser")
#
# quote = [(x.get_text(strip=True, separator=" ")) for x in soup.select(
#         'span[data-parade-type="promoarea"] .figure_block ~ p')]
#
# db = mysql.connector.Connect(
#         host="127.0.0.1",
#         user="root",
#         password="Demon@",
#         database="my_quotes",
#         charset="utf8mb4"
#     )
#
# mycursor = db.cursor()
#
#
# mycursor.execute("")
# db.commit()
# db.close()





# mycursor.execute("SHOW TABLES")
# for x in mycursor:
# #       print(x)
# sql  = """INSERT INTO all_quotes(quote) VALUES(%s)"""
#
# cursor = db.cursor
#
# cursor.execute(sql, quote)
#
# db.commit()
#
# db.close()


# cursor = db.cursor()
# sql = "INSERT INTO  all_quotes(quote) VALUES(%s)"
#
# cursor.execute(sql,quote)
# db.commit()
#
# print(cursor.rowcount, "record inserted")



