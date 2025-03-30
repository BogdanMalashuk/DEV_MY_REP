import time
import requests

urls = ["https://www.youtube.com/?app=desktop&hl=ru",
        "https://www.facebook.com/?locale=ru_RU",
        "https://teachmeskills.by/"]


def send_response(input_url):
    response = requests.get(input_url)
    print(f"{input_url} - {response.status_code}")


start_time = time.time()

for url in urls:
    send_response(url)

end_time = time.time()
print(f"1 program time: {end_time - start_time} sec")


#  0.60-0.85
