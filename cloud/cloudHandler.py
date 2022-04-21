import os
import random

from config import CHUNK_SIZE

def storeFile(file):
    name = file.name.split('/')[-1]
    with open(f'./cloud/data/{name}', 'wb') as cloudFile:
        cloudFile.write(file.read())

def generateSampleChunks(chunks, name):
    '''
        creates randrom number of data from the file.
    '''

    sampleChunks = []
    name = name.split('/')[-1]
    with open(f'./cloud/data/{name}', 'rb') as file:
        file_size = os.path.getsize(file.name)
        remaining_size = file_size

        chunkNum = 0
        
        while remaining_size > 0 and chunkNum <= len(chunks):
            if remaining_size <= CHUNK_SIZE:
                file_bytes = file.read(remaining_size)
                remaining_size -= remaining_size
            else:
                file_bytes = file.read(CHUNK_SIZE)
                remaining_size -= CHUNK_SIZE
            
            if chunkNum in chunks:
                sampleChunks.append(file_bytes)
            chunkNum += 1

    return sampleChunks