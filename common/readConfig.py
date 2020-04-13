import os
from configparser import ConfigParser

class ReadConfig(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(r"E:\code\person\lsn2\venv\config.ini",encoding="utf-8-sig")
    def get_eamil(self,param):
        return self.cf.get("EMAIL",param)
if __name__ == '__main__':
    a = ReadConfig()
    print(a.get_eamil("mail_host"))
