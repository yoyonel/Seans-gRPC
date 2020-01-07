"""A module for runnin the client an N processes"""
from multiprocessing import Process
import client

if __name__ == "__main__":
    COUNT = 32
    PROCESSES = {}
    for x in range(COUNT):
        PROCESSES[x] = Process(target=client.run)

    for x in range(COUNT):
        PROCESSES[x].start()
