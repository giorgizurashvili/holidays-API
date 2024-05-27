import requests
import json
import sqlite3
country=input('sheiyvanet qveynis dasaxeleba mokled mag:GE')
key='4b0acdcd254c4d818905463727fa71e2'
year=input('Enter the year')
month=input('Enter the numeric name of the month ')
day=input('Enter the day')
url=f"https://holidays.abstractapi.com/v1/"
payload={'api_key':key,'country':country,'year':year,'month':month,'day':day}
response=requests.get(url,params=payload)
print(response.status_code)
print(response.url)
print(response)
print(response.headers)

data = response.json()
with open('jsonn.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

result_json = response.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
print(res_structured)
try:
    name =res[0]['name']
    print(f'at the time of your choice is {name} in {country}')
    conn = sqlite3.connect('holidays.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS holydays (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT,
            name TEXT,
            year TEXT,
            month TEXT,
            day TEXT
        )''')
    c.execute('''
        insert into holydays (country, name, year, month, day) VALUES (?, ?, ?, ?,?)
        ''', (country, name, year, month, day))
    conn.commit()
    conn.close()
except:
    print(f'There is no holiday in {country} on the date you selected')