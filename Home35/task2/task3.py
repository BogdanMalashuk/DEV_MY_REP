import time
import requests
import multiprocessing

urls = ["https://www.youtube.com/?app=desktop&hl=ru",
        "https://www.facebook.com/?locale=ru_RU",
        "https://teachmeskills.by/"]


def send_response(input_url):
    response = requests.get(input_url)
    print(f"{input_url} - {response.status_code}")


if __name__ == "__main__":
    start_time = time.time()

    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(send_response, urls)

    end_time = time.time()
    print(f"3 program time: {end_time - start_time} sec")


#  0.44-0.47
