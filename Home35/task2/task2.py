import time
import requests
import threading

urls = ["https://www.youtube.com/?app=desktop&hl=ru",
        "https://www.facebook.com/?locale=ru_RU",
        "https://teachmeskills.by/"]


def send_response(input_url):
    response = requests.get(input_url)
    print(f"{input_url} - {response.status_code}")


start_time = time.time()


threads = []
for url in urls:
    thread = threading.Thread(target=send_response, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"2 program time: {end_time - start_time} sec")


#  0.28-0.35
