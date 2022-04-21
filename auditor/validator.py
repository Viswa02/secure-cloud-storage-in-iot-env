import random
import math

from config import CHUNK_SIZE

def validate(sampleChunks, meta):
    '''
        validates a files integrity.
    '''
    print(f'File size: {meta["size"]}')
    print(f'Number of samples: {len(sampleChunks)}')
    bf = meta['bf']
    for sampleChunk in sampleChunks:
        if not sampleChunk in bf:
            return False

    return True

def generateRandromChunkNumbers(file_size, sampleParam):
    '''
        generates randrom chunk numbers to be retrived from integrity verification
    '''
    sampleChunkNums = []
    remaining_size = file_size
    numOfChunks = math.ceil(file_size / CHUNK_SIZE)

    for i in range(numOfChunks):
        if random.random() < sampleParam:
            sampleChunkNums.append(i)    
    
    return sampleChunkNums