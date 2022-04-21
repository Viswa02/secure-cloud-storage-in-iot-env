import os
import sys
from bloom_filter import BloomFilter
import pickle
import random

from auditor.generator import generateMetaData
from auditor.validator import validate, generateRandromChunkNumbers
from cloud.cloudHandler import storeFile, generateSampleChunks

from config import CHUNK_SIZE, SAMPLE_PARAM

# localBf['name'] = 'test_input.txt'

# def generateSampleChunks(localBf):
#     '''
#         creates randrom number of data from the file.
#     '''

#     sampleChunks = []
#     remaining_size = localBf['size']
#     file = open(localBf['name'], 'rb')
        
#     while remaining_size > 0:
#         if remaining_size <= CHUNK_SIZE:
#             file_bytes = file.read(remaining_size)
#             remaining_size -= remaining_size
#         else:
#             file_bytes = file.read(CHUNK_SIZE)
#             remaining_size -= CHUNK_SIZE
        
#         if random.random() <= 0.3:
#             sampleChunks.append(file_bytes)

#     return sampleChunks

if sys.argv[1] == 'generate':
    # generate meta-data
    f = open('./iot/data/test_input.txt', 'rb')
    bf = generateMetaData(f)
    print(bf)
    f.close()

    # Store the meta-data in local storage
    with open('./meta_data/test.bf', 'wb') as bf_file:
        pickle.dump(bf, bf_file)

    file = open('./iot/data/test_input.txt', 'rb')

    storeFile(file)
elif sys.argv[1] == 'validate':
    # load the meta-data from local storage
    with open('./meta_data/test.bf', 'rb') as bf_file:
        localBf = pickle.load(bf_file)
    sampleChunkNums = generateRandromChunkNumbers(localBf['size'], SAMPLE_PARAM)
    sampleChunks = generateSampleChunks(sampleChunkNums, localBf['name'])
    print(localBf)
    print(f'Integrity: {validate(sampleChunks, localBf)}')