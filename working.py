import requests
import datetime
from datetime import datetime
import yadisk

# Задача №1

resp = requests.get("https://akabab.github.io/superhero-api/api/all.json")
our_superheros = {}
for superheros in resp.json():
    if superheros["name"] == "Hulk" or superheros["name"] == "Captain America" or superheros["name"] == "Thanos":
        our_superheros.setdefault(superheros["name"], superheros["powerstats"]["intelligence"])

print(f'Smartest superhero - {max(our_superheros).upper()}!!!')

# Задача №2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": f'OAuth {token}'}
        params = {"path": "Netology 18.03.2023.txt", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        href = data.get("href")
        response = requests.put(href, data=open("test.txt", "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("File downloaded")
        else:
            print(response.status_code)


if __name__ == "__main__":
    path_to_file = "Netology 18.03.2023.txt"
    token = "TOKEN"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

# Задача №2

y = yadisk.YaDisk(token="TOKEN")
y.remove("/test.txt", permanently=True)
y.upload("test.txt", "/test.txt")

# Задача №3 *


def get_questions(days, tagged):
    one_day_unix_time = 86400
    current_datetime = int(datetime.timestamp(datetime.now()))
    past_datetime = current_datetime - days * one_day_unix_time

    PARAMETERS = dict(fromdate=past_datetime, todate=current_datetime, tagged=tagged, site="stackoverflow")

    response = requests.get("https://api.stackexchange.com//2.3/questions", params=PARAMETERS)
    for questions in response.json().get("items"):
        print(f'{questions["title"]}\n{questions["tags"]}\n'
              f'{datetime.fromtimestamp(questions["creation_date"]).strftime("%Y-%m-%d")}\n{"*" * 40}')


get_questions(2, "python")