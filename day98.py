import multiprocessing
import requests


def downloadFile(url, names):
    print(f"start downloading{names}")
    response = requests.get(url)
    open(f"files2/file{names}.jpg", "wb").write(response.content)
    print(f"finished downloading{names}")
if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(50):
        # downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

