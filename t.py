import os
import time
from os.path import join, getsize

filename = "D:\\workplace\\picture\\6"
# def get_file():
#     l=[]
#     for root,dirs,files in os.walk()

def getOneFileTime(filename):

    filemt = time.localtime(os.stat(filename).st_mtime)
    print(filemt)
    print(time.strftime("%Y-%m-%d %H:%M:%S", filemt))

if __name__ == '__main__':
    k=os.walk(filename)
    for root, dirs, files in os.walk(filename):
        print(files)
