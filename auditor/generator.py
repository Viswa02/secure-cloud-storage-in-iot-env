from bloom_filter import BloomFilter
import os

from config import MAX_ELEMENTS
from config import ERROR_RATE
from config import CHUNK_SIZE

def createBloomFilter():
    '''
        creates a bloom-filter with the project configuration.
    '''
    
    return BloomFilter(max_elements=MAX_ELEMENTS, error_rate=ERROR_RATE)

def generateMetaData(file):
    '''
        function to generate meta-data for a given file.
    '''

    file_name = file.name
    file_size = os.path.getsize(file.name)
    meta = {
        'name': file_name,
        'size': file_size
    }
    bf = createBloomFilter()
    remaining_size = file_size
    
    while remaining_size > 0:
        if remaining_size <= CHUNK_SIZE:
            file_bytes = file.read(remaining_size)
            remaining_size -= remaining_size
        else:
            file_bytes = file.read(CHUNK_SIZE)
            remaining_size -= CHUNK_SIZE
        bf.add(file_bytes)

    meta['bf'] = bf

    return meta