import io, time
from helpers.logs import *

class FileStream():

    __file=None

    def __init__(self, filename:str):
        self.__file = filename
        
    def streamFile(self)->str:

        do_log("FILE", self.__file)
        file=io.open(self.__file, mode="r")

        file.seek(0,2)
        while True:
            line = file.readline()
            do_log("LINE", line)
            if not line:
                time.sleep(0.1)
                continue
            yield line