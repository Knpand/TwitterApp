import catAPI
import twitterAPI
import threading


if __name__ == "__main__":
    thread_1 = threading.Thread(target=catAPI.autoreply)
    thread_2 = threading.Thread(target=twitterAPI.autoreply)

    thread_1.start()
    thread_2.start()