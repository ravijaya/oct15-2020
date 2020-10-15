from os import listdir
from os.path import join, isfile, getsize, getmtime, basename
from time import ctime
from pprint import pprint as pp


class DirectoryListing:
    def __init__(self, *args):
        self.directories = args
        self.container = dict()
        self.read_directories()

    def read_directories(self):
        for dir_name in self.directories:
            directory_content = (join(dir_name, item) for item in listdir(dir_name))  # generator
            for file_name in filter(isfile, directory_content):
                properties = [getsize(file_name), ctime(getmtime(file_name))]
                file_name = basename(file_name)
                self.container.setdefault(dir_name, {})[file_name] = properties


if __name__ == '__main__':
    dl = DirectoryListing('/tmp', '/home/ravijaya', '/home/ravijaya/Downloads')
    pp(dl.container)
