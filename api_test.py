import requests
import json

url = 'http://localhost:8008/api/ask'

question = "How can I eat a hot dog underwater? 🌭🤿"

payload = json.dumps({
    "phrase": question
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    print("Answer:", response.json().get('answer'))
else:
    print("Error:", response.status_code, response.text)